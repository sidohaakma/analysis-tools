import sys
import ast
import opal.core

def do_command(args):
    """
    Execute REST command without commandline intervention

    Add REST command specific options
    "'ws', 'Web service path, for instance: /datasource/xxx/table/yyy/variable/vvv'"
    "'method', 'HTTP method (default is GET, others are POST, PUT, DELETE, OPTIONS)'"
    "'accept', 'Accept header (default is application/json)'"
    "'content-type', 'Content-Type header (default is application/json)'"
    "'headers', 'Custom headers in the form of: { 'Key2': 'Value2', 'Key2': 'Value2' }'"
    "'json', 'Pretty JSON formatting of the response'"
    """
    # Build and send request
    try:
        request = opal.core.OpalClient.build(opal.core.OpalClient.LoginInfo.parse(args)).new_request()
        request.fail_on_error()

        if args.accept:
            request.accept(args.accept)
        else:
            request.accept_json()

        if args.content_type:
            request.content_type(args.content_type)
            request.content(args.content)

        if args.headers:
            headers = ast.literal_eval(args.headers)
            for key in headers.keys():
                request.header(key, headers[key])

        if args.verbose:
            request.verbose()

        # send request
        request.method(args.method).resource(args.ws)
        response = request.send()

        # format response
        res = response.content
        if args.json:
            res = response.pretty_json()
        elif args.method in ['OPTIONS']:
            res = response.headers['Allow']

        # output to stdout
        print res
    except Exception, e:
        print e
        sys.exit(2)
    except pycurl.error, error:
        errno, errstr = error
        print >> sys.stderr, 'An error occurred: ', errstr
        sys.exit(2)