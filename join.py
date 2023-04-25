import json
with open('5.7.json') as f:
    p57= json.load(f)

with open('8.0.json') as f:
    p8= json.load(f)

for p in p57:
    p57_name = p['Name']
    