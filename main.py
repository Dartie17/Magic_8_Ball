import random
import answers
from time import sleep

sleep(1)
print("Привет... Я магический шар... И я знаю ответ на любой твой вопрос...")
print()

sleep(1)
print("Скажи мне, как тебя зовут?")
print()

name = input()
print()

sleep(1)
print("Привет,", name + "...")
print()


def magic_8_ball():
    sleep(1)
    print("Задавай свой вопрос...")
    print()

    input()
    print()

    sleep(3)
    print(random.choice(answers.ans))
    print()


magic_8_ball()

while 1 == 1:
    sleep(1)
    print("Хочешь задать еще вопрос?")
    print()

    sleep(1)
    answer = input()
    print()

    if answer.lower() == "да":
        magic_8_ball()
    else:
        sleep(1)
        print("Как знаешь...")
        break