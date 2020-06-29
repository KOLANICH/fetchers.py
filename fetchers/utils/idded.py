from abc import ABC

import re
import unicodedata

idSanitizerRx = re.compile("\W")
def getPathSafeIDComponent(iD: str) -> str:
	return idSanitizerRx.subn(lambda m: "_" + unicodedata.name(m.group(0)).replace(" ", "_") + "_", iD)[0]


class IDded(ABC):
	__slots__ = ()

	marker = None
	idComponents = ()

	@property
	def id(self):
		self.delimiter.join((self.marker,) + tuple(getPathSafeIDComponent(c) for c in self.idComponents))
