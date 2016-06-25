from urllib2 import Request, urlopen
import json

headers = {
  'Accept': 'application/json'
}
request = Request('http://api.themoviedb.org/3/genre/18/movies?api_key=03bb4843dcfd206b47dc2872f71aa418', headers=headers)

response_body = urlopen(request).read()
parsed = json.loads(response_body)

for i in parsed['results']:
    print i['title']
