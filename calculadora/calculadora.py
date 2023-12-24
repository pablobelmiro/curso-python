import os

print("========")
operations = {
    '+': 'sum',
    '-': 'sub',
    '/': 'div',
    '*': 'mult',
    '^': 'expo'
}

while True:
    cmd = 'clear'
    os.system(cmd)
    i = 0
    for op, name in operations.items():
        print(i, ':', name)
        i += 1
    print("")
    print("Choose the operation:")
    op = int(input())
    op_str = list(operations.items())[op]
    print("")
    print("{} choosed.".format(op_str[1]))
    print("")
    print("")
    print("tell me the first value")
    v1 = float(input())
    print("tell me the second value")
    v2 = float(input())

    match op:
        case 0:
            result = v1 + v2
        case 1:
            result = v1 - v2
        case 2:
            result = v1 / v2
        case 3:
            result = v1 * v2
        case 4:
            result = v1 ** v2
    print("")
    print('the result of {} between {} and {} is = {}'.format(op_str[1], v1, v2, result))
    print("")
    print("want to make another operation? [y|n]")
    flag = input()

    if(flag == 'n' or flag == 'N'):
        print("Goodbye ;D")
        break
    else:
        continue
