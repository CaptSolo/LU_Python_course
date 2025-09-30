import random

def guess_a_number():

    my_number = random.randint(1, 101)

    for i in range(7):

        try:
            user_guess = input("Ievadi skaitli no 1 līdz 100: ")
            user_guess_int = int(user_guess)

        except ValueError:
            print("Šis nav vesels skaitlis.")
            print()
            continue

        if user_guess_int < my_number:
            print("Ievadītais skaitlis ir pārāk mazs")
            print()
        
        elif user_guess_int > my_number:
            print("Ievadītais skaitlis ir pārāk liels")
            print()

        else:
            print("Uzminēji!")
            break


if __name__ == "__main__":
    print("Running as a script:")
    print()

    guess_a_number()

