from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('forms.html')

# Ruta para procesar el formulario
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        university = request.form['university']
        return f"""
            <h1>¡Hola, {first_name} {last_name}!</h1>
            <p>Tienes {age} años y estudias en {university}.</p>
        """
    return "<p>Método no permitido</p>"

if __name__ == "__main__":
    app.run(debug=True)
