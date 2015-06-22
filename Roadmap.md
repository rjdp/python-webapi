## Oauth2 and HTTPS support ##

Many APIs support the oauth2 protocol for user authentication. It would be nice to offer a simple interface for authorizing a WebApi instance to a specific site user. HTTPS support should be added before user authentication to promote security.

```
api = WebApi("https://my.secure.site/api/", appkey="my_appkey")
api._authorize("username", "user_authtoken")
## do stuff with the api
api._deauthorize()
```


## Subclasses ##

Add shortcut methods to make subclassing WebApi easier. Subclassing WebApi should be as elegant and well defined as subclassing the "base entity" class for a modern ORM dbms.


## Python 2 Compatibility ##

Maybe?