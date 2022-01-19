import math
# инфа о начале игры
def infa(*args):
    print(*args)

# получает ввод от пользователя
# и возвращает его в нижнем регистре
def get_user_input(s=""):
	user_input = input(s)
	return user_input.lower()

user_input = ""
machine = ""
str_1 = "выбери число от 0-20, я попробую его угадать. Продолжить нажми <enter>"
str_2 = "Для выхода нажми 'r', и нажми <enter>"
str_3 = "Твое число"
str_4 = "Твое число 15"
str_5 = "Твое число 18"
str_6 = "Твое число 19"
str_7 = "Твое число 20"
str_8 = "Твое число 5"
str_9 = "Твое число 3"
str_10 = "Твое число 2"
str_11 = "Твое число 1"
a = 0
b = 20
c = 10
d = 15
more = "Для выбора <больше>, нажми '>'"
less = "Для выбора <меньше>, нажми '<'"
right = "Для выбора <верно>, нажми '='"
# игровой цикл
while (True):
    infa(str_1, str_2)
    if user_input == 'r':
        break

    user = int(input("Загадай число, и нажми <enter>"))
    print("Твое число", (a+b)/2) # число 10   
    infa(more)
    infa(less)
    infa(right)
    user_input = get_user_input() 
    if user_input == '>':
        print("Твое число", (c+b)/2) # число 15
        infa(more)
        infa(less)
        infa(right)
        user_input = get_user_input()
        if user_input == '<':
            print("Твое число", d - 1)# число 14
            infa(more)
            infa(less)
            infa(right)
            user_input = get_user_input()
        elif user_input == '<':
            print("Твое число", d - 2)# число 13
        if user_input == '>':
            print("Твое число", (math.ceil(d+b)/2))# число 18
            infa(more)
            infa(less)
            infa(right)
            user_input = get_user_input()
            if user_input == '<':
                print("Твое число", (math.floor(d+b)/2))# число 17
                infa(more)
                infa(less)
                infa(right)
                user_input = get_user_input()
                if user_input == '<':
                    print("Твое число", d + 1)# число 16
                    infa(more)
                    infa(less)
                    infa(right)
                    user_input = get_user_input()
                elif user_input == '=':
                     print("ты угадал")  
       
            
            
            if user_input == '>':
                print("Твое число", b-1)# число 19
                infa(more)
                infa(less)
                infa(right)
                user_input = get_user_input()
            elif user_input == '=':
                print("ты угадал")  
                if user_input == '>':
                    print("Твое число", b)# число 20
                    infa(more)
                    infa(less)
                    infa(right)
                    user_input = get_user_input()
                elif user_input == '=':
                    print("ты угадал")  
        elif user_input == '<':
            y = math.ceil(x+c)/2 # число 13
            infa(more)
            infa(less)
            infa(right)
        elif user_input == '=':
            print("ты угадал")  
    elif user_input == '=':
        machine = get_user_input(str_3)
        c = (b-a)/2 # число 5
        infa(more)
        infa(less)
        infa(right)
    elif user_input == '=':
        print("ты угадал") 
        
     
    
        


            
    
