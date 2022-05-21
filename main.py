from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db
from config import Poll
from config import PollData
from config import atlaspoll
import discord

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\sqlite\\library.db'

client = discord.Client()

@client.event
async def vote(message):
    if message.content.startswith('!Albion'):
        albionVote = PollData(option='Albion', poll=atlaspoll, user_id=message.author.id)
        await db.session.add(albionVote)
        db.session.commit()
    elif message.content.startswith('!Hibernia'):
        hiberniaVote = PollData(option='Hibernia', poll=atlaspoll, user_id=message.author.id)
        await db.session.add(hiberniaVote)
        db.session.commit()
    elif message.content.startswith('!Midgard'):
        midgardVote = PollData(option='Midgard', poll=atlaspoll, user_id=message.author.id)
        await db.session.add(hiberniaVote)
        db.session.commit()

