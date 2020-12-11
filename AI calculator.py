
'''
----- PLEASE INSTALL THIS PACKAGES IN YOUR TARMINAL OR IDE -----

PIP INSTALL MYWIN32
PIP INSTALL DISPATCH

'''


#
# THIS IS A ARTIFICIAL CALCULATOR,
#
# THIS IS A ONLY FOR FUN....

# CREATED BY MR.HACKER - (JUNAID AHAMAD)



def speak(str):

    from win32com.client import Dispatch

    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)       # This is a speak function, i am using this all time in coding..


speak('hello sir, i am assistant of Junaid sir,')
speak('sir, this is security purpose, please enter password for opening this...')
print("\t\t\tPASSWORD - EVEN DEAD I AM THE HERO")
speak(' Please enter this password in capital latter, which is being displayed on your smart Screen')
hero_id =input("PASSWORD: ")

while True:
    if 'EVEN DEAD I AM THE HERO' == hero_id:
        speak('Welcome sir')
        speak('sir, i am solving your problem in calculator.. let\'s start ')
        print('\n\n')
        # Driver code.........
        if __name__ == '__main__':
            # a = int(input("Enter the first number"))
            # speak(a)
            # b = int(input("Enter the second number"))
            # speak(b)
            # c = a * b
            # speak(f'{a} of {b} multiply is ')
            # # print(c)
            # speak(c)
            print("\t\t\t---THIS IS A ARTIFICIAL CALCULATOR---")
            speak("sir, enter your first number ")
            print('\n')
            first_number = float(input('Enter Your First Number: '))
            speak("sir, enter your second number")
            Second_number = float(input('Enter your second number: '))
            print('+,-,*,/,**,%')
            speak("sir, choose your Arithmatic operation amongst any of the operation which is being displayed on your smart Screen ")
            arithmatic_op = input("Enter arithmatic operation: ")
            if arithmatic_op == '+':
                result = first_number + Second_number
                speak(f'{first_number} + {Second_number} is')
                print(result)
                speak(result)
            elif arithmatic_op == '-':
                result1 = first_number - Second_number
                speak(f'{first_number} - {Second_number} is')
                print(result1)
                speak(result1)
            elif arithmatic_op == '*':
                result2 = first_number * Second_number
                speak(f'{first_number} * {Second_number} is')
                print(result2)
                speak(result2)
            elif arithmatic_op == '/':
                result3 = first_number / Second_number
                speak(f'{first_number} / {Second_number} is')
                print(result3)
                speak(result3)
            elif arithmatic_op == '**':
                result4 = first_number ** Second_number
                speak(f'{first_number} % {Second_number} is')
                print(result4)
                speak(result4)
            elif arithmatic_op == '%':
                result5 = first_number % Second_number
                speak(f'{first_number} % {Second_number} is')
                print(result5)
                speak(result5)
            else:
                speak("Your input is not correct, please try again...")
    else:
        speak("sorry sir, this password is wrong")
        break

