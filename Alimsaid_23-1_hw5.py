data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

for i in data:
    if i.isnumeric():
        codes.append(i)
    else:
        designations.append(i)

operators = {}
i = 0
while i < len(codes):
    operators[designations[i]] = {codes[i]}
    i += 1

operators.pop('Katel')
operators.pop('Fonex')
operators['O!'].add('0504')
operators['O!'].add('0708')
operators['Beeline'].add('0222')
operators['Beeline'].add('0774')
operators['Megacom'].add('0775')
operators['Megacom'].add('0557')
print(operators)
for key,  value in operators.items():
    print(f"{key} - {value}")
