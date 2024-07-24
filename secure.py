#! /usr/bin/env python3
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.after_request
def set_security_headers(response):
    # Content-Security-Policy helps prevent XSS attacks by specifying which dynamic resources are
    # allowed to load. In this example, we only allow resources from the same origin ('self').
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self';"
    # X-XSS-Protection: This header enables the XSS filter in the browser.
    # When the filter is enabled, it will sanitize the page if an XSS attack is detected.
    response.headers['X-XSS-Protection'] = "1; mode=block"
    # X-Content-Type-Options: This header prevents browsers from MIME-sniffing a response away
    # from the declared content-type.
    response.headers['X-Content-Type-Options'] = "nosniff"
    # Strict-Transport-Security: This header forces the browser to use HTTPS for all subsequent
    # requests to the web server.
    response.headers['Strict-Transport-Security'] = "max-age=31536000; includeSubDomains"
    return response


@app.route('/')
def home():
    name = request.args.get('name', 'World')
    template = '<h1>Hello, {}!</h1>'.format(name)
    return render_template_string(template)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
