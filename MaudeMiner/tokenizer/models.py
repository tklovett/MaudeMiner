from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from MaudeMiner.database import db
from MaudeMiner.database.base import base


# def create():
# 	print "Creating Tables: "
# 	base.metadata.create_all(db.engine)
# 	print "OK"

# def drop():
# 	print "Dropping Tables: "
# 	base.metadata.drop_all(db.engine)
# 	print "OK"

Contains_Token = Table('Contains_Token', base.metadata,
	Column('report_key', Integer, ForeignKey('Narratives.report_key')),
	Column('token_id', Integer, ForeignKey('Tokens.id'))
)

class Token(base):
	__tablename__ = "Tokens"

	id             = Column(Integer, primary_key=True, autoincrement=True)
	word           = Column(String)
	part_of_speech = Column(String)

	# narratives = relationship("Narrative", secondary=Contains_Token)
	narratives = relationship("Narrative",
        secondary=Contains_Token,
        backref="tokens")

	def __init__(self, word=None, part_of_speech=None):
		self.word = word
		self.part_of_speech = part_of_speech

	def __repr__(self):
		return "<Token('%s','%s')>" %(self.word, self.part_of_speech)

