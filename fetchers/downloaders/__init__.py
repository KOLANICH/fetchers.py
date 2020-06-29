import typing
from abc import abstractmethod, ABC
from pathlib import Path, PurePath
import datetime
import sys

from ..webServices import DownloadTarget as GHDownloadTarget, DownloadTargetFile as GHDownloadTargetFile

#from ..webServices.GitHub import GitHubService
from ..tools.download import download
from ..DownloadTarget import DownloadTarget


class Downloader(ABC):
	__slots__ = ()

	@abstractmethod
	def __call__(self, downloadTargets: typing.Mapping[str, DownloadTarget], targetDir):
		raise NotImplementedError()


class Aria2Downloader(Downloader):
	__slots__ = ("downloadTargets",)

	def __call__(self, downloadTargets: typing.Mapping[str, DownloadTarget], targetDir: Path) -> typing.Mapping[str, DownloadTarget]:
		for k, v in downloadTargets.items():
			v.fsPath = targetDir / v.role
		#print("downloadTargets", downloadTargets)
		download(downloadTargets.values())
		return downloadTargets


defaultDownloader = Aria2Downloader()
