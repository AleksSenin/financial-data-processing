from flask import Flask, render_template
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    fig = px.line(x=[1, 2, 3], y=[150.25, 151.75, 153.00], title='Stock Prices')
    graph = fig.to_html(full_html=False)
    return render_template("index.html", graph=graph)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
