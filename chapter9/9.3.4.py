import re

separator=re.compile('\|')

annotation = 'ATOM:CA|RES:ALA|CHAIN:B|NUMRES:166'

columns=separator.split(annotation)

new_annotation=separator.sub('@',annotation,2)

print(columns)

print(new_annotation)