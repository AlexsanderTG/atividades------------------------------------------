from jogoteca import app, db
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario, FormularioRegistro,  FormularioEdicaoUsuario
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    if usuario:
        if form.senha.data == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = FormularioRegistro()
    if form.validate_on_submit():
        nickname = form.nickname.data
        nome = form.nome.data
        senha = form.senha.data

        usuario = Usuarios.query.filter_by(nickname=nickname).first()
        if usuario:
            flash('Nickname já cadastrado!')
            return redirect(url_for('registro'))

        novo_usuario = Usuarios(nickname=nickname, nome=nome, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Usuário registrado com sucesso!')
        return redirect(url_for('index'))

    return render_template('registro.html', titulo='Registrar Usuário', form=form)


@app.route('/editar_perfil', methods=['GET', 'POST'])
def editar_perfil():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('editar_perfil')))

    usuario = Usuarios.query.filter_by(nickname=session['usuario_logado']).first()
    if not usuario:
        flash('Usuário não encontrado.')
        return redirect(url_for('index'))

    form = FormularioEdicaoUsuario()
    if form.validate_on_submit():
        usuario.nome = form.nome.data
        if form.senha.data:
            usuario.senha = form.senha.data
        db.session.commit()
        flash('Perfil atualizado com sucesso!')
        return redirect(url_for('index'))

    form.nome.data = usuario.nome
    return render_template('editar_usuario.html', titulo='Editando Perfil', form=form)
