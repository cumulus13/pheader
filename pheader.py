#!/usr/bin/env python2

from __future__ import print_function
import sys
import re
if sys.version_info.major == 3:
	from urllib.parse import urlparse
else:
	from urlparse import urlparse
try:
	from pydebugger.debug import debug
except:
	def debug(*args, **kwargs):
		return ''
from make_colors import make_colors
from pprint import pprint

def set_header(header_str = None, url = '', origin = ''):
    """generate mediafire url to direct download url

    Args:
        header_str (str, optional): raw headers data/text from browser on development mode
        url (str, optional): for referer tag
        origin (str, optional): for origin tag

    Returns:
        TYPE: dict: headers data
    """
    if url:
    	url = "\n" + "referer: {}".format(url)
    else:
    	url = ''
    if url and origin:
    	origin = urlparse(url)
    	origin = "\n" + "origin: " + origin.scheme + "://" + origin.netloc
    else:
    	origin = ''
    if not header_str:
        header_str ="""content-length:	117
		cache-control:	max-age=0
		upgrade-insecure-requests:	1{}
		content-type:	application/x-www-form-urlencoded
		user-agent:	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36
		accept:	text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
		sec-fetch-site:	same-origin
		sec-fetch-mode:	navigate
		sec-fetch-user:	?1
		sec-fetch-dest:	document{}
		accept-encoding:	gzip, deflate
		accept-language:	en-US,en;q=0.9,id;q=0.8,ru;q=0.7
		cookie:	aff=3199; cookieconsent_dismissed=yes""".format(origin, url)

    debug(header_str = header_str)
    header_str = list(filter(None, re.split("\n|\r|\t\t", header_str)))
    debug(header_str = header_str)
    headers = {key.strip():value.strip() for key,value in [re.split(": |:\t", i) for i in header_str]}
    debug(headers = headers)
    return headers

def headers(*args, **kwargs):
	return set_header(*args, **kwargs)

def usage():

	import argparse
	parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
	parser.add_argument('HEADERS', help = 'string of headers, usually copy from dev tool browser, or type "c" for get string from clipboard', action='store')
	parser.add_argument('-u', '--url', help = 'Add url referer to url', action = 'store')
	parser.add_argument('-o', '--origin', help = 'Add url origin to url', action = 'store')
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		debug(args_HEADERS = args.HEADERS)		
		if args.HEADERS == 'c':
			try:
				import clipboard
				args.HEADERS = clipboard.paste()
			except:
				print(make_colors("Please install `clipboard` before (pip install clipboard) !", 'lw', 'r'))

		
		headers = set_header(args.HEADERS, args.url, args.origin)
		pprint(headers)

if __name__ == '__main__':
	usage()




