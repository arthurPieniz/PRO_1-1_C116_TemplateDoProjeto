# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Arthur" # escreva seu nome
    idade = "14" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/flask_2")
def pai():

    nome = "Marzo"
    idade = "48" 

    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/flask_3")
def home():

    nome = "Juliana" 
    idade = "14" 

    return render_template('mãe.html' , nome = nome , idade = idade)



# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
