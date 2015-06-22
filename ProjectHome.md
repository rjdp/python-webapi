## Python WebApi ##

A high level wrapper for Python's urllib.
```
>>> facebook.search("Carmen Sandiego")
```

**[Download WebApi](https://code.google.com/p/python-webapi/source/checkout)**


### Web Services as Intelligent Databases ###

This project serves two purposes. It is first and foremost a tool that developers can use to speed up web application development. With WebApi, you can query data from different web services just like you query data from different tables in a database.

This "normalization" of web services into object instances of common types is, I believe, a step towards the semantic web. By treating other web services as "intelligent databases," transfer of information in pragmatic form from one service to the next becomes fundamental.

I hope this project inspires development of new web service mashups that would be difficult to get working with urllib and raw http requests.


---


## The generic WebApi class ##
**Generic API usage**
```
from webapi import WebApi

fb = WebApi("http://graph.facebook.com/")
print( fb.search(q = "friday") )
```

Here, you see how the WebApi class can be used to query Facebook's api. The query sent to Facebook will be `GET http://graph.facebook.com/search?q=jet%20ponies` This general scheme here is: `GET (baseurl)+(function name)+?(function arguments)`

You can specify the request method (`get` and `post` supported) and the response type (`text` and `json` supported) using optional arguments to the function.

```
data = fb.search(q = "jet ponies", _method = "post" , _returntype = "json")
```

This will submit a `post` request to the base url (specified at fb's initialization) with the query "q=jet ponies." Once the call returns, it will automatically parse the return text with python's json decoder, returning a python data object.


---


## Subclassing WebApi ##
If you need more flexibility, WebApi gives you the ability to create site-speciffic api objects by subclassing the generic WebApi class. Think of these objects as entities in a traditional database model. Below is the FacebookApi model included in example\_models.py. The model configures an internal base url, the data return type, and creates a method called "page" that gives access to api calls like `http://graph.facebook.com/objectid`, which do not follow the traditional API call/querystring format.

**Model Definition**
```
from webapi import WebApi

class FacebookApi(WebApi):
	_url = "http://graph.facebook.com/"
	_returntype = "json"
	
	def page(self, objectid):
		self._curcall = str(objectid)
		return self.call()
```

Here's how you might interact with the FacebookApi model to print out the pages for the top five search results of "jet ponies."

**Model Usage**
```
fb = FacebookApi()
search = fb.search(q = "jet ponies")
for result in search["data"][:5]:
	print( fb.page(result["id"]) )
```


---


## Using WebApi.call() Directly ##

If you're working with a more complex API, you might want to try using WebApi.call directly. This method is called under the hood for all generic and model-based queries. You can use WebApi.call like this:

```
fb = FacebookApi()
fb.call("some-user-id/checkins")
# or
fb.call("some-post-id/comments", _method="post", message="Comment data")
```


---


## Links ##

  * Check the [Roadmap](Roadmap.md) for ideas on how you can help!
  * Browse the [source code trunk](https://code.google.com/p/python-webapi/source/browse/#svn/trunk)