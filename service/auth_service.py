import jwt
import random
import os
from datetime import datetime, timedelta
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_WHATSAPP = "whatsapp:+14155238886"

def gerar_codigo():
    return str(random.randint(1000, 9999))

def enviar_whatsapp(celular, codigo):
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(
        from_=TWILIO_WHATSAPP,
        to=f"whatsapp:+55{celular}",
        body=f"Seu código de ativação é: {codigo}"
    )

def gerar_token(email):
    payload = {
        "email": email,
        "exp": datetime.utcnow() + timedelta(hours=8)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verificar_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"erro": "Token expirado"}
    except jwt.InvalidTokenError:
        return {"erro": "Token inválido"}