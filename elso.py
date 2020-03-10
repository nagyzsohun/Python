print("Please choose your mood!") 
mood = input("a) happy b) great c) nervous d) sad e) relaxed")

if mood=="happy" or mood== "a":
    print("It is great to see you happy!")
elif mood=="great" or mood=='b':
    print("It is great!")
elif mood=='nervous' or mood== 'c':
    print('Take a deep breath 3 times!')
elif mood=="sad" or mood== 'd':
    print('Go to sleep')
elif mood=="relaxed" or mood== 'e':
    print("Take a deep breath 3 times.")
elif mood=="excited" or mood== 'f':
    print("Drink a relax tea!")
else:
    print("Cheer up, mate!")

print("End!")