# imgscraper
This microservice can be used to get the url's of the first 15 images returned by a query on Bing.

# Connecting:
This microservice uses a socket pipeline. It is intended to be run locally. Your client program's socket must connect to the microservice's host and port. Make sure to have the server file in the same directory as your client.

# Request format

The service expects to receive a utf-8 encoded json-serialized messages. A message must have the following format:

{"query":"(insert the query that you want to search for here)"}

ex: {"query": "dog"}

Right now query is the only parameter, but more parameters may be added in the future.

# Response format

A response is also a json-serialized message in the following format: 

{"(imgquery#)":"image url"}

where the imgquery# is the number out of 15 images and the image url is the url link to the image.
An example of a use case for these image URL's returned is that they can be retrieved in a program and set to display as the img-source in a web app.

The file testclient.py shows an example of how a client could interact with the server.
