import random
#from playsound import playsound
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import QtMultimedia
QtMultimedia.QSound.play('metallica-the-unforgiven.mp3')
# СОБЫТИЯ

Random_aim = random.randint(1, 3)  # Создание рандомной цели


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
Carry_King = Adventurer("Керри Кинг", "Военный", 4, 2, 1, 3, 2, 3, "Раз в раунд может дублировать на "
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


# ДИАЛОГОВОЕ ОКНО ЗАСТАВКИ

class Screensaver(object):
    def __init__(self):
        self.pushButton = QtWidgets.QPushButton(Dialog2)

    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(1800, 800)

        hbox = QHBoxLayout()
        pixmap = QPixmap("Fon_Screensaver.jpg")
        lbl = QLabel()
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        Dialog2.setLayout(hbox)

        Dialog2.move(100, 200)
        Dialog2.setWindowTitle('Red Rock')

        #playsound('metallica-the-unforgiven.mp3')



# ДИАЛОГОВОЕ ОКНО ПЕРВОЙ МЕНЮ

# ДИАЛОГОВОЕ ОКНО ПЕРВОЙ МИССИИ


class Mission_1(object):
    def __init__(self):
        self.pushButton = QtWidgets.QPushButton(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog2")
        Dialog.resize(1800, 800)

        hbox = QHBoxLayout()
        pixmap = QPixmap("Fon 2.jpg")
        lbl = QLabel()
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        Dialog.setLayout(hbox)

        Dialog.move(100, 200)
        Dialog.setWindowTitle('Red Rock')

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 580, 141, 141))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setIconSize(QtCore.QSize(120, 120))
        self.pushButton.setIcon(QtGui.QIcon("Lock.png"))  # Равнина
        self.pushButton.setStyleSheet("background-color: teal;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 510, 141, 141))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_2.setIcon(QtGui.QIcon("Lock.png"))  # Равнина
        self.pushButton_2.setStyleSheet("background-color: teal;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 510, 141, 141))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_3.setIcon(QtGui.QIcon("Lock.png"))  # Равнина
        self.pushButton_3.setStyleSheet("background-color: teal;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 440, 141, 141))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_4.setIcon(QtGui.QIcon("Lock.png"))  # Пустыня
        self.pushButton_4.setStyleSheet("background-color: yellow;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 370, 141, 141))
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_5.setIcon(QtGui.QIcon("Lock.png"))  # Джунгли
        self.pushButton_5.setStyleSheet("background-color: green;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 370, 141, 141))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_6.setIcon(QtGui.QIcon("Lock.png"))  # Джунгли
        self.pushButton_6.setStyleSheet("background-color: green;")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 300, 141, 141))
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_7.setIcon(QtGui.QIcon("Lock.png"))  # Джунгли
        self.pushButton_7.setStyleSheet("background-color: green;")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 300, 141, 141))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_8.setIcon(QtGui.QIcon("Lock.png"))  # Равнина
        self.pushButton_8.setStyleSheet("background-color: teal;")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(630, 300, 141, 141))
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_9.setIcon(QtGui.QIcon("Lock.png"))  # Джунгли
        self.pushButton_9.setStyleSheet("background-color: green;")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 230, 141, 141))
        self.pushButton_10.setMouseTracking(False)
        self.pushButton_10.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_10.setIcon(QtGui.QIcon("Lock.png"))  # Пустыня
        self.pushButton_10.setStyleSheet("background-color: yellow;")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(490, 230, 141, 141))
        self.pushButton_11.setMouseTracking(False)
        self.pushButton_11.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_11.setIcon(QtGui.QIcon("Lock.png"))  # Пустыня
        self.pushButton_11.setStyleSheet("background-color: yellow;")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(70, 160, 141, 141))
        self.pushButton_12.setMouseTracking(False)
        self.pushButton_12.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_12.setIcon(QtGui.QIcon("Lock.png"))  # Гора
        self.pushButton_12.setStyleSheet("background-color: coral;")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(350, 160, 141, 141))
        self.pushButton_13.setMouseTracking(False)
        self.pushButton_13.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_13.setIcon(QtGui.QIcon("Lock.png"))  # Джунгли
        self.pushButton_13.setStyleSheet("background-color: green;")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")

        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(630, 160, 141, 141))
        self.pushButton_14.setMouseTracking(False)
        self.pushButton_14.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_14.setIcon(QtGui.QIcon("Lock.png"))  # Гора
        self.pushButton_14.setStyleSheet("background-color: coral;")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(350, 20, 141, 141))
        self.pushButton_15.setMouseTracking(False)
        self.pushButton_15.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_15.setIcon(QtGui.QIcon("Lock.png"))  # Гора
        self.pushButton_15.setStyleSheet("background-color: coral;")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_16 = QtWidgets.QPushButton(Dialog)  # Ночь
        self.pushButton_16.setGeometry(QtCore.QRect(875, 10, 120, 120))
        self.pushButton_16.setMouseTracking(False)
        self.pushButton_16.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_16.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_16.setIcon(QtGui.QIcon("Moon2.png"))
        self.pushButton_16.setStyleSheet("color: white;")
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_17 = QtWidgets.QPushButton(Dialog)  # Исследование
        self.pushButton_17.setGeometry(QtCore.QRect(675, 480, 120, 120))
        self.pushButton_17.setMouseTracking(False)
        self.pushButton_17.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_17.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_17.setIcon(QtGui.QIcon("binoculars.jpg"))
        self.pushButton_17.setStyleSheet("color: white;")
        self.pushButton_17.setObjectName("pushButton_16")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(1110, 40, 611, 401))
        self.label.setStyleSheet("background-color: cornflowerblue;")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setText("Test")
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(1110, 490, 611, 201))
        self.textEdit.setStyleSheet("background-color: lightseagreen;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
Dialog2 = QtWidgets.QDialog()

sc = Screensaver()
sc.setupUi(Dialog)

ui = Mission_1()
ui.setupUi(Dialog2)

Dialog.show()


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
    ui.pushButton_15.setIcon(QtGui.QIcon("Mountain 2.jpg"))
    if Random_aim == 1:
        ui.label.setText("Вы у цели")
    else:
        ui.label.setText(random_mount_event())


def mount14():
    global position
    position = "В горах"
    ui.pushButton_14.setIcon(QtGui.QIcon("Mountain 2.jpg"))
    if Random_aim == 2:
        ui.label.setText("Вы у цели")
    else:
        ui.label.setText(random_mount_event())


def mount12():
    global position
    position = "В горах"
    ui.pushButton_12.setIcon(QtGui.QIcon("Mountain 2.jpg"))
    if Random_aim == 3:
        ui.label.setText("Вы у цели")
    else:
        ui.label.setText(random_mount_event())


def mount_night():
    global position
    position = "В горах"
    ui.label.setText(random_night_mount_event())


print(position)




def jungle13():
    ui.pushButton_13.setIcon(QtGui.QIcon("Palm 2.jpg"))


def jungle7():
    ui.pushButton_7.setIcon(QtGui.QIcon("Palm 2.jpg"))


def jungle9():
    ui.pushButton_9.setIcon(QtGui.QIcon("Palm 2.jpg"))


def jungle5():
    ui.pushButton_5.setIcon(QtGui.QIcon("Palm 2.jpg"))


def jungle6():
    ui.pushButton_6.setIcon(QtGui.QIcon("Palm 2.jpg"))


def desert10():
    ui.pushButton_10.setIcon(QtGui.QIcon("Desert 2.jpg"))


def desert11():
    ui.pushButton_11.setIcon(QtGui.QIcon("Desert 2.jpg"))


def desert4():
    ui.pushButton_4.setIcon(QtGui.QIcon("Desert 2.jpg"))


def plane8():
    ui.pushButton_8.setIcon(QtGui.QIcon("Plane 3.jpg"))


def plane2():
    ui.pushButton_2.setIcon(QtGui.QIcon("Plane 3.jpg"))


def plane3():
    ui.pushButton_3.setIcon(QtGui.QIcon("Plane 3.jpg"))


def plane1():
    ui.pushButton.setIcon(QtGui.QIcon("Plane 3.jpg"))


def research():  # ИССЛЕДОВАНИЕ
    pass


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

sys.exit(app.exec_())