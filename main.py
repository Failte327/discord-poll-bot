from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db
from config import Poll
from config import PollData
from config import atlaspoll
import asyncio
import discord
from discord.ext import commands
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\sqlite\\library.db'

client = discord.Client()

emb = discord.Embed(title='Atlas Launch Numbers')
emb.add_field(name = 'Albion', value='', inline=False)
emb.add_field(name = 'Hibernia', value='\n', inline=False)
emb.add_field(name = 'Midgard', value='\n', inline=False)

@client.event
async def on_message(message):
    if message.content.startswith('!Albion'):
        print ('Albion Vote Received')
        albionVote = PollData(option='Albion', poll=atlaspoll, user_id=message.author.id)
        db.session.add(albionVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        await channel.send('Vote Received!')
    elif message.content.startswith('!Hibernia'):
        print ('Hibernia Vote Received')
        hiberniaVote = PollData(option='Hibernia', poll=atlaspoll, user_id=message.author.id)
        db.session.add(hiberniaVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        await channel.send('Vote Received!')
    elif message.content.startswith('!Midgard'):
        print ('Midgard Vote Received')
        midgardVote = PollData(option='Midgard', poll=atlaspoll, user_id=message.author.id)
        db.session.add(midgardVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        await channel.send('Vote Received!')

client.run('OTc3NDI2NDUwOTQyNjgxMTM4.GQ630h.mCVm7Nzn9Z8L-6yqEx0fm5dB_YnniXzKnKE3D8')