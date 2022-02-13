class Persons:
    persons_in_team = {"Нико Робин": True,
                       "Джим Киперс": True,
                       "Марко Волкодав": True,
                       "Кэри Кинг": True,
                       "Ангела": True,
                       "Ник Джеймс": True}
    actions_of_adventurers_in_team_dict_for_using = {"Нико Робин": 5,
                              "Джим Киперс": 5,
                              "Марко Волкодав": 6,
                              "Кэри Кинг": 5,
                              "Ангела": 5,
                              "Ник Джеймс": 4}

def subtract_value_from_actions_of_team(actions_lost):
    Persons.actions_of_adventurers_in_team_dict_for_using = \
        {i: Persons.actions_of_adventurers_in_team_dict_for_using[i] \
            - actions_lost for i in Persons.actions_of_adventurers_in_team_dict_for_using}


def subtract_value_from_actions_of_adventurer(name_of_adventurer, actions_of_adventurer):
    Persons.actions_of_adventurers_in_team_dict_for_using[name_of_adventurer] = \
        Persons.actions_of_adventurers_in_team_dict_for_using[name_of_adventurer] - actions_of_adventurer


def check_if_actions_0_or_more():
    for adventurer in Persons.actions_of_adventurers_in_team_dict_for_using:
        if Persons.actions_of_adventurers_in_team_dict_for_using[adventurer] < 0:
            return False

        return True

print(check_if_actions_0_or_more())
subtract_value_from_actions_of_team(50)
print(check_if_actions_0_or_more())
subtract_value_from_actions_of_adventurer("Джим Киперс", 500)
print(Persons.actions_of_adventurers_in_team_dict_for_using)












class A:
    def func(self):
        1+1

class B(A):
    def func(self):
        1+1

instance1 = B()
instance2 = A()
instance1.func()
instance2.func()


