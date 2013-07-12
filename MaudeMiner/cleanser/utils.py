from string import translate

address_abbreviations = {
	"BLDG": "BUILDING",
	"&": "AND",
	"STE": "SUITE",
	"INTL": "INTERNATIONAL",
	"DEPT": "DEPARTMENT",
	"CTR": "CENTER",
	# street types
	"RD": "ROAD",
	"ST": "STREET",
	"AVE": "AVENUE",
	"BLVD": "BOULEVARD",
	"RT": "ROUTE",
	"DR": "DRIVE",
	"PL": "PLACE",
	"LN": "LANE",
	"CT": "COURT",
	"CIR": "CIRCLE",
	"PKWY": "PARKWAY",
	"PWY": "PARKWAY",
	"HWY": "HIGHWAY",
	# cardinal directions
	"N": "NORTH",
	"NW": "NORTHWEST",
	"W": "WEST",
	"SW": "SOUTHWEST",
	"S": "SOUTH",
	"SE": "SOUTHEAST",
	"E": "EAST",
	"NE": "NORTHEAST",
}

name_abbreviations = {
	"DIV": "DIVISION",
	"INTL": "INTERNATIONAL",
	"INC": "INCORPORATED",
	"CORP": "CORPORTATION",
	"LTD": "LIMITED",
	"CO": "COMPANY",
	"MFG": "MANUFACTURING",
}

def unabbreviate(field, abbreviations):
	words = field.split(' ')
	for i in range(len(words)):
		if words[i] in abbreviations:
			words[i] = abbreviations[words[i]]
	return ' '.join(words)

def remove_punctuation(field, replace=' '):
	punctuation_chars = u"-,./()"

	unicode_replace = unicode(replace)
	punctuation_map = dict.fromkeys(map(ord, punctuation_chars), unicode_replace)
	return field.translate(punctuation_map)

def normalize_whitespace(field):
	return " ".join(field.split())
