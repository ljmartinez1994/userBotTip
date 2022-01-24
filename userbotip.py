import asyncio 
import sys
import logging
import telethon.sync
from telethon import TelegramClient, events, sync, functions, types

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 8854348
api_hash = 'e60c16ae50eb984fd0b3de638b5bbb16'

client = TelegramClient('vdelavega', api_id, api_hash)

async def do_something(me):
  # "me" is a user object. You can pretty-print
  # any Telegram object with the "stringify" method:
  print(me.stringify())

  # When you print something, you see a representation of it.
  # You can access all attributes of Telegram objects with
  # the dot operator. For example, to get the username:
  username = me.username
  print(username)
  print(me.phone)
  
  # You can, of course, use markdown in your messages:
  message = await client.send_message(
            'me',
            'This message has **bold**, `code`, __italics__ and '
            'a [nice website](https://example.com)!',
            link_preview=False
        )
  
  # You can reply to messages directly if you have a message object
  await message.reply('Cool!')


async def main():
  #await client.start() 
  async with client:
    client.run_until_disconnected() 
    #print((await client.get_me()).stringify())
    #await client.send_message('ljmartinez', 'Hello! Talking to you from Telethon')
    me = await client.get_me()
    await do_something(me)

#asyncio.run(main())
#asyncio.get_event_loop().run_until_complete(main())
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
@client.on(events.NewMessage)
async def receive_message(event):
  print ("ENTROOOOOOOOOOOOOOOOO")
  if 'hello' in event.raw_text:
        await event.reply('hi!')  

#client.run_until_disconnected();    
asyncio.run(main())