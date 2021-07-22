# print("""\
#   usage: things[how to use]
#   -a  all the files
#   -b   all the bathes """)
#
# # SLICING
#
# word = "Python"
#
# print(word[:1])
# print(word[1:3])
# print(word[5])
# print(word[1])
# print(word[:-1])
# print(word[-1])
# print(word[-2])
# print(word[-3:-1])
#
# # https://docs.python.org/3/library/stdtypes.html#textseq
#
# print("This is the latest \name")
# print(r"This is the latest \name")
#
# # str class
#
# print(str("This is the name"))
# myNum = str(10)
# print(myNum)
# print(type(myNum))
#
# # Common Sequence Operations
#
# for i in word:
#     print(i)
#
# print(max(word))
# print(min(word))
#
# name = "This is the name of the thunder"
# print(name.index('t'))
# print(name[8])
# print(name.count('t'))
#
# # String Methods
#
# name = "ddsprasad"
#
# print(name.capitalize())
# print(name.center(20))
# print(len(name.center(20)))
#
# print(name.istitle())
#
# name = name.capitalize()
# print(name.istitle())
#
# myList = ['I','AM','The']
# mysep = ' '
#
# print(mysep.join(myList))
#
# txt = "I could eat bananas all the day"
#
# print(txt.partition('bananas'))
#
# print(txt.split(' '))
# print(txt.rsplit(' '))
#
# str1 = "JhonDipPeta"
# str2 = "JaSonAy"
#
# def getMiddleThreeChar(txt):
#     txtLenth = round(len(txt)/2)
#     print(round(txtLenth))
#     middleTxt = txt[txtLenth-2:-txtLenth+2]
#     return middleTxt
#
# print(getMiddleThreeChar(str1))
# print(getMiddleThreeChar(str2))

# def insertInMiddle(str1,str2):
#     """"
#     Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
#     s1 = "Ault"
#     s2 = "Kelly"
#     Expected Output:
#     AuKellylt
#
#     """
#     lenstr = round(len(str1)/2) # round is even for odd length strings
#     finalresult = str1[:lenstr]+str2+str1[-lenstr:]
#     return finalresult
#
# print(insertInMiddle("autl","dds"))
# print(insertInMiddle("durgaprasad","sankara"))


# def firstMiddlelast(txt1,txt2):
#     """"
#     Given two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string
#     s1 = "America"
#     s2 = "Japan"
#
#     output: AJrpan
#     """
#     firstchars = txt1[0] + txt2[0]
#     lastchars = txt1[-1] + txt2[-1]
#
#     txt1len = int(len(txt1) / 2)  # instead of round its better to use int because always falls back to floor
#     txt2len = int(len(txt2) / 2)
#
#     middlechars = txt1[txt1len : txt1len+1] + txt2[txt2len : txt2len+1]
#
#     return firstchars+middlechars+lastchars
#
# print(firstMiddlelast("America","Japan"))



# def lowerAnduppersort(str1):
#     """"
#     Arrange string characters such that lowercase letters should come first
#     str1 = PyNaTive
#     output: yaivePNT
#     """
#     lowStrings = []
#     upStrings = []
#     for i in str1:
#         if i.islower():
#             lowStrings.append(i)
#         else:
#             upStrings.append(i)
#
#     return ''.join(lowStrings+upStrings)
#
#
# print(lowerAnduppersort("PyNaTive"))

# str1 = "P@#yn26at^&i5ve"
#
# # print("char".isidentifier())
#
# def getcounts(str1):
#     """"
#     Count all lower case, upper case, digits, and special symbols from a given string
#     """
#     uppercount  = 0
#     lowercount = 0
#     digitcount = 0
#     symbolcount = 0
#
#     for chr in str1:
#         if chr.isupper():
#             uppercount+=1
#         elif chr.islower():
#             lowercount+=1
#         elif chr.isdigit():
#             digitcount+=1
#         else:
#             symbolcount+=1
#     return f"UpperCase Count {uppercount} \nLowerCase Count {lowercount} \nDigit Count {digitcount} \nSymbol Count {symbolcount}"
#
# print(getcounts(str1))










