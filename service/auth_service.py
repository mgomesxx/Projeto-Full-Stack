import jwt
import random
from datetime import datetime, timedelta
from twilio.rest import Client

SECRET_KEY = "123456789"

TWILIO_SID = "ACbfe4c81746a0345b5029c1b9f8e122f7"
TWILIO_TOKEN = "85dcc3b9079de75dc671337766c56b7c"
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