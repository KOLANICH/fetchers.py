import typing
import datetime
import sys
from re import Pattern
from pathlib import Path, PurePath

from . import Discoverer, Discovered
from ..webServices import GitHubService
from ..FetchConfig import FetchConfig
from ..DownloadTarget import DownloadTarget


class GitHubReleasesDiscoverer(Discoverer):
	__slots__ = ("repo", "titleRx", "tagRx", "downloadFileNamesRxs", "targetSelector")

	marker = "GitHub"

	@property
	def idComponents(self):
		return (self.repo, self.tagRx, self.titleRx, self.downloadFileNamesRxs, self.targetSelector)

	def __init__(self, repo: str, tagRx: Pattern, downloadFileNamesRxs: typing.Mapping, titleRx: None = None, targetSelector: None = None) -> None:
		self.repo = repo
		self.tagRx = tagRx
		self.titleRx = titleRx
		self.downloadFileNamesRxs = downloadFileNamesRxs
		if targetSelector is None:
			targetSelector = max
		self.targetSelector = targetSelector

	def __call__(self, fetchConfig: FetchConfig) -> Discovered:
		gh = GitHubService(*self.repo.split("/"))
		tgts = list(gh.getTargets(self.titleRx, self.tagRx, self.downloadFileNamesRxs))

		#print("tgts", repr(tgts))

		selectedTarget = self.targetSelector(tgts)

		print("Selected release:", selectedTarget, file=sys.stderr)
		yield Discovered(selectedTarget.version, {k: DownloadTarget(v.role, v.name, v.uri, max(v.created, v.modified)) for k, v in selectedTarget.files.items()})
