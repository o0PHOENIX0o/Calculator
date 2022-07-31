print("\n\n\t\t\tWelcome To Calculator:\n")
while True:
    a=[str(a) for a in input('enter: ').split()]
    if len(a)==1:
        print('\n\t\t\twrong format \n\t please use spaces between the operator and operands\n')
    else:
        try:
            num1 = int(a[0])
            num2 = int(a[-1])
            symbol = a[1]
            if symbol.lower() in ['+','plus','add','sum']:
                print(num1+num2)
            elif symbol.lower() in ['-','min','minus','subtract','sub']:
                print(num1-num2)
            elif symbol.lower() in ['x','*','mul','multiply']:
                print(num1*num2)
            elif symbol.lower() in ['÷','/','div','divide' ]:
                print(num1/num2)              
        except Exception as e:
            print("\n\t\tdidn't undersatnd what you mean by: ")
            print('_'*60,end='')
            for i in range(len(a)):
                if i==0:
                    print('\n\t\t\t',end='')
                print(a[i],end=' ')
            print('\n','_'*60,end='')
            print('\n\n\t\ttry again')
