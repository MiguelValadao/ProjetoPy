from flask import Flask 

# Currículo HTML Aula dia 15/05

app = Flask(__name__)

@app.route('/')
def entrada():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                div {
                    width: 100%;
                    text-align: center;
                    font-family: Arial, sans-serif;
                    margin-top: 15%;
                }
            </style>
            <title>Home</title>
        </head>
        <body>
            <div><h1>Currículo Miguel Teixeira Valadão</h1>
        
            <h2><a href="/meucurriculo">Ir para página</a></h2>
           </div>
        </body>
        </html>
    '''

@app.route('/meucurriculo')
def curriculo():
    return '''
        <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Miguel Valadão - Currículo</title>
    <style>
        :root {
            --text-color: #333;
            --heading-color: #000;
            --link-color: #0056b3;
            --line-color: #ccc;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.5;
            color: var(--text-color);
            max-width: 850px;
            margin: 40px auto;
            padding: 20px;
            background-color: #f9f9f9;
        }

        .resume-card {
            background: #fff;
            padding: 40px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            margin: 0;
            font-variant: small-caps;
            font-size: 2.5rem;
            color: var(--heading-color);
        }

        .contact-info {
            font-size: 0.9rem;
            margin-top: 10px;
        }

        .contact-info a {
            color: var(--text-color);
            text-decoration: underline;
        }

        section {
            margin-top: 20px;
        }

        h2 {
            border-bottom: 1px solid var(--line-color);
            text-transform: uppercase;
            font-size: 1.2rem;
            margin-bottom: 10px;
            color: var(--heading-color);
        }

        .entry {
            margin-bottom: 15px;
        }

        .entry-header {
            display: flex;
            justify-content: space-between;
            font-weight: bold;
        }

        .entry-sub {
            display: flex;
            justify-content: space-between;
            font-style: italic;
            font-size: 0.95rem;
        }

        ul {
            margin: 5px 0 10px 20px;
            padding: 0;
        }

        li {
            margin-bottom: 3px;
            font-size: 0.9rem;
        }

        .skills-list p {
            margin: 5px 0;
            font-size: 0.9rem;
        }

        @media (max-width: 600px) {
            .entry-header, .entry-sub {
                flex-direction: column;
            }
            .resume-card { padding: 20px; }
        }
    </style>
</head>
<body>

<div class="resume-card">
    <header>
        <h1>Miguel Valadão</h1>
        <div class="contact-info">
            (31) 98235-5861 | Rua Pilar 215, Grajaú - BH<br>
            <a href="mailto:migueltvaladao@gmail.com">migueltvaladao@gmail.com</a> | 
            <a href="https://www.linkedin.com/in/miguel-valadão-973578310/">linkedin.com/in/Miguel-Valadao</a> | 
            <a href="https://github.com/MiguelValadao">github.com/MiguelValadao</a>
        </div>
    </header>

    <section>
        <h2>Educação</h2>
        <div class="entry">
            <div class="entry-header">
                <span>Colégio Cotemig</span>
                <span>Belo Horizonte, MG</span>
            </div>
            <div class="entry-sub">
                <span>Aluno Técnico em Informática (Backend & Mobile)</span>
                <span>Fev. 2024 — Dez. 2026</span>
            </div>
        </div>
    </section>

    <section>
        <h2>Experiência</h2>
        <div class="entry">
            <div class="entry-header">
                <span>Versa Informática</span>
                <span>Savassi, BH</span>
            </div>
            <div class="entry-sub">
                <span>Estagiário Analista de Suporte</span>
                <span>Abril 2025 — Dezembro 2025</span>
            </div>
            <ul>
                <li>Identificação, registro e resolução de incidentes e problemas no ambiente do sistema.</li>
                <li>Registro e acompanhamento de chamados para garantir retorno rápido e eficaz ao cliente.</li>
                <li>Comunicação com equipes internas para repassar bugs e solicitações complexas.</li>
                <li>Suporte técnico ao cliente e resolução de problemas.</li>
                <li>Comunicação clara e empática.</li>
            </ul>
        </div>
    </section>

    <section>
        <h2>Projetos</h2>
        <div class="entry">
            <div class="entry-header">
                <span>CATAS | Flutter, Dart, Python, Supabase</span>
                <span>Dez 2025 — Presente</span>
            </div>
            <ul>
                <li>Desenvolvimento de fluxos de automação de tarefas por meio de prompt do usuário.</li>
            </ul>
        </div>

        <div class="entry">
            <div class="entry-header">
                <span>ReminderApp | Python, Tkinter, Bootstrap</span>
                <span>Out 2025 — Nov 2025</span>
            </div>
            <ul>
                <li>Aplicativo de lembretes desktop com agendamento e notificações nativas.</li>
                <li>Criação de lembretes contínuos e agendados com data/hora fixa.</li>
                <li>Otimização de entrega de mensagens via sistema operacional.</li>
            </ul>
        </div>

        <div class="entry">
            <div class="entry-header">
                <span>Code.it | React, TypeScript, Supabase</span>
                <span>Set 2025 — Nov 2025</span>
            </div>
            <ul>
                <li>Rede social em formato de fórum para profissionais de TI.</li>
                <li>Implementação de GitHub OAuth e Google OAuth 2.0.</li>
                <li>Funcionalidades de interação dinâmica (curtidas, comentários e respostas).</li>
            </ul>
        </div>
    </section>

    <section>
        <h2>Habilidades Técnicas</h2>
        <div class="skills-list">
            <p><strong>Linguagens:</strong> Java, Python, C#, SQL (PostgreSQL), JavaScript, HTML/CSS, TypeScript, Dart, Kotlin, Swift</p>
            <p><strong>Frameworks:</strong> React, Flask, ASP.NET, Flutter</p>
            <p><strong>Ferramentas:</strong> Git, Google Cloud Platform, VS Code, Visual Studio, PyCharm, GitHub, AWS</p>
            <p><strong>Idiomas:</strong> Português (Nativo), Inglês (C1), Espanhol (Intermediário)</p>
        </div>
    </section>
</div>

</body>
</html>

    '''

if __name__ == '__main__':
    app.run(debug=True)
