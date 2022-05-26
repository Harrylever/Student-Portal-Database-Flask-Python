# import os
# import random
# from random import randint


# number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# small_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# capital_Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# def randNamerFunc():
#     # small_Letters_shuffled = random.shuffle(small_Letters)
#     # capital_Letters_shuffled = random.shuffle(capital_Letters)
#     nameArray = []
#     for i in range(1, 4):
#         nameArray.append(random.choice(capital_Letters))
#         nameArray.append(random.choice(small_Letters))
#         nameArray.append(random.choice(number_list))
#     print(nameArray)
#     random.shuffle(nameArray)
#     print(nameArray)

#     nameString = ""
#     nameArray2 = []
#     for char in nameArray:
#         nameArray2.append(char)
#         nameString += char
#     nameString += ".png"
#     print(nameString)

# # print(small_Letters_shuffled)
# # print(capital_Letters_shuffled)


# randNamerFunc()

# def add_student():
#     nameArray = []
#     for i in range(1, 4):
#         nameArray.append(random.choice(capital_Letters))
#         nameArray.append(random.choice(small_Letters))
#         nameArray.append(random.choice(number_list))
#     print(nameArray)
#     random.shuffle(nameArray)
#     print(nameArray)

#     nameString = ""
#     nameArray2 = []
#     for char in nameArray:
#         nameArray2.append(char)
#         nameString += char
#     nameString += "0"
    # print(nameString)

    # dir = os.path.join("/home/kha1ide/Desktop/Ustacky FullStack PY Dev/Capstone Backend Project/", f'static/images/{nameString}')
    # if not os.path.exists(dir):
    #     os.mkdir(dir)
    
    # /home/kha1ide/Desktop/Ustacky FullStack PY Dev/Capstone Backend Project/static/images

# add_student()


thisList = [{'img_string': 'ffkekslll3-3'}, {'name': 'keral'}]
print(thisList[0]['img_string'])
