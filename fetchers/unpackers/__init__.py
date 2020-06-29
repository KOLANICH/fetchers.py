import typing
from pathlib import Path


from ..FetchConfig import FetchConfig
from ..DownloadTarget import DownloadTarget
from ..styles import styles



class Unpacker:
	def __init__(self, dir2ArtifactsMapping: typing.Mapping[str, str]) -> None:
		self.dir2ArtifactsMapping = dir2ArtifactsMapping

	def __call__(self, config: FetchConfig, downloadedFiles, extrDir: Path):
		raise NotImplementedError()


