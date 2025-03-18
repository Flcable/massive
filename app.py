from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo ao Sistema de Gerenciamento de Objetos SIGO!'

if __name__ == '__main__':
    app.run(debug=True)