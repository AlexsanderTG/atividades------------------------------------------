import os
from flask import Flask
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

from jogoteca import app  # Certifique-se de que o módulo jogoteca está corretamente importado aqui

class FormularioJogo(FlaskForm):
    nome = StringField("Nome do jogo", [DataRequired(), Length(min=1, max=50)])
    categoria = StringField("Categoria", [DataRequired(), Length(min=1, max=40)])
    console = StringField("Console", [DataRequired(), Length(min=1, max=20)])
    salvar = SubmitField("Salvar")

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))