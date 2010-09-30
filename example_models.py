from webapi import WebApi

class FacebookApi(WebApi):
	_url = "http://graph.facebook.com/"
	_returntype = "json"
	
	def page(self, objectid):
		self._curcall = str(objectid)
		return self.api()

