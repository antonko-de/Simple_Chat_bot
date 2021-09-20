def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    answer = ''
    while not answer == '2':
        answer = input("""Why do we use methods?\n1. To repeat a statement multiple times\n
2. To decompose a program into several small subroutines.\n
3. To determine the execution time of a program.\n
4. To interrupt the execution of a program.
""")
        if not answer == '2':
            print('Please try again.')
    print('Completed, have a nice day!')


def test2():
    print('One more question and we are off!')
    answer2 = ''
    while not answer2 == '3':
        answer2 = input("""What does IDE stand for?\n
1. International Design Environment.\n
2. Intern Development Engine.\n
3. Integrated Development Environment.\n
4. I Do Exercise.
""")
        if not answer2 == '3':
            print('Never, ever give up!')
    print('Congrats, you did it!')


def end():
    print('Congratulations, have a nice day!')


greet('Prime Pumpkin', '2021')  # change it as you need
remind_name()
guess_age()
count()
test()
test2()
end()
