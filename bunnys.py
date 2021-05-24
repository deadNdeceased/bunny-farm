## Oh no! Our bunny friend (fred) got lost in this list :( 
## Help him find his way back to his lover (samantha)<3

## ------------- DO NOT EDIT ME ------------- ##

fred = "hi im fred!"
samantha = "hi im samantha!"
timothy = "hi im timothy!"
alex = "hi im alex!"

bunny_farm = [fred, samantha, alex, timothy]

## ------------- DO NOT EDIT ME ------------- ##

## vvvvvvvvvvvvv YOUR CODE GOES HERE vvvvvvvvvvvvv ##
a = bunny_farm.pop(3)
bunny_farm.insert(1,a)

## ^^^^^^^^^^^^^ YOUR CODE GOES HERE ^^^^^^^^^^^^^ ##


## ------------- DO NOT EDIT ME ------------- ##

for i in bunny_farm:
    print(i)

for i in range(len(bunny_farm) - 1):
    if bunny_farm[i] == fred and bunny_farm[i+1] == samantha:
        print("Thank you for reuniting us! <3")
    elif bunny_farm[i] == samantha and bunny_farm[i+1] == fred:
        print("Thank you for reuniting us! <3")

## ------------- DO NOT EDIT ME ------------- ##
