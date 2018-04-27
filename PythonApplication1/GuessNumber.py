#get the number which will be guess
Number=input('Input the number and call another person to guess: ');
#change the type from str to int
theNumber=int(Number);
#define the go as ture
go=True;

#start the while loop
while go:
    #get the number which use to guess
    guessNumber=input('Input the number you guess: ');
    #change the type from str to int
    getGuessNumber=int(guessNumber);
    #start if
    if getGuessNumber == theNumber:
        print('Congratulations!!!!');
        go=False;
    elif getGuessNumber < theNumber:
        print('Too small');
    else:
        print('Too big');
    #close if
else:
    print('Finish');
#close while