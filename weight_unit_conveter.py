weight=int(input('what is your weight'))
unit=input("is your weight is in lbs or kgs ")
if unit == 'kg' or unit == 'KG' or unit == 'Kg':
    weight1=weight*2.2
    print(f'{weight1} is your weight in lbs')
elif unit == 'lbs' or unit == 'LBS' or unit == 'LBs' or unit == 'Lbs':
    weight2=weight/2.2
    print(f'{weight2} is nyour weight in kgs')
else:
    print('your input is not corect')
