from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

class PollData(db.Model):
    # Initialize the Column
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
    option = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)

    # Initialize the relationship
    poll = db.relationship('Poll', backref=db.backref('polldata', lazy=True))

    # For displaying our database record rather than just numbers
    def __repr__(self):
        return '<Option %r>' % self.option

db.create_all()

atlaspoll = Poll(name='What realm will you play on Atlas Launch')

option = PollData(option='Albion', poll=atlaspoll, user_id=1)
option = PollData(option='Hibernia', poll=atlaspoll, user_id=1)
option = PollData(option='Midgard', poll=atlaspoll, user_id=1)

db.session.add(atlaspoll)
db.session.add(option)

db.session.commit()

print(PollData.query.all())