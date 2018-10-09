import re

separator=re.compile('\|')

annotation = 'ATOM:CA|RES:ALA|CHAIN:B|NUMRES:166'

columns=separator.split(annotation)

print(columns)