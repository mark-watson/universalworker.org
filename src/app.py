from flask import Flask, request, render_template_string
from brave_search import brave_search

app = Flask(__name__)

# HTML template for the home page
HOME_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Brave Search</title>
</head>
<body>
    <h1>Brave Search</h1>
    <form action="/search" method="post">
        <input type="text" name="query" placeholder="Enter search query" required>
        <input type="number" name="num_results" placeholder="Number of results" required>
        <input type="submit" value="Search">
    </form>
</body>
</html>
"""

# HTML template for the search results page
RESULTS_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <ul>
        {% for result in results %}
            <li>{{ result }}</li>
        {% endfor %}
    </ul>
    <a href="/">New search</a>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HOME_PAGE_TEMPLATE)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    num_results = int(request.form['num_results'])
    results = brave_search(query, num_results)
    return render_template_string(RESULTS_PAGE_TEMPLATE, results=results)

if __name__ == '__main__':
    app.run(debug=True)