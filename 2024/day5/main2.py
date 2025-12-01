inp=open('input').read().strip()
rules, data = inp.split('\n\n')
parsed_rules = []
for rule in rules.split('\n'):
	parsed_rules.append(rule.split('|'))
parsed_data = []
for row in data.split('\n'):
	parsed_data.append(row.split(','))
total = 0
cmp_rules={}
def rules_for_data(dat):
	for rule in parsed_rules:
		if rule[0] in dat and rule[1] in dat:
			yield rule
for rule in parsed_rules:
	cmp_rules[tuple(rule)]=1
import random
for parsed_row in parsed_data:
	if all(rule[0] not in parsed_row or rule[1] not in parsed_row or parsed_row.index(rule[0])<parsed_row.index(rule[1]) for rule in parsed_rules):
		continue
	filtered_rules = list(rules_for_data(parsed_row))
	while 1:
		unbroken = True
		for rule in filtered_rules:
			x,y=rule
			if x in parsed_row and y in parsed_row:
				ofx,ofy = parsed_row.index(x), parsed_row.index(y)
				if ofx < ofy:parsed_row[ofx], parsed_row[ofy] =  parsed_row[ofy], parsed_row[ofx];unbroken = False
		if unbroken:total += int(parsed_row[len(parsed_row)//2]); break
print(total)
