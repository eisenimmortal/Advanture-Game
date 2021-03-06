# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import ui
from PyQt5.QtWidgets import QLabel

Random_aim = random.randint(1, 3)  # Создание рандомной цели
if Random_aim == 1:
    pass
if Random_aim == 2:
    pass
if Random_aim == 3:
    pass


def random_mount_event():
    Random_Mount_Event = random.randint(1, 3)
    if Random_Mount_Event == 1:  # События горы при открытии
        print("Пробираясь по сыпучему откосу, вы оступаетесь и катитесь по волне осыпающихся камней. "
              "Пройдите проверку самообладания 2. Прибавьте 1 к сложности за каждые 3 кг груза. "
              "При провале получите 1 легкое ранение и потеряйте в этой локации 1 случайный предмет. ")

    if Random_Mount_Event == 2:
        print("Ваш путь преграждает небольшая скала. "
              "Можно потратить по 1 дополнительному действию,"
              " чтоб обойти ее, либо каждый должен пройти проверку силы 3, чтобы забраться наверх.")

    if Random_Mount_Event == 3:
        print("На вашем пути оказывается глубокая расщелина."
              "Группа может потратить дополнительное движение чтобы обойти ее. "
              "Имея альпинистское снаряжение, любой член экспедиции может пройти проверку Акробатики 3, "
              "чтобы попробовать перепрыгнуть через расщелину и помочь остальным переправиться. "
              "При провале он получает тяжелое ранение.")
    return


def random_night_mount_event():
    Random_Night_Mount_Event = random.randint(1, 3)
    if Random_Night_Mount_Event == 1:  # События горы ночью
        print("Холодный ветер пробирает до костей. "
              "Путешественники без теплого одеяла получают состояние Озноб.")
    if Random_Night_Mount_Event == 2:
        print("На огонь костра слетается много насекомых. "
              "Исследователь с наименьшим показателем Внимания получает состояние Укусы насекомых. ")
    if Random_Night_Mount_Event == 3:
        print("Вы предусмотрительно накидываете травы и песка на землю, чтобы не спать на жестких камнях. "
              "Таким образом вам удается выспаться в относительном комфорте.")
    return


def random_jungle_event():
    Random_Jungle_Event = random.randint(1, 3)
    if Random_Jungle_Event == 1:  # События джунглей при открытии
        print("Проходя по тропе вы замечаете необычные следы. "
              "Любой член экспедиции может пройти проверку внимательности 3. "
              "При успехе вы находите тропу диких кабанов. Эта локация получает знак охоты 4.")
    if Random_Jungle_Event == 2:
        print("Продираясь по густым зарослям, вы сбиваетесь с тропы. "
              "Каждый член экспедиции теряет дополнительное действие. ")
    if Random_Jungle_Event == 3:
        print("Заросли становятся все гуще. "
              "Игрок идущие во главе экспедиции должен пройти проверку Навигации 3. "
              "При провале вы возвращаетесь в предыдущую локацию, не открывая новую.")
    return


def random_night_jungle_event():
    Random_Night_Jungle_Event = random.randint(1, 3)
    if Random_Night_Jungle_Event == 1:  # События джунглей ночью
        print("Вы просыпаетесь от осознания того, что кто-то разворошил костер. "
              "Дикие кабаны прибежали на свет и разбросав угли скрылись. "
              "В лагере начинается пожар. "
              "Если есть запас воды, лидер экспедиции должен пройдите проверку самообладания 2, "
              "чтобы потушить костер. Иначе или при провале, "
              "член экспедиции с наименьшим самообладанием уничтожает случайную вещь и получает 1 легкое ранение.")
    if Random_Night_Jungle_Event == 2:
        print("Всю ночь вы вздрагиваете от каждого шороха. "
              "Наутро вы встаете еще более уставшим, чем когда ложились. "
              "На следующий ход все члены экспедиции получают -1 к выносливости и -1 к силе.")
    if Random_Night_Jungle_Event == 3:
        print("Ночью проходит дождь. Вы тратите много сил на защиту лагеря от затопления. "
              "Каждый исследователь получает на следующий ход -1 выносливость.  "
              "Если в локации нет знака доступа к питьевой воды, "
              "на следующий ход эта локация получает знак доступа к воде.")
    return


def random_plane_event():
    Random_Plane_Event = random.randint(1, 3)
    if Random_Plane_Event == 1:  # События равнин при открытии
        print("Тропа перед вами сильно петляет, идущий во главе экспедиции может пройти проверку навигации 4, "
              "чтобы попробовать найти короткий путь. При провале ничего не происходит. "
              "При успехе группа может переместиться в соседнюю локацию Равнину,  без затраты передвижения.")
    if Random_Plane_Event == 2:
        print("Тропу преграждает быстротекущая река. "
              "Группа может потратить 1 дополнительное движение, "
              "чтобы найти более безопасное место для пересечения, "
              "либо каждый член группы проходит проверку Силы 2. "
              "При провале получите 1 легкое ранение. Все исследователи могут пополнить запасы воды.")
    if Random_Plane_Event == 3:
        print("Вы натыкаетесь на стаю диких собак. Выложите врага – Дикие Собаки.")
    return


def random_night_plane_event():
    Random_Night_Plane_Event = random.randint(1, 3)
    if Random_Night_Plane_Event == 1:  # События равнин ночью
        print("Ночь прошла без происшествий, "
              "но наутро вы обнаруживаете, что ваши запасы еды сильно погрызли крысы. "
              "Исследователи теряют в сумме 2 запаса еды.")
    if Random_Night_Plane_Event == 2:
        print("Ночь была приятной и успокаивающей. "
              "Каждый исследователь может вылечить 1 негативное состояние.")
    if Random_Night_Plane_Event == 3:
        print("Вы слишком поздно поняли что разбили лагерь в близости к муравейникам. "
              "Всю ночь вы отчаянно боролись с этими насекомыми. "
              "Исследователи с самообладанием ниже 3-х получают в следующем дне на 1 очко передвижения меньше.")
    return


def random_desert_event():
    Random_Desert_Event = random.randint(1, 3)
    if Random_Desert_Event == 1:  # События пустынь при открытии
        print("Дорогу преграждает песчаная насыпь. Каждый исследователь проходит проверку Акробатики 2. "
              "Если у всех успех – группа проходит без происшествий. "
              "Если хотя бы один исследователь провалил проверку, "
              "группа вынуждена либо потратить дополнительное движение на прохождение этого участка, "
              "либо отступить назад. ")
    if Random_Desert_Event == 2:
        print("Вы пробираетесь по этим засушливым территориям уже очень долго, "
              "в глазах рябит от этого несменяемого маршрута. "
              "В усталости вы почти не смотрите под ноги,  и попадаете ногой прямо в змеиное гнездо. "
              "Выложите врага Ядовитая змея.")
    if Random_Desert_Event == 3:
        print("Тропа разделяется на множество мелких троп. "
              "Впереди идущий должен пройти проверку Навигации 3. "
              "При успехе можно выбрать любую локацию, соединенную с исходной, и переместится в нее, "
              "без дополнительных затрат передвижения. "
              "При провале вы попадаете в ту локацию, в которую двигались изначально.")
    return


def random_night_desert_event():
    Random_Night_Desert_Event = random.randint(1, 3)
    if Random_Night_Desert_Event == 1:  # События пустынь ночью
        print("Ночь была ветреная, и засушливая. Если в локации нет источника воды, "
              "каждый исследователь должен потратить запас воды.")
    if Random_Night_Desert_Event == 2:
        print("Вы проспали относительно спокойно, лишь изредка просыпаясь от тихих шорохов. "
              "Наутро вы замечаете как вокруг лагеря много следов змей, "
              "и одна из них угрожающе шипит глядя на вас. "
              "Выложите врага Ядовитая змея.")
    if Random_Night_Desert_Event == 3:
        print("Вы готовите укромное место для ночлега и слегка раскапываете землю. "
              "Внезапно вы натыкаетесь на гнездо термитов. "
              "Исследователь с самым высоким показателем силы получает состояние Укусы насекомых.")


class Ui_Dialog(object):
    def __init__(self):
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(852, 673)
        Dialog.setStyleSheet("background-color: gray;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 80, 61, 61))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton.setStyleSheet("background-color: blue;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 100, 61, 61))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_2.setStyleSheet("background-color: blue;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 80, 61, 61))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_3.setStyleSheet("background-color: blue;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4.setGeometry(QtCore.QRect(310, 100, 61, 61))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_4.setStyleSheet("background-color: blue;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 80, 61, 61))
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_5.setStyleSheet("background-color: blue;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 140, 61, 61))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_6.setStyleSheet("background-color: blue;")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 140, 61, 61))
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setIcon(QtGui.QIcon("Mountain.jpg"))  # Гора
        self.pushButton_7.setStyleSheet("background-color: brown;")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 140, 61, 61))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_8.setStyleSheet("background-color: blue;")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 160, 61, 61))
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_9.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_9.setStyleSheet("background-color: blue;")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 160, 61, 61))
        self.pushButton_10.setMouseTracking(False)
        self.pushButton_10.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_10.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_10.setStyleSheet("background-color: blue;")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(130, 200, 61, 61))
        self.pushButton_11.setMouseTracking(False)
        self.pushButton_11.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_11.setIcon(QtGui.QIcon("Mountain.jpg"))  # Гора
        self.pushButton_11.setStyleSheet("background-color: brown;")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(250, 200, 61, 61))
        self.pushButton_12.setMouseTracking(False)
        self.pushButton_12.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_12.setIcon(QtGui.QIcon("Forest.jpg"))  # Лес
        self.pushButton_12.setStyleSheet("background-color: green;")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(370, 200, 61, 61))
        self.pushButton_13.setMouseTracking(False)
        self.pushButton_13.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_13.setIcon(QtGui.QIcon("Mountain.jpg"))  # Гора
        self.pushButton_13.setStyleSheet("background-color: brown;")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")

        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(190, 220, 61, 61))
        self.pushButton_14.setMouseTracking(False)
        self.pushButton_14.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_14.setIcon(QtGui.QIcon("Desert.jpg"))  # Пустыня
        self.pushButton_14.setStyleSheet("background-color: yellow;")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 220, 61, 61))
        self.pushButton_15.setMouseTracking(False)
        self.pushButton_15.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_15.setIcon(QtGui.QIcon("Desert.jpg"))  # Пустыня
        self.pushButton_15.setStyleSheet("background-color: yellow;")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(130, 260, 61, 61))
        self.pushButton_16.setMouseTracking(False)
        self.pushButton_16.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_16.setIcon(QtGui.QIcon("Forest.jpg"))  # Лес
        self.pushButton_16.setStyleSheet("background-color: green;")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(250, 260, 61, 61))
        self.pushButton_17.setMouseTracking(False)
        self.pushButton_17.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_17.setIcon(QtGui.QIcon("Swamp.jpg"))  # Джунгли
        self.pushButton_17.setStyleSheet("background-color: gray;")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")

        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(370, 260, 61, 61))
        self.pushButton_18.setMouseTracking(False)
        self.pushButton_18.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_18.setIcon(QtGui.QIcon("Forest.jpg"))  # Лес
        self.pushButton_18.setStyleSheet("background-color: green;")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")

        self.pushButton_19 = QtWidgets.QPushButton(Dialog)
        self.pushButton_19.setGeometry(QtCore.QRect(190, 280, 61, 61))
        self.pushButton_19.setMouseTracking(False)
        self.pushButton_19.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_19.setIcon(QtGui.QIcon("Forest.jpg"))  # Лес
        self.pushButton_19.setStyleSheet("background-color: green;")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")

        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(310, 280, 61, 61))
        self.pushButton_20.setMouseTracking(False)
        self.pushButton_20.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_20.setIcon(QtGui.QIcon("Forest.jpg"))  # Лес
        self.pushButton_20.setStyleSheet("background-color: green;")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")

        self.pushButton_21 = QtWidgets.QPushButton(Dialog)
        self.pushButton_21.setGeometry(QtCore.QRect(130, 320, 61, 61))
        self.pushButton_21.setMouseTracking(False)
        self.pushButton_21.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_21.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_21.setStyleSheet("background-color: blue;")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")

        self.pushButton_22 = QtWidgets.QPushButton(Dialog)
        self.pushButton_22.setGeometry(QtCore.QRect(250, 320, 61, 61))
        self.pushButton_22.setMouseTracking(False)
        self.pushButton_22.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_22.setIcon(QtGui.QIcon("Desert.jpg"))  # Пустыня
        self.pushButton_22.setStyleSheet("background-color: yellow;")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")

        self.pushButton_23 = QtWidgets.QPushButton(Dialog)
        self.pushButton_23.setGeometry(QtCore.QRect(370, 320, 61, 61))
        self.pushButton_23.setMouseTracking(False)
        self.pushButton_23.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_23.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_23.setStyleSheet("background-color: blue;")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")

        self.pushButton_24 = QtWidgets.QPushButton(Dialog)
        self.pushButton_24.setGeometry(QtCore.QRect(190, 340, 61, 61))
        self.pushButton_24.setMouseTracking(False)
        self.pushButton_24.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_24.setIcon(QtGui.QIcon("Swamp.jpg"))  # Джунгли
        self.pushButton_24.setStyleSheet("background-color: gray;")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")

        self.pushButton_25 = QtWidgets.QPushButton(Dialog)
        self.pushButton_25.setGeometry(QtCore.QRect(310, 340, 61, 61))
        self.pushButton_25.setMouseTracking(False)
        self.pushButton_25.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_25.setIcon(QtGui.QIcon("Swamp.jpg"))  # Джунгли
        self.pushButton_25.setStyleSheet("background-color: gray;")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")

        self.pushButton_26 = QtWidgets.QPushButton(Dialog)
        self.pushButton_26.setGeometry(QtCore.QRect(130, 380, 61, 61))
        self.pushButton_26.setMouseTracking(False)
        self.pushButton_26.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_26.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_26.setStyleSheet("background-color: blue;")
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")

        self.pushButton_27 = QtWidgets.QPushButton(Dialog)
        self.pushButton_27.setGeometry(QtCore.QRect(250, 380, 61, 61))
        self.pushButton_27.setMouseTracking(False)
        self.pushButton_27.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_27.setIcon(QtGui.QIcon("Swamp.jpg"))  # Джунгли
        self.pushButton_27.setStyleSheet("background-color: gray;")
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")

        self.pushButton_28 = QtWidgets.QPushButton(Dialog)
        self.pushButton_28.setGeometry(QtCore.QRect(370, 380, 61, 61))
        self.pushButton_28.setMouseTracking(False)
        self.pushButton_28.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_28.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_28.setStyleSheet("background-color: blue;")
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")

        self.pushButton_29 = QtWidgets.QPushButton(Dialog)
        self.pushButton_29.setGeometry(QtCore.QRect(190, 400, 61, 61))
        self.pushButton_29.setMouseTracking(False)
        self.pushButton_29.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_29.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_29.setStyleSheet("background-color: blue;")
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")

        self.pushButton_30 = QtWidgets.QPushButton(Dialog)
        self.pushButton_30.setGeometry(QtCore.QRect(310, 400, 61, 61))
        self.pushButton_30.setMouseTracking(False)
        self.pushButton_30.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_30.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_30.setStyleSheet("background-color: blue;")
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")

        self.pushButton_31 = QtWidgets.QPushButton(Dialog)
        self.pushButton_31.setGeometry(QtCore.QRect(130, 440, 61, 61))
        self.pushButton_31.setMouseTracking(False)
        self.pushButton_31.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_31.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_31.setStyleSheet("background-color: blue;")
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")

        self.pushButton_32 = QtWidgets.QPushButton(Dialog)
        self.pushButton_32.setGeometry(QtCore.QRect(250, 440, 61, 61))
        self.pushButton_32.setMouseTracking(False)
        self.pushButton_32.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_32.setIcon(QtGui.QIcon("Ship.jpg"))  # Вода
        self.pushButton_32.setStyleSheet("background-color: purple;")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")

        self.pushButton_33 = QtWidgets.QPushButton(Dialog)
        self.pushButton_33.setGeometry(QtCore.QRect(370, 440, 61, 61))
        self.pushButton_33.setMouseTracking(False)
        self.pushButton_33.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_33.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_33.setStyleSheet("background-color: blue;")
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")

        self.pushButton_34 = QtWidgets.QPushButton(Dialog)
        self.pushButton_34.setGeometry(QtCore.QRect(430, 170, 61, 61))
        self.pushButton_34.setMouseTracking(False)
        self.pushButton_34.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_34.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_34.setStyleSheet("background-color: blue;")
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")

        self.pushButton_35 = QtWidgets.QPushButton(Dialog)
        self.pushButton_35.setGeometry(QtCore.QRect(430, 230, 61, 61))
        self.pushButton_35.setMouseTracking(False)
        self.pushButton_35.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_35.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_35.setStyleSheet("background-color: blue;")
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")

        self.pushButton_36 = QtWidgets.QPushButton(Dialog)
        self.pushButton_36.setGeometry(QtCore.QRect(430, 290, 61, 61))
        self.pushButton_36.setMouseTracking(False)
        self.pushButton_36.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_36.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_36.setStyleSheet("background-color: blue;")
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")

        self.pushButton_37 = QtWidgets.QPushButton(Dialog)
        self.pushButton_37.setGeometry(QtCore.QRect(430, 350, 61, 61))
        self.pushButton_37.setMouseTracking(False)
        self.pushButton_37.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_37.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_37.setStyleSheet("background-color: blue;")
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")

        self.pushButton_38 = QtWidgets.QPushButton(Dialog)
        self.pushButton_38.setGeometry(QtCore.QRect(10, 250, 61, 61))
        self.pushButton_38.setMouseTracking(False)
        self.pushButton_38.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_38.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_38.setStyleSheet("background-color: blue;")
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")

        self.pushButton_39 = QtWidgets.QPushButton(Dialog)
        self.pushButton_39.setGeometry(QtCore.QRect(70, 340, 61, 61))
        self.pushButton_39.setMouseTracking(False)
        self.pushButton_39.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_39.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_39.setStyleSheet("background-color: blue;")
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")

        self.pushButton_40 = QtWidgets.QPushButton(Dialog)
        self.pushButton_40.setGeometry(QtCore.QRect(70, 280, 61, 61))
        self.pushButton_40.setMouseTracking(False)
        self.pushButton_40.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_40.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_40.setStyleSheet("background-color: blue;")
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")

        self.pushButton_41 = QtWidgets.QPushButton(Dialog)
        self.pushButton_41.setGeometry(QtCore.QRect(70, 220, 61, 61))
        self.pushButton_41.setMouseTracking(False)
        self.pushButton_41.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_41.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_41.setStyleSheet("background-color: blue;")
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")

        self.pushButton_42 = QtWidgets.QPushButton(Dialog)
        self.pushButton_42.setGeometry(QtCore.QRect(70, 160, 61, 61))
        self.pushButton_42.setMouseTracking(False)
        self.pushButton_42.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_42.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_42.setStyleSheet("background-color: blue;")
        self.pushButton_42.setText("")
        self.pushButton_42.setObjectName("pushButton_42")

        self.pushButton_43 = QtWidgets.QPushButton(Dialog)
        self.pushButton_43.setGeometry(QtCore.QRect(490, 260, 61, 61))
        self.pushButton_43.setMouseTracking(False)
        self.pushButton_43.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_43.setIcon(QtGui.QIcon("Cloud.jpg"))  # Вода
        self.pushButton_43.setStyleSheet("background-color: blue;")
        self.pushButton_43.setText("")
        self.pushButton_43.setObjectName("pushButton_43")

        self.pushButton_44 = QtWidgets.QPushButton(Dialog)  # Ночь
        self.pushButton_44.setGeometry(QtCore.QRect(490, 440, 61, 61))
        self.pushButton_44.setMouseTracking(False)
        self.pushButton_44.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_44.setText("Ночь")
        self.pushButton_44.setStyleSheet("color: white;")
        self.pushButton_44.setObjectName("pushButton_44")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(610, 40, 211, 201))
        self.label.setStyleSheet("background-color: white;")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setText("test")
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(610, 290, 211, 201))
        self.textEdit.setStyleSheet("background-color: white;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


# if __name__ == "__main__":
import sys

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
