import sys
from firebase import firebase
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit

class User():
    def __init__(self):
        self.email = ''
        self.barcode = ''
        self.groups = []


class NewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 450, 500)
        self.setWindowTitle('Новый пользователь')

        self.user = User()

        self.email_label = QLabel(self)
        self.email_label.setText('Email:')
        self.email_label.move(80, 30)

        self.email_gap = QLineEdit(self)
        self.email_gap.move(80, 70)

        self.barcode_label = QLabel(self)
        self.barcode_label.setText('Штих-код:')
        self.barcode_label.move(80, 130)

        self.barcode_gap = QLineEdit(self)
        self.barcode_gap.move(80, 170)

        self.group_label = QLabel(self)
        self.group_label.setText('По одной введите группы пользователя:')
        self.group_label.move(80, 230)

        self.group_gap = QLineEdit(self)
        self.group_gap.move(80, 270)

        self.add_group_btn = QPushButton('Добавить группу в список групп', self)
        self.add_group_btn.resize(self.add_group_btn.sizeHint())
        self.add_group_btn.move(75, 310)
        self.add_group_btn.clicked.connect(self.add_group)

        self.btn1 = QPushButton('Добавить в базу', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(40, 380)
        self.btn1.clicked.connect(self.user_init)

        self.btn2 = QPushButton('Завершить', self)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(275, 380)
        self.btn2.clicked.connect(self.close_all)

    def add_group(self):
        if self.group_gap.text() == '':
            return
        self.user.groups.append(self.group_gap.text())
        self.group_gap.setText('')

    def clear_all(self):
        self.email_gap.setText('')
        self.barcode_gap.setText('')

    def user_init(self):
        self.user.email = self.email_gap.text()
        self.user.email.join(list(filter(lambda x: x.isalpha(), self.user.email)))
        if self.user.email == '':
            self.clear_all()
            return
        self.user.barcode = self.barcode_gap.text()
        if self.user.barcode == '':
            self.clear_all()
            return
        self.user.barcode = int(self.user.barcode)
        self.user.groups = list(set(self.user.groups))
        self.clear_all()
        self.send()

    def send(self):
        data = {
            'code': self.user.barcode,
            'groups': {}
        }
        for id in self.user.groups:
            data['groups'][id] = id
        base.put('/users/', self.user.email, data)

    def close_all(self):
        sys.exit(app.exec_())


class Group():
    def __init__(self):
        self.name = ''
        self.members = []


class NewGroup(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 450, 400)
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

        self.btn1 = QPushButton('Добавить в базу', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(40, 280)
        self.btn1.clicked.connect(self.group_init)

        self.btn2 = QPushButton('Завершить', self)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(275, 280)
        self.btn2.clicked.connect(self.close_all)

    def add_member(self):
        new_member = self.member_gap.text()
        new_member.join(list(filter(lambda x: x.isalpha(), new_member)))
        if new_member == '':
            return
        self.group.members.append(new_member)
        self.member_gap.setText('')

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
            'users': {}
        }
        for email in self.group.members:
            data['users'][email] = email
        base.put('/groups/', self.group.name, data)

    def close_all(self):
        sys.exit(app.exec_())


class Event():
    def __init__(self):
        self.name = ''
        self.description = ''
        self.groups = []
        self.is_optional = False
        self.place = ''
        self.date = ''
        self.time_begin = ''
        self.time_end = ''


class NewEvent(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 700, 700)
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

        self.date_label = QLabel(self)
        self.date_label.setText('Дата в формате дд.мм.гг:')
        self.date_label.move(500, 130)

        self.date_gap = QLineEdit(self)
        self.date_gap.move(500, 160)

        self.timeb_label = QLabel(self)
        self.timeb_label.setText('Начало в формате чч.мм:')
        self.timeb_label.move(500, 230)

        self.timeb_gap = QLineEdit(self)
        self.timeb_gap.move(500, 260)

        self.timee_label = QLabel(self)
        self.timee_label.setText('Конец в формате чч.мм:')
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
        self.date_gap.setText('')
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
        if self.date_gap.text().count('.') != 2:
            self.clear_all()
            return
        self.event.date = self.date_gap.text()
        if self.timeb_gap.text().count('.') != 1:
            self.clear_all()
            return
        self.event.time_begin = self.timeb_gap.text()
        if self.timee_gap.text().count('.') != 1:
            self.clear_all()
            return
        self.event.time_end = self.timee_gap.text()
        self.clear_all()
        self.send()

    def send(self):
        data = {
            'description': self.event.description,
            'invited_groups': {},
            'is_optional': self.event.is_optional,
            'place': self.event.place,
            'date': self.event.date,
            'time': {
                'begin': self.event.time_begin,
                'end': self.event.time_end
            }
        }
        for id in self.event.groups:
            data['invited_groups'][id] = id
        base.put('/events/', self.event.name, data)

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
        self.open_user_wind = NewUser()
        self.open_user_wind.show()

    def new_group(self):
        self.open_group_wind = NewGroup()
        self.open_group_wind.show()

    def new_event(self):
        self.open_event_wind = NewEvent()
        self.open_event_wind.show()


if __name__ == '__main__':
    base = firebase.FirebaseApplication("https://redditboard-39f65.firebaseio.com/", None)
    app = QApplication(sys.argv)
    wid = MainWidget()
    wid.show()
    sys.exit(app.exec())