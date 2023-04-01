from flask import Flask

app = Flask(__name__) #Inicializamos la app 

app.secret_key = "Llave requete secreta"
