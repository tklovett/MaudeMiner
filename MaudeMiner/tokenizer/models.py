from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from MaudeMiner.database import db
from MaudeMiner.database.base import base


Contains_Token = Table('Contains_Token', base.metadata,
	Column('report_key', Integer, ForeignKey('Narratives.report_key')),
	Column('token_id', Integer, ForeignKey('Tokens.id'))
)

class Token(base):
	__tablename__ = "Tokens"

	id             = Column(Integer, primary_key=True, autoincrement=True)
	word           = Column(String)
	part_of_speech = Column(String)

	narratives = relationship("Narrative",
        secondary=Contains_Token,
        backref="tokens")

	def __init__(self, word=None, part_of_speech=None):
		self.word = word
		self.part_of_speech = part_of_speech

	def __repr__(self):
		return "<Token('%s','%s')>" %(self.word, self.part_of_speech)


class Word(base):
	__tablename__ = "Words"
	id        = Column(Integer, primary_key=True, autoincrement=True)
	word      = Column(String)
	frequency = Column(Integer)

	def __init__(self, word=None, frequency=0):
		self.word = word
		self.frequency = frequency
	
	def __repr__(self):
		return "<Word('{0}', '{1}')>".format(self.word, self.frequency)

