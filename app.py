from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about():
    return "Pagina sobre"



@app.route("/")
def hello_world():
    return "Hello World"

if (__name__ == "__main__"): #  Para desenvolvimento LOCAL, execucação do arquivo manualmente
    app.run(debug=True)
