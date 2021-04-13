from itertools import permutations


def questonOne():
    elements = int(input())
    myList = []
    for i in range(elements):
        myList.append(int(input()))
    print(sum(myList))


def questionTwo():
    elements = int(input())
    myList = []
    for i in range(elements):
        myList.append(int(input()))
    print(max(myList))


def questionThree():
    elements = int(input())
    myList = []
    count = 0
    for i in range(elements):
        myList.append(input())
    for each in myList:
        if len(each) >= 2 and each[0] == each[len(each)-1]:
            count += 1
    print(count)


def questionFour():
    elements = int(input())
    myList = []
    for i in range(elements):
        myList.append(input())
    newList = list(set(myList))
    print(newList)


def questionFive(list1, list2):
    return len(list(set(list1) & set(list2))) > 0


def questionSix():
    elements = int(input())
    myList = []
    for i in range(elements):
        myList.append(input())
    for each in list(permutations(myList)):
        print(list(each))


def questionSeven():
    rows = int(input())
    columns = int(input())
    myList = []
    flattenedList = []
    for i in range(rows):
        sublist = []
        for each in range(columns):
            sublist.append(input())
        myList.append(sublist)
    for each in myList:
        flattenedList.extend(each)
    print(myList, flattenedList, sep='\n')


def questionEight():
    elements = int(input())
    myList = []
    for i in range(elements):
        myList.append(input())
    myDictionary = {}
    for each in myList:
        if each in myDictionary.keys():
            myDictionary[each] += 1
        else:
            myDictionary[each] = 1
    print(myDictionary)


def questionNine():
    elements = int(input())
    myList = []
    for i in range(elements):
        myList.append(input())
    subElements = int(input())
    mySubList = []
    for i in range(subElements):
        mySubList.append(input())
    for i in range(len(myList)-len(mySubList)+1):
        if mySubList == myList[i:i+len(mySubList)]:
            print(True)
            break
    else:
        print(False)


def questionTen():
    finalList = []
    elements = int(input())
    list1 = []
    for i in range(elements):
        list1.append(input())
    list2 = []
    for i in range(elements):
        list2.append(input())
    for i in range(elements):
        myDict = {}
        myDict['list1_parameter'] = list1[i]
        myDict['list2_parameter'] = list2[i]
        finalList.append(myDict)
    print(finalList)


# questonOne()
# questionTwo()
# questionThree()
# questionFour()
# print(questionFive([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
# questionSix()
# questionSeven()
# questionEight()
# questionNine()
# questionTen()
