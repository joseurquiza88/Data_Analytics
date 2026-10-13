import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env
load_dotenv()

remitente = os.getenv("EMAIL_REMITENTE")
destinatario = os.getenv("EMAIL_DESTINATARIO")
password = os.getenv("EMAIL_PASSWORD")
servidor = os.getenv("SMTP_SERVER", "smtp.gmail.com")
puerto = int(os.getenv("SMTP_PORT", "587"))

# 2. Verificar que estén configuradas las credenciales
if not remitente or not destinatario or not password:
    raise ValueError("Faltan variables de correo en el archivo .env.")

# 3. Crear el mensaje
mensaje = EmailMessage()
mensaje["Subject"] = "Prueba de automatización - Monitoreo de ventas"
mensaje["From"] = remitente
mensaje["To"] = destinatario

mensaje.set_content(
    """
Hola,

Este es un correo de prueba enviado automáticamente
desde Python para el proyecto de monitoreo de ventas.

Si recibiste este mensaje, la conexión con Gmail funciona correctamente.

Saludos.
"""
)

# 4. Enviar el correo
try:
    with smtplib.SMTP(servidor, puerto) as smtp:
        smtp.starttls()
        smtp.login(remitente, password)
        smtp.send_message(mensaje)

    print("Correo enviado correctamente.")

except smtplib.SMTPAuthenticationError:
    print(
        "Error de autenticación. Verificá que el correo sea correcto "
        "y que EMAIL_PASSWORD contenga la contraseña de aplicación.")

except Exception as error:
    print(f"No se pudo enviar el correo: {error}")