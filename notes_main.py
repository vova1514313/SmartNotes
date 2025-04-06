def message(txt):
    mesBox = QMessageBox()
    mesBox.setText(txt)
    mesBox.show()
    mesBox.exec()

def add_note():
    note_name, ok = QInputDialog.getText(win, "Добавтить заметку", "Название заметки: ")
    if ok and note_name != "":
        data[note_name] = {"текст" : "", "теги" : []}
        notesList.addItem(note_name)
        tagsList.addItems(data[note_name]["теги"])

def show_note():
    key = notesList.selectedItems()[0].text()
    textEdit.setText(data[key]["текст"])
    tagsList.clear()
    tagsList.addItems(data[key]["теги"])

def save_note():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        data[key]["текст"] = textEdit.toPlainText()
        with open("Data.json", "w") as file:
            json.dump(data, file, sort_keys=True)
    else:
        message('Вы не выбрали заметку!')

def del_note():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        del data[key]
        notesList.clear()
        tagsList.clear()
        textEdit.clear()
        notesList.addItems(data)
        with open("Data.json", "w") as file:
            json.dump(data, file, sort_keys=True)
    else:
        message('Вы не выбрали заметку!')

def add_tag():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        tag = lineEdit.text()
        if not tag in data[key]["теги"]:
            data[key]["теги"].append(tag)
            tagsList.addItem(tag)
            lineEdit.clear()
        with open("Data.json", "w") as file:
            json.dump(data, file, sort_keys=True)
    else:
        message('Вы не выбрали заметку!')

def del_tag():
    if tagsList.selectedItems():
        key = notesList.selectedItems()[0].text()
        tag = tagsList.selectedItems()[0].text()
        data[key]['теги'].remove(tag)
        tagsList.clear()
        tagsList.addItems(data[key]["теги"])
        with open("Data.json", "w") as file:
            json.dump(data, file, sort_keys=True)
    else:
        message('Вы не выбрали тег!')

def search_tag():
    tag = lineEdit.text()
    if search_tag_btn.text() == "искать по тегу" and not(tag in ['', ' ']):
        notes_filtered = {}
        for note in data:
            if tag in data[note]["теги"]:
                notes_filtered[note]=data[note]
        search_tag_btn.setText("Сбросить поиск")
        notesList.clear()
        tagsList.clear()
        notesList.addItems(notes_filtered)
    elif search_tag_btn.text() == "Сбросить поиск":
        lineEdit.clear()
        notesList.clear()
        tagsList.clear()
        notesList.addItems(data)
        search_tag_btn.setText("искать по тегу")
    else:
        message('Вы не ввели тег для поиска!')

import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout, 
    QRadioButton,
    QGroupBox,
    QPushButton,
    QButtonGroup,
    QListWidget,
    QLineEdit,
    QTextEdit,
    QInputDialog,
    QMessageBox)

k = 0.8
app = QApplication([])
win = QWidget()
win.setWindowTitle('Умеые заметки')
w = int(1600 * k)
h = int(900 * k)

textEdit = QTextEdit()
notesList = QListWidget()
tagsList = QListWidget()
lineEdit = QLineEdit()
add_note_btn = QPushButton('создать заметку')
del_note_btn = QPushButton('удалить заметку')
save_note_btn = QPushButton('сохранить заметку')
add_tag_btn = QPushButton('добавить тег')
del_tag_btn = QPushButton('удалить тег')
search_tag_btn = QPushButton('искать по тегу')

main_line = QHBoxLayout()
left_line = QVBoxLayout()
right_line = QVBoxLayout()

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line7 = QHBoxLayout()

line1.addWidget(notesList)
line2.addWidget(add_note_btn)
line2.addWidget(del_note_btn)
line3.addWidget(save_note_btn)
line4.addWidget(tagsList)
line5.addWidget(lineEdit)
line6.addWidget(add_tag_btn)
line6.addWidget(del_tag_btn)
line7.addWidget(search_tag_btn)

right_line.addLayout(line1)
right_line.addLayout(line2)
right_line.addLayout(line3)
right_line.addLayout(line4)
right_line.addLayout(line5)
right_line.addLayout(line6)
right_line.addLayout(line7)

left_line.addWidget(textEdit)

main_line.addLayout(left_line, 60)
main_line.addLayout(right_line, 40)

win.setLayout(main_line)

add_note_btn.clicked.connect(add_note)
notesList.itemClicked.connect(show_note)
save_note_btn.clicked.connect(save_note)
del_note_btn.clicked.connect(del_note)
add_tag_btn.clicked.connect(add_tag)
del_tag_btn.clicked.connect(del_tag)
search_tag_btn.clicked.connect(search_tag)

with open("Data.json", "r") as file:
    data = json.load(file)
notesList.addItems(data)

win.show()
app.exec_()


    
