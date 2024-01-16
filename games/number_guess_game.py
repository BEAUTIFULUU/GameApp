import random


def validate_num_range_and_generate_random_num(frst_num: int, scn_num: int) -> int:
    while True:
        if (
            1 <= frst_num <= 100
            and 1 <= scn_num <= 100
            and scn_num > frst_num
            and scn_num - frst_num >= 10
        ):
            print("Given range is valid, generating random number...")
            random_num = random.randint(frst_num, scn_num)
            return random_num

        else:
            print("Invalid number range.")
            frst_num = int(input("Select number from 1 to 100: "))
            scn_num = int(
                input("Select number from 1 to 100 bigger than the first one: ")
            )


def guess_the_number(num_rng: tuple, random_nm: int, max_guesses: int = 7) -> int:
    print(f"Numbers range is: {num_rng}.")
    guesses = 0

    while True:
        guess_num = int(input("Guess the number: "))
        guesses += 1
        guesses_left = max_guesses - guesses

        if num_rng[0] <= guess_num <= num_rng[1] and guesses_left > 0:
            diff = guess_num - random_nm

            if guess_num > random_nm and 0 < diff <= 5:
                print(
                    f"Guessed number is too big but it's very hot! You have {guesses_left} left."
                )

            elif guess_num > random_nm and diff > 5:
                print(
                    f"Guessed number is too big and it's cold! You have {guesses_left} left."
                )

            elif guess_num < random_nm and 0 > diff >= -5:
                print(
                    f"Guessed number is too small but it's very hot! You have {guesses_left} left."
                )

            elif guess_num < random_nm and diff < -5:
                print(
                    f"Guessed number is too small and it's cold! You have {guesses_left} left."
                )

            elif guess_num == random_nm:
                print(
                    f"Congratulations, You guessed correctly! Guesses left: {guesses_left}"
                )
                return guesses_left

        elif guesses_left == 0:
            print("No chances left. Try again!")
            break

        else:
            print("Try again!")


def number_guess_game(first_num: int, second_num: int) -> int:

    rnd_num = validate_num_range_and_generate_random_num(
        frst_num=first_num, scn_num=second_num
    )
    result = guess_the_number(num_rng=(first_num, second_num), random_nm=rnd_num)
    return result
