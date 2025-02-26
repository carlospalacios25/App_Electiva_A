from flask import Flask, render_template, request, redirect, flash
from config import obtener_conexion
import bcrypt

app = Flask(__name__)
app.secret_key = "supersecreto"  # Necesario para usar mensajes flash

# Ruta para mostrar el formulario de registro
@app.route('/')
def index():
    return render_template('registro.html')

# Ruta para registrar usuarios
@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']

    # Hashear la contraseña
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO usuarios (nombre, email, password_hash) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, email, password_hash))
        conexion.commit()
        conexion.close()
        flash("Usuario registrado correctamente", "success")
    except Exception as e:
        flash(f"Error al registrar: {str(e)}", "danger")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
