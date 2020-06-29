import typing
from datetime import datetime

from .utils.ReprMixin import ReprMixin


class DownloadTarget(ReprMixin):
	__slots__ = ("role", "name", "uris", "fsPath", "time")

	def __init__(self, role: str, name: str, uris: str, time: datetime, fsPath: None = None) -> None:
		self.role = role
		self.name = name
		self.uris = uris
		self.fsPath = fsPath
		self.time = time
