import typing
from abc import abstractmethod, ABC
from pathlib import Path

from OpenPGPAbs import ChosenBackend
from ..utils.integrity import parseHashesFile, sumFile
from ..DownloadTarget import DownloadTarget

from ..utils.idded import IDded

class Verifier(IDded):
	@abstractmethod
	def __call__(self, uris: typing.Mapping[Path, str]):
		raise NotImplementedError()
