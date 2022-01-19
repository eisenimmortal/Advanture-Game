import random
import sys
import time
import PyQt5
from PIL import Image
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication, QScrollArea)
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QDir


# СОБЫТИЯ

Random_aim = random.randint(1, 3)  # Создание рандомной цели

img = Image.open('Moon2.png')
watermark_before_resize = Image.open('Bat.png')
watermark = watermark_before_resize.resize((108, 108))

img.paste(watermark, (0, 0), watermark)
img.save("img_with_watermark.png")


def random_mount_event():
    Random_Mount_Event = random.randint(1, 3)
    if Random_Mount_Event == 1:  # События горы при открытии
        return ("Пробираясь по сыпучему откосу, \nвы оступаетесь и катитесь по\n волне осыпающихся камней.\n"
                "Пройдите проверку самообладания 2. \nПрибавьте 1 к сложности за \nкаждые 3 кг груза. \n"
                "При провале получите 1 легкое \nранение и потеряйте в этой локации \n1 случайный предмет. ")

    if Random_Mount_Event == 2:
        return ("Ваш путь преграждает небольшая \nскала. "
                "Можно потратить по 1 \nдополнительному действию,\n"
                " чтоб обойти ее, либо \nкаждый должен пройти проверку \nсилы 3, чтобы забраться наверх.")

    if Random_Mount_Event == 3:
        return ("На вашем пути оказывается глубокая \nрасщелина."
                "Группа может потратить \nдополнительное движение чтобы \nобойти ее. "
                "Имея альпинистское \nснаряжение, любой член экспедиции \nможет пройти проверку Акробатики 3,\n"
                "чтобы попробовать перепрыгнуть \nчерез расщелину и помочь остальным \nпереправиться. "
                "При провале он \nполучает тяжелое ранение.")
    return


def random_night_mount_event():
    Random_Night_Mount_Event = random.randint(1, 3)
    if Random_Night_Mount_Event == 1:  # События горы ночью
        return ("Холодный ветер пробирает до костей. \n"
                "Путешественники без теплого \nодеяла получают состояние Озноб.")
    if Random_Night_Mount_Event == 2:
        return ("На огонь костра слетается \nмного насекомых.\n"
                "Исследователь с наименьшим \nпоказателем Внимания \nполучает состояние Укусы насекомых. ")
    if Random_Night_Mount_Event == 3:
        return ("Вы предусмотрительно накидываете \nтравы и песка на землю, чтобы \nне спать на жестких камнях.\n"
                "Таким образом вам удается \nвыспаться в относительном комфорте.")
    return


def random_jungle_event():
    Random_Jungle_Event = random.randint(1, 3)
    if Random_Jungle_Event == 1:  # События джунглей при открытии
        return ("Проходя по тропе вы \nзамечаете необычные следы.\n"
                "Любой член экспедиции \nможет пройти проверку \nвнимательности 3.\n"
                "При успехе вы находите \nтропу диких кабанов. \nЭта локация получает знак \nохоты 4.")
    if Random_Jungle_Event == 2:
        return ("Продираясь по густым \nзарослям, вы сбиваетесь с тропы.\n"
                "Каждый член экспедиции \nтеряет дополнительное действие.\n ")
    if Random_Jungle_Event == 3:
        return ("Заросли становятся все \nгуще. "
                "Игрок идущие во главе \nэкспедиции должен пройти \nпроверку Навигации 3.\n "
                "При провале вы \nвозвращаетесь в предыдущую \nлокацию, не открывая новую.")
    return


def random_night_jungle_event():
    Random_Night_Jungle_Event = random.randint(1, 3)
    if Random_Night_Jungle_Event == 1:  # События джунглей ночью
        return ("Вы просыпаетесь от осознания \nтого, что кто-то разворошил костер. \n"
                "Дикие кабаны прибежали на свет \nи разбросав угли скрылись. \n"
                "В лагере начинается пожар. \n"
                "Если есть запас воды, лидер \nэкспедиции должен пройдите \nпроверку самообладания 2, \n"
                "чтобы потушить костер. \nИначе или при провале, \n"
                "член экспедиции с наименьшим \nсамообладанием уничтожает \nслучайную вещь и получает \n1 легкое ранение.")
    if Random_Night_Jungle_Event == 2:
        return ("Всю ночь вы вздрагиваете \nот каждого шороха. \n"
                "Наутро вы встаете еще более \nуставшим, чем когда ложились. \n"
                "На следующий ход все члены \nэкспедиции получают -1 к \nвыносливости и -1 к силе.")
    if Random_Night_Jungle_Event == 3:
        return ("Ночью проходит дождь. \nВы тратите много сил на \nзащиту лагеря от затопления. \n"
                "Каждый исследователь получает \nна следующий ход -1 выносливость.\n"
                "Если в локации нет знака \nдоступа к питьевой воды, \n"
                "на следующий ход эта \nлокация получает знак \nдоступа к воде.")
    return


def random_plane_event():
    Random_Plane_Event = random.randint(1, 3)
    if Random_Plane_Event == 1:  # События равнин при открытии
        return ("Тропа перед вами сильно петляет, \nидущий во главе экспедиции \nможет пройти проверку навигации 4,\n"
                "чтобы попробовать найти короткий \nпуть. При провале ничего \nне происходит."
                " При успехе группа \nможет переместиться в соседнюю \nлокацию Равнину,  без затраты \nпередвижения.")
    if Random_Plane_Event == 2:
        return ("Тропу преграждает \nбыстротекущая река.\n"
                "Группа может потратить \n1 дополнительное движение, \n"
                "чтобы найти более безопасное \nместо для пересечения,\n"
                "либо каждый член группы \nпроходит проверку Силы 2. \n"
                "При провале получите 1 легкое \nранение. Все исследователи \nмогут пополнить запасы воды.")
    if Random_Plane_Event == 3:
        return ("Вы натыкаетесь на стаю диких собак. \nВыложите врага – Дикие Собаки.")
    return


def random_night_plane_event():
    Random_Night_Plane_Event = random.randint(1, 3)
    if Random_Night_Plane_Event == 1:  # События равнин ночью
        return ("Ночь прошла без происшествий, \n"
                "но наутро вы обнаруживаете, что \nваши запасы еды сильно погрызли \nкрысы. "
                "Исследователи теряют в \nсумме 2 запаса еды.")
    if Random_Night_Plane_Event == 2:
        return ("Ночь была приятной и \nуспокаивающей. "
                "Каждый \nисследователь может вылечить 1 \nнегативное состояние.")
    if Random_Night_Plane_Event == 3:
        return ("Вы слишком поздно поняли \nчто разбили лагерь в близости \nк муравейникам. "
                "Всю ночь \nвы отчаянно боролись \nс этими насекомыми. "
                "Исследователи \nс самообладанием ниже 3-х получают \nв следующем дне на 1 очко \nпередвижения меньше.")
    return


def random_desert_event():
    Random_Desert_Event = random.randint(1, 3)
    if Random_Desert_Event == 1:  # События пустынь при открытии
        return ("Дорогу преграждает песчаная насыпь.\n Каждый исследователь проходит\n проверку Акробатики 2. \n"
                "Если у всех успех \n– группа проходит без происшествий.\n "
                "Если хотя бы один \nисследователь провалил проверку,\n "
                "группа вынуждена либо\n потратить дополнительное движение\n на прохождение этого участка,\n "
                "либо отступить назад. ")
    if Random_Desert_Event == 2:
        return ("Вы пробираетесь по этим засушливым \nтерриториям уже очень долго,\n "
                "в глазах рябит от этого\n несменяемого маршрута.\n "
                "В усталости вы почти\n не смотрите под ноги, и попадаете\n ногой прямо в змеиное гнездо.\n "
                "Выложите врага Ядовитая змея.")
    if Random_Desert_Event == 3:
        return ("Тропа разделяется на\n множество мелких троп.\n "
                "Впереди идущий должен\n пройти проверку Навигации 3.\n "
                "При успехе можно выбрать любую\n локацию, соединенную с исходной,\n и переместится в нее, "
                "без \nдополнительных затрат передвижения.\n "
                "При провале вы попадаете\n в ту локацию, в которую двигались\n изначально.")
    return


def random_night_desert_event():
    Random_Night_Desert_Event = random.randint(1, 3)
    if Random_Night_Desert_Event == 1:  # События пустынь ночью
        return ("Ночь была ветреная, \nи засушливая. Если \nв локации нет источника воды, \n"
                "каждый исследователь \nдолжен потратить запас воды.")
    if Random_Night_Desert_Event == 2:
        return ("Вы проспали относительно \nспокойно, лишь изредка просыпаясь \nот тихих шорохов. \n"
                "Наутро вы замечаете как \nвокруг лагеря много следов змей, \n"
                "и одна из них угрожающе \nшипит глядя на вас. \n"
                "Выложите врага Ядовитая змея.")
    if Random_Night_Desert_Event == 3:
        return ("Вы готовите укромное место \nдля ночлега и слегка \nраскапываете землю. \n"
                "Внезапно вы натыкаетесь \nна гнездо термитов. \n"
                "Исследователь с самым высоким \nпоказателем силы получает \nсостояние Укусы насекомых.")

        # ВРАГИ


class Enemy:  # Создание базового класса врага:
    def __init__(self, name, type_of_enemy, danger, reaction, wound_making, behavior, gives_food):
        self.name = name
        self.type_of_enemy = type_of_enemy
        self.danger = danger
        self.reaction = reaction
        self.wound_making = wound_making
        self.behavior = behavior
        self.gives_food = gives_food


wild_dog = Enemy("Дикая собака", "Хищник", 3, 2,
                 "Ранение: Легкая рана. При повторном ранении - состояние Серъёзное Кровотечение",
                 "Нападает в первую очередь на исследователей с наименьшим показателем самообладания. Меняет цель "
                 "после каждой атаки",
                 3)

poisoned_snake = Enemy("Ядовитая змея", "Змея", 2, 3,
                       "Ранение: Получите состояние Укус ядовитой змеи",
                       "Нападает в первую очередь на исследователей с наибольшим показателем акробатики. Продолжает"
                       "нападать на одну и ту же цель. Если никто не зацитит",
                       1)

wild_boar = Enemy("Дикий кабан", "Хищник", 4, 3,
                  "Ранение: Легкая рана", "Нападает в первую очередь на исследователей с наибольшим показателем силы."
                                          "Меняет цель после каждой атаки", 5)


# Путешественники


class Adventurer:  # Создание базового класса путешественника:
    def __init__(self, name, profession, strength, endurance, agility, attentiveness, navigation, composure, special):
        self.name = name
        self.profession = profession
        self.strength = strength
        self.endurance = endurance
        self.agility = agility
        self.attentiveness = attentiveness
        self.navigation = navigation
        self.composure = composure
        self.special = special


Nico_Robin = Adventurer("Нико Робин", "Архиолог", 2, 2, 3, 3, 2, 3, "Все предметы Артефакты для неё весят "
                                                                    "вдвое меньше")
Jim_Kippers = Adventurer("Джим Киперс", "Навигатор", 3, 2, 2, 2, 3, 3, "Может использовать жетоны ловкости "
                                                                       "как жетоны Хладнокровия и наоборот")
Marco_Wolfhound = Adventurer("Марко Волкодав", "Охотник", 3, 3, 1, 3, 2, 2, "Все карты для охоты в его руках "
                                                                            "действуют вдвое лучше")
Carry_King = Adventurer("Кэри' Кинг", "Военный", 4, 2, 1, 3, 2, 3, "Раз в раунд может дублировать на "
                                                                   "проверку любого другого исследователя "
                                                                   "жетон "
                                                                   "Ловкости или Хладнокровия из общего "
                                                                   "запаса")
Angela = Adventurer("Ангела", "Навигатор", 1, 2, 3, 4, 4, 2, "Раз в раунд, во время проверки любого "
                                                             "исследователя может перевернуть "
                                                             "вытянутый жетон на другую сторону")
Nick_James = Adventurer("Ник Джеймс", "Военный, Врач", 3, 1, 2, 3, 1, 4, "За ночь может вылечить одну тяжелую "
                                                                         "рану у другого исследователя без "
                                                                         "траты аптечки")


# ДИАЛОГОВОЕ ОКНО МЕНЮ

class Menu(object):
    # def __init__(self):
    #     self.pushButton = QtWidgets.QPushButton(Dialog_menu)

    def setupUi(self, Dialog_menu):
        Dialog_menu.setObjectName("Dialog_menu")
        Dialog_menu.resize(1300, 800)

        hbox = QHBoxLayout()
        pixmap = QPixmap("Стартовое меню.jpg")
        lbl = QLabel()
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        Dialog_menu.setLayout(hbox)

        Dialog_menu.setWindowTitle('Стартовое меню')

        self.media_player = QMediaPlayer()  # МУЗЫКА
        url = QUrl.fromLocalFile("metallica-the-unforgiven.mp3")
        content = QMediaContent(url)
        self.media_player.setMedia(content)
        self.media_player.play()

        self.pushButton = QtWidgets.QPushButton(Dialog_menu)
        self.pushButton.setGeometry(QtCore.QRect(442, 224, 423, 94))
        self.pushButton.setIcon(QtGui.QIcon("Game Pictures/Новая игра.jpg"))
        self.pushButton.setIconSize(QtCore.QSize(423, 94))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog_menu)
        self.pushButton_2.setGeometry(QtCore.QRect(442, 330, 421, 94))
        self.pushButton_2.setIcon(QtGui.QIcon("Game Pictures/Сохранить.jpg"))
        self.pushButton_2.setIconSize(QtCore.QSize(421, 94))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog_menu)
        self.pushButton_3.setGeometry(QtCore.QRect(442, 436, 421, 93))
        self.pushButton_3.setIcon(QtGui.QIcon("Game Pictures/Загрузить.jpg"))
        self.pushButton_3.setIconSize(QtCore.QSize(421, 93))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog_menu)
        self.pushButton_4.setGeometry(QtCore.QRect(442, 540, 421, 93))
        self.pushButton_4.setIcon(QtGui.QIcon("Game Pictures/Настройки.jpg"))
        self.pushButton_4.setIconSize(QtCore.QSize(425, 95))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog_menu)
        self.pushButton_5.setGeometry(QtCore.QRect(442, 644, 421, 93))
        self.pushButton_5.setIcon(QtGui.QIcon("Game Pictures/Выход.jpg"))
        self.pushButton_5.setIconSize(QtCore.QSize(425, 95))
        self.pushButton_5.setObjectName("pushButton_5")


# Диалоговое окно истории

class History(object):
    # def __init__(self):
    #     self.pushButton = QtWidgets.QPushButton(Dialog_menu)

    def setupUi(self, History):
        History.setObjectName("History")
        History.resize(1800, 1000)

        hbox = QHBoxLayout()
        pixmap = QPixmap("Game Pictures/story-screen.jpg")
        lbl = QLabel()
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        History.setLayout(hbox)

        History.setWindowTitle('Expedition')

        self.pushButton = QtWidgets.QPushButton(History)
        self.pushButton.setGeometry(QtCore.QRect(442, 824, 403, 90))
        self.pushButton.setIcon(QtGui.QIcon("Game Pictures/dalee.png"))
        self.pushButton.setIconSize(QtCore.QSize(423, 94))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(History)
        pixmap1 = QPixmap("Game Pictures/mission-text1.jpg")  # Перцы)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(900, 10, 900, 1000)


class History_2(object):
    # def __init__(self):
    #     self.pushButton = QtWidgets.QPushButton(Dialog_menu)

    def setupUi(self, History_2):
        History_2.setObjectName("History_2")
        History_2.resize(1800, 1000)

        hbox = QHBoxLayout()
        pixmap = QPixmap("Game Pictures/story-screen.jpg")
        lbl = QLabel()
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        History_2.setLayout(hbox)

        History_2.setWindowTitle('Expedition')

        self.pushButton = QtWidgets.QPushButton(History_2)
        self.pushButton.setGeometry(QtCore.QRect(442, 824, 403, 90))
        self.pushButton.setIcon(QtGui.QIcon("Game Pictures/dalee.png"))
        self.pushButton.setIconSize(QtCore.QSize(423, 94))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(History_2)
        pixmap1 = QPixmap("Game Pictures/mission-text2.jpg")  # Перцы)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(900, 10, 900, 1000)


class History_3(object):
    # def __init__(self):
    #     self.pushButton = QtWidgets.QPushButton(Dialog_menu)

    def setupUi(self, History_3):
        History_3.setObjectName("History_3")
        History_3.resize(1800, 1000)

        hbox = QHBoxLayout()
        pixmap = QPixmap("Game Pictures/story-screen.jpg")
        lbl = QLabel()
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        History_3.setLayout(hbox)

        History_3.setWindowTitle('Expedition')

        self.pushButton = QtWidgets.QPushButton(History_3)
        self.pushButton.setGeometry(QtCore.QRect(442, 824, 403, 90))
        self.pushButton.setIcon(QtGui.QIcon("Game Pictures/dalee.png"))
        self.pushButton.setIconSize(QtCore.QSize(423, 94))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(History_3)
        pixmap1 = QPixmap("Game Pictures/mission-text3.jpg")  # Перцы)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(900, 10, 900, 1000)


# Диалоговое меню выбора персоонажей

class Character_selection(object):
    # def __init__(self):
    #     self.pushButton = QtWidgets.QPushButton(Dialog_menu)



    def setupUi(self, Character_selection):
        Character_selection.setObjectName("Сharacter_selection")
        Character_selection.resize(1500, 1200)

        hbox = QHBoxLayout()
        pixmap1 = QPixmap("Персы.png")  # Перцы)
        lbl = QLabel()
        lbl.setPixmap(pixmap1)
        hbox.addWidget(lbl)
        Character_selection.setLayout(hbox)

        Character_selection.setWindowTitle('Change_persons')

        self.QCheckBox = QtWidgets.QCheckBox(Character_selection)
        self.QCheckBox.setText("Выбрать Нико Робин")
        self.QCheckBox.setGeometry(250, 280, 500, 500)

        self.QCheckBox_2 = QtWidgets.QCheckBox(Character_selection)
        self.QCheckBox_2.setText("Выбрать Джим Киперс")
        self.QCheckBox_2.setGeometry(860, 280, 500, 500)

        self.QCheckBox_3 = QtWidgets.QCheckBox(Character_selection)
        self.QCheckBox_3.setText("Выбрать Марко-Волкодав")
        self.QCheckBox_3.setGeometry(1450, 280, 500, 500)

        self.QCheckBox_4 = QtWidgets.QCheckBox(Character_selection)
        self.QCheckBox_4.setText("Выбрать Кэри Кинг")
        self.QCheckBox_4.setGeometry(250, 730, 500, 500)

        self.QCheckBox_5 = QtWidgets.QCheckBox(Character_selection)
        self.QCheckBox_5.setText("Выбрать Ангела")
        self.QCheckBox_5.setGeometry(860, 730, 500, 500)

        self.QCheckBox_6 = QtWidgets.QCheckBox(Character_selection)
        self.QCheckBox_6.setText("Выбрать Ник Гаймз")
        self.QCheckBox_6.setGeometry(1450, 730, 500, 500)

        self.pushButton = QtWidgets.QPushButton(Character_selection)
        self.pushButton.setGeometry(QtCore.QRect(750, 15, 403, 94))
        self.pushButton.setIcon(QtGui.QIcon("Game Pictures/dalee.png"))
        self.pushButton.setIconSize(QtCore.QSize(423, 94))
        self.pushButton.setObjectName("pushButton")


# ДИОЛОГОВОЕ ОКНО РАСПРЕДЕЛЕНИЯ ШМОТОК

class Item_distribution(object):
                                             # Сумки
    Nico_Robin_bag = {"Еда": 1}          # 7 кг
    Jim_Kippers_bag = {"Еда": 1}         # 8 кг
    Marco_Wolfhound_bag = {"Еда": 1}     # 8 кг
    Carry_King_bag = {"Еда": 1}          # 9 кг
    Angela_bag = {"Еда": 1}              # 6 кг
    Nick_James_bag = {"Еда": 1}          # 8 кг

    @staticmethod
    def nico_over():
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("Нико Робин перегружена")
        msgBox.setWindowTitle("Предупреждение")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        returnValue = msgBox.exec()  # Если не сохранить в переменную то всё сломается

    @staticmethod
    def Jim_over():
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("Джим Киперс перегружен")
        msgBox.setWindowTitle("Предупреждение")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        returnValue = msgBox.exec()  # Если не сохранить в переменную то всё сломается

    @staticmethod
    def Marco_over():
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("Марко Волкодав перегружен")
        msgBox.setWindowTitle("Предупреждение")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        returnValue = msgBox.exec()  # Если не сохранить в переменную то всё сломается

    @staticmethod
    def Cary_over():
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("Кэри Кинг перегружен")
        msgBox.setWindowTitle("Предупреждение")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        returnValue = msgBox.exec()  # Если не сохранить в переменную то всё сломается

    @staticmethod
    def angela_over():
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("Ангела перегружена")
        msgBox.setWindowTitle("Предупреждение")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        returnValue = msgBox.exec()  # Если не сохранить в переменную то всё сломается

    @staticmethod
    def nick_over():
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("Ник Ждеймс перегружен")
        msgBox.setWindowTitle("Предупреждение")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        returnValue = msgBox.exec()  # Если не сохранить в переменную то всё сломается


    def set_proggressbars(self):
        Idi.Nico_progress1.setValue(int(((sum(Item_distribution.Nico_Robin_bag.values())) * 100) / 7))
        if int(((sum(Item_distribution.Nico_Robin_bag.values())) * 100) / 7) > 100:
            Item_distribution.nico_over()
        Idi.Jim_progress2.setValue(int(((sum(Item_distribution.Jim_Kippers_bag.values()))*100)/8))
        if int(((sum(Item_distribution.Jim_Kippers_bag.values()))*100)/8) > 100:
            Item_distribution.Jim_over()
        Idi.Marco_progress3.setValue(int(((sum(Item_distribution.Marco_Wolfhound_bag.values()))*100)/8))
        if int(((sum(Item_distribution.Marco_Wolfhound_bag.values()))*100)/8) > 100:
            Item_distribution.Marco_over()
        Idi.Carry_progress4.setValue(int(((sum(Item_distribution.Carry_King_bag.values())) * 100) / 9))
        if int(((sum(Item_distribution.Carry_King_bag.values())) * 100) / 9) > 100:
            Item_distribution.Cary_over()
        Idi.Angela_progress5.setValue(int(((sum(Item_distribution.Angela_bag.values())) * 100) / 6))
        if int(((sum(Item_distribution.Angela_bag.values())) * 100) / 6) > 100:
            Item_distribution.angela_over()
        Idi.Nick_progress6.setValue(int(((sum(Item_distribution.Nick_James_bag.values())) * 100) / 8))
        if int(((sum(Item_distribution.Nick_James_bag.values())) * 100) / 8) > 100:
            Item_distribution.nick_over

    def set_text_to_labels(self):
        nico_str = ""
        for key, items in Item_distribution.Nico_Robin_bag.items():
            nico_str = nico_str + str(key) + " - " + str(items) + " кг \n"
        Idi.Nico_bag_label.setText(nico_str)
        Jim_str = ""
        for key, items in Item_distribution.Jim_Kippers_bag.items():
            Jim_str = Jim_str + str(key) + " - " + str(items) + " кг \n"
        Idi.Jim_bag_label.setText(Jim_str)
        Marco_str = ""
        for key, items in Item_distribution.Marco_Wolfhound_bag.items():
            Marco_str = Marco_str + str(key) + " - " + str(items) + " кг \n"
        Idi.Marco_bag_label.setText(Marco_str)
        Carry_str = ""
        for key, items in Item_distribution.Carry_King_bag.items():
            Carry_str = Carry_str + str(key) + " - " + str(items) + " кг \n"
        Idi.Carry_bag_label.setText(Carry_str)
        Angela_str = ""
        for key, items in Item_distribution.Angela_bag.items():
            Angela_str = Angela_str + str(key) + " - " + str(items) + " кг \n"
        Idi.Angela_bag_label.setText(Angela_str)
        Nick_str = ""
        for key, items in Item_distribution.Angela_bag.items():
            Nick_str = Nick_str + str(key) + " - " + str(items) + " кг \n"
        Idi.Nick_bag_label.setText(Nick_str)

    def set_start_value_for_progressbars(self):
        Idi.Nico_progress1.setValue(10)
        Idi.Jim_progress2.setValue(10)
        Idi.Marco_progress3.setValue(10)
        Idi.Carry_progress4.setValue(10)
        Idi.Angela_progress5.setValue(10)
        Idi.Nick_progress6.setValue(10)


    def stick_function(self):
        Item_distribution.Nico_Robin_bag.pop("Посох 1", "")
        Item_distribution.Jim_Kippers_bag.pop("Посох 1", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Посох 1", "")
        Item_distribution.Carry_King_bag.pop("Посох 1", "")
        Item_distribution.Angela_bag.pop("Посох 1", "")
        Item_distribution.Nick_James_bag.pop("Посох 1", "")
        if self.stick_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Посох 1"] = 0.5
        elif self.stick_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Посох 1"] = 0.5
        elif self.stick_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Посох 1"] = 0.5
        elif self.stick_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Посох 1"] = 0.5
        elif self.stick_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Посох 1"] = 0.5
        elif self.stick_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Посох 1"] = 0.5
        self.set_proggressbars()
        self.set_start_value_for_progressbars()
        self.set_text_to_labels()


    def stick2_function(self):
        Item_distribution.Nico_Robin_bag.pop("Посох 2", "")
        Item_distribution.Jim_Kippers_bag.pop("Посох 2", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Посох 2", "")
        Item_distribution.Carry_King_bag.pop("Посох 2", "")
        Item_distribution.Angela_bag.pop("Посох 2", "")
        Item_distribution.Nick_James_bag.pop("Посох 2", "")
        if self.stick2_combobox.currentText() == "Нико Робин":
             Item_distribution.Nico_Robin_bag["Посох 2"] = 0.5
        elif self.stick2_combobox.currentText() == "Джим Киперс":
             Item_distribution.Jim_Kippers_bag["Посох 2"] = 0.5
        elif self.stick2_combobox.currentText() == "Марко Волкодав":
              Item_distribution.Marco_Wolfhound_bag["Посох 2"] = 0.5
        elif self.stick2_combobox.currentText() == "Кэри Кинг":
             Item_distribution.Carry_King_bag["Посох 2"] = 0.5
        elif self.stick2_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Посох 12"] = 0.5
        elif self.stick2_combobox.currentText() == "Ник Джеймс":
             Item_distribution.Nick_James_bag["Посох 2"] = 0.5
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def bag_function(self):
         Item_distribution.Nico_Robin_bag.pop("Рюкзак", "")
         Item_distribution.Jim_Kippers_bag.pop("Рюкзак", "")
         Item_distribution.Marco_Wolfhound_bag.pop("Рюкзак", "")
         Item_distribution.Carry_King_bag.pop("Рюкзак", "")
         Item_distribution.Angela_bag.pop("Рюкзак", "")
         Item_distribution.Nick_James_bag.pop("Рюкзак", "")
         if self.bag_combobox.currentText() == "Нико Робин":
             Item_distribution.Nico_Robin_bag["Рюкзак"] = 1
         elif self.bag_combobox.currentText() == "Джим Киперс":
             Item_distribution.Jim_Kippers_bag["Рюкзак"] = 1
         elif self.bag_combobox.currentText() == "Марко Волкодав":
             Item_distribution.Marco_Wolfhound_bag["Рюкзак"] = 1
         elif self.bag_combobox.currentText() == "Кэри Кинг":
             Item_distribution.Carry_King_bag["Рюкзак"] = 1
         elif self.bag_combobox.currentText() == "Ангела":
             Item_distribution.Angela_bag["Рюкзак"] = 1
         elif self.bag_combobox.currentText() == "Ник Джеймс":
             Item_distribution.Nick_James_bag["Рюкзак"] = 1
         self.set_start_value_for_progressbars()
         self.set_proggressbars()
         self.set_text_to_labels()

    def compass_function(self):
        Item_distribution.Nico_Robin_bag.pop("Компас", "")
        Item_distribution.Jim_Kippers_bag.pop("Компас", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Компас", "")
        Item_distribution.Carry_King_bag.pop("Компас", "")
        Item_distribution.Angela_bag.pop("Компас", "")
        Item_distribution.Nick_James_bag.pop("Компас", "")
        if self.compass_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Компас"] = 0
        elif self.compass_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Компас"] = 0
        elif self.compass_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Компас"] = 0
        elif self.compass_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Компас"] = 0
        elif self.compass_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Компас"] = 0
        elif self.compass_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Компас"] = 0
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def rope_function(self):
        Item_distribution.Nico_Robin_bag.pop("Веревка", "")
        Item_distribution.Jim_Kippers_bag.pop("Веревка", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Веревка", "")
        Item_distribution.Carry_King_bag.pop("Веревка", "")
        Item_distribution.Angela_bag.pop("Веревка", "")
        Item_distribution.Nick_James_bag.pop("Веревка", "")
        if self.rope_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Веревка"] = 0.5
        elif self.rope_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Веревка"] = 0.5
        elif self.rope_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Веревка"] = 0.5
        elif self.rope_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Веревка"] = 0.5
        elif self.rope_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Веревка"] = 0.5
        elif self.rope_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Веревка"] = 0.5
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def wineskin_function(self):
        Item_distribution.Nico_Robin_bag.pop("Бурдюк 1", "")
        Item_distribution.Jim_Kippers_bag.pop("Бурдюк 1", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Бурдюк 1", "")
        Item_distribution.Carry_King_bag.pop("Бурдюк 1", "")
        Item_distribution.Angela_bag.pop("Бурдюк 1", "")
        Item_distribution.Nick_James_bag.pop("Бурдюк 1", "")
        if self.wineskin_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Бурдюк 1"] = 0.6
        elif self.wineskin_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Бурдюк 1"] = 0.6
        elif self.wineskin_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Бурдюк 1"] = 0.6
        elif self.wineskin_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Бурдюк 1"] = 0.6
        elif self.wineskin_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Бурдюк 1"] = 0.6
        elif self.wineskin_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Бурдюк 1"] = 0.6
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def wineskin2_function(self):
        Item_distribution.Nico_Robin_bag.pop("Бурдюк 2", "")
        Item_distribution.Jim_Kippers_bag.pop("Бурдюк 2", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Бурдюк 2", "")
        Item_distribution.Carry_King_bag.pop("Бурдюк 2", "")
        Item_distribution.Angela_bag.pop("Бурдюк 2", "")
        Item_distribution.Nick_James_bag.pop("Бурдюк 2", "")
        if self.wineskin2_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Бурдюк 2"] = 0.6
        elif self.wineskin2_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Бурдюк 2"] = 0.6
        elif self.wineskin2_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Бурдюк 2"] = 0.6
        elif self.wineskin2_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Бурдюк 2"] = 0.6
        elif self.wineskin2_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Бурдюк 2"] = 0.6
        elif self.wineskin2_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Бурдюк 2"] = 0.6
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def flask_function(self):
        Item_distribution.Nico_Robin_bag.pop("Фляга 1", "")
        Item_distribution.Jim_Kippers_bag.pop("Фляга 1", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Фляга 1", "")
        Item_distribution.Carry_King_bag.pop("Фляга 1", "")
        Item_distribution.Angela_bag.pop("Фляга 1","")
        Item_distribution.Nick_James_bag.pop("Фляга 1", "")
        if self.flask_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Фляга 1"] = 0.4
        elif self.flask_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Фляга 1"] = 0.4
        elif self.flask_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Фляга 1"] = 0.4
        elif self.flask_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Фляга 1"] = 0.4
        elif self.flask_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Фляга 1"] = 0.4
        elif self.flask_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Фляга 1"] = 0.4
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def flask2_function(self):
        Item_distribution.Nico_Robin_bag.pop("Фляга 2", "")
        Item_distribution.Jim_Kippers_bag.pop("Фляга 2", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Фляга 2", "")
        Item_distribution.Carry_King_bag.pop("Фляга 2", "")
        Item_distribution.Angela_bag.pop("Фляга 2", "")
        Item_distribution.Nick_James_bag.pop("Фляга 2", "")
        if self.flask2_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Фляга 2"] = 0.4
        elif self.flask2_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Фляга 2"] = 0.4
        elif self.flask2_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Фляга 2"] = 0.4
        elif self.flask2_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Фляга 2"] = 0.4
        elif self.flask2_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Фляга 2"] = 0.4
        elif self.flask2_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Фляга 2"] = 0.4
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def flask3_function(self):
        Item_distribution.Nico_Robin_bag.pop("Фляга 3", "")
        Item_distribution.Jim_Kippers_bag.pop("Фляга 3", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Фляга 3", "")
        Item_distribution.Carry_King_bag.pop("Фляга 3", "")
        Item_distribution.Angela_bag.pop("Фляга 3", "")
        Item_distribution.Nick_James_bag.pop("Фляга 3", "")
        if self.flask3_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Фляга 3"] = 0.4
        elif self.flask3_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Фляга 3"] = 0.4
        elif self.flask3_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Фляга 3"] = 0.4
        elif self.flask3_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Фляга 3"] = 0.4
        elif self.flask3_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Фляга 3"] = 0.4
        elif self.flask3_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Фляга 3"] = 0.4
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def blanket1_function(self):
        Item_distribution.Nico_Robin_bag.pop("Одеяло 1", "")
        Item_distribution.Jim_Kippers_bag.pop("Одеяло 1", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Одеяло 1", "")
        Item_distribution.Carry_King_bag.pop("Одеяло 1", "")
        Item_distribution.Angela_bag.pop("Одеяло 1", "")
        Item_distribution.Nick_James_bag.pop("Одеяло 1", "")
        if self.blanket_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Одеяло 1"] = 1
        elif self.blanket_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Одеяло 1"] = 1
        elif self.blanket_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Одеяло 1"] = 1
        elif self.blanket_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Одеяло 1"] = 1
        elif self.blanket_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Одеяло 1"] = 1
        elif self.blanket_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Одеяло 1"] = 1
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def blanket2_function(self):
        Item_distribution.Nico_Robin_bag.pop("Одеяло 2", "")
        Item_distribution.Jim_Kippers_bag.pop("Одеяло 2", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Одеяло 2", "")
        Item_distribution.Carry_King_bag.pop("Одеяло 2", "")
        Item_distribution.Angela_bag.pop("Одеяло 2", "")
        Item_distribution.Nick_James_bag.pop("Одеяло 2", "")
        if self.blanket2_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Одеяло 2"] = 1
        elif self.blanket2_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Одеяло 2"] = 1
        elif self.blanket2_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Одеяло 2"] = 1
        elif self.blanket2_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Одеяло 2"] = 1
        elif self.blanket2_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Одеяло 2"] = 1
        elif self.blanket2_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Одеяло 2"] = 1
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def tent_for_3_function(self):
        Item_distribution.Nico_Robin_bag.pop("Палатка на 3их", "")
        Item_distribution.Jim_Kippers_bag.pop("Палатка на 3их", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Палатка на 3их", "")
        Item_distribution.Carry_King_bag.pop("Палатка на 3их", "")
        Item_distribution.Angela_bag.pop("Палатка на 3их", "")
        Item_distribution.Nick_James_bag.pop("Палатка на 3их", "")
        if self.tent_for_3_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Палатка на 3их"] = 4.5
        elif self.tent_for_3_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Палатка на 3их"] = 4.5
        elif self.tent_for_3_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Палатка на 3их"] = 4.5
        elif self.tent_for_3_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Палатка на 3их"] = 4.5
        elif self.tent_for_3_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Палатка на 3их"] = 4.5
        elif self.tent_for_3_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Палатка на 3их"] = 4.5
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def machete_function(self):
        Item_distribution.Nico_Robin_bag.pop("Мачете", "")
        Item_distribution.Jim_Kippers_bag.pop("Мачете", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Мачете", "")
        Item_distribution.Carry_King_bag.pop("Мачете", "")
        Item_distribution.Angela_bag.pop("Мачете", "")
        Item_distribution.Nick_James_bag.pop("Мачете", "")
        if self.machete_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Мачете"] = 0.5
        elif self.machete_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Мачете"] = 0.5
        elif self.machete_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Мачете"] = 0.5
        elif self.machete_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Мачете"] = 0.5
        elif self.machete_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Мачете"] = 0.5
        elif self.machete_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Мачете"] = 0.5
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def climbing_equipment_function(self):
        Item_distribution.Nico_Robin_bag.pop("Альпинистское снаряжение", "")
        Item_distribution.Jim_Kippers_bag.pop("Альпинистское снаряжение", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Альпинистское снаряжение", "")
        Item_distribution.Carry_King_bag.pop("Альпинистское снаряжение", "")
        Item_distribution.Angela_bag.pop("Альпинистское снаряжение", "")
        Item_distribution.Nick_James_bag.pop("Альпинистское снаряжение", "")
        if self.climbing_equipment_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Альпинистское снаряжение"] = 1
        elif self.climbing_equipment_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Альпинистское снаряжение"] = 1
        elif self.climbing_equipment_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Альпинистское снаряжение"] = 1
        elif self.climbing_equipment_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Альпинистское снаряжение"] = 1
        elif self.climbing_equipment_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Альпинистское снаряжение"] = 1
        elif self.climbing_equipment_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Альпинистское снаряжение"] = 1
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def knife_function(self):
        Item_distribution.Nico_Robin_bag.pop("Нож", "")
        Item_distribution.Jim_Kippers_bag.pop("Нож", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Нож", "")
        Item_distribution.Carry_King_bag.pop("Нож", "")
        Item_distribution.Angela_bag.pop("Нож", "")
        Item_distribution.Nick_James_bag.pop("Нож", "")
        if self.knife_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Нож"] = 0.3
        elif self.knife_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Нож"] = 0.3
        elif self.knife_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Нож"] = 0.3
        elif self.knife_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Нож"] = 0.3
        elif self.knife_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Нож"] = 0.3
        elif self.knife_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Нож"] = 0.3
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def medic_kid_function(self):
        Item_distribution.Nico_Robin_bag.pop("Аптечка", "")
        Item_distribution.Jim_Kippers_bag.pop("Аптечка", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Аптечка", "")
        Item_distribution.Carry_King_bag.pop("Аптечка", "")
        Item_distribution.Angela_bag.pop("Аптечка", "")
        Item_distribution.Nick_James_bag.pop("Аптечка", "")
        if self.medik_kid_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Аптечка"] = 0.5
        elif self.medik_kid_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Аптечка"] = 0.5
        elif self.medik_kid_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Аптечка"] = 0.5
        elif self.medik_kid_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Аптечка"] = 0.5
        elif self.medik_kid_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Аптечка"] = 0.5
        elif self.medik_kid_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Аптечка"] = 0.5
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def fracture_first_aid_function(self):
        Item_distribution.Nico_Robin_bag.pop("Первая помощь при переломах", "")
        Item_distribution.Jim_Kippers_bag.pop("Первая помощь при переломах", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Первая помощь при переломах", "")
        Item_distribution.Carry_King_bag.pop("Первая помощь при переломах", "")
        Item_distribution.Angela_bag.pop("Первая помощь при переломах", "")
        Item_distribution.Nick_James_bag.pop("Первая помощь при переломах", "")
        if self.fracture_medik_kid_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Первая помощь при переломах"] = 0.5
        elif self.fracture_medik_kid_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Первая помощь при переломах"] = 0.5
        elif self.fracture_medik_kid_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Первая помощь при переломах"] = 0.5
        elif self.fracture_medik_kid_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Первая помощь при переломах"] = 0.5
        elif self.fracture_medik_kid_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Первая помощь при переломах"] = 0.5
        elif self.fracture_medik_kid_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Первая помощь при переломах"] = 0.5
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def antidode_function(self):
        Item_distribution.Nico_Robin_bag.pop("Противоядие", "")
        Item_distribution.Jim_Kippers_bag.pop("Противоядие", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Противоядие", "")
        Item_distribution.Carry_King_bag.pop("Противоядие", "")
        Item_distribution.Angela_bag.pop("Противоядие", "")
        Item_distribution.Nick_James_bag.pop("Противоядие", "")
        if self.antidote_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Противоядие"] = 0.5
        elif self.antidote_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Противоядие"] = 0.5
        elif self.antidote_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Противоядие"] = 0.5
        elif self.antidote_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Противоядие"] = 0.5
        elif self.antidote_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Противоядие"] = 0.5
        elif self.antidote_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Противоядие"] = 0.5
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def trap_function(self):
        Item_distribution.Nico_Robin_bag.pop("Капкан", "")
        Item_distribution.Jim_Kippers_bag.pop("Капкан", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Капкан", "")
        Item_distribution.Carry_King_bag.pop("Капкан", "")
        Item_distribution.Angela_bag.pop("Капкан", "")
        Item_distribution.Nick_James_bag.pop("Капкан", "")
        if self.trap_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Капкан"] = 1
        elif self.trap_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Капкан"] = 1
        elif self.trap_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Капкан"] = 1
        elif self.trap_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Капкан"] = 1
        elif self.trap_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Капкан"] = 1
        elif self.trap_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Капкан"] = 1
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def travelling_set_function(self):
        Item_distribution.Nico_Robin_bag.pop("Походный набор", "")
        Item_distribution.Jim_Kippers_bag.pop("Походный набор", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Походный набор", "")
        Item_distribution.Carry_King_bag.pop("Походный набор", "")
        Item_distribution.Angela_bag.pop("Походный набор", "")
        Item_distribution.Nick_James_bag.pop("Походный набор", "")
        if self.trevelling_set_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Походный набор"] = 1
        elif self.trevelling_set_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Походный набор"] = 1
        elif self.trevelling_set_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Походный набор"] = 1
        elif self.trevelling_set_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Походный набор"] = 1
        elif self.trevelling_set_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Походный набор"] = 1
        elif self.trevelling_set_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Походный набор"] = 1
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

    def flare_function(self):
        Item_distribution.Nico_Robin_bag.pop("Сигнальная ракета", "")
        Item_distribution.Jim_Kippers_bag.pop("Сигнальная ракета", "")
        Item_distribution.Marco_Wolfhound_bag.pop("Сигнальная ракета", "")
        Item_distribution.Carry_King_bag.pop("Сигнальная ракета", "")
        Item_distribution.Angela_bag.pop("Сигнальная ракета", "")
        Item_distribution.Nick_James_bag.pop("Сигнальная ракета", "")
        if self.flare_combobox.currentText() == "Нико Робин":
            Item_distribution.Nico_Robin_bag["Сигнальная ракета"] = 0.5
        elif self.flare_combobox.currentText() == "Джим Киперс":
            Item_distribution.Jim_Kippers_bag["Сигнальная ракета"] = 0.5
        elif self.flare_combobox.currentText() == "Марко Волкодав":
            Item_distribution.Marco_Wolfhound_bag["Сигнальная ракета"] = 0.5
        elif self.flare_combobox.currentText() == "Кэри Кинг":
            Item_distribution.Carry_King_bag["Сигнальная ракета"] = 0.5
        elif self.flare_combobox.currentText() == "Ангела":
            Item_distribution.Angela_bag["Сигнальная ракета"] = 0.5
        elif self.flare_combobox.currentText() == "Ник Джеймс":
            Item_distribution.Nick_James_bag["Сигнальная ракета"] = 0.5
        self.set_start_value_for_progressbars()
        self.set_proggressbars()
        self.set_text_to_labels()

        # print(Item_distribution.Nico_Robin_bag, "Nico")
        # print(int(((sum(Item_distribution.Nico_Robin_bag.values()))*100)/7))
        # print(Item_distribution.Jim_Kippers_bag, "Jim")
        # print(Item_distribution.Marco_Wolfhound_bag, "Marco")
        # print(Item_distribution.Carry_King_bag, "Carry")
        # print(Item_distribution.Angela_bag, "Angela")
        # print(Item_distribution.Nick_James_bag, "Nick")
        # print("")

    def change_proggressbars_text(self):
        Idi.Nico_progress1.setFormat(str(int(((sum(Item_distribution.Nico_Robin_bag.values())) * 100) / 7)) + " % Загруженность")
        Idi.Jim_progress2.setFormat(str(int(((sum(Item_distribution.Jim_Kippers_bag.values())) * 100) / 8)) + " % Загруженность")
        Idi.Marco_progress3.setFormat(str(int(((sum(Item_distribution.Marco_Wolfhound_bag.values())) * 100) / 8)) + " % Загруженность")
        Idi.Carry_progress4.setFormat(str(int(((sum(Item_distribution.Carry_King_bag.values())) * 100) / 9)) + " % Загруженность")
        Idi.Angela_progress5.setFormat(str(int(((sum(Item_distribution.Angela_bag.values())) * 100) / 6)) + " % Загруженность")
        Idi.Nick_progress6.setFormat(str(int(((sum(Item_distribution.Nick_James_bag.values())) * 100) / 8)) + " % Загруженность")
    # def func(self):
    #       print(self.stick_combobox.currentText())   # Функцию поменять

    def setupUi(self, Item_distribution):
        Item_distribution.setObjectName("Item_distribution")
        Item_distribution.resize(1500, 1200)

        hbox = QHBoxLayout()
        pixmap1 = QPixmap("Game Pictures/story-screen.jpg")  # Экран истории)
        lbl = QLabel()
        lbl.setPixmap(pixmap1)
        hbox.addWidget(lbl)
        Item_distribution.setLayout(hbox)

        Item_distribution.setWindowTitle('Item_distribution')


        self.stick_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Посох.png")
        self.stick_labbel.setPixmap(pixmap1)
        self.stick_labbel.setGeometry(100, 200, 100, 100)
        self.stick_labbel.setToolTip("0.5кг. Раз в день на передвижение тратится \nна 1 действие меньше \n(не может быть меньше 1 действия). \nПри сражении с врагами +1 к силе")

        self.stick_combobox = QtWidgets.QComboBox(Item_distribution)
        self.stick_combobox.setGeometry(100, 300, 100, 20)
        self.stick_combobox.activated.connect(self.stick_function)   # комбобокс (выпадающий список)
        self.stick_combobox.activated.connect(self.change_proggressbars_text)

        self.stick2_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Посох.png")
        self.stick2_labbel.setPixmap(pixmap1)
        self.stick2_labbel.setGeometry(250, 200, 100, 100)
        self.stick2_labbel.setToolTip("0.5кг. Раз в день на передвижение тратится \nна 1 действие меньше \n(не может быть меньше 1 действия). \nПри сражении с врагами +1 к силе")

        self.stick2_combobox = QtWidgets.QComboBox(Item_distribution)
        self.stick2_combobox.setGeometry(250, 300, 100, 20)
        self.stick2_combobox.activated.connect(self.stick2_function)
        self.stick2_combobox.activated.connect(self.change_proggressbars_text)

        self.bag_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Рюкзак.png")
        self.bag_labbel.setPixmap(pixmap1)
        self.bag_labbel.setGeometry(400, 200, 100, 100)
        self.bag_labbel.setToolTip("1 кг. Увеличивает грузоподъемность на 2 кг")

        self.bag_combobox = QtWidgets.QComboBox(Item_distribution)
        self.bag_combobox.setGeometry(400, 300, 100, 20)
        self.bag_combobox.activated.connect(self.bag_function)
        self.bag_combobox.activated.connect(self.change_proggressbars_text)

        self.compass_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Компас.png")
        self.compass_labbel.setPixmap(pixmap1)
        self.compass_labbel.setGeometry(550, 200, 100, 100)
        self.compass_labbel.setToolTip("0кг. Дает +2 к параметру навигации.")

        self.compass_combobox = QtWidgets.QComboBox(Item_distribution)
        self.compass_combobox.setGeometry(550, 300, 100, 20)
        self.compass_combobox.activated.connect(self.compass_function)
        self.compass_combobox.activated.connect(self.change_proggressbars_text)

        self.rope_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Веревка.png")
        self.rope_labbel.setPixmap(pixmap1)
        self.rope_labbel.setGeometry(700, 200, 100, 100)
        self.rope_labbel.setToolTip("0.5кг. При перемещении в горных районах \nпозволяет одному из исследователей \nпотратить на 1 действие меньше.")

        self.rope_combobox = QtWidgets.QComboBox(Item_distribution)
        self.rope_combobox.setGeometry(700, 300, 100, 20)
        self.rope_combobox.activated.connect(self.rope_function)
        self.rope_combobox.activated.connect(self.change_proggressbars_text)

        self.wineskin_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Бурдюк.png")
        self.wineskin_labbel.setPixmap(pixmap1)
        self.wineskin_labbel.setGeometry(850, 200, 100, 100)
        self.wineskin_labbel.setToolTip("0,6кг полный, 0,3кг пустой. Помогает сохранить воду. \nВмещает две дневные нормы воды.")

        self.wineskin_combobox = QtWidgets.QComboBox(Item_distribution)
        self.wineskin_combobox.setGeometry(850, 300, 100, 20)
        self.wineskin_combobox.activated.connect(self.wineskin_function)
        self.wineskin_combobox.activated.connect(self.change_proggressbars_text)

        self.wineskin2_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Бурдюк.png")
        self.wineskin2_labbel.setPixmap(pixmap1)
        self.wineskin2_labbel.setGeometry(1000, 200, 100, 100)
        self.wineskin2_labbel.setToolTip("0,6кг полный, 0,3кг пустой. Помогает сохранить воду. \nВмещает две дневные нормы воды.")

        self.wineskin2_combobox = QtWidgets.QComboBox(Item_distribution)
        self.wineskin2_combobox.setGeometry(1000, 300, 100, 20)
        self.wineskin2_combobox.activated.connect(self.wineskin2_function)
        self.wineskin2_combobox.activated.connect(self.change_proggressbars_text)

        self.flask_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Фляга.png")
        self.flask_labbel.setPixmap(pixmap1)
        self.flask_labbel.setGeometry(1150, 200, 100, 100)
        self.flask_labbel.setToolTip("0,4кг полная, 0,2кг пустая. Помогает сохранить воду. \nВмещает одну дневную норму воды.")

        self.flask_combobox = QtWidgets.QComboBox(Item_distribution)
        self.flask_combobox.setGeometry(1150, 300, 100, 20)
        self.flask_combobox.activated.connect(self.flask_function)
        self.flask_combobox.activated.connect(self.change_proggressbars_text)

        self.flask2_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Фляга.png")
        self.flask2_labbel.setPixmap(pixmap1)
        self.flask2_labbel.setGeometry(1300, 200, 100, 100)
        self.flask2_labbel.setToolTip("0,4кг полная, 0,2кг пустая. Помогает сохранить воду. \nВмещает одну дневную норму воды.")

        self.flask2_combobox = QtWidgets.QComboBox(Item_distribution)
        self.flask2_combobox.setGeometry(1300, 300, 100, 20)
        self.flask2_combobox.activated.connect(self.flask2_function)
        self.flask2_combobox.activated.connect(self.change_proggressbars_text)

        self.flask3_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Фляга.png")
        self.flask3_labbel.setPixmap(pixmap1)
        self.flask3_labbel.setGeometry(1450, 200, 100, 100)
        self.flask3_labbel.setToolTip("0,4кг полная, 0,2кг пустая. Помогает сохранить воду. \nВмещает одну дневную норму воды.")

        self.flask3_combobox = QtWidgets.QComboBox(Item_distribution)
        self.flask3_combobox.setGeometry(1450, 300, 100, 20)
        self.flask3_combobox.activated.connect(self.flask3_function)
        self.flask3_combobox.activated.connect(self.change_proggressbars_text)

        self.blanket_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Тёплое одеяло.png")
        self.blanket_labbel.setPixmap(pixmap1)
        self.blanket_labbel.setGeometry(1600, 200, 100, 100)
        self.blanket_labbel.setToolTip("1кг. Защищает от холода одного человека")

        self.blanket_combobox = QtWidgets.QComboBox(Item_distribution)
        self.blanket_combobox.setGeometry(1600, 300, 100, 20)
        self.blanket_combobox.activated.connect(self.blanket1_function)
        self.blanket_combobox.activated.connect(self.change_proggressbars_text)

        self.blanket2_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Тёплое одеяло.png")
        self.blanket2_labbel.setPixmap(pixmap1)
        self.blanket2_labbel.setGeometry(1750, 200, 100, 100)
        self.blanket2_labbel.setToolTip("1кг. Защищает от холода одного человека")

        self.blanket2_combobox = QtWidgets.QComboBox(Item_distribution)
        self.blanket2_combobox.setGeometry(1750, 300, 100, 20)
        self.blanket2_combobox.activated.connect(self.blanket2_function)
        self.blanket2_combobox.activated.connect(self.change_proggressbars_text)

        self.tent_for_3_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/3х местная палатка.png")
        self.tent_for_3_labbel.setPixmap(pixmap1)
        self.tent_for_3_labbel.setGeometry(100, 400, 100, 100)
        self.tent_for_3_labbel.setToolTip("4,5кг. Разложить - 1 действие. \nИсследователи ночующие без палатки, \nвосстанавливают на 1 действие меньше за ночь.")

        self.tent_for_3_combobox = QtWidgets.QComboBox(Item_distribution)
        self.tent_for_3_combobox.setGeometry(100, 500, 100, 20)
        self.tent_for_3_combobox.activated.connect(self.tent_for_3_function)
        self.tent_for_3_combobox.activated.connect(self.change_proggressbars_text)

        self.machete_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Мачете.png")
        self.machete_labbel.setPixmap(pixmap1)
        self.machete_labbel.setGeometry(250, 400, 100, 100)
        self.machete_labbel.setToolTip("0,5кг. При использовании во время \nсражения дает +2 к силе и наносит + 1 повреждение.\n"
                                       "При передвижении по джунглям, \nвпереди идущий может потратить дополнительное\n действие, чтоб уменьшить сложность похода на 1.")

        self.machete_combobox = QtWidgets.QComboBox(Item_distribution)
        self.machete_combobox.setGeometry(250, 500, 100, 20)
        self.machete_combobox.activated.connect(self.machete_function)
        self.machete_combobox.activated.connect(self.change_proggressbars_text)

        self.climbing_equipment_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Альпенистское снаряжение.png")
        self.climbing_equipment_labbel.setPixmap(pixmap1)
        self.climbing_equipment_labbel.setGeometry(400, 400, 100, 100)
        self.climbing_equipment_labbel.setToolTip("1кг. Пробираясь по горной местности, \nигрок с этой картой может потратить \nдополнительное действие, чтобы остальные члены "
                                                  "\nэкспедиции потратили на одной дествие меньше.")

        self.climbing_equipment_combobox = QtWidgets.QComboBox(Item_distribution)
        self.climbing_equipment_combobox.setGeometry(400, 500, 100, 20)
        self.climbing_equipment_combobox.activated.connect(self.climbing_equipment_function)
        self.climbing_equipment_combobox.activated.connect(self.change_proggressbars_text)

        self.knife_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Нож.png")
        self.knife_labbel.setPixmap(pixmap1)
        self.knife_labbel.setGeometry(550, 400, 100, 100)
        self.knife_labbel.setToolTip("0,3 кг. + 1 внимание при поиске еды \n+ 1 сила во время сражения.")

        self.knife_combobox = QtWidgets.QComboBox(Item_distribution)
        self.knife_combobox.setGeometry(550, 500, 100, 20)
        self.knife_combobox.activated.connect(self.knife_function)
        self.knife_combobox.activated.connect(self.change_proggressbars_text)

        self.medik_kid_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Аптечка.png")
        self.medik_kid_labbel.setPixmap(pixmap1)
        self.medik_kid_labbel.setGeometry(700, 400, 100, 100)
        self.medik_kid_labbel.setToolTip("0,5кг. За 1 действие можно вылечить легкое ранение \nили остановить тяжелое кровотечение. Имеет 3 заряда.")

        self.medik_kid_combobox = QtWidgets.QComboBox(Item_distribution)
        self.medik_kid_combobox.setGeometry(700, 500, 100, 20)
        self.medik_kid_combobox.activated.connect(self.medic_kid_function)
        self.medik_kid_combobox.activated.connect(self.change_proggressbars_text)

        self.fracture_medik_kid_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Первая помочь при переломах.png")
        self.fracture_medik_kid_labbel.setPixmap(pixmap1)
        self.fracture_medik_kid_labbel.setGeometry(850, 400, 100, 100)
        self.fracture_medik_kid_labbel.setToolTip("0,5кг. За 1 действие можно вылечить тяжелое ранение, \nранение или использовать при переломах.")

        self.fracture_medik_kid_combobox = QtWidgets.QComboBox(Item_distribution)
        self.fracture_medik_kid_combobox.setGeometry(850, 500, 100, 20)
        self.fracture_medik_kid_combobox.activated.connect(self.fracture_first_aid_function)
        self.fracture_medik_kid_combobox.activated.connect(self.change_proggressbars_text)

        self.antidote_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Противоядие.png")
        self.antidote_labbel.setPixmap(pixmap1)
        self.antidote_labbel.setGeometry(1000, 400, 100, 100)
        self.antidote_labbel.setToolTip("0,5кг. За 1 действие можно вылечить Укус насекомых, \nУкус ядовитой змеи. Имеет 3 зарядов")

        self.antidote_combobox = QtWidgets.QComboBox(Item_distribution)
        self.antidote_combobox.setGeometry(1000, 500, 100, 20)
        self.antidote_combobox.activated.connect(self.antidode_function)
        self.antidote_combobox.activated.connect(self.change_proggressbars_text)

        self.trap_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Капкан.png")
        self.trap_labbel.setPixmap(pixmap1)
        self.trap_labbel.setGeometry(1150, 400, 100, 100)
        self.trap_labbel.setToolTip("1кг. Установка/снятие - 1 действие. \nЗащищает лагерь от нападения хищников в ночное время. \n"
                                    "Могут пользоваться только исследователи с навыком Охота.")

        self.trap_combobox = QtWidgets.QComboBox(Item_distribution)
        self.trap_combobox.setGeometry(1150, 500, 100, 20)
        self.trap_combobox.activated.connect(self.trap_function)
        self.trap_combobox.activated.connect(self.change_proggressbars_text)

        self.trevelling_set_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Походный набор.png")
        self.trevelling_set_labbel.setPixmap(pixmap1)
        self.trevelling_set_labbel.setGeometry(1300, 400, 100, 100)
        self.trevelling_set_labbel.setToolTip("1кг. Удваивает количество провизии, \nкоторую можно получить за убийство животных.")

        self.trevelling_set_combobox = QtWidgets.QComboBox(Item_distribution)
        self.trevelling_set_combobox.setGeometry(1300, 500, 100, 20)
        self.trevelling_set_combobox.activated.connect(self.travelling_set_function)
        self.trevelling_set_combobox.activated.connect(self.change_proggressbars_text)

        self.flare_labbel = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Game Pictures/Предметы/Сигнальная ракета.png")
        self.flare_labbel.setPixmap(pixmap1)
        self.flare_labbel.setGeometry(1450, 400, 100, 100)
        self.flare_labbel.setToolTip("0.5кг. Если вы как минимум в трех локациях от зоны высадки, \nможете за 1 действие сбросить эту карту, \n"
                                     "и передвинуть счетчик времени на 1 деление назад по треку.")

        self.flare_combobox = QtWidgets.QComboBox(Item_distribution)
        self.flare_combobox.setGeometry(1450, 500, 100, 20)
        self.flare_combobox.activated.connect(self.flare_function)
        self.flare_combobox.activated.connect(self.change_proggressbars_text)



        self.pushButton = QtWidgets.QPushButton(Item_distribution)          # Далее
        self.pushButton.setGeometry(QtCore.QRect(750, 15, 403, 94))
        self.pushButton.setIcon(QtGui.QIcon("Game Pictures/dalee.png"))
        self.pushButton.setIconSize(QtCore.QSize(423, 94))
        self.pushButton.setObjectName("pushButton")

        self.Nico_label = QtWidgets.QLabel(Item_distribution)               # Иконки персов
        pixmap1 = QPixmap("Persons/Nico Robin face small.png")
        self.Nico_label.setPixmap(pixmap1)
        self.Nico_label.setGeometry(130, 700, 300, 300)

        self.Nico_progress1 = QtWidgets.QProgressBar(Item_distribution)
        self.Nico_progress1.setGeometry(130, 950, 220, 20)
        self.Nico_progress1.setValue(0)
        self.Nico_progress1.setFormat("Загруженность")
        self.Nico_progress1.setAlignment(Qt.Qt.AlignCenter)
        self.Nico_progress1.setFont(QtGui.QFont("18"))
        self.Nico_progress1.setFixedWidth(150)

        self.Nico_bag_label = QtWidgets.QLabel(Item_distribution)
        self.Nico_bag_label.setGeometry(QtCore.QRect(130, 550, 150, 200))
        self.Nico_bag_label.setStyleSheet("background-color: grey;")
        self.Nico_bag_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Nico_bag_label.setWordWrap(True)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.Nico_bag_label.setFont(font)
        # self.Nico_bag_label.setText("Test")
        self.Nico_bag_label.setObjectName("Nico_bag_label")

        self.Jim_label_2 = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Persons/Jim Kipers face small.png")
        self.Jim_label_2.setPixmap(pixmap1)
        self.Jim_label_2.setGeometry(430, 700, 300, 300)

        self.Jim_progress2 = QtWidgets.QProgressBar(Item_distribution)
        self.Jim_progress2.setGeometry(430, 950, 220, 20)
        self.Jim_progress2.setValue(0)
        self.Jim_progress2.setFormat("Загруженность")
        self.Jim_progress2.setAlignment(Qt.Qt.AlignCenter)
        self.Jim_progress2.setFont(QtGui.QFont("18"))
        self.Jim_progress2.setFixedWidth(150)

        self.Jim_bag_label = QtWidgets.QLabel(Item_distribution)
        self.Jim_bag_label.setGeometry(QtCore.QRect(430, 550, 150, 200))
        self.Jim_bag_label.setStyleSheet("background-color: grey;")
        self.Jim_bag_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Jim_bag_label.setWordWrap(True)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.Jim_bag_label.setFont(font)
        # self.Jim_bag_label.setText("Test")
        self.Jim_bag_label.setObjectName("Jim_bag_label")

        self.Marco_label_3 = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Persons/Marco - Volkodav face small.png")
        self.Marco_label_3.setPixmap(pixmap1)
        self.Marco_label_3.setGeometry(730, 700, 300, 300)

        self.Marco_progress3 = QtWidgets.QProgressBar(Item_distribution)
        self.Marco_progress3.setGeometry(730, 950, 220, 20)
        self.Marco_progress3.setValue(0)
        self.Marco_progress3.setFormat("Загруженность")
        self.Marco_progress3.setAlignment(Qt.Qt.AlignCenter)
        self.Marco_progress3.setFont(QtGui.QFont("18"))
        self.Marco_progress3.setFixedWidth(150)

        self.Marco_bag_label = QtWidgets.QLabel(Item_distribution)
        self.Marco_bag_label.setGeometry(QtCore.QRect(730, 550, 150, 200))
        self.Marco_bag_label.setStyleSheet("background-color: grey;")
        self.Marco_bag_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Marco_bag_label.setWordWrap(True)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.Marco_bag_label.setFont(font)
        # self.Marco_bag_label.setText("Test")
        self.Marco_bag_label.setObjectName("Marco_bag_label")

        self.Carry_label_4 = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Persons/Carry King face small.png")
        self.Carry_label_4.setPixmap(pixmap1)
        self.Carry_label_4.setGeometry(1030, 700, 300, 300)

        self.Carry_progress4 = QtWidgets.QProgressBar(Item_distribution)
        self.Carry_progress4.setGeometry(1030, 950, 220, 20)
        self.Carry_progress4.setValue(0)
        self.Carry_progress4.setFormat("Загруженность")
        self.Carry_progress4.setAlignment(Qt.Qt.AlignCenter)
        self.Carry_progress4.setFont(QtGui.QFont("18"))
        self.Carry_progress4.setFixedWidth(150)

        self.Carry_bag_label = QtWidgets.QLabel(Item_distribution)
        self.Carry_bag_label.setGeometry(QtCore.QRect(1030, 550, 150, 200))
        self.Carry_bag_label.setStyleSheet("background-color: grey;")
        self.Carry_bag_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Carry_bag_label.setWordWrap(True)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.Carry_bag_label.setFont(font)
        # self.Carry_bag_label.setText("Test")
        self.Carry_bag_label.setObjectName("Carry_bag_label")

        self.Angela_label_5 = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Persons/Angela face small.png")
        self.Angela_label_5.setPixmap(pixmap1)
        self.Angela_label_5.setGeometry(1330, 700, 300, 300)

        self.Angela_progress5 = QtWidgets.QProgressBar(Item_distribution)
        self.Angela_progress5.setGeometry(1330, 950, 220, 20)
        self.Angela_progress5.setValue(0)
        self.Angela_progress5.setFormat("Загруженность")
        self.Angela_progress5.setAlignment(Qt.Qt.AlignCenter)
        self.Angela_progress5.setFont(QtGui.QFont("18"))
        self.Angela_progress5.setFixedWidth(150)

        self.Angela_bag_label = QtWidgets.QLabel(Item_distribution)
        self.Angela_bag_label.setGeometry(QtCore.QRect(1330, 550, 150, 200))
        self.Angela_bag_label.setStyleSheet("background-color: grey;")
        self.Angela_bag_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Angela_bag_label.setWordWrap(True)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.Angela_bag_label.setFont(font)
        # self.Angela_bag_label.setText("Test")
        self.Angela_bag_label.setObjectName("Angela_bag_label")

        self.Nick_label_6 = QtWidgets.QLabel(Item_distribution)
        pixmap1 = QPixmap("Persons/Nick Gramzik Graims face small.png")
        self.Nick_label_6.setPixmap(pixmap1)
        self.Nick_label_6.setGeometry(1630, 700, 300, 300)

        self.Nick_progress6 = QtWidgets.QProgressBar(Item_distribution)
        self.Nick_progress6.setGeometry(1630, 950, 220, 20)
        self.Nick_progress6.setValue(0)
        self.Nick_progress6.setFormat("Загруженность")
        self.Nick_progress6.setAlignment(Qt.Qt.AlignCenter)
        self.Nick_progress6.setFont(QtGui.QFont("18"))
        self.Nick_progress6.setFixedWidth(150)

        self.Nick_bag_label = QtWidgets.QLabel(Item_distribution)
        self.Nick_bag_label.setGeometry(QtCore.QRect(1630, 550, 150, 200))
        self.Nick_bag_label.setStyleSheet("background-color: grey;")
        self.Nick_bag_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Nick_bag_label.setWordWrap(True)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.Nick_bag_label.setFont(font)
        # self.Nick_bag_label.setText("Test")
        self.Nick_bag_label.setObjectName("Nick_bag_label")


# ДИАЛОГОВОЕ ОКНО ПЕРВОЙ МИССИИ


class Mission_1(object):
    # def __init__(self):
    #     self.pushButton = QtWidgets.QPushButton(Dialog)

    def setupUi(self, Dialog_mission_1):
        Dialog_mission_1.setObjectName("Dialog_mission_1")
        Dialog_mission_1.resize(1800, 800)

        hbox = QHBoxLayout()
        pixmap = QPixmap("Fon 2.jpg")
        lbl = QLabel()
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        Dialog_mission_1.setLayout(hbox)

        Dialog_mission_1.setWindowTitle('Red Rock')

        self.pushButton_1_advaturer = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_1_advaturer.setGeometry(QtCore.QRect(675, 721, 141, 141))
        self.pushButton_1_advaturer.setMouseTracking(False)
        self.pushButton_1_advaturer.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_1_advaturer.setIcon(QtGui.QIcon("Persons/Angela face.png"))  # Перс 1
        self.pushButton_1_advaturer.setStyleSheet("background-color: PowderBlue;")
        self.pushButton_1_advaturer.setText("")
        self.pushButton_1_advaturer.hide()
        self.pushButton_1_advaturer.setObjectName("pushButton")

        self.pushButton_2_advaturer = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_2_advaturer.setGeometry(QtCore.QRect(900, 721, 141, 141))
        self.pushButton_2_advaturer.setMouseTracking(False)
        self.pushButton_2_advaturer.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_2_advaturer.setIcon(QtGui.QIcon("Ship.jpg"))  # Перс 2
        self.pushButton_2_advaturer.setStyleSheet("background-color: PowderBlue;")
        self.pushButton_2_advaturer.setText("")
        self.pushButton_2_advaturer.hide()
        self.pushButton_2_advaturer.setObjectName("pushButton")

        self.pushButton_3_advaturer = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_3_advaturer.setGeometry(QtCore.QRect(1125, 721, 141, 141))
        self.pushButton_3_advaturer.setMouseTracking(False)
        self.pushButton_3_advaturer.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_3_advaturer.setIcon(QtGui.QIcon("Ship.jpg"))  # Перс 3
        self.pushButton_3_advaturer.setStyleSheet("background-color: PowderBlue;")
        self.pushButton_3_advaturer.setText("")
        self.pushButton_3_advaturer.hide()
        self.pushButton_3_advaturer.setObjectName("pushButton")

        self.pushButton_4_advaturer = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_4_advaturer.setGeometry(QtCore.QRect(1350, 721, 141, 141))
        self.pushButton_4_advaturer.setMouseTracking(False)
        self.pushButton_4_advaturer.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_4_advaturer.setIcon(QtGui.QIcon("Ship.jpg"))  # Перс 4
        self.pushButton_4_advaturer.setStyleSheet("background-color: PowderBlue;")
        self.pushButton_4_advaturer.setText("")
        self.pushButton_4_advaturer.hide()
        self.pushButton_4_advaturer.setObjectName("pushButton")

        self.pushButton_5_advaturer = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_5_advaturer.setGeometry(QtCore.QRect(1575, 721, 141, 141))
        self.pushButton_5_advaturer.setMouseTracking(False)
        self.pushButton_5_advaturer.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_5_advaturer.setIcon(QtGui.QIcon("Ship.jpg"))  # Перс 5
        self.pushButton_5_advaturer.setStyleSheet("background-color: PowderBlue;")
        self.pushButton_5_advaturer.setText("")
        self.pushButton_5_advaturer.hide()
        self.pushButton_5_advaturer.setObjectName("pushButton")

        self.pushButton_ship = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_ship.setGeometry(QtCore.QRect(350, 721, 141, 141))
        self.pushButton_ship.setMouseTracking(False)
        self.pushButton_ship.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_ship.setIcon(QtGui.QIcon("Ship.jpg"))  # Корабль
        self.pushButton_ship.setStyleSheet("background-color: PowderBlue;")
        self.pushButton_ship.setText("")
        self.pushButton_ship.setEnabled(False)
        self.pushButton_ship.setObjectName("pushButton")

        self.pushButton = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton.setGeometry(QtCore.QRect(350, 580, 141, 141))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setIconSize(QtCore.QSize(120, 120))
        self.pushButton.setIcon(QtGui.QIcon("1 б.png"))  # Равнина
        self.pushButton.setStyleSheet("background-color: teal;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 510, 141, 141))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_2.setIcon(QtGui.QIcon("2 б.png"))  # Равнина
        self.pushButton_2.setStyleSheet("background-color: teal;")
        self.pushButton_2.setText("")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 510, 141, 141))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_3.setIcon(QtGui.QIcon("3 б.png"))  # Равнина
        self.pushButton_3.setStyleSheet("background-color: teal;")
        self.pushButton_3.setText("")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 440, 141, 141))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_4.setIcon(QtGui.QIcon("4 б.png"))  # Пустыня
        self.pushButton_4.setStyleSheet("background-color: yellow;")
        self.pushButton_4.setText("")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 370, 141, 141))
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_5.setIcon(QtGui.QIcon("5 б.png"))  # Джунгли
        self.pushButton_5.setStyleSheet("background-color: green;")
        self.pushButton_5.setText("")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 370, 141, 141))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_6.setIcon(QtGui.QIcon("6 б.png"))  # Джунгли
        self.pushButton_6.setStyleSheet("background-color: green;")
        self.pushButton_6.setText("")
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 300, 141, 141))
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_7.setIcon(QtGui.QIcon("7 б"))  # Джунгли
        self.pushButton_7.setStyleSheet("background-color: green;")
        self.pushButton_7.setText("")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 300, 141, 141))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_8.setIcon(QtGui.QIcon("8 б.png"))  # Равнина
        self.pushButton_8.setStyleSheet("background-color: teal;")
        self.pushButton_8.setText("")
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_9.setGeometry(QtCore.QRect(630, 300, 141, 141))
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_9.setIcon(QtGui.QIcon("9 б.png"))  # Джунгли
        self.pushButton_9.setStyleSheet("background-color: green;")
        self.pushButton_9.setText("")
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 230, 141, 141))
        self.pushButton_10.setMouseTracking(False)
        self.pushButton_10.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_10.setIcon(QtGui.QIcon("10 б.png"))  # Пустыня
        self.pushButton_10.setStyleSheet("background-color: yellow;")
        self.pushButton_10.setText("")
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_11.setGeometry(QtCore.QRect(490, 230, 141, 141))
        self.pushButton_11.setMouseTracking(False)
        self.pushButton_11.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_11.setIcon(QtGui.QIcon("11 б.png"))  # Пустыня
        self.pushButton_11.setStyleSheet("background-color: yellow;")
        self.pushButton_11.setText("")
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_12.setGeometry(QtCore.QRect(70, 160, 141, 141))
        self.pushButton_12.setMouseTracking(False)
        self.pushButton_12.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_12.setIcon(QtGui.QIcon("12 б.png"))  # Гора
        self.pushButton_12.setStyleSheet("background-color: coral;")
        self.pushButton_12.setText("")
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_13.setGeometry(QtCore.QRect(350, 160, 141, 141))
        self.pushButton_13.setMouseTracking(False)
        self.pushButton_13.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_13.setIcon(QtGui.QIcon("13 б.png"))  # Джунгли
        self.pushButton_13.setStyleSheet("background-color: green;")
        self.pushButton_13.setText("")
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setObjectName("pushButton_13")

        self.pushButton_14 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_14.setGeometry(QtCore.QRect(630, 160, 141, 141))
        self.pushButton_14.setMouseTracking(False)
        self.pushButton_14.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_14.setIcon(QtGui.QIcon("14 б.png"))  # Гора
        self.pushButton_14.setStyleSheet("background-color: coral;")
        self.pushButton_14.setText("")
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_15.setGeometry(QtCore.QRect(350, 20, 141, 141))
        self.pushButton_15.setMouseTracking(False)
        self.pushButton_15.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_15.setIcon(QtGui.QIcon("15 б.png"))  # Гора
        self.pushButton_15.setStyleSheet("background-color: coral;")
        self.pushButton_15.setText("")
        self.pushButton_15.setEnabled(False)
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_16 = QtWidgets.QPushButton(Dialog_mission_1)  # Ночь
        self.pushButton_16.setGeometry(QtCore.QRect(875, 10, 120, 120))
        self.pushButton_16.setMouseTracking(False)
        self.pushButton_16.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_16.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_16.setIcon(QtGui.QIcon("img_with_watermark.png"))
        #        self.pushButton_16.setIcon(QtGui.QIcon("bat.png"))
        self.pushButton_16.setStyleSheet("color: white;")
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_17 = QtWidgets.QPushButton(Dialog_mission_1)  # Исследование
        self.pushButton_17.setGeometry(QtCore.QRect(675, 480, 120, 120))
        self.pushButton_17.setMouseTracking(False)
        self.pushButton_17.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_17.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_17.setIcon(QtGui.QIcon("binoculars.jpg"))
        self.pushButton_17.setStyleSheet("color: white;")
        self.pushButton_17.setObjectName("pushButton_16")

        self.pushButton_18 = QtWidgets.QPushButton(Dialog_mission_1)
        self.pushButton_18.setGeometry(QtCore.QRect(900, 490, 141, 141))
        self.pushButton_18.setMouseTracking(False)
        self.pushButton_18.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_18.setStyleSheet("background-color: teal;")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setText("Меню")
        self.pushButton_18.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(Dialog_mission_1)
        self.label.setGeometry(QtCore.QRect(1110, 40, 611, 401))
        self.label.setStyleSheet("background-color: cornflowerblue;")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setText("Test")
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(Dialog_mission_1)
        self.textEdit.setGeometry(QtCore.QRect(1110, 490, 611, 201))
        self.textEdit.setStyleSheet("background-color: lightseagreen;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog_mission_1)  # Эта часть кода сгенерированна программой, вроде можно убрать, но страшно
        QtCore.QMetaObject.connectSlotsByName(Dialog_mission_1)

    def retranslateUi(self, Dialog_mission_1):  # И это тоже
        _translate = QtCore.QCoreApplication.translate
        Dialog_mission_1.setWindowTitle(_translate("Dialog_mission_1", "Dialog_mission_1"))


app = QtWidgets.QApplication(sys.argv)
Dialog_mission_1 = QtWidgets.QDialog()  # Диалог миссии 1
Dialog_menu = QtWidgets.QDialog()  # Диалог меню
Dialog_history = QtWidgets.QDialog()  # Диалог истории
Dialog_Character_selection = QtWidgets.QDialog()  # Диалог выбора персоонажей
Dialog_history_2 = QtWidgets.QDialog()  # Диалог чтения истории 2
Dialog_history_3 = QtWidgets.QDialog()  # Диалог чтения истории 3
Dialog_Item_distribution = QtWidgets.QDialog()  # Диалог выбора шмоток

menu = Menu()  # подключение меню
menu.setupUi(Dialog_menu)

history = History()  # подключение истории
history.setupUi(Dialog_history)

history_2 = History_2()  # подключение истории 2
history_2.setupUi(Dialog_history_2)

history_3 = History_3()  # подключение истории 3
history_3.setupUi(Dialog_history_3)

ui = Mission_1()  # Подключение мисии 1
ui.setupUi(Dialog_mission_1)

char_s = Character_selection()  # Подключение Выбора персоонажей
char_s.setupUi(Dialog_Character_selection)

Idi = Item_distribution()  # Подключение раскидывания шмоток
Idi.setupUi(Dialog_Item_distribution)

Dialog_Character_selection.show()  # Запуск вего этого дерьма


def start_history():
    Dialog_menu.close()
    Dialog_history.show()


def to_history2():
    Dialog_history.close()
    Dialog_history_2.open()


def to_history3():
    Dialog_Item_distribution.close()
    Dialog_history_3.open()


def return_to_menu():
    Dialog_mission_1.close()
    Dialog_menu.show()


def to_create_team():
    Dialog_history_2.close()
    Dialog_Character_selection.open()

def add_persons_to_list():
    for key in Persons.persons_in_team:
        if Persons.persons_in_team[key] == True:
            Persons.persons_in_team_list.append(key)
    print(Persons.persons_in_team_list)

def set_amount_of_advantures():
    print(len(Persons.persons_in_team_list))
    if len(Persons.persons_in_team_list) == 3:
        Persons.amount_of_adventurers = 3
        ui.pushButton_1_advaturer.show()
        ui.pushButton_2_advaturer.show()
        ui.pushButton_3_advaturer.show()
    if len(Persons.persons_in_team_list) == 4:
        Persons.amount_of_adventurers = 4
        ui.pushButton_1_advaturer.show()
        ui.pushButton_2_advaturer.show()
        ui.pushButton_3_advaturer.show()
        ui.pushButton_4_advaturer.show()
    if len(Persons.persons_in_team_list) == 5:
        Persons.amount_of_adventurers = 5
        ui.pushButton_1_advaturer.show()
        ui.pushButton_2_advaturer.show()
        ui.pushButton_3_advaturer.show()
        ui.pushButton_4_advaturer.show()
        ui.pushButton_5_advaturer.show()

def set_three_coosen_adventurers():
    if Persons.persons_in_team_list[0] == "Нико Робин":
        ui.pushButton_1_advaturer.setIcon(QtGui.QIcon("Persons/Nico Robin face.png"))
    if Persons.persons_in_team_list[0] == "Джим Киперс":
        ui.pushButton_1_advaturer.setIcon(QtGui.QIcon("Persons/Jim Kipers face.png"))
    if Persons.persons_in_team_list[0] == "Марко Волкодав":
        ui.pushButton_1_advaturer.setIcon(QtGui.QIcon("Persons/Marco - Volkodav face.png"))
    if Persons.persons_in_team_list[0] == "Кэри Кинг":
        ui.pushButton_1_advaturer.setIcon(QtGui.QIcon("Persons/Carry King face.png"))
    if Persons.persons_in_team_list[0] == "Ангела":
        ui.pushButton_1_advaturer.setIcon(QtGui.QIcon("Persons/Angela face.png"))
    if Persons.persons_in_team_list[0] == "Ник Джеймс":
        ui.pushButton_1_advaturer.setIcon(QtGui.QIcon("Persons/Nick Gramzik Graims face.png"))

    if Persons.persons_in_team_list[1] == "Нико Робин":
        ui.pushButton_2_advaturer.setIcon(QtGui.QIcon("Persons/Nico Robin face.png"))
    if Persons.persons_in_team_list[1] == "Джим Киперс":
        ui.pushButton_2_advaturer.setIcon(QtGui.QIcon("Persons/Jim Kipers face.png"))
    if Persons.persons_in_team_list[1] == "Марко Волкодав":
        ui.pushButton_2_advaturer.setIcon(QtGui.QIcon("Persons/Marco - Volkodav face.png"))
    if Persons.persons_in_team_list[1] == "Кэри Кинг":
        ui.pushButton_2_advaturer.setIcon(QtGui.QIcon("Persons/Carry King face.png"))
    if Persons.persons_in_team_list[1] == "Ангела":
        ui.pushButton_2_advaturer.setIcon(QtGui.QIcon("Persons/Angela face.png"))
    if Persons.persons_in_team_list[1] == "Ник Джеймс":
        ui.pushButton_2_advaturer.setIcon(QtGui.QIcon("Persons/Nick Gramzik Graims face.png"))

    if Persons.persons_in_team_list[2] == "Нико Робин":
        ui.pushButton_3_advaturer.setIcon(QtGui.QIcon("Persons/Nico Robin face.png"))
    if Persons.persons_in_team_list[2] == "Джим Киперс":
        ui.pushButton_3_advaturer.setIcon(QtGui.QIcon("Persons/Jim Kipers face.png"))
    if Persons.persons_in_team_list[2] == "Марко Волкодав":
        ui.pushButton_3_advaturer.setIcon(QtGui.QIcon("Persons/Marco - Volkodav face.png"))
    if Persons.persons_in_team_list[2] == "Кэри Кинг":
        ui.pushButton_3_advaturer.setIcon(QtGui.QIcon("Persons/Carry King face.png"))
    if Persons.persons_in_team_list[2] == "Ангела":
        ui.pushButton_3_advaturer.setIcon(QtGui.QIcon("Persons/Angela face.png"))
    if Persons.persons_in_team_list[2] == "Ник Джеймс":
        ui.pushButton_3_advaturer.setIcon(QtGui.QIcon("Persons/Nick Gramzik Graims face.png"))

def set_4th_coosen_adventurers():
    if Persons.persons_in_team_list[3] == "Нико Робин":
        ui.pushButton_4_advaturer.setIcon(QtGui.QIcon("Persons/Nico Robin face.png"))
    if Persons.persons_in_team_list[3] == "Джим Киперс":
        ui.pushButton_4_advaturer.setIcon(QtGui.QIcon("Persons/Jim Kipers face.png"))
    if Persons.persons_in_team_list[3] == "Марко Волкодав":
        ui.pushButton_4_advaturer.setIcon(QtGui.QIcon("Persons/Marco - Volkodav face.png"))
    if Persons.persons_in_team_list[3] == "Кэри Кинг":
        ui.pushButton_4_advaturer.setIcon(QtGui.QIcon("Persons/Carry King face.png"))
    if Persons.persons_in_team_list[3] == "Ангела":
        ui.pushButton_4_advaturer.setIcon(QtGui.QIcon("Persons/Angela face.png"))
    if Persons.persons_in_team_list[3] == "Ник Джеймс":
        ui.pushButton_4_advaturer.setIcon(QtGui.QIcon("Persons/Nick Gramzik Graims face.png"))

def set_5th_coosen_adventurers():
    if Persons.persons_in_team_list[4] == "Нико Робин":
        ui.pushButton_5_advaturer.setIcon(QtGui.QIcon("Persons/Nico Robin face.png"))
    if Persons.persons_in_team_list[4] == "Джим Киперс":
        ui.pushButton_5_advaturer.setIcon(QtGui.QIcon("Persons/Jim Kipers face.png"))
    if Persons.persons_in_team_list[4] == "Марко Волкодав":
        ui.pushButton_5_advaturer.setIcon(QtGui.QIcon("Persons/Marco - Volkodav face.png"))
    if Persons.persons_in_team_list[4] == "Кэри Кинг":
        ui.pushButton_5_advaturer.setIcon(QtGui.QIcon("Persons/Carry King face.png"))
    if Persons.persons_in_team_list[4] == "Ангела":
        ui.pushButton_5_advaturer.setIcon(QtGui.QIcon("Persons/Angela face.png"))
    if Persons.persons_in_team_list[4] == "Ник Джеймс":
        ui.pushButton_5_advaturer.setIcon(QtGui.QIcon("Persons/Nick Gramzik Graims face.png"))

def set_faces_of_adventurers():
    if Persons.amount_of_adventurers == 3:
        set_three_coosen_adventurers()
    if Persons.amount_of_adventurers == 4:
        set_three_coosen_adventurers()
        set_4th_coosen_adventurers()
    if Persons.amount_of_adventurers == 5:
        set_three_coosen_adventurers()
        set_4th_coosen_adventurers()
        set_5th_coosen_adventurers()



def to_mission1():
    Dialog_history_3.close()
    add_persons_to_list()
    set_amount_of_advantures()
    set_faces_of_adventurers()
    Dialog_mission_1.open()



class Persons:
    persons_in_team = {"Нико Робин": True,
                                   "Джим Киперс": True,
                                   "Марко Волкодав": True,
                                   "Кэри Кинг": True,
                                   "Ангела": True,
                                   "Ник Джеймс": True}

    persons_in_team_list = []

    amount_of_adventurers = 0

    @staticmethod
    def to_save_persons_in_team():
        Persons.persons_in_team = {"Нико Робин": char_s.QCheckBox.isChecked(),
                                   "Джим Киперс": char_s.QCheckBox_2.isChecked(),
                                   "Марко Волкодав": char_s.QCheckBox_3.isChecked(),
                                   "Кэри Кинг": char_s.QCheckBox_4.isChecked(),
                                   "Ангела": char_s.QCheckBox_5.isChecked(),
                                   "Ник Джеймс": char_s.QCheckBox_6.isChecked()}

    @staticmethod
    def to_count_persons_in_team():
        persons = int(sum(Persons.persons_in_team.values()))
        return persons

    @staticmethod
    def to_turn_off_not_taken_adventurers():
        for person in Persons.persons_in_team:
            if Persons.persons_in_team[person] == False:
                if person == "Нико Робин":
                    Idi.Nico_label.hide()
                    Idi.Nico_progress1.hide()
                    Idi.Nico_bag_label.hide()
                if person == "Джим Киперс":
                    Idi.Jim_label_2.hide()
                    Idi.Jim_progress2.hide()
                    Idi.Jim_bag_label.hide()
                if person == "Марко Волкодав":
                    Idi.Marco_label_3.hide()
                    Idi.Marco_progress3.hide()
                    Idi.Marco_bag_label.hide()
                if person == "Кэри Кинг":
                    Idi.Carry_label_4.hide()
                    Idi.Carry_progress4.hide()
                    Idi.Carry_bag_label.hide()
                if person == "Ангела":
                    Idi.Angela_label_5.hide()
                    Idi.Angela_progress5.hide()
                    Idi.Angela_bag_label.hide()
                if person == "Ник Джеймс":
                    Idi.Nick_label_6.hide()
                    Idi.Nick_progress6.hide()
                    Idi.Nick_bag_label.hide()


    @staticmethod
    def turn_on_comboboxes():
        taken_persons = {"Выберите": True}
        for i in Persons.persons_in_team:
            if Persons.persons_in_team[i] == 1:
                taken_persons[i] = Persons.persons_in_team[i]

        Idi.stick_combobox.addItems(taken_persons)
        Idi.stick2_combobox.addItems(taken_persons)
        Idi.bag_combobox.addItems(taken_persons)
        Idi.compass_combobox.addItems(taken_persons)
        Idi.rope_combobox.addItems(taken_persons)
        Idi.wineskin_combobox.addItems(taken_persons)
        Idi.wineskin2_combobox.addItems(taken_persons)
        Idi.flask_combobox.addItems(taken_persons)
        Idi.flask2_combobox.addItems(taken_persons)
        Idi.flask3_combobox.addItems(taken_persons)
        Idi.blanket_combobox.addItems(taken_persons)
        Idi.blanket2_combobox.addItems(taken_persons)
        Idi.tent_for_3_combobox.addItems(taken_persons)
        Idi.machete_combobox.addItems(taken_persons)
        Idi.climbing_equipment_combobox.addItems(taken_persons)
        Idi.knife_combobox.addItems(taken_persons)
        Idi.medik_kid_combobox.addItems(taken_persons)
        Idi.fracture_medik_kid_combobox.addItems(taken_persons)
        Idi.antidote_combobox.addItems(taken_persons)
        Idi.trap_combobox.addItems(taken_persons)
        Idi.trevelling_set_combobox.addItems(taken_persons)
        Idi.flare_combobox.addItems(taken_persons)




    @staticmethod
    def to_check_correct_number_of_persons_and_if_correct_go_further():
        if Persons.to_count_persons_in_team() < 6 and Persons.to_count_persons_in_team() > 2:
            Dialog_Character_selection.close()
            Dialog_Item_distribution.show()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText("Выберите от 3 до 5 персонажей")
            msgBox.setWindowTitle("QMessageBox Example")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

            returnValue = msgBox.exec()  # Если не сохранить в переменную то всё сломается



def take_items():       # Переход на распределение предметов
    Persons.to_save_persons_in_team()
    Persons.turn_on_comboboxes()
    Persons.to_turn_off_not_taken_adventurers()
    Persons.to_check_correct_number_of_persons_and_if_correct_go_further()


def distribute_items():
    if (int(((sum(Item_distribution.Nico_Robin_bag.values())) * 100) / 7) > 100 or
            int(((sum(Item_distribution.Jim_Kippers_bag.values()))*100)/8) > 100 or
            int(((sum(Item_distribution.Marco_Wolfhound_bag.values()))*100)/8) > 100 or
            int(((sum(Item_distribution.Carry_King_bag.values())) * 100) / 9) > 100 or
            int(((sum(Item_distribution.Angela_bag.values())) * 100) / 6) > 100 or
            int(((sum(Item_distribution.Nick_James_bag.values())) * 100) / 8) > 100):

                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setText("Устраните перегрузку")
                msgBox.setWindowTitle("Предупреждение")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                returnValue = msgBox.exec()  # Если не сохранить в переменную то всё сломается
    else:
        Dialog_Item_distribution.close()
        Dialog_history_3.show()  # Пока так потом переделаю


menu.pushButton.clicked.connect(start_history)
history.pushButton.clicked.connect(to_history2)
history_2.pushButton.clicked.connect(to_create_team)  # Пока так
history_3.pushButton.clicked.connect(to_mission1)
char_s.pushButton.clicked.connect(take_items)
Idi.pushButton.clicked.connect(distribute_items)


def night():
    if position == "В равнинах":
        plane_night()
    elif position == "В пустынях":
        desert_night()
    elif position == "В джунглях":
        jungle_night()
    elif position == "В горах":
        mount_night()


position = "На Корабле"


def plane():
    global position
    position = "В равнинах"
    ui.label.setText(random_plane_event())


def plane_night():
    global position
    position = "В равнинах"
    ui.label.setText(random_night_plane_event())


def desert():
    global position
    position = "В пустынях"
    ui.label.setText(random_desert_event())


def desert_night():
    global position
    position = "В пустынях"
    ui.label.setText(random_night_desert_event())


def jungle():
    global position
    position = "В джунглях"
    ui.label.setText(random_jungle_event())


def jungle_night():
    global position
    position = "В джунглях"
    ui.label.setText(random_night_jungle_event())


def mount15():
    global position
    position = "В горах"
    ui.pushButton_15.setIcon(QtGui.QIcon("15 а.png"))
    if Random_aim == 1:
        ui.label.setText("Вы у цели")
    else:
        ui.label.setText(random_mount_event())

    disable_all_terrytory_buttons()
    ui.pushButton_13.setEnabled(True)


def mount14():
    global position
    position = "В горах"
    ui.pushButton_14.setIcon(QtGui.QIcon("14 а.png"))
    if Random_aim == 2:
        ui.label.setText("Вы у цели")
    else:
        ui.label.setText(random_mount_event())

    disable_all_terrytory_buttons()
    ui.pushButton_9.setEnabled(True)
    ui.pushButton_11.setEnabled(True)


def mount12():
    global position
    position = "В горах"
    ui.pushButton_12.setIcon(QtGui.QIcon("12 а.png"))
    if Random_aim == 3:
        ui.label.setText("Вы у цели")
    else:
        ui.label.setText(random_mount_event())

    disable_all_terrytory_buttons()
    ui.pushButton_7.setEnabled(True)
    ui.pushButton_10.setEnabled(True)


def mount_night():
    global position
    position = "В горах"
    ui.label.setText(random_night_mount_event())


# print(position)


def jungle13():
    ui.pushButton_13.setIcon(QtGui.QIcon("13 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_8.setEnabled(True)
    ui.pushButton_10.setEnabled(True)
    ui.pushButton_11.setEnabled(True)
    ui.pushButton_15.setEnabled(True)
    ui.pushButton_8.setEnabled(True)


def jungle7():
    ui.pushButton_7.setIcon(QtGui.QIcon("7 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_5.setEnabled(True)
    ui.pushButton_10.setEnabled(True)
    ui.pushButton_12.setEnabled(True)


def jungle9():
    ui.pushButton_9.setIcon(QtGui.QIcon("9 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_6.setEnabled(True)
    ui.pushButton_11.setEnabled(True)
    ui.pushButton_14.setEnabled(True)


def jungle5():
    ui.pushButton_5.setIcon(QtGui.QIcon("5 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_2.setEnabled(True)
    ui.pushButton_4.setEnabled(True)
    ui.pushButton_7.setEnabled(True)
    ui.pushButton_8.setEnabled(True)
    ui.pushButton_10.setEnabled(True)


def jungle6():
    ui.pushButton_6.setIcon(QtGui.QIcon("6 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_3.setEnabled(True)
    ui.pushButton_4.setEnabled(True)
    ui.pushButton_8.setEnabled(True)
    ui.pushButton_9.setEnabled(True)
    ui.pushButton_11.setEnabled(True)


def desert10():
    ui.pushButton_10.setIcon(QtGui.QIcon("10 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_5.setEnabled(True)
    ui.pushButton_7.setEnabled(True)
    ui.pushButton_8.setEnabled(True)
    ui.pushButton_12.setEnabled(True)
    ui.pushButton_13.setEnabled(True)


def desert11():
    ui.pushButton_11.setIcon(QtGui.QIcon("11 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_6.setEnabled(True)
    ui.pushButton_8.setEnabled(True)
    ui.pushButton_9.setEnabled(True)
    ui.pushButton_13.setEnabled(True)
    ui.pushButton_14.setEnabled(True)


def desert4():
    ui.pushButton_4.setIcon(QtGui.QIcon("4 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton.setEnabled(True)
    ui.pushButton_2.setEnabled(True)
    ui.pushButton_3.setEnabled(True)
    ui.pushButton_5.setEnabled(True)
    ui.pushButton_6.setEnabled(True)
    ui.pushButton_8.setEnabled(True)


def plane8():
    ui.pushButton_8.setIcon(QtGui.QIcon("8 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_4.setEnabled(True)
    ui.pushButton_5.setEnabled(True)
    ui.pushButton_6.setEnabled(True)
    ui.pushButton_10.setEnabled(True)
    ui.pushButton_11.setEnabled(True)
    ui.pushButton_13.setEnabled(True)


def plane2():
    ui.pushButton_2.setIcon(QtGui.QIcon("2 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton.setEnabled(True)
    ui.pushButton_4.setEnabled(True)
    ui.pushButton_5.setEnabled(True)


def plane3():
    ui.pushButton_3.setIcon(QtGui.QIcon("3 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton.setEnabled(True)
    ui.pushButton_4.setEnabled(True)
    ui.pushButton_6.setEnabled(True)

def plane1():
    ui.pushButton.setIcon(QtGui.QIcon("1 а.png"))
    disable_all_terrytory_buttons()
    ui.pushButton_ship.hide()
    ui.pushButton_2.setEnabled(True)
    ui.pushButton_3.setEnabled(True)
    ui.pushButton_4.setEnabled(True)

def research():  # ИССЛЕДОВАНИЕ
    pass

def disable_all_terrytory_buttons():
    ui.pushButton.setEnabled(False)
    ui.pushButton_2.setEnabled(False)
    ui.pushButton_3.setEnabled(False)
    ui.pushButton_4.setEnabled(False)
    ui.pushButton_5.setEnabled(False)
    ui.pushButton_6.setEnabled(False)
    ui.pushButton_7.setEnabled(False)
    ui.pushButton_8.setEnabled(False)
    ui.pushButton_9.setEnabled(False)
    ui.pushButton_10.setEnabled(False)
    ui.pushButton_11.setEnabled(False)
    ui.pushButton_12.setEnabled(False)
    ui.pushButton_13.setEnabled(False)
    ui.pushButton_14.setEnabled(False)
    ui.pushButton_15.setEnabled(False)


ui.pushButton.clicked.connect(plane)
ui.pushButton.clicked.connect(plane1)
ui.pushButton_2.clicked.connect(plane)
ui.pushButton_2.clicked.connect(plane2)
ui.pushButton_3.clicked.connect(plane)
ui.pushButton_3.clicked.connect(plane3)
ui.pushButton_4.clicked.connect(desert)
ui.pushButton_4.clicked.connect(desert4)
ui.pushButton_5.clicked.connect(jungle)
ui.pushButton_5.clicked.connect(jungle5)
ui.pushButton_6.clicked.connect(jungle)
ui.pushButton_6.clicked.connect(jungle6)
ui.pushButton_7.clicked.connect(plane)
ui.pushButton_7.clicked.connect(jungle7)
ui.pushButton_8.clicked.connect(plane)
ui.pushButton_8.clicked.connect(plane8)
ui.pushButton_9.clicked.connect(jungle)
ui.pushButton_9.clicked.connect(jungle9)
ui.pushButton_10.clicked.connect(desert)
ui.pushButton_10.clicked.connect(desert10)
ui.pushButton_11.clicked.connect(desert)
ui.pushButton_11.clicked.connect(desert11)
ui.pushButton_12.clicked.connect(mount12)
ui.pushButton_13.clicked.connect(plane)
ui.pushButton_13.clicked.connect(jungle13)
ui.pushButton_14.clicked.connect(mount14)
ui.pushButton_15.clicked.connect(mount15)
ui.pushButton_16.clicked.connect(night)
ui.pushButton_17.clicked.connect(research)
ui.pushButton_18.clicked.connect(return_to_menu)

sys.exit(app.exec_())