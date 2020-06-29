import typing
from urllib.parse import urlencode, urlparse, ParseResult as URIParseResult
from .Service import *
from .DownloadTarget import *
from .services import *


def _detectService(uri) -> URIParseResult:
	parsedURI = urlparse(uri)
	for s in servicesRegistry:
		detectionResult = s.detect(parsedURI)
		#print(s, uri, detectionResult)
		if detectionResult:
			args = s.genArgs(parsedURI)
			return (s, args)


def detectService(uri) -> URIParseResult:
	res = _detectService(uri)
	if res:
		serviceClass, ctorArgs = res
		return serviceClass(**ctorArgs)
