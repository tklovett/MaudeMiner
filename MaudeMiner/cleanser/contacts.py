from MaudeMiner.core.database import db
from MaudeMiner.core.models import Contact, Event
from sqlalchemy import or_

from MaudeMiner.cleanser.utils import remove_punctuation, normalize_whitespace, unabbreviate
from MaudeMiner.cleanser.utils import address_abbreviations, name_abbreviations


def cleanse():
	print("Cleansing contacts...")
	session = db.get_session()
	q = session.query(Contact)
	q = q.filter(or_(Contact.name != "", Contact.street_1 != ""))
	
	for contact in q:
		# Clean name
		contact.name = remove_punctuation(contact.name)
		contact.name = normalize_whitespace(contact.name)
		contact.name = unabbreviate(contact.name, name_abbreviations)
		
		# Clean street_1
		contact.street_1 = remove_punctuation(contact.street_1)
		contact.street_1 = normalize_whitespace(contact.street_1)
		contact.street_1 = unabbreviate(contact.street_1, address_abbreviations)
		
		session.flush() # TODO not flush this often? is it necessary?
	session.commit()

	print "Done"


if __name__ == '__main__':
	run()