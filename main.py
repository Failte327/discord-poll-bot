from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import discord


client = discord.Client()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\sqlite\\library.db'

db = SQLAlchemy(app)
db.init_app(app)

class Poll(db.Model):
    # Initialize the Column
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # For displaying our database record rather than just numbers
    def __repr__(self):
        return '<Poll %r>' % self.name

class VotingOption(db.Model):
    # Initialize the Column
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
    option = db.Column(db.String(100), nullable=False)

    # Initialize the relationship
    poll = db.relationship('Poll', backref=db.backref('votingoptions', lazy=True))

    # For displaying our database record rather than just numbers
    def __repr__(self):
        return '<Option %r>' % self.option

atlaspoll = Poll(name='Atlas Launch Realm')
option = VotingOption(option='Midgard', poll=atlaspoll)
option = VotingOption(option='Hibernia', poll=atlaspoll)
option = VotingOption(option='Albion', poll=atlaspoll)

db.session.add(atlaspoll)
db.session.add(option)

db.session.commit()

print(VotingOption.query.all())