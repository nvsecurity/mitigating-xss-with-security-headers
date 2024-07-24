#! /usr/bin/env python3
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def home():
    name = request.args.get('name', 'World')
    template = '<h1>Hello, {}!</h1>'.format(name)
    return render_template_string(template)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
