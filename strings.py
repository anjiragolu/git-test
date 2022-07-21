# create string
# string_1 ="python is easy language"
# print("i know" ,string_1)
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>
# string_2 = '''hii,how are you
#            welcome to my world'''
# print(string_2)
#
#access the last element
# string_1 ="python is easy language"
# print(string_1[-1])
#
#access the elements
# string_1 ="python is easy language"
# print(string_1[4])
# print(string_1[8])
# print(string_1[16])
#
#In strings update or delete of the characters  not possible.
# string_1 ="python is easy language"
# string_1[4] ='a'
# print(string_1)
# "TypeError: 'str' object does not support item assignment"
# string_1 ="python is easy language"
# print(string_1[4] == "a" )
#
#update a string
# string_1 ="python is easy language"
# string_1 ="python is hard language"
# print(string_1)

#
#IN string we can't delete character but we can delete entire string.
# string_del = "python"
# print(string_del)
# del string_del[2]#TypeError: 'str' object doesn't support item deletion
# del string_del
# print(string_del)
#
#
#print('{} ,"hiii how are you"'.format("hello"))#>>>using format option in a simple string
#
#
# strings_2 = "{},python is simple language">>>>>>>>using format option for avalue stored in a variable
# print(strings_2.format('i know'))
#
#
#print('my name is john,iam {} age old'.format(12))>>>>>>formatting a string using a numeric constant
#
#
#Multiple placeholders in format() function
# strings_3 ="{},how are you. {} is your {}?"
# print(strings_3.format("hii","what","name"))
#
#
#Formatting Strings using Escape Sequences
# \n  :- """Breaks the string into a new line"""
# print('I designed this rhyme to explain in due time\nAll I know')
#print("I know everything but\ni don't tell")
# \t  :- "Adds a horizontal tab"'
# print('Time is a \tvaluable thing')
#print('Watch it fly by\\as the pendulum swings')
#
#
#To demonstrate the use of formatters
# with positional key arguments.
# string_3 = '{0} is simple {1} and it is easy to {2}'
# print(string_3.format("python","language","learn"))
#
#
#print("%-50s" % ("tony strak",))>>>>>>> givig SpawnProcess
##
#
# string_5 = 'wakanda black panther'
# title_string = string_5.title
# print('one of the marvel heros = ', string_5)
# print("one od the dc heros = ",title_string)
# ####
#line = "Geek1 \nGeek2 \nGeek3"
#print(line)


#
#
# string_6 = 'Python is currently the most widely used multi-purpose'
# print(string_6[::-1])# Reverse the order


# print(string_6[:15]) # slicing with starting


# print(string_6[6:])  # slicing givenindex to ending

# print(string_6[4:12:2]) # slicing with step
#  

# r = input('enter some  string to reverse:')# reverse string
# output = r[::-1]
# print('reversed string:',output)


#s = "alpha  currently used"
#r = reversed (s)           #>>>>> using reversed function
#for i in r:
   # print(i)

#output =''.join(r)
#print(output)      #>>>>>> joint the lines


#
#"concattenation"
#a = "avatar" + 'is a good movie'

#print(a)

#"membership"
# a ='avatar movie is good movie'
# print('good' in a)


# r = [1,2,3,4,4,4,3,5,6,5,6,1,2,3]
# g = ()
# for i in r:
#     if i not in g:
#         g.append(i)
#     else:
#         print(g) 
# print(g)   

# t = ["a",'b','c',"a",'b','c',"a",'b','c']
# v = {}
# for i in t:
#     v[i]=t.count(i)
# print(v)

#t = ["a",'b','c',"a",'b','c',"a",'b','c']#>>>> find the duplicates using set function
#x = set(t)
#print(x)


#We can iterate through a string using a for loop. Here is an example to count the number of 'l's in a string.
# count = 0
# for letter in 'Hello World':
#     if(letter == 'l'):        #>>>>how many 'l'in the 'Hello world'  
#         count += 1
# print(count,'letters found')

#
#
# r = 'ABCAGDCBFCFBGHSFGBGF'
# count = 0
# for i in r:
#     if(i == 'B'):
#         count += 1
# print(count,"letters found")


#
# 
# ""enumerate()""
# str_1 ='cold'
# list_enumerate = list(enumerate(str_1))                                                                                                          
# print('list(enumerate(str) = ', list_enumerate)

#
#
#
# string_7 = "hello world"
# string_8 =list(enumerate(string_7))
# print('this is enumerate function;',string_8)

# #
#
# string_7 ='{}, {}, and {}'.format('anji','anil','anuj')
# print(string_7)

####
# string_8 ="In this tutorial, we will learn about the Python String find"
# print(string_8.find("we",1))

#
#
# x = "In\nthis\ntutorial,\nwe will\nlearn\nabout the Python String find"
# print(x)


#
#
#
# x = "{}  {} and {}".format('john','bill','sean')#>>>>> using defult order
# print(x)
#
#
# x ="{1} , {0} and {2}".format("AB",'HB','MB')# >>>>.using positional arguments.
# print(x)

#
#
# x ="in this tutorial, we will learn about the Python String find"
# print(x.upper())
     
#
#
# x ="in this tutorial, we will learn about the Python String find"
# print(x.lower())
     
#
#
# x ="inthistutorial we will learn about the Python String find"
# print(x.split())                                                #>>>>>>> split method

#
#
#
# i ='in this tutorial, we will learn about the Python String find'
# print(i.count('i'))

#
# i ='in this tutorial, we will learn about the Python in String find'
# substring ='find'                                                     #>>>>> count method
# x =i.count(substring)
# print(x)
#
#

# i ='this tutorial, we will learn about the Python String find'
# substring = i[0:8]
# print('using substring',substring)        # >>>>>>>>>>>>using substring slice the string

#
#
#

#i ='in this tutorial, we will learn about the Python String find'
#print(i.swapcase()) #####>>>>>>>>           >>>>>> >>>>>>>>     >>>>>>>> swapcase
#print(i.capitalize())

#
#
#print(i.endswith("fun"))
#x =i.encode()
#print(x)


str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub,80))

# str1 = "JhonDipPeta"
# result =str1[0]
# l =len(str1)
# mi =int(l/2)
# result =result+str1[mi]
# result = result +str1[l -1]
# print(result)

#
#
#streing_9 ='my isname isisis jameis isis bond'
# # print(r.replace('is','was'))
#print(streing_9.replce("is","was", 3))


#
#
# str = "this is string example....wow!!! this is really string"
# print (str.replace("is", "was"))
# print (str.replace("is", "was", 3))

#
#
# import string
# result = string.digits
# print(result)

#
#
# def Convert(string):
#     li = list(string.split(" "))
#     return li
# str1 = "Geeks for Geeks"
# print(Convert(str1))

###
# string_10 = 'Geeks for Geeks '
# y =list(string_10.split(""))

# print(y)
# txt = " Hello World "
# x =txt.strip()
# print(x)






    





           
