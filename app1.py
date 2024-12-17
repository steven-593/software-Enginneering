from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('forms.html')

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        return f"""
            <h1>Celular Registrado</h1>
            <p>Marca: {marca}</p>
            <p>Modelo: {modelo}</p>
            <p>Precio: {precio}</p>
        """
    return "<p>Método no permitido</p>"

if __name__ == "__main__":
    app.run(debug=True)
