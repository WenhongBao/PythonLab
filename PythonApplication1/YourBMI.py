#get height and weight
getHeight=input('Please input your height(M): ');
getWeight=input('Please input your weight(KG): ');

#change then from str to float
height=float(getHeight);
weight=float(getWeight);

#count BMI
BMI=weight/(height**2);
#print the BMI
print('Your BMI is: ',BMI);

#start if
if BMI<18.5:
    print('Too Thin');
elif BMI<25:
    print('Good');
elif BMI<28:
    print('A little Fat');
elif BMI<32:
    print('Fat');
else:
    print('Too Fat!!');

print('Finish');