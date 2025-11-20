from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

#############################################################
# ROTA 1: RETORNANDO JSON (http://127.0.0.1:5000/)
@app.route("/")
def index():
    return jsonify({"mensagem":"Hello Json!"})

#############################################################
# ROTA 2: UTILIZANDO JINJA (http://127.0.0.1:5000/hello/seu_nome)
@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome=None):
    return render_template('hello.html', name=nome)

#############################################################
# ROTA 3: PASSAGEM DE PARÂMETRO - NÚMERO INTEIRO (http://127.0.0.1:5000/show/123)
@app.route('/show/<int:id>')
def show(id):
    return 'Valor recebido id = %d' % id

#############################################################
# ROTA 4: VERIFICANDO O METODO HTTP (GET e POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f'Login via POST para o usuário: {username}'
    else:
        return '''
<html>
<body>
<form method="post" action="/login">
<p><input type=text name=username placeholder="Nome de usuário">
<p><input type=submit value=Login>
</form>
</body>
</html>
'''

#############################################################
# ROTA 5: Pagina nao encontrada - erro 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

#############################################################
if __name__ == '__main__':
    app.run(debug=True)