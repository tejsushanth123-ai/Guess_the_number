import random



def guess_number():
    return list(input("What is your guess"))
def number_generator():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]
def clue_giver(code,useInput):
    if useInput == code:
        return "CODE CRACKED!"
    clues = []
    for ind,num in enumerate(useInput):
        if num == code[ind]:
            clues.append("Matched")
        elif num in code:
            clues.append("Close")
    if clues==[]:
        return ["Nope"]
    else:
        return clues

print("Welcome to the game")
generateCode = number_generator()
print("code is generated, choose a 3 digit number")
clueReport = []
while clueReport != "CODE CRACKED":
    guess = guess_number()
    clueReport = clue_giver(guess,generateCode)
    print("Here is the result: ")
    for clues in clueReport:
        print(clues)