def invalid_transactions(transactions):
    parsed = []
    for i, t in enumerate(transactions):
        name, time, amount, city = t.split(',')
        parsed.append({
            'index': i,
            'name': name,
            'time': int(time),
            'amount': int(amount),
            'city': city,
            'original': t
        })

    invalid = set()

    for i in range(len(parsed)):
        t1 = parsed[i]

        if t1['amount'] > 1000:
            invalid.add(t1['index'])

        for j in range(len(parsed)):
            if i == j:
                continue

            t2 = parsed[j]

            if t1['name'] == t2['name'] and t1['city'] != t2['city']:
                if abs(t1['time'] - t2['time']) <= 60:
                    invalid.add(t1['index'])
                    invalid.add(t2['index'])

    return [transactions[i] for i in sorted(invalid)]

print(invalid_transactions(["alice,20,800,mtv","alice,50,100,beijing"]))