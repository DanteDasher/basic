"""
dec > bin
dec > oct
dec > hex
bin > dec
bin > oct
bin > hex
oct > dec
oct > bin
hex > dec
hex > bin

"""
while True:
    o = input('Opções \n1 - dec > bin \n2 - dec > oct \n3 - dec > hex \n4 - bin > dec')
    if o == '1':
        r = ''
        n = int(input('Digite o valor:'))
        while True:
            t = str(n % 2)
            n = n / 2
            r = t[0] + r
            if n < 2:
                r = str(n)[0] + r
                break
        print(r)
    if o == '2':
        r = ''
        n = int(input('Digite o valor:'))
        while True:
            t = str(n % 8)
            n = n / 8
            r = t[0] + r
            if n < 8:
                r = str(n)[0] + r
                break
        print(r)
    if o == '3':
        r = ''
        n = int(input('Digite o valor:'))
        while True:
            t = str(n % 16)
            n = n / 16
            if t == '10':
                r = 'A' + r
            elif t == '11':
                r = 'B' + r
            elif t == '12':
                r = 'C' + r
            elif t == '13':
                r = 'D' + r
            elif t == '14':
                r = 'E' + r
            elif t == '15':
                r = 'F' + r
            else:
                r = t[0] + r
            if n < 16:
                if n == '10':
                    r = 'A' + r
                elif n == '11':
                    r = 'B' + r
                elif n == '12':
                    r = 'C' + r
                elif n == '13':
                    r = 'D' + r
                elif n == '14':
                    r = 'E' + r
                elif n == '15':
                    r = 'F' + r
                else:
                    r = str(n)[0] + r
                
                break
        print(r)
    if o == '4':
        z = 0
        n = input('Digite o valor:')
        while True:
            tc = n.count('')
            ca = 2
            for c in range (0,tc-1,1):
                ni = int(n[tc - ca])
                z = z + ((2**c) * ni)
                ca = ca + 1
            print(z)
            break





    if o == 'q':
        break