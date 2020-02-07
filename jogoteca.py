from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'alura'

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


 


jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('God of War4','Ação','PLAY4')
jogo3 = Jogo('Mortal Kombat','Ação','PLAY4')
lista_jogos = [jogo1,jogo2,jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo="Jogos", jogos=lista_jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html',titulo='Novo Jogo')

@app.route('/criar',methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso !')
        return redirect('/')

    else:
        flash('Usuário ou senha invalida !')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuario deslogado !')
    return redirect('/login')





app.run(host='0.0.0.0', port=8000,debug=True)