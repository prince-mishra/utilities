"""mechanize.
TODO : expose this as a web service
"""
import mechanize
query_string	= "some query"
email_id		= "some@email.here"
r 				= mechanize.Request("http://www.google.com/alerts/create")
res 			= mechanize.urlopen(r)
forms 			= mechanize.ParseResponse(res, backwards_compat=False)
form 			= forms[0]
form["q"] 		= query_string
form["e"] 		= email_id
r2 				= form.click()
res2 			= mechanize.urlopen(r2)
print res2.read()