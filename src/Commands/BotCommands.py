# bot.py
import random



def randomDice(number_of_dice, number_of_sides):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    return ', '.join(dice)


def getTask():
    file = open(r'Resources\MyTasks', 'r')
    Str = file.read()
    L = Str.splitlines()
    if (len(L) == 0):
        L = ["No tasks to do !"]
        return L
    for j in range(len(L)):
        for i in range(len(L)):
            if (len(L[i]) == 0):
                L.pop(i)
                break

    for k in range(len(L)):
        x = L[k]
        L[k] = "Task " + str(k + 1) + ": " + x
        print("Task " + str(k + 1) + ": " + x)

    file.close()
    return L


def addTask(s):
    file = open(r'Resources\MyTasks', 'a')
    file.write(s + "\n")
    file.close()
    return True


def getStrings() :
    file = open(r'Resources\MyTasks', 'r')
    Str = file.read()
    file.close()
    return Str

def removeTask(Idx):
    Str = getStrings()
    L = Str.splitlines()
    if (len(L) == 0):
        return False
    for x in Idx:
        if (x >= len(L)):
            return False
    file = open(r'Resources\MyTasks', 'w')
    for j in range(len(L)):
        for i in range(len(L)):
            if (len(L[i]) == 0):
                L.pop(i)
                break

    print("Index : ")
    print(Idx)
    for x in Idx:
        if (x >= len(L)):
            return False
        L[x] = ""

    for j in range(len(L)):
        for i in range(len(L)):
            if (len(L[i]) == 0):
                L.pop(i)
                break

    for k in range(len(L)):
        L[k] = L[k] + "\n"

    file.writelines(L)
    file.close()
    return True
