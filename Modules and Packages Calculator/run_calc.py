from addition import add
from subtraction import subtract

ops = {'+': add.add,
       '-': subtract.subtract}

def main():
    a, op, b = input().split()
    a, b = map(int, (a, b))
    print(ops[op](a, b))

if __name__ == '__main__':
    main()