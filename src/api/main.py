
from dotenv import load_dotenv
from flask import Flask, request,render_template, redirect, url_for
load_dotenv()

app = Flask(__name__)

# Root URL
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
