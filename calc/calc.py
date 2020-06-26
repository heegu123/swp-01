from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])

    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    sum, mul = "a+b", "a*b"
    error = " "
    if '' not in [a,b]:
        if a.isdigit() and b.isdigit() :
            a, b = int(a), int(b)
            sum = a+b
            mul = a*b
        else:
            sum, mul = '', ''
            for i in [a, b]:
                if i.isdigit()==False:
                    error += "Error : %s is not integer\n" %i
    elif a=='' and b=='':
        sum = ''
        mul = ''
        error = "Nothing Entered"
    elif a=='' and b!='':
        sum, mul = '', ''
        error += "Error : a is not entered\n"
        if b.isdigit()==False:
            error += "Error : %s is not integer" %b
    elif a!='' and b=='':
        sum, mul = '', ''
        error += "Error : b is not entered\n"
        if a.isdigit()==False:
            error += "Error : %s is not integer" %b
    response_body = html % {'sum':sum, 'mul':mul,'error':error}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
