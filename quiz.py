print("welcom to quiz")

playing = input(" Do you want to play ?  ")

if playing.lower() != 'yes':
    quit()

print("let's play." )
score = 0

answer = input("Fe2O3 is ore of ? ")
if answer.lower() == "heamatite":
    print("correct")
    score += 1
else:
    print("incorret try another")    

answer = input("PbSis ore of ? ")
if answer.lower() == "galena":
    print("correct")
    score += 1
else:
    print("incorret try another")

answer = input("FeCO3 is ore of ? ")
if answer.lower() == "siderite":
    print("correct")
    score += 1
else:
    print("incorret try another")

answer = input("TiO2 is ore of ? ")
if answer.lower() == "rutile":
    print("correct")
    score += 1
else:
    print("incorret try another")

answer = input("NaCl is ore of ? ")
if answer.lower() == "rock salt":
    print("correct")
    score += 1
else:
    print("incorret try another")

print("you got"+  str(score)  +  "questions correct")

print("you got"+  str((score/5)*100)  +  "%")