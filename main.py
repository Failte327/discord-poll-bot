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

channelid = 978751904496631868

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('!Albion') and channel.id == channelid:
        print ('Albion Vote Received')
        albionVote = PollData(option='Albion', poll=atlaspoll)
        db.session.add(albionVote)
        db.session.commit()
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!Hibernia') and channel.id == channelid:
        print ('Hibernia Vote Received')
        hiberniaVote = PollData(option='Hibernia', poll=atlaspoll)
        db.session.add(hiberniaVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!Midgard') and channel.id == channelid:
        print ('Midgard Vote Received')
        midgardVote = PollData(option='Midgard', poll=atlaspoll)
        db.session.add(midgardVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!Count') and channel.id == channelid:
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!hib') and channel.id == channelid:
        print ('Hibernia Vote Received')
        hiberniaVote = PollData(option='Hibernia', poll=atlaspoll)
        db.session.add(hiberniaVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!hibernia') and channel.id == channelid:
        print ('Hibernia Vote Received')
        hiberniaVote = PollData(option='Hibernia', poll=atlaspoll)
        db.session.add(hiberniaVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!midgard') and channel.id == channelid:
        print ('Midgard Vote Received')
        midgardVote = PollData(option='Midgard', poll=atlaspoll)
        db.session.add(midgardVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!mid') and channel.id == channelid:
        print ('Midgard Vote Received')
        midgardVote = PollData(option='Midgard', poll=atlaspoll)
        db.session.add(midgardVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!alb') and channel.id == channelid:
        print ('Albion Vote Received')
        albionVote = PollData(option='Albion', poll=atlaspoll)
        db.session.add(albionVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)
    elif message.content.startswith('!albion') and channel.id == channelid:
        print ('Albion Vote Received')
        albionVote = PollData(option='Albion', poll=atlaspoll)
        db.session.add(albionVote)
        db.session.commit()
        channel = message.channel
        print(PollData.query.all())
        voteCountAlb = PollData.query.filter_by(option='Albion').count()
        voteCountHib = PollData.query.filter_by(option='Hibernia').count()
        voteCountMid = PollData.query.filter_by(option='Midgard').count()
        chart = discord.Embed(title='Atlas Launch Numbers', description='Pledge your realm allegiance with !Albion, !Hibernia, and !Midgard')
        chart.add_field(name = 'Albion', value=voteCountAlb, inline=False)
        chart.add_field(name = 'Hibernia', value=voteCountHib, inline=False)
        chart.add_field(name = 'Midgard', value=voteCountMid, inline=False)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(message.author, overwrite=overwrite)
        async for message in channel.history(limit=4000):
            await message.delete()
        await channel.send(embed = chart)

client.run('OTc3NDI2NDUwOTQyNjgxMTM4.GQ630h.mCVm7Nzn9Z8L-6yqEx0fm5dB_YnniXzKnKE3D8')