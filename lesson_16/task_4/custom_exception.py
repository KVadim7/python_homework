class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as file:
            file.write(f'Error: {msg}\n')


try:
    raise CustomException('Custom error')
except CustomException as a:
    print(f"This is {a}")
