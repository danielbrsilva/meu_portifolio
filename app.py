from flask import Flask, render_template, request

app = Flask(__name__)

# Simulação de Banco de Dados de Projetos
meus_projetos = [
    {
        "id": 1,
        "nome": "Attude Fitness",
        "tecnologia": "JavaScript",
        "desc": "Um site de cadastro de uma academia.",
        "github": "https://github.com/danielbrsilva/attude_fitness"
    },
    {
        "id": 2,
        "nome": "Mark Fit",
        "tecnologia": "HTML/CSS",
        "desc": "Um site de vendas de produtos fitness.",
        "github": "https://github.com/danielbrsilva/mark_fit"
    },
    {
        "id": 3,
        "nome": "Sistema de Receitas",
        "tecnologia": "Flask",
        "desc": "Um site de receitas de culinária.",
        "github": "https://github.com/danielbrsilva/sistema_de_receitas"
    }
]

@app.route('/')
def index():
    # A Home mostra um resumo ou boas-vindas
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    # Passa a lista completa de projetos
    return render_template('projetos.html', projetos=meus_projetos)

@app.route('/projeto/<int:id>')
def projeto_detalhe(id):
    # Busca o projeto pelo ID na lista
    projeto = next((p for p in meus_projetos if p['id'] == id), None)
    return render_template('projeto_detalhe.html', projeto=projeto)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        return "Sinal transmitido com sucesso! Entrarei em contato em breve."
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)