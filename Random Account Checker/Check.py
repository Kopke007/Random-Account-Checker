import random
import requests

def check_token(token):
    headers = {
        'Authorization': f'{token}'
    }
    url = 'https://discord.com/api/v9/users/@me'
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True  
        else:
            return False  
    except Exception as e:
        print(f'An error occured: {str(e)}')
        return False

def check_tokens_from_file(filename):
    try:
        with open(filename, 'r') as file:
            tokens = file.readlines()
            for token in tokens:
                token = token.strip()  
                if check_token(token):
                    print(f'{token} IS VALID!')
                    with open("Tokens.txt", "a") as Tokens:
                        Tokens.write(f'{token}\n')
                else:
                    print(f"{token} is not valid")

    except FileNotFoundError:
        print(f"{filename} can not finded.")

if __name__ == "__main__":
    while True:
        check_tokens_from_file('tryTokens.txt')
