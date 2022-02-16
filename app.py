from flask import Flask, g, render_template, flash, request, redirect
import sqlite3

DATABASE = "blog.bd"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def fim_requisicao(exc):
    g.bd.close()

@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id desc"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({
            "titulo":titulo,
            "texto":texto
        })
    return render_template("exibir_entradas.html", posts=entradas)

@app.route('/inserir', methods=['POST'])
def inserir_entrada():
    sql = "INSERT INTO entradas(titulo, texto) VALUES(?, ?);"
    titulo = request.form['titulo']
    texto = request.form['texto']
    g.bd.execute(sql, [titulo, texto])
    g.bd.commit()
    return redirect('/')
