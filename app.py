
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    # Aqui você pode adicionar a lógica para cadastrar o cliente em um banco de dados ou fazer qualquer outra operação desejada
    return 'Cliente cadastrado com sucesso!'

if __name__ == '__main__':
    app.run()