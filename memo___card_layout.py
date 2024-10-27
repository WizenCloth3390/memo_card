from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 
from random import shuffle

provider = None
# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно
menu_btn = QPushButton('Меню')

# кнопка прибирає вікно і повертає його після закінчення таймера
rest_btn = QPushButton('Відпочити')

# введення кількості хвилин
time_box = QSpinBox()

# кнопка відповіді "Ок" / "Наступний"
ok_btn = QPushButton('Ок')

# текст питання
question_label = QLabel("")

# Опиши групу перемикачів
question_group = QGroupBox("Варіанти відповіді")
radio_group = QButtonGroup()
radio1 = QRadioButton()
radio2 = QRadioButton()
radio3 = QRadioButton()
radio4 = QRadioButton()

radio_group.addButton(radio1)
radio_group.addButton(radio2)
radio_group.addButton(radio3)
radio_group.addButton(radio4)

# Опиши панель з результатами
resault_group = QGroupBox("Результати")
resault = QLabel("")
true_resault = QLabel("")

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
true_answer = QRadioButton("")

def card() :
    main_layout = QVBoxLayout()
    
    component1 = header()
    main_layout.addLayout(component1)
    
    main_layout.addStretch(1)
    main_layout.addWidget(question_label, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addStretch(1)
        
    component2 = questionFrom()
    main_layout.addWidget(component2, stretch=8)
    component3 = answerFrom()
    main_layout.addWidget(component3, stretch=8)
    
    main_layout.addStretch(1)
    
    horizontal_btn = QHBoxLayout()
    horizontal_btn.addStretch(1)
    horizontal_btn.addWidget(ok_btn, stretch=2)
    horizontal_btn.addStretch(1)
    main_layout.addLayout(horizontal_btn)
    main_layout.addStretch(1)
    
    #СХОВАЄМ ПИТАННЯ
    resault_group.hide()
    question_group.hide()
    
    return main_layout

def header() : 
    header_layout = QHBoxLayout()
    
    time_box.setValue(30)

    header_layout.addWidget(menu_btn, Qt.AlignmentFlag.AlignLeft)
    header_layout.addStretch(4)

    header_layout.addWidget(rest_btn, Qt.AlignmentFlag.AlignLeft)
    header_layout.addWidget(time_box, Qt.AlignmentFlag.AlignLeft)
    
    Q = QLabel('Хвилини')
    header_layout.addWidget(Q)    

    return header_layout

def questionFrom() :
    question_group_layout = QVBoxLayout()

    question_supgroup1 = QHBoxLayout()
    question_supgroup2 = QHBoxLayout()
    
    question_supgroup1.addWidget(radio1)
    question_supgroup1.addWidget(radio2)
    question_supgroup2.addWidget(radio3)
    question_supgroup2.addWidget(radio4)
    
    question_group_layout.addLayout(question_supgroup1)
    question_group_layout.addLayout(question_supgroup2)
    
    question_group.setLayout(question_group_layout)
    
    return question_group
    
def answerFrom() :
    answer_group_layout = QVBoxLayout()
    answer_group_layout.addWidget(resault, alignment=Qt.AlignmentFlag.AlignCenter)
    resault_group.setLayout(answer_group_layout)
    
    return resault_group

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    resault_group.show()
    question_group.hide()

def show_question():
    resault_group.hide()
    question_group.show()

def setQuestionstoCard(questions) :
    global provider
    provider = questions
    
def generateQuestion() :
    my_question = provider.giveRandomQuestion()
    setQuestion(my_question.question, my_question.right_answer, my_question.wrong1, my_question.wrong2, my_question.wrong3)    
    show_question()
    
# Події
def setQuestion(my_question, tanswer, fanswer1, fanswer2, fanswer3):
    global true_answer
    
    question_label.setText(my_question)
    radio_btns = [radio1, radio2, radio3, radio4]
    
    shuffle(radio_btns)
    
    radio_btns[0].setText(tanswer)
    radio_btns[1].setText(fanswer1)
    radio_btns[2].setText(fanswer2)
    radio_btns[3].setText(fanswer3)
    
    radio_group.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    radio_group.setExclusive(True)
    
    true_answer = radio_btns[0]

def check_answer() :
    global true_answer
    
    if(true_answer.isChecked()) :
        resault.setText("Вірно")
    else :
        resault.setText("Не вірно")

def click_ok() :
    if(ok_btn.text() == "Ок") :
        check_answer()
        ok_btn.setText("Наступний")
        show_result()
    else :
        generateQuestion()
        ok_btn.setText("Ок")

def give_rest_time() :
    return time_box.value() * 1000

ok_btn.clicked.connect(click_ok)
