from flask import Flask, render_template, request # type: ignore
from calculadora import calcular

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"]) 
def index():
    if request.method == "POST":
        return calcular()
    return render_template('calculator.html', etapas="", resultado="")

if __name__ == '__main__':
    app.run(debug=True)
    