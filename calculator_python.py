number1=int(input('what is your first number:'))
number2=int(input('what is your second number:'))
opertaor=input('what operation do you want to chose(+\-\*\/):')
if opertaor=='+':
    sum=number1+number2
    print(f'{number1} + {number2} = {sum}')
elif opertaor=='-':
    sub=number1-number2
    print(f'{number1} - {number2} = {sub}')
elif opertaor=='*':
    multiply=number1*number2
    print(f'{number1} * {number2} = {multiply}')
elif opertaor=='/':
    div=number1/number2
    print(f'{number1} / {number2} = {div}')
else:
    print('write the correct operator')
    