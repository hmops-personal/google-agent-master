import sys  # Importamos el módulo de sistema para leer argumentos
import vertexai
from vertexai.generative_models import GenerativeModel

from google.oauth2 import service_account

# 1. Ruta a tu archivo de llave JSON
KEY_PATH = "./service-account.json"

# 2. Creamos el objeto de credenciales
creds = service_account.Credentials.from_service_account_file(KEY_PATH)

# 3. Pasamos las credenciales al inicializar Vertex AI
vertexai.init(
    project="adk-test-491718", 
    location="southamerica-east1", 
    credentials=creds
)

model = GenerativeModel("gemini-2.5-flash")

chat = model.start_chat()
# Primera interacción
strInput = input ("Por favor ingresa tu texto:")
while strInput.lower() != "salir":
    response = chat.send_message(strInput)
    print(response.text)
    strInput = input ("Por favor ingresa tu texto:")