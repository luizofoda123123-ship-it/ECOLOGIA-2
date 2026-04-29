from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>ola gente, como vcs estao?</h1><br><img src="https://media.tenor.com/ABSA7YeoBi8AAAAi/pode-não-man-pode-nao-man.gif" /> <br> <a href="http://127.0.0.1:5500/modulo2/index.html">clique aqui</a>'

app.run(debug=True)