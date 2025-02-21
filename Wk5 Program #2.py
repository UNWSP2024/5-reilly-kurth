import random

#get numbers
def added_numbers():
    num1 = random.randint(1,1000)
    num2 = random.randint(1, 1000)
    return num1, num2

#find answer and get student answer
def answer_check(num1, num2, students_answer):
    correct = num1 + num2
    if students_answer == correct:
        return True, correct
    else:
        return False, correct


#display and input
def finish():
    num1, num2 = added_numbers()
    print(f"{num1}\n + {num2}\n------")
    students_answer = int(input("Enter your answer:"))

    is_correct, correct = answer_check(num1, num2, students_answer)
    if is_correct:
        print("Congratulations!")
    else:
        print("The correct answer is", correct)

if __name__ == "__main__":
    finish()
