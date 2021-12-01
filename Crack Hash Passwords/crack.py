import hashlib

print('\n****************************')
print('***** P@$$W0RD CR@CKER *****')
print('****************************\n')

print('-------> Only Can Crack passwords which are hashed by md5 algorithms!\n')

password = input('Enter Hashed Password : ')
pwd_not_found = ""

path = input('Enter Your File Path : ')

try:
    file1 = open(path, 'r')
except:
    print('\nError..!')
    print('Invalid File Path..!')  
    print('You Entered path : '+path)
    quit()  

Lines = file1.readlines()

for line in Lines:
    txt = line.strip('\n')

    # enc_txt = txt.encode('utf-8')
    hash_txt = hashlib.md5(txt.encode('utf-8'))
    last_txt = hash_txt.hexdigest()

    if password == last_txt:
        print('\n\nA password Found!')
        print("The Password is : "+txt)
        print('\n')
        pwd_not_found = "No"
        break 
    else:
        pwd_not_found = "Yes"   

file1.close()

if pwd_not_found == "Yes":
    print("\nPassword Not Found!\n")

print("*************")    