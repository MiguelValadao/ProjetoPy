import math
from flask import render_template, request # type: ignore

def calcular():
    operacao = request.form.get("operacao")
    
    if operacao == "bhaskara":
        try:
            a = float(request.form.get("num1", 0))
            b = float(request.form.get("num2", 0))
            c = float(request.form.get("num3", 0))
            
            if a == 0:
                resultado = "Erro: 'a' não pode ser zero"
                etapas = "Em uma equação do 2º grau, o coeficiente 'a' deve ser diferente de zero."
            else:
                delta = (b ** 2) - (4 * a * c)
                etapas = f"Δ = {b}² - 4 * {a} * {c} = {delta}"
                
                if delta < 0:
                    resultado = "Sem raízes reais"
                    etapas += f"<br>Como Δ < 0, a equação não possui raízes reais."
                elif delta == 0:
                    x = -b / (2 * a)
                    resultado = f"x = {x}"
                    etapas += f"<br>x = -({b}) / (2 * {a}) = {x}"
                else:
                    x1 = (-b + math.sqrt(delta)) / (2 * a)
                    x2 = (-b - math.sqrt(delta)) / (2 * a)
                    resultado = f"x1 = {x1}, x2 = {x2}"
                    etapas += f"<br>x = (-({b}) ± √{delta}) / (2 * {a})"
                    etapas += f"<br>x1 = {x1}<br>x2 = {x2}"
        except ValueError:
            resultado = "Erro"
            etapas = "Por favor, insira valores numéricos válidos."
            
        return render_template('calculator.html', etapas=etapas, resultado=resultado)

    # Lógica para as outras operações
    try:
        num1 = float(request.form.get("num1", 0))
        
        if operacao == "sqrt":
            if num1 < 0:
                resultado = "Erro: número negativo"
                etapas = f"Não existe raiz real de {num1}."
            else:
                res = math.sqrt(num1)
                resultado = str(res)
                etapas = f"√{num1} = {res}"
        else:
            num2_valor = request.form.get("num2", "").strip()
            if not num2_valor:
                return render_template(
                    "calculator.html",
                    etapas="Informe o segundo número para esta operação.",
                    resultado="",
                )
            num2 = float(num2_valor)

            if operacao == "+":
                res = num1 + num2
                etapas = f"{num1} + {num2} = {res}"
            elif operacao == "-":
                res = num1 - num2
                etapas = f"{num1} - {num2} = {res}"
            elif operacao == "*":
                res = num1 * num2
                etapas = f"{num1} * {num2} = {res}"
            elif operacao == "/":
                if num2 == 0:
                    res = "Erro"
                    etapas = "Divisão por zero não é permitida."
                else:
                    res = num1 / num2
                    etapas = f"{num1} / {num2} = {res}"
            elif operacao == "**":
                res = num1 ** num2
                etapas = f"{num1} ^ {num2} = {res}"
            elif operacao == "log":
                if num1 <= 0 or num2 <= 0 or num2 == 1:
                    res = "Erro"
                    etapas = "Logaritmo inválido (base e logaritmando devem ser > 0, base != 1)."
                else:
                    res = math.log(num1, num2)
                    etapas = f"log_{num2}({num1}) = {res}"
            else:
                res = "Operação inválida"
                etapas = ""
            
            resultado = str(res)
            
    except ValueError:
        resultado = "Erro"
        etapas = "Entrada inválida."

    return render_template('calculator.html', etapas=etapas, resultado=resultado)
