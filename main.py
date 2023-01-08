import discord
import subprocess

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
  # check if the message is a command
  if message.content.startswith('!c'):
    # execute the command and get the output
    command = message.content[2:]
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    response = output.stdout.decode()

    # send the response back to Discord as a message
    await message.channel.send(response)

client.run('BOT_TOKEN')
