from flask import Flask, render_template, abort
import json
import os

with open("books.json") as libros:
    datos=json.load(libros)
    
app=Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html', libros=datos)

@app.route('/libro/<isbn>')
def libro(isbn):
    for l in datos:

        if "isbn" in l.keys() and isbn == l["isbn"]:
            return render_template('libros.html', libro=l) 

    return abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
            return render_template('categoria.html', libros=datos, categoria=categoria)

app.run("0.0.0.0",5000,debug=True)
