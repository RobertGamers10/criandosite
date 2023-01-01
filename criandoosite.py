from flask import Flask, render_template

app = Flask(__name__)

#Criar a 1° pagina do Site
#route -> churrasconopao.com/
#funcao -> o que vai ser exibido nesta pagina

@app.route("/")
def homepage():
	return render_template("homepage.html")

@app.route("/robert")
def robert():
	return render_template("robert.html")
	
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
	return render_template("usuarios.html", nome_usuario=nome_usuario)


#Colocar o Site no ar
if __name__ == "__main__":
	app.run(debug=True)

#servidor do Heroku


