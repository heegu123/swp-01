from cgi import parse_qs
from template2 import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])

    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    if '' not in [a, b, c]:
        a, b = int(a), int(b)
	response_body = html % {
	'sum' : a+b,
	'mul' : a*b,
	}
    else :
	response_body = html % {
	'sum' : "",
	'mul' : "",
	}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
