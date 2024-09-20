import random
import string

def banner():
    print(f'''
  /$$$$$$                                                    /$$$$$$$                               /$$$$$$                     
 /$$__  $$                                                  | $$__  $$                             /$$__  $$                    
| $$  \__/  /$$$$$$   /$$$$$$$ /$$   /$$  /$$$$$$   /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$$ /$$$$$$$| $$  \__/  /$$$$$$  /$$$$$$$ 
|  $$$$$$  /$$__  $$ /$$_____/| $$  | $$ /$$__  $$ /$$__  $$| $$$$$$$/|____  $$ /$$_____//$$_____/| $$ /$$$$ /$$__  $$| $$__  $$
 \____  $$| $$$$$$$$| $$      | $$  | $$| $$  \__/| $$$$$$$$| $$____/  /$$$$$$$|  $$$$$$|  $$$$$$ | $$|_  $$| $$$$$$$$| $$  \ $$
 /$$  \ $$| $$_____/| $$      | $$  | $$| $$      | $$_____/| $$      /$$__  $$ \____  $$\____  $$| $$  \ $$| $$_____/| $$  | $$
|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$| $$     |  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$
 \______/  \_______/ \_______/ \______/ |__/       \_______/|__/      \_______/|_______/|_______/  \______/  \_______/|__/  |__/
                                                                                                                
                                                        
                                                \033[32mby midnight_mihir\033[0m
          ''')
    
banner()

def password():
    while True:
        user_input = input("Enter the Length of your password or type 'quit' to exit: ")
        if user_input.lower() == "quit":
            print("Thanks.!")
            print("Exiting the program...")
            break
        try:
            length = int(user_input)
            if length >= 16 and length <= 24:
                characters = string.ascii_letters + string.digits + string.punctuation
                generated_password = ''.join(random.choice(characters) for i in range(length))
                print("Your Password Generated Successfully:")
                print(f"\033[32m{generated_password}\033[0m")
            else:
                print(f'"Length should be in the range between\033[0m \033[33m16-24\033[0m characters."')
        except ValueError:
            print(f"\033[31mLength must be an integer.\033[0m")

if __name__ == "__main__":
    password()
