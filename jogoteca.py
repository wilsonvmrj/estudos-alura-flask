from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'alura'

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self,id,nome,senha):
        self.id = id
        self.nome = nome
        self.senha = senha


usuarios1 = Usuario('wilson','Wilson Magalhaes','1234')
usuarios2 = Usuario('mimi','Michele Magalhaes','4321')
usuarios3 = Usuario('jose','Jose das Coves','1234')
usuarios = {
            usuarios1.id: usuarios1,
            usuarios2.id: usuarios2,
            usuarios3.id: usuarios3,
}



jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('God of War4','Ação','PLAY4')
jogo3 = Jogo('Mortal Kombat','Ação','PLAY4')
lista_jogos = [jogo1,jogo2,jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo="Jogos", jogos=lista_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novo')))
    return render_template('novo.html',titulo='Novo Jogo')

@app.route('/criar',methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso !')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário ou senha invalida !')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuario deslogado !')
    return redirect(url_for('login'))





app.run(host='0.0.0.0', port=8000,debug=True)