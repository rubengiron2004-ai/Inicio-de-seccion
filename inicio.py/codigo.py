import os
from dotenv import load_dotenv
import tkinter as tk

# Cargar las variables desde el archivo .env
load_dotenv()

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")


# === FUNCIONES (3 requeridas) ===
def capturar_credenciales():
    """1. Captura el usuario y contraseña desde los campos de entrada."""
    usuario = entry_email.get().strip()
    contrasena = entry_password.get()
    return usuario, contrasena


def validar_credenciales(usuario, contrasena):
    """2. Valida si los datos coinciden con APP_USER y APP_PASSWORD."""
    if not APP_USER or not APP_PASSWORD:
        return False
    return usuario == APP_USER and contrasena == APP_PASSWORD


def mostrar_mensaje():
    """3. Coordina la validación y muestra el resultado en Tkinter."""
    usuario, contrasena = capturar_credenciales()

    if validar_credenciales(usuario, contrasena):
        label_mensaje.config(text="Acceso correcto", fg="green")
    else:
        label_mensaje.config(text="Usuario o contraseña incorrectos", fg="red")


# === INTERFAZ TKINTER ===
ventana = tk.Tk()
ventana.title("Validar credenciales")
ventana.geometry("320x260")

# == Usuario / Correo ==
label_email = tk.Label(ventana, text="Ingrese su usuario o correo:")
label_email.pack(pady=(15, 5))

entry_email = tk.Entry(ventana, width=30)
entry_email.pack(pady=5)

# == Contraseña ==
label_password = tk.Label(ventana, text="Ingrese su contraseña:")
label_password.pack(pady=(10, 5))

entry_password = tk.Entry(ventana, show="*", width=30)
entry_password.pack(pady=5)

# == Botón ==
button = tk.Button(ventana, text="Ingresar", command=mostrar_mensaje)
button.pack(pady=15)

# == Etiqueta para el mensaje de validación ==
label_mensaje = tk.Label(ventana, text="", font=("Arial", 10, "bold"))
label_mensaje.pack(pady=5)

ventana.mainloop()