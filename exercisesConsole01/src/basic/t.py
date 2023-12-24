def f3():
    import sys
#    for line in sys.stdin:
#       yield line.strip('\n')
    print('leer  line')
    for line in sys.stdin:
        print('antes del if')
        if 'exit' == line.strip('\n'):
            break
        print(f'Processing Message from sys.stdin *****{line}*****')
        yield line.strip('\n')
        print(f'Processing yield *****{line}*****')
    print("Done")
#    line1 = lines.next()
#    print(line1)

def f2():
    import sys
    import re
    """ for x in range(10):
        print(x)
    
    s_strs = 'oneXXXtwoYYYthreeZZZfour'
    print(re.split('XXX|YYY|ZZZ', s_strs))
    
    s_strs = '10000010001'
    t=tuple(re.split('1+', s_strs))
    print(t[1])
    """
    
    for i in range(-2, 2):
        print(i)

def f1():
    import sys
#    for line in sys.stdin:
#       yield line.strip('\n')
    for line in sys.stdin:
        if 'exit' == line.strip('\n'):
            break
        print(f'Processing Message from sys.stdin *****{line}*****')
    print("Done")
#    line1 = lines.next()
#    print(line1)
    
def main():
    obj = f3()
    print(f'Processing Message from sys.stdin *****{next(obj)}*****')


if __name__ == '__main__':
    main()

