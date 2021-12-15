import os
import base64
import hashlib

def md5Crak():
    password = str(input('Enter Hashed Password : '))
    pwd_not_found = ""

    path = input('Enter Your File Path : ')

    try:
        file1 = open(path, 'r')
    except:
        print('\nError..!')
        print('Invalid File Path..!')  
        print('You Entered path : '+path)
        input('[Exit]') 

    Lines = file1.readlines()

    for line in Lines:
        txt = line.strip('\n')

        # enc_txt = txt.encode('utf-8')
        hash_txt = hashlib.md5(txt.encode('utf-8'))
        last_txt = hash_txt.hexdigest()

        if password == last_txt:
            print('\n\nA Password Found :)\a')
            print("The Password is : "+txt)
            print('\n')
            pwd_not_found = "No"
            break 
        else:
            pwd_not_found = "Yes"
            print("[!] Password not found : "+txt)   

    file1.close()

    if pwd_not_found == "Yes":
        print("\nPassword Not Found :(\n Try with Different Password Set...\n\a")

def banner():
    print('\n    **    ** ** **         ****          **    **     **             ****** **********')
    print('   **     **     **       **  **        **     **    **                **      **')
    print('  **      ** **  **      **     **     **      **  **                  **      **')
    print(' **       ** **         ** ***** **   **       ****                    **      **')
    print(' **       **   **      **         **  **       **  **                  **      **')
    print('   **     **    **    **           **   **     **    **                **      **')
    print('     **   **     **  **             **    **   **      **            ******    **\n')


def clear():
	os.system('cls')    

def base64_decode():
    password = input("Enter base64 encode password : ")
    low_pwd = password.lower()
    base64_message = low_pwd
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decode_pwd = message_bytes.decode('ascii')  
    print("The Password is : "+decode_pwd)
    print("\n")


def rot13_decode():
    password = input("Enter rot13 password : ")
    low_pwd = password.lower()

    abc = "abcdefghijklmnopqrstuvwxyz"
    rot_13 = lambda x: "".join([abc[(abc.find(c)+13)%26] for c in x])

    decrypted_text = rot_13(low_pwd)
    print('The Password is : ' + decrypted_text)   
    print("\n") 