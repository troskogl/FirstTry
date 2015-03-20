# Author: Oyvind Ellefsen
# Version 0.1

import os
import jinja2
import csv

TEMPLATE_FILENAME = 'cisco.j2'
CSVDATA_FILENAME = 'data.csv'

def get_data(row):

	# Hent data fra csv filen

	data_fields = {
		field_name: field_value
		for field_name, field_value in row.items()
	}

## ---------------------------------------------------------------------------
## Sett opp Jinja2 og hent template
## ---------------------------------------------------------------------------

env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.getcwd()),
	trim_blocks=True, lstrip_blocks=True)

template = env.get_template(TEMPLATE_FILENAME)

## ---------------------------------------------------------------------------
## Les CSV og fyll inn data for hver linje
## ---------------------------------------------------------------------------

for row in csv.DictReader(open(CSVDATA_FILENAME)):
	get_data(row)
	with open(row['HOSTNAME'] + '.txt', 'w+') as f:
		f.write(template.render(row))

##
## all done!
##