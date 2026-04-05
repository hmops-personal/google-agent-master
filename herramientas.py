import sys  # Importamos el módulo de sistema para leer argumentos
# import vertexai
# from vertexai.generative_models import GenerativeModel

# from google.oauth2 import service_account

# # 1. Ruta a tu archivo de llave JSON
# KEY_PATH = "./service-account.json"

# # 2. Creamos el objeto de credenciales
# creds = service_account.Credentials.from_service_account_file(KEY_PATH)

# # 3. Pasamos las credenciales al inicializar Vertex AI
# vertexai.init(
#     project="adk-test-491718", 
#     location="southamerica-east1", 
#     credentials=creds
# )

# model = GenerativeModel("gemini-2.5-flash")

def aplicar_impuesto_pais (monto:float) -> float:
    impuesto = monto * 1.3
    return impuesto

def obtener_tasas_del_dia() -> dict:
    """
    Returns: Un diccionario con las cotizaciones.
    """
   
    tasas = {
        "oficial": 920.50,
        "blue": 1250.00,
        "tarjeta": 1470.20
    }
    return tasas

def aplicar_descuento_jubilado(monto: float) -> float:
    """
    Aplica un descuento del 15% exclusivo para jubilados.
    Args:
        monto: El valor base antes del descuento.
    Returns:
        El monto final con el descuento aplicado.
    """
    return monto * 0.85


def obtener_tasa_cambio_dolar() -> float:
    """
    Obtiene la tasa de cambio actual del dólar a pesos argentinos.

    Returns:
        La tasa de cambio actual (ej: 1000.0).
    """
    prompt = "Cual es la tasa de cambio de pesos a dolars oficial actualmente en Argentina? solamente el numero sin texto adicional"
    
    print  (f"Tasa de cambio obtenida: {respuesta.text.strip()} ARS/USD")  # Imprime la tasa obtenida para verificar

    try:
        return float(respuesta.text.strip())
    except ValueError:
        print("Error: No se pudo obtener una tasa de cambio válida.")
        return 0.0  # Retorna 0.0 en caso de error
    

def calcular_cotizacion_dolar(monto_dolar: float, tasa_cambio: float) -> float:
    """
    Convierte un monto en dólares a pesos argentinos usando una tasa específica.

    Args:
        monto_dolar: La cantidad de dólares a convertir.
        tasa_cambio: El valor actual del dólar en pesos (ej: 1000.0).

    Returns:
        El valor equivalente en pesos argentinos (ARS).
    """
    return monto_dolar * tasa_cambio


if __name__ == "__main__":
    if len(sys.argv) > 2:
        tasas = obtener_tasas_del_dia()
        tasa_cambio_dolar = tasas.get (sys.argv[2],0.0)  # Obtiene la tasa según el tipo especificado (oficial, blue, tarjeta
        if tasa_cambio_dolar == 0.0:
            print(f"Error: Tipo de cambio '{sys.argv[2]}' no reconocido. Opciones válidas: oficial, blue, tarjeta.")
        else:           
            pesos = calcular_cotizacion_dolar(float(sys.argv[1]), tasa_cambio_dolar)
            print(f"{sys.argv[1]} dólares equivalen a {pesos} pesos argentinos, a una tasa de cambio de {tasa_cambio_dolar} ARS/USD.")  
    else:
        print("Error: Por favor, ingresá un monto. Ejemplo: python herramientas.py 100 TIPO_CAMBIO (oficial, blue, tarjeta)")

# if __name__ == "__main__":
#     # sys.argv es una lista que contiene los argumentos de la terminal
#     # sys.argv[0] es siempre el nombre del archivo (herramientas.py)
#     # sys.argv[1] será el primer parámetro que escribas
#     #TASA_CAMBIO_DOLAR = 1450.0  # Ejemplo de tasa de cambio fija

#     if len(sys.argv) > 1:
#     #    monto_input = float(sys.argv[1]) # Convertimos el texto a número
#     #    resultado = aplicar_impuesto_pais(monto_input)
#     #    print(f"Monto ingresado: ${monto_input} -> Total con Impuesto: ${resultado}")
#         TASA_CAMBIO_DOLAR = obtener_tasa_cambio_dolar()  # Obtenemos la tasa de cambio actual
#         if TASA_CAMBIO_DOLAR == 0.0:
#             print("No se pudo obtener la tasa de cambio, no se realizará la conversión.")
#         else:
#             pesos = calcular_cotizacion_dolar(float(sys.argv[1]), TASA_CAMBIO_DOLAR)
#             print(f"{sys.argv[1]} dólares equivalen a {pesos} pesos argentinos, a una tasa de cambio de {TASA_CAMBIO_DOLAR} ARS/USD.")
#     else:
#         print("Error: Por favor, ingresá un monto. Ejemplo: python herramientas.py 100")

