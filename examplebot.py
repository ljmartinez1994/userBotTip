# importamos las librerías requeridas
from asyncio.windows_events import NULL
from logging import NullHandler
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
  
# App_ID, Api_Hash obtenidos desde web de Telegram de autorización de aplicación
appID = '8854348'
appAPIHash = 'e60c16ae50eb984fd0b3de638b5bbb16'
# Token del Bot de Telegram al que llegará el mensaje
tokenBot = '123456789:ABCDEFGHIJKLMNOPQRST'
# Mensaje que se enviará al chat del Bot de Telegram
mensaje1 = "Envío de mensaje desde aplicación Python a chat de bot de Telegram por ProyectoA, usando el ID de Chat 👍" 
mensaje2 = "Envío de mensaje desde aplicación Python a chat de bot de Telegram por ProyectoA, usando el nombre de usuario 👍"
# Número de telefóno móvil (incluyendo código de país)
numeroTelefono = '+34666777888'
# Nombre de usuario en Telegram al que se enviará el mensaje
nombreUsuarioTelegram = 'mi_usuario_telegram'
# O bien, si no queremos usar el nombre de usuario, el ID del chat al que se enviará el mensaje
idChat = '@ljmartinez'

print("Conectando con Telegram...")
# Creamos sesión de Telegram
clienteTelegram = TelegramClient('sesión', appID, appAPIHash)

print("Iniciando sesión en Telegram...")  
# Iniciamos una sesión de Telegram
clienteTelegram.connect()
 
# Si se ejecuta por primera vez, Telegram generará un código de inicio de sesión
# en el chat de Telegram "Telegram", si es así, la aplicación 
# pedirá este código de inicio de sesión
print("Comprobando autorización...")
if not clienteTelegram.is_user_authorized():
    clienteTelegram.send_code_request(numeroTelefono)
    # Pedimos el código de inicio de sesión que haya enviado Telegram al usuario
    try:
        clienteTelegram.sign_in(numeroTelefono, input('Introduzca el Código de inicio de sesión: '))
    except SessionPasswordNeededError:
        clienteTelegram.sign_in(numeroTelefono, input('Introduzca la contraseña: '))

# *** Enviar mensaje usando el ID de chat de Telegram ***
try:
    print("Creando un receptor de Telegram a partir del ID de chat de Tetlegram...")
    receptorChat = clienteTelegram.get_input_entity(idChat)
    async def main():
        # Enviamos el mensaje al chat de Telegram
        # Se enviará al chat de Telegram del Bot con ID indicado en el receptor
        print("Enviando mensaje a chat de Bot del receptor de Telegram (ID Chat)...")
        await clienteTelegram.send_message(receptorChat, mensaje1)
        #Solo a modo informativo, obtenemos el nombre del Bot de Telegram al que enviamos el mensaje
        print("Enviado mensaje a chat de Bot [{}] de Telegram".format(idChat))
        
    # Para que se ejecute la tarea anterior del método asíncrono
    clienteTelegram.loop.run_until_complete(main()) 

except Exception as e:
    print("Se ha producido un error en el envío por ID de Chat: {}".format(e));

# *** Enviar mensaje usando nombre de usuario de Telegram ***
try:    
    print("Creando un receptor de Telegram a partir del nombre de usuario de Tetlegram...")
    receptorNombre = clienteTelegram.get_input_entity(nombreUsuarioTelegram)
    
    async def main():
        # Enviamos el mensaje al chat de Telegram
        # Se enviará al chat de Telegram del Bot con el usuario indicado en el receptor
        print("Enviando mensaje a chat de Bot del receptor de Telegram (usuario)...")
        await clienteTelegram.send_message(receptorNombre, mensaje2)
        print("Enviado mensaje a chat de Bot del receptor [{}] de Telegram".format(nombreUsuarioTelegram))

    clienteTelegram.loop.run_until_complete(main()) # Para que se ejecute la tarea anterior del método asíncrono

except Exception as e:
    print("Se ha producido un error en el envío por nombre de usuario: {}".format(e));

# Desconectamos la sesión de Telegram abierta
print("Desconectando sesión de Telegram...")
clienteTelegram.disconnect()
print("Desconectado y fin del programa")