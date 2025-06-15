from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to the bigenning of Flask!"

if __name__ == '__main__':
    app.run(debug=True)
