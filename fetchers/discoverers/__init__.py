import typing
from abc import abstractmethod

from AnyVer import AnyVer

from ..webServices import DownloadTarget as ServiceDownloadTarget, DownloadTargetFile
from ..tools.download import download
from ..DownloadTarget import DownloadTarget
from ..FetchConfig import FetchConfig

from ..utils.idded import IDded

class Discovered:
	__slots__ = ("version", "targets")

	def __init__(self, version: AnyVer, targets: typing.Mapping[str, DownloadTarget]) -> None:
		self.version = version
		self.targets = targets


class Discoverer(IDded):
	__slots__ = ()

	@abstractmethod
	def __call__(self, fetchConfig: FetchConfig) -> Discovered:
		raise NotImplementedError()

