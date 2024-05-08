from flask import Flask, render_template, request
from gomaps import maps_search


app = Flask(__name__)

@app.route('/')
@app.route('/<keyword>/')
def search(keyword = None):
    if keyword != None:
        results = maps_search(keyword)
        output = results[0].get_values()
        return render_template('index.html', leads=output)
    else:
        return render_template('index.html', leads=output)


if __name__ == '__main__':
    app.run()
