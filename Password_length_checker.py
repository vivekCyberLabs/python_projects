import re
import math


def check_strength(password:str) -> str :
    score = 0
    if re.search(r"[a-z]",password):score+=1
    if re.search(r"[A-Z]",password):score+=1
    if re.search(r"[0-9]",password):score+=1
    if re.search(r"[^\w\s]",password):score+=1

    if score<2:return "weak password"
    elif score<4:return "medium password"
    else :return "strong password"
    


def charaset_size(password: str) -> int:
    size  = 0
    if re.search(r"[a-z]",password):size+=26
    if re.search(r"[A-Z]",password):size+=26
    if re.search(r"[0-9]",password):size+=10
    if re.search(r"[^\w\s]",password):size+=32 #random characters

    return size


def entropy(password:str) -> float:
    c_size = charaset_size(password)
    if c_size == 0:
        return 0
    return(
        len(password)*math.log2(c_size)
    )


def entropy_strength(password:str)->int:
    e = entropy(password)
    if e < 28:
        return "Very Weak"
    elif e < 40:
        return "Weak"
    elif e < 60:
        return "Medium"
    elif e < 80:
        return "Strong"
    else:
        return "Very Strong"


def sequence_check(password:str)->bool:
    seq_len=3
    for i in range(len(password.lower())-seq_len+1): # len(pssword)-seq_length gives last check first index number
        chunk=password[i:i+seq_len]

        if all(ord(chunk[j+1])-ord(chunk[j])==1 for j in range(len(chunk)-1)):
            return True
        if chunk.isdigit() and all(ord(chunk[j+1])-ord(chunk[j])==1 for j in range(len(chunk)-1)):
            return True
    return False


def repetition_check(password:str,repeated_threshold=3)->bool:
    return any(len(m.group(0))>=repeated_threshold
              for m in re.finditer(r"(.)\1*", password))




pw = input("enter the password : ")

print("Password : ",check_strength(pw))
print(f"Entropy : {round(entropy(pw),2)} bits")
print(f"strength of randomness : {entropy_strength(pw)}")


if sequence_check(pw):
    print("sequence of number or character is spotted..eg:abc,123")

if repetition_check(pw):
    print("(X).Repetitive characters found :  change the password")




