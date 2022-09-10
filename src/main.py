import discord
import random


TOKEN = "TOKEN"

intents = discord.Intents.default()
intents.message_content = True



client = discord.Client(intents=intents)

@client.event
async def no_ready():
  print('we hava logged in as {0.user}'.format(client))
  
  
  
@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username} : {username} ({channel})')
  
  if message.author == client.user:
    return 
  
  
  if message.channel.name == 'chats':
    if user_message.lower() == 'hello':
      await message.channel.send(f'hello to {username}!')
      return 
    elif user_message.lower() == 'bay':
      await message.channel.send(f'see you {username}')
      return
    elif user_message.lower() == 'random':
      response = f'this is your number {random.randrange(100000)}'
      await message.channel.send(randrange)
      return
    
    
    
    if user_message.lower() == 'anywhere':
      await message.channel.send('no anywhere')
      return
    
    
    
client.run(TOKEN)
