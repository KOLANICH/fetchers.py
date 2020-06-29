from . import Compression

import struct
from pathlib import Path

class GZIP(Compression):
	id = "gz"

	@staticmethod
	def extractOriginalSize(archPath: Path, packedSize: int) -> int:
		with archPath.open("rb") as arch:
			arch.seek(packedSize - 4)
			return struct.unpack("<I", arch.read(4))[0]
