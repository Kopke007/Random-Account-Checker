import random

def generate_random_token():
    token = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-', k=72))
    return token

for i in range(135):
    random_token = generate_random_token()
    Ttokens = open("tryTokens.txt", "a")
    Ttokens.write(f'{random_token} \n') 
