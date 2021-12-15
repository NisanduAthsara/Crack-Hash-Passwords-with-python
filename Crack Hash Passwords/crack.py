import hashlib
import os
import funcs
import base64

funcs.banner()

print('[*] Only Can Crack passwords which are hashed by md5 , base64 ,rot13 algorithms!\n')

type_of_func = str(input("Enter Your Algorithm Type : "))

type_of_func1 = type_of_func.replace(" ","")
type_of_func2 = type_of_func.lower()

funcs.clear()
funcs.banner()

if type_of_func2 == "md5":
    funcs.md5Crak()

elif type_of_func2 == "base64":
    funcs.base64_decode()

elif type_of_func2 == "rot13":
	funcs.rot13_decode()

else:
	print("Invalid Encrytion Method..!")

print("Thanks For Use CR@CK IT")   

input('[!]Exit : ')
exit()