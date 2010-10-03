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
	_url = ""
	_method = "get"
	_returntype = "text"
	
	def __init__(self, url=None, method=None, returntype=None):
		if url:
			self._url = url
		if method:
			self._method = method
		if returntype:
			self._returntype = returntype
	
	def call(self, url=None, **kwargs):
		# Process special args
		if url:
			self._curcall = url
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
		# Construct query
		query = urllib.urlencode(kwargs)
		if method == "post":
			req = urllib2.Request(self._url+self._curcall, query)
		else:
			req = urllib2.Request(self._url+self._curcall+"?"+query)
		# Execute query
		response = urllib2.urlopen(req).read()
		# Process returned data
		if returntype == "json":
			return json.loads(response)
		else:
			return response
	
	def __getattr__(self, name):
		self._curcall = name
		return self.call
