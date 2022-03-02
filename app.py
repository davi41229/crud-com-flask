#crud com flask e sqlalchemy
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'C:/sqlite3/estudantes.sqlite3'



db = SQLAlchemy(app)

class Estudante(db.Model):
	id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(150))
	idade = db.Column(db.Integer)

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade




@app.route('/')
def index():
	estudantes = Estudante.query.all()
	return render_template('index.html', estudantes=estudantes)


if __name__ == '__main__':
	
	app.run(debug=True, port=3000)
