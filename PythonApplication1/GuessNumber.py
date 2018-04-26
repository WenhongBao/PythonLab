theNumber=input('Input the number and call another person to guess: ');
go=True;

while go:
    guessNumber=input('Input the number you guess: ');
    if guessNumber == theNumber:
        print('Congratulations!!!!');
        go=False;
    elif guessNumber < theNumber:
        print('Too small');
    else:
        print('Too big');
else:
    print('Finish');