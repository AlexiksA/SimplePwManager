from cryptography.fernet import Fernet, InvalidToken
from time import sleep

def genKey():
    key = Fernet.generate_key()
    print(f"Your new generated key is: {key}")
    print(f"Press Enter after you have written it down")
    input()

def addPw():
    name = input('Account name: ')
    pwd = input('Password: ')
    fer = Fernet(input('Key: '))
    encryptedPw = fer.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as pwFile:
        if(pwFile.writable()):
            pwFile.write(name + "|" + encryptedPw + "\n")

def viewPw():
    try:
        fer = Fernet(input('Key: '))
    except ValueError as e:
        print(f'{e}')
        return
    with open('passwords.txt', 'r') as pwFile:
        for line in pwFile.readlines():
            data = line.rstrip()
            user, pwd = data.split('|')

            try:
                decryptedPw = fer.decrypt(pwd.encode()).decode()
            except InvalidToken:
                print(f"User: {user} | Password: Not your fricking problem")
            else:
                print(f"User: {user} | Password: {decryptedPw}")

#if(__name__ == "__main__"):
#    print("This is a primitive Password Manager")
    # sleep(3)

    # while(1):
    #     mode = input("GenKey, Add, View or Q? ").lower()
    #     if(mode == "genkey"):
    #         genKey()
    #     elif(mode == "add"):
    #         addPw()
    #     elif(mode == "view"):
    #         viewPw()
    #     elif(mode == "q"):
    #         break
    #     else:
    #         print("Not a known mode")