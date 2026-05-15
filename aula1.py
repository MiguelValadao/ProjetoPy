from flask import Flask 

app = Flask(__name__)

@app.route('/')
def decorador():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Home</title>
        </head>
        <body>
            <h1>O Que São Decoradores</h1>
        
            <h2><a href="/decorador">Ir para pagina</a></h2>
           
        </body>
        </html>
    '''

@app.route('/decorador')
def decoradorSet():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Decoradores</title>
        </head>
        <body>
        <h1>Decoradores</h1>
            <div style="width: 50%; text-align: justify;">
                <p>Decoradores (decorators) em Python são funções que modificam ou aprimoram o comportamento de outras funções ou métodos sem alterar seu código-fonte original. Eles permitem adicionar funcionalidades extras — como login, temporização ou controle de acesso — de maneira elegante, reutilizável e com a sintaxe @nome_do_decorador</p>
            </div>
           
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)