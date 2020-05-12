import sys
from firebase import firebase
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QTableWidget, QTableWidgetItem

class User():
    def __init__(self):
        self.email = ''
        self.barcode = ''
        self.groups = []

class NewUser2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global table_list
        self.setGeometry(100, 100, 600, 500)

        self.table2 = QTableWidget(self)
        self.table2.setColumnCount(3)
        self.table2.setRowCount(len(table_list))
        self.table2.setHorizontalHeaderLabels(['email', 'штрих-код', 'группы через запятую'])
        self.table2.move(80, 30)
        self.table2.resize(500, 400)
        self.table2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        for i in range(len(table_list)):
            self.table2.setItem(i, 0, QTableWidgetItem(table_list[i].email))
            self.table2.setItem(i, 1, QTableWidgetItem(table_list[i].barcode))
            self.table2.setItem(i, 2, QTableWidgetItem(','.join(table_list[i].groups)))

        self.btn1 = QPushButton('Добавить в базу (таблицу можно редактировать)', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(80, 430)
        self.btn1.clicked.connect(self.send)

    def my_format(self, s):
        l = 0
        while s[l] == ' ':
            l += 1
        r = len(s) - 1
        while s[r] == ' ':
            r -= 1
        return s[l:r + 1]

    def send(self):
        for i in range(len(table_list)):
            table_list[i].email = self.table2.item(i, 0).text()
            table_list[i].email.join(list(filter(lambda x: x.isalpha(), table_list[i].email)))
            table_list[i].barcode = self.table2.item(i, 1).text()
            table_list[i].barcode = int(table_list[i].barcode)
            table_list[i].groups = self.table2.item(i, 2).text().split(',')
            table_list[i].groups = [self.my_format(table_list[i].groups[j]) for j in range(len(table_list[i].groups))]
        data = {}
        for e in table_list:
            data[e.email] = {}
            data[e.email]['code'] = e.barcode
            data[e.email]['groups'] = {}
            for id in e.groups:
                data[e.email]['groups'][id] = id
        base.put('/', 'users', data)
        sys.exit(app.exec_())


class NewUser1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 500)
        self.setWindowTitle('Новые пользователи')

        self.user = User()

        label = QLabel(self)
        label.setText('Вставьте фрагмент таблицы с участниками в формате')
        label.move(80, 30)

        self.table1 = QTableWidget(self)
        self.table1.setColumnCount(3)
        self.table1.setRowCount(0)
        self.table1.setHorizontalHeaderLabels(['email', 'штрих-код', 'группы через запятую'])
        self.table1.move(80, 60)
        self.table1.resize(400, 23)
        self.table1.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.main_gap = QLineEdit(self)
        self.main_gap.move(80, 83)
        self.main_gap.resize(400, 23)

        self.check_btn = QPushButton('Проверить', self)
        self.check_btn.resize(self.check_btn.sizeHint())
        self.check_btn.move(75, 105)
        self.check_btn.clicked.connect(self.check)

    def check(self):
        global table_list
        raw_table = self.main_gap.text().split('\n')
        for s in raw_table:
            new_user = User()
            user_str = s.split('\t')
            new_user.email = user_str[0]
            new_user.barcode = user_str[1]
            new_user.groups = user_str[2].split(',')
            table_list.append(new_user)

        self.open_user2_wind = NewUser2()
        self.open_user2_wind.show()


class Group():
    def __init__(self):
        self.name = ''
        self.members = []
        self.faq = {}


class NewGroup(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 450, 550)
        self.setWindowTitle('Новые группы')

        self.group = Group()

        self.name_label = QLabel(self)
        self.name_label.setText('Название:')
        self.name_label.move(80, 30)

        self.name_gap = QLineEdit(self)
        self.name_gap.move(80, 70)

        self.member_label = QLabel(self)
        self.member_label.setText('По одному введите email участников группы:')
        self.member_label.move(80, 130)

        self.member_gap = QLineEdit(self)
        self.member_gap.move(80, 170)

        self.add_member_btn = QPushButton('Добавить участника', self)
        self.add_member_btn.resize(self.add_member_btn.sizeHint())
        self.add_member_btn.move(75, 210)
        self.add_member_btn.clicked.connect(self.add_member)

        self.faq_label = QLabel(self)
        self.faq_label.setText('FAQ по одному, первый блок - вопрос, второй - ответ:')
        self.faq_label.move(80, 280)

        self.faq_ask_gap = QLineEdit(self)
        self.faq_ask_gap.move(80, 310)

        self.faq_answer_gap = QLineEdit(self)
        self.faq_answer_gap.move(300, 310)

        self.add_faq_btn = QPushButton('Добавить вопрос', self)
        self.add_faq_btn.resize(self.add_faq_btn.sizeHint())
        self.add_faq_btn.move(75, 340)
        self.add_faq_btn.clicked.connect(self.add_faq)

        self.btn1 = QPushButton('Добавить в базу', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(40, 450)
        self.btn1.clicked.connect(self.group_init)

        self.btn2 = QPushButton('Завершить', self)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(275, 450)
        self.btn2.clicked.connect(self.close_all)

    def add_member(self):
        new_member = self.member_gap.text()
        new_member.join(list(filter(lambda x: x.isalpha(), new_member)))
        if new_member == '':
            return
        self.group.members.append(new_member)
        self.member_gap.setText('')

    def add_faq(self):
        question = self.faq_ask_gap.text()
        if question == '':
            return
        self.faq_ask_gap.setText('')
        answer = self.faq_answer_gap.text()
        if answer == '':
            return
        self.faq_answer_gap.setText('')
        self.group.faq[question] = answer

    def clear_all(self):
        self.name_gap.setText('')

    def group_init(self):
        self.group.name = self.name_gap.text()
        if self.group.name == '':
            self.clear_all()
            return
        self.group.members = list(set(self.group.members))
        self.clear_all()
        self.send()

    def send(self):
        data = {
            'users': {},
            'faq': self.group.faq
        }
        for email in self.group.members:
            data['users'][email] = email
        base.put('/groups/', self.group.name, data)
        self.group = Group()

    def close_all(self):
        sys.exit(app.exec_())


class Event():
    def __init__(self):
        self.name = ''
        self.description = ''
        self.groups = []
        self.is_optional = False
        self.place = ''
        self.time_begin = ''
        self.time_end = ''


class NewEvent(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 700)
        self.setWindowTitle('Новые события')

        self.event = Event()

        self.name_label = QLabel(self)
        self.name_label.setText('Название:')
        self.name_label.move(80, 30)

        self.name_gap = QLineEdit(self)
        self.name_gap.move(80, 60)

        self.description_label = QLabel(self)
        self.description_label.setText('Описание:')
        self.description_label.move(80, 130)

        self.description_gap = QLineEdit(self)
        self.description_gap.move(80, 160)

        self.group_label = QLabel(self)
        self.group_label.setText('По одному введите названия приглашенных групп:')
        self.group_label.move(80, 230)

        self.group_gap = QLineEdit(self)
        self.group_gap.move(80, 260)

        self.add_group_btn = QPushButton('Добавить группу', self)
        self.add_group_btn.resize(self.add_group_btn.sizeHint())
        self.add_group_btn.move(75, 290)
        self.add_group_btn.clicked.connect(self.add_group)

        self.optional_label = QLabel(self)
        self.optional_label.setText('1 если мероприятие необязательное к посещению, иначе 0:')
        self.optional_label.move(80, 370)

        self.optional_gap = QLineEdit(self)
        self.optional_gap.move(80, 400)

        self.place_label = QLabel(self)
        self.place_label.setText('Место проведения:')
        self.place_label.move(500, 30)

        self.place_gap = QLineEdit(self)
        self.place_gap.move(500, 60)

        self.timeb_label = QLabel(self)
        self.timeb_label.setText('Начало в формате yyyy/mm/dd hh:mm:')
        self.timeb_label.move(500, 230)

        self.timeb_gap = QLineEdit(self)
        self.timeb_gap.move(500, 260)

        self.timee_label = QLabel(self)
        self.timee_label.setText('Конец в формате yyyy/mm/dd hh:mm:')
        self.timee_label.move(500, 330)

        self.timee_gap = QLineEdit(self)
        self.timee_gap.move(500, 360)

        self.btn1 = QPushButton('Добавить в базу', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(75, 580)
        self.btn1.clicked.connect(self.event_init)

        self.btn2 = QPushButton('Завершить', self)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(500, 580)
        self.btn2.clicked.connect(self.close_all)

    def add_group(self):
        new_group = self.group_gap.text()
        if new_group == '':
            return
        self.event.groups.append(new_group)
        self.group_gap.setText('')

    def clear_all(self):
        self.name_gap.setText('')
        self.description_gap.setText('')
        self.optional_gap.setText('')
        self.place_gap.setText('')
        self.timeb_gap.setText('')
        self.timee_gap.setText('')

    def event_init(self):
        self.event.name = self.name_gap.text()
        if self.event.name == '':
            self.clear_all()
            return
        self.event.description = self.description_gap.text()
        self.event.groups = list(set(self.event.groups))
        if self.optional_gap.text() != '0':
            self.event.is_optional = True
        else:
            self.event.is_optional = False
        self.event.place = self.place_gap.text()
        if self.timeb_gap.text().count('/') != 2:
            self.clear_all()
            return
        self.event.time_begin = self.timeb_gap.text()
        if self.timee_gap.text().count('/') != 2:
            self.clear_all()
            return
        self.event.time_end = self.timee_gap.text()
        self.clear_all()
        self.send()

    def send(self):
        data = {
            'description': self.event.description,
            'invited_groups': self.event.groups,
            'is_optional': self.event.is_optional,
            'place': self.event.place,
            'dateStart': self.event.time_begin,
            'dateEnd': self.event.time_end,
            'visitors': 0
        }
        base.put('/events/', self.event.name, data)
        self.event = Event()

    def close_all(self):
        sys.exit(app.exec_())


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 400)

        self.btn_user = QPushButton('Добавить пользователей', self)
        self.btn_user.resize(self.btn_user.sizeHint())
        self.btn_user.move(50, 50)
        self.btn_user.clicked.connect(self.new_user)

        self.btn_group = QPushButton('Добавить группы', self)
        self.btn_group.resize(self.btn_group.sizeHint())
        self.btn_group.move(50, 150)
        self.btn_group.clicked.connect(self.new_group)

        self.btn_event = QPushButton('Добавить события', self)
        self.btn_event.resize(self.btn_event.sizeHint())
        self.btn_event.move(50, 250)
        self.btn_event.clicked.connect(self.new_event)

    def new_user(self):
        self.open_user_wind = NewUser1()
        self.open_user_wind.show()

    def new_group(self):
        self.open_group_wind = NewGroup()
        self.open_group_wind.show()

    def new_event(self):
        self.open_event_wind = NewEvent()
        self.open_event_wind.show()


if __name__ == '__main__':
    global table_list
    table_list = []
    base = firebase.FirebaseApplication("https://redditboard-39f65.firebaseio.com/", None)
    app = QApplication(sys.argv)
    wid = MainWidget()
    wid.show()
    sys.exit(app.exec())