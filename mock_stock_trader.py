cash = 10000.0
stock = 0.0
last_value = None

f = open('V.csv')
for line in f.readlines()[::-1][:-1][100:]:
    line = line.split(',')
    date = line[0]
    value = float(line[1])
    if last_value:
        stock = stock / last_value * value
    last_value = value
    print date, value, "cash:", cash, "stock:", stock, "total", cash + stock
    variable = raw_input()
    command = variable.split()
    if len(command) != 2:
        continue
    if command[0] == 'b':
        sign = 1
    elif command[0] == 's':
        sign = -1
    amount = sign * float(command[1])
    if cash - amount < 0 or stock + amount < 0:
        print "failed"
        continue
    cash -= amount
    stock += amount

