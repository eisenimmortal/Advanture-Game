import random
# инфо о игре
def displey_infa(*args):
    print(*args)

# получает ввод от пользователя
# и возвращает его в нижнем регистре
def get_user_input(s=""):
	user_input = input(s)
	return user_input.lower()

user_input = ""
str_1 = "Играть нажми <enter>"
str_2 = "Для выхода введи 'e'"
koloda = [6,7,8,9,10,2,3,4,11] * 4
random.shuffle(koloda)
user_count = 0
mashine_count = 0

while True:
    displey_infa(str_1)
    displey_infa(str_2)
    user_input = get_user_input()
    if user_input == 'e':
        break
    
    user_input = input("Возьми картыыыы y/n")
    if user_input == 'y':
        user_current = koloda.pop()*2
        print("Вам попаласть карта с достоинством %d" %user_current)
        user_count += user_current
        print('У вас %d очков' %user_count)
        while True:
            user_input = input("Возьми карту y/n")
            if user_input == 'y':
                user_current = koloda.pop()
                print("Вам попаласть карта с достоинством %d" %user_current)
                user_count += user_current
                if user_count > 21:
                    print("Перебор", user_count)
                    mashine_current = koloda.pop()
                    mashine_count += mashine_current
                    print("Мне попаласть карта с достоинством %d" %mashine_current)
                    print("Вы проиграли")
                    break
                elif user_count == 21:
                    print(user_count)
                else:
                    print('У вас %d очков' %user_count)
            elif user_input == 'n':
                print('У вас %d очков' %user_count)
                break
    elif user_input == 'n':
        break
    
    mashine_current = koloda.pop()*2
    print("Мне попаласть карта с достоинством %d" %mashine_current)
    mashine_count += mashine_current
    if mashine_count >= 17:
        print("Мне хватиттттт", mashine_count)
        
        continue
 
    while True:
        mashine_current = koloda.pop()
        print("Мне попаласть карта с достоинством %d" %mashine_current)
        mashine_count += mashine_current
        if mashine_count >= 17:
            print("Мне хватитт", mashine_count)
            break
        elif mashine_count > 21:
            print("Перебор", mashine_count)
            break
        elif mashine_count == 21:
            print(mashine_count)
            break
    
    if mashine_count < user_count <= 21:
        print("Вы выйграли")
    elif mashine_count == user_count:
        print("Ничья")
    elif user_count <  mashine_count <= 21:
        print("Вы проиграли")
        break
    break

    

        
        
    
    
