inp=open('input').read().strip()
rules, data = inp.split('\n\n')
parsed_rules = []
for rule in rules.split('\n'):
	parsed_rules.append(rule.split('|'))
parsed_data = []
for row in data.split('\n'):
	parsed_data.append(row.split(','))
total = 0
for parsed_row in parsed_data:
	total += all(rule[0] not in parsed_row or rule[1] not in parsed_row or parsed_row.index(rule[0])<parsed_row.index(rule[1]) for rule in parsed_rules) and \
		int(parsed_row[len(parsed_row)//2])
print(total)
