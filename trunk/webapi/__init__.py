##########################
#	WebApi
#	http://code.google.com/p/python-webapi/
#	License: BSD
#	Author: Jordan Perr
#	Version: 1
#	Date: 9/30/2010
##########################

import urllib, urllib2
import sys
try:
	import json
except:
	import simplejson as json


class WebApi(object):
	
	def __init__(self, url, method="get", returntype="text"):
		self._url = url
		self._method = method
		self._returntype = returntype
	
	def _fetch(self, call, query, method):
		if method == "post":
			req = urllib2.Request(self._url+call, query)
		else:
			req = urllib2.Request(self._url+call+"?"+query)
		response = urllib2.urlopen(req)
		return response.read()
	
	def api(self, **kwargs):
		if "_method" in kwargs:
			method = kwargs["_method"].lower()
			del kwargs["_method"]
		else:
			method = self._method
		if "_returntype" in kwargs:
			returntype = kwargs["_returntype"].lower()
			del kwargs["_returntype"]
		else:
			returntype = self._returntype
		query = urllib.urlencode(kwargs)
		return self._fetch(self._curcall, query, returntype)
	
	def __getattr__(self, name):
		self._curcall = name
		return self.api
