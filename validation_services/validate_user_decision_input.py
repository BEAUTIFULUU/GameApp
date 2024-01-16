def get_valid_input(prompt: str, error_message: str) -> int | str:
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print(error_message)
