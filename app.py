from flask import Flask, request, render_template, redirect, url_for
from datetime import date
import sqlite3
from sqlite3 import Error
import os

# Instancia da Aplicacao Flask
app = Flask(__name__)

# Definicao do caminho do banco de dados 
DATABASE = 'database/db-produtos.db'

#######################################################
# Rota Principal (Redireciona para a lista)
@app.route('/')
def index():
    return redirect(url_for('listar'))

#######################################################
# 1. Cadastrar produtos (CREATE)
@app.route('/produtos/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    mensagem = ''
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        precocompra = request.form.get('precocompra')
        precovenda = request.form.get('precovenda')
        datacriacao = date.today()
        
        if descricao and precocompra and precovenda:
            registro = (descricao, precocompra, precovenda, datacriacao)
            try:
                conn = sqlite3.connect(DATABASE)
                sql = ''' INSERT INTO produtos(descricao, precocompra, precovenda, datacriacao) 
                          VALUES(?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()
                mensagem = f'Produto "{descricao}" cadastrado com sucesso!'
            except Error as e:
                print(e)
                mensagem = f'Erro ao cadastrar: {e}'
            finally:
                if conn: conn.close()
        else:
             mensagem = 'Erro: Todos os campos são obrigatórios.'
        
        return render_template('cadastrar.html', mensagem=mensagem) 
    
    return render_template('cadastrar.html')

#######################################################
# 2. Listar produtos (READ)
@app.route('/produtos/listar', methods=['GET'])
def listar():
    registros = []
    try:
        conn = sqlite3.connect(DATABASE)
        sql = '''SELECT * FROM produtos'''
        cur = conn.cursor()
        cur.execute(sql)
        registros = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn: conn.close()
    
    return render_template('listar.html', regs=registros)

#######################################################
# 3. Excluir produto (DELETE)
@app.route('/produtos/excluir/<int:idproduto>', methods=['POST'])
def excluir(idproduto):
    try:
        conn = sqlite3.connect(DATABASE)
        sql = 'DELETE FROM produtos WHERE idproduto = ?'
        cur = conn.cursor()
        cur.execute(sql, (idproduto,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn: conn.close()
            
    return redirect(url_for('listar'))

#######################################################
# 4. Alterar produto (UPDATE)
@app.route('/produtos/alterar/<int:idproduto>', methods=['GET', 'POST'])
def alterar(idproduto):
    
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        precocompra = request.form.get('precocompra')
        precovenda = request.form.get('precovenda')
        
        if descricao and precocompra and precovenda:
            registro = (descricao, precocompra, precovenda, idproduto)
            try:
                conn = sqlite3.connect(DATABASE)
                sql = ''' UPDATE produtos SET descricao = ?, precocompra = ?, precovenda = ? 
                          WHERE idproduto = ? '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()
            except Error as e:
                print(e)
            finally:
                if conn: conn.close()
        
        return redirect(url_for('listar'))

    # Método GET: Carrega o produto para o formulário
    produto = None
    try:
        conn = sqlite3.connect(DATABASE)
        sql = 'SELECT * FROM produtos WHERE idproduto = ?'
        cur = conn.cursor()
        cur.execute(sql, (idproduto,))
        produto = cur.fetchone() 
    except Error as e:
        print(e)
    finally:
        if conn: conn.close()

    if produto:
        return render_template('alterar.html', produto=produto)
    else:
        return render_template('404.html'), 404

#######################################################
# Rota de Erro 404
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

#######################################################
# Execucao da Aplicacao
if __name__ == '__main__':
    app.run(debug=True)