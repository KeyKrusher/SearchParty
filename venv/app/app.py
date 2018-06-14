from flask import Flask, render_template, request, flash
from searcher import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    render_template("index.html")
    if request.method == 'POST':
        search_query = request.form['query']
        search_sitename = request.form['sitename']
        search_depth = request.form['depth']
        search = Search(search_query, search_sitename, search_depth)
        result = search.search()
        
    else:
        flash("Please fill in the textboxes")

if __name__ == "__main__":
    app.run()