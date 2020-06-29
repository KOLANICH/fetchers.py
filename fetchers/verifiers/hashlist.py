import typing
from pathlib import Path

from . import Verifier
from ..DownloadTarget import DownloadTarget
from ..utils.integrity import parseHashesFile, sumFile

class HashlistVerifier(Verifier):
	__slots__ = ()


	marker = "hashlist"

	@property
	def idComponents(self):
		return (self.hashesFile, self.hashesSig, self.hashFunc, self.keyFingerprint, self.keyFile, self.verifierClass.id)

	def __init__(self, verifierClass: typing.Type[Verifier], hashFunc: typing.Callable, hashesFileName: str, signatureFileName: str, keyFingerprint: str, keyFile: Path = None, **verifierArgs) -> None:
		self.hashesFile = hashesFileName
		self.hashesSig = signatureFileName
		self.hashFunc = hashFunc
		self.verifierClass = verifierClass
		self.verifierArgs = verifierArgs
		self.keyFingerprint = keyFingerprint
		self.keyFile = keyFile

	def __call__(self, downloadsDir: Path, downloadedTargets: typing.Iterable[DownloadTarget]) -> None:
		print("downloadedTargets", downloadedTargets)
		sigTarget = downloadedTargets[self.hashesSig]
		hashesTarget = downloadedTargets[self.hashesFile]

		del downloadedTargets[self.hashesSig], downloadedTargets[self.hashesFile]

		hashesRaw = hashesTarget.fsPath.read_bytes()
		hashesSigRaw = sigTarget.fsPath.read_bytes()
		v = self.verifierClass((((self.hashesFile, hashesRaw), (self.hashesSig, hashesSigRaw), self.keyFingerprint, self.keyFile),))

		v(downloadsDir, (self.hashesFile,))

		hashes = parseHashesFile(hashesRaw.decode("utf-8"))
		print("hashes", hashes)

		for t in downloadedTargets.values():
			archiveEtalonHash = hashes[t.name].lower()
			actualFileHash = sumFile(t.fsPath, (self.hashFunc,))[0]
			if actualFileHash.lower() != archiveEtalonHash:
				raise Exception("Bad hash for the downloaded file!", t, actualFileHash.lower(), archiveEtalonHash)
