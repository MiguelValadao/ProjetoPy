from flask import Flask, render_template

# Currículo HTML Aula dia 15/05

app = Flask(__name__)

@app.route('/')
def main_Route():
    return render_template('index.html')

@app.route('/cotemig/<nome>')
def dinamic_Route(nome):
    return f'Bem vindo {nome} à Escola Técnica do COTEMIG'

if __name__ == '__main__':
    app.run(debug=True)