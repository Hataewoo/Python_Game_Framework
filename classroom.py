##
##
##sen = "I am not gonna do this damn homework."
##
##print(sen.find("am")) # sen's index is start from 0
### so "I"'s index is 0, " "=1(space), a=2 so result will be 2
##print(sen.find("a")) # also the result is 2
##
##sen2 = "me was me"
##print(sen2.find("me")) # result will be 0 because if computer
### found "me" then it will not look for other "me"
##
##print(sen2.find("black")) # result will be -1 which means can't find
##
##print() # just for change line in the result page. not important
##
##lst = ["orange", "red", "blue", "yellow"]
### lst's 0 is "orange", and "red"'s index is 1, "blue"'s index is 1......
##print(lst.index("red")) # result is 1.
##
### print(lst.index("grey")) # the error will be occured not like find()
### Since it doesn't exist.
##
##print(", ".join(lst))
##sen3 = "_".join(lst)
##print(sen3)
##
##print()
############################
##sen = "I will eat every sushi in this town."
##print(sen)
##sen2 = sen.replace("sushi", "shirimp") # Must define to another variable
##print(sen)
##print(sen2)
##
##print()
##lst2 = sen.split(" ")
##print(lst2) # put strings' into lst2 split by " "(space)






### 4 Variables and Simple Data Types

##name = "ada Lovelace"
##print(name.title())
##print(name.upper())
##print(name.lower())
##print(name.capitalize())
##print(name.swapcase())
##
##
##f = "ada"
##l = "lovelace"
##full = f, l
##print(full)
##print(type(full))
##
##
##print(f"내 이름은 {f}")
##
##name = " qwertqwertqw "
##print(name.strip()) #맨 앞뒤의 띄어쓰기 삭제
##print(name.strip("q")) 
### .rstrip(), .lstrip()
##
##
##
##cau_url = "https://mportal.cau.ac.kr"
##simple_url = cau_url.removeprefix("https://")
##print(simple_url)
##
##
##word = "deadpool"
##print(word.count("o"))
##print(word.find("p")) # even it doesn't exist, it will show -1
##print(word.index("p")) # not exist -> error
##
##
##print(word.join("abc")) # wtf
##print("a".join(word)
##print(word.replace("oo","__"))
##print(word.split("o"))

##import this

##def convertListToString(x):
##    return " ".join(x)
##lst = ['Life', 'is', 'too', 'short']
##print(convertListToString(lst)) ##################################3

##def replaceColonWithHash(x):
##    return x.replace(":","#")
##st = "a:b:c:d"
##print(replaceColonWithHash(st))


##my_list = [1,2,3,['a','b','c']]
##
##print("".join(my_list[3]))


##my_list2 = [1,2,['a','b',['Life','is']]]
##print(" ".join(my_list2[2][2]))
##
##lst = [10, "Python", 20, "is", 30, "great"]
##
### Step 1: Filter out only the string elements
##strings_only = [str(item) for item in lst if isinstance(item, str)]
##
### Step 2: Concatenate all the strings
##concatenated_string = ''.join(strings_only)
##
### Step 3: Create a new list by repeating the modified list twice
##new_list = strings_only * 2
##
### Step 4: Append the concatenated string to the end of the new list
##new_list.append(concatenated_string)
##
##print(new_list)

##lst.insert(2,"df")
##del lst[2]
##lst.pop(3)
##lst.remove("df")
##lst.sort()
##lst.sort(reverse=True)
##print(sorted(lst))
##print(lst.reverse())

##lst = ["dfd", "sasgs", "xcv", "df", "cvcbvb", "df", "vnghter"]
##print(lst.index("df"))
##print(lst.count("df"))
##print(lst.extend(["qwe","xbhfhghg"]))
##print(lst)

##lst.max()
##lst.min()
##lst.sum()

##lst = ["notebook", "pencil", "eraser", "marker", "pencil"]
##del lst[lst.index("pencil")]
##print(lst)


##def convertListToString(x):
##    return " ".join(x)

##squares = [value**2 for value in range(1,11)]
##print(squares)


##lst = ["pizza", "falafel", "carrot cake"]
##lst2 = lst[:] ##########################################
##lst.append("cannoli")
##lst2.append("burrito")
##print(lst)
##print(lst2)

##data_tuple = (42,"Python", (8,16), "Tutorial", 3.14)
##print(data_tuple[0])
##print(data_tuple[2][0]+data_tuple[2][1])
##print(len(data_tuple[3]))
##print(data_tuple[0]*data_tuple[4])


##def isQualified(x,y):
##    if y >= 5 or (x >= 30 and y >= 3):
##        return True
##    else :
##        return False
##
##print(isQualified(7,2))
##print(isQualified(2,7))
##print(isQualified(35,3))
##print(isQualified(20,4))


##def game_369():
##    for i in range(1,301):
##        clap = 0
##        num = str(i)
##        for j in range(len(num)):
##            if num[j] == '3' or num[j] == '6' or num[j] == '9':
##                clap += 1
##        print(i, clap)
##
##
##game_369()
##print()
##
##
##def game_3691():
##    for i in range(1,301):
##        clap = 0
##        num = i
##        while num > 0:
##            n = num % 10
##            if n == 3 or n == 6 or n == 9:
##                clap += 1
##            num //= 10
##            
##        print(i, clap)
##
##game_3691()

##배라31에서2 6 10 14 18 22 26 30
##num % 4 = 2를 말하면 이길 수 있음

##티모 베인 마스터


##dic1 = {"a":1,"b":2,"c":3}
##dic2 = {"b":2,"c":4,"d":3}
##dic3 = {}
##for x in dic1:
##    if x in dic2:
##        if dic1[x] == dic2[x]:
##            dic3[x] = dic1[x]
##print(dic3)
            
##a = "Hello"
##print(set(a))

##a = (1,1,1,2,2,3)
##b = (2,5,6,6,6,6)
##set_a = set(a)
##set_b = set(b)
##print(set_a and set_b)
##print(set_a or set_b)
##print(set_b or set_a) 
##print(set_a & set_b) # 교집합
##print(set_b | set_a) # 합집합
##print(set_b.union(set_a)) # 합집합
##
##print((set_a - set_b) | (set_b - set_a))
## difference

##a = [1,2,3,4,5]
##b = [4,5,6,7,8]
##a2 = set(a)
##b2 = set(b)
##print(set(a).intersection(set(b)))
##print(a2&b2)

##############x = {"a":1, "b":2, "c":1, "d":3}
##############seen_set = set()
##############output = {}
##############for k,v in x.items():
##############    if v not in seen_set:
##############        output[k] = v
##############        seen_set.add(v)
##############print(output)

##############word = "ababc"
##############st = set()
##############for i in range(len(word)):
##############    for j in range(i,len(word)):
##############        st.add(word[i:j+1])
##############print(len(st))

##student_0 = {"name": "최수현", "grade": None, "gender": "female"}
##student_1 = {"name": "김진우", "grade": None, "gender": "female"}
##student_2 = {"name": "이시현", "grade": None, "gender": "female"}
##student_3 = {"name": "김민우", "grade": None, "gender": "female"}


##dic = {"player1":24, "player2":47, "player3":32}
##name = ""
##top = -1
##for k,v in dic.items():
##    if v > top:
##        top = v
##        name = k
##print(name)

################print(max(dic, key=dic.get))


##ans = "Seoul"
##
##while True:
##    ask = input("Where is the capital of Korea?: ")
##    if ask == ans:
##        print("Correct!")
##        break
##    else :
##        print("Wrong!")

##ans =""
##while ans != "Seoul":
##    ans = input("Where is the capital of Korea?: ")
##    if ans != "Seoul":
##        print("Wrong!")
##print("Correct!")

##cnt = 1
##tree_standing = True
##while tree_standing:
##    if cnt <= 10:
##        print("Hit %d: The tree is still standing." %cnt)
##        cnt += 1
##    elif cnt > 10 :
##        print("After ten hits, the tree has fallen!")
##        tree_standing = False


##stock = 10
##price = 300
##
##while True:
##    pay = int(input("Insert Money: "))
##    if pay == 300:
##        print("Here is your coffee.")
##        stock -= 1
##    elif pay > 300 :
##        re = pay - 300
##        print("Here is your coffee and your change of %dwon" %re)
##        stock -= 1
##    else :
##        print("Money refunded, not enough to buy coffee.")
##        print("Remaining coffee supply: %dunits" %stock)
##
##    if stock == 0:
##        print("All the coffee is sold out. Sales stopped.")
##        break




    



































