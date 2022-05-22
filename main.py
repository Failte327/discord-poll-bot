from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db
from config import Poll
from config import PollData
from config import atlaspoll
import asyncio
import discord

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\sqlite\\library.db'

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!Albion'):
        print ('Albion Vote Received')
        userid = message.author.id
        albionVote = PollData(option='Albion', poll=atlaspoll, user_id=userid)
        db.session.add(albionVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        await channel.send(embed = chart)
    elif message.content.startswith('!Hibernia'):
        print ('Hibernia Vote Received')
        userid = message.author.id
        hiberniaVote = PollData(option='Hibernia', poll=atlaspoll, user_id=userid)
        db.session.add(hiberniaVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        await channel.send(embed = chart)
    elif message.content.startswith('!Midgard'):
        print ('Midgard Vote Received')
        userid = message.author.id
        midgardVote = PollData(option='Midgard', poll=atlaspoll, user_id=userid)
        db.session.add(midgardVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        await channel.send(embed = chart)

client.run('OTc3NDI2NDUwOTQyNjgxMTM4.GQ630h.mCVm7Nzn9Z8L-6yqEx0fm5dB_YnniXzKnKE3D8')