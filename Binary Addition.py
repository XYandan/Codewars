def add_binary(a,b):
    num=a+b
    la=[]
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        la.append(str(remainder))
        if num == 0:
            return ''.join(la[::-1])
