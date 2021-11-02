'''
Andy Walsh
Sep. 9th, 2021
'''

'''
my_string = "dhbd"
print(type(len(my_string)))

i = 1
while i < len(my_string):
    print(i)
    i +=1
'''
def converte_input ():
    print("convert input")
    try:
        int_input = int(input("please give an int value from 0 to 255 : "))
    except:
        print("you picked " , int_input)
        print(type(int_input))

    if type(int_input) == type(0):
        print("all_good")
    if type(int_input):
        print("you dumb dumb, know your numbers!")

converte_input()
