from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton, QMenu
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QPainter, QColor, QPen

from widgets.date_cell import DateCell
from widgets.resize_dialog import ResizeDialog

class CalendarUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Calendar")
        self.setGeometry(100, 100, 900, 700)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        header_layout = QHBoxLayout()

        today = QDate.currentDate()
        self.date_label = QLabel(f"오늘은 {today.year()}년 {today.month()}월 {today.day()}일 {today.toString('dddd')}")
        self.date_label.setFont(QFont("ONE 모바일POP", 14))
        self.date_label.setStyleSheet("background: transparent; color: black;")
        header_layout.addWidget(self.date_label)

        # 메뉴 버튼 (≡)
        menu_btn = QPushButton("≡")
        menu_btn.setFixedSize(36, 36)
        menu_btn.setStyleSheet("font-size:20px; background: transparent;")
        menu_btn.setCursor(Qt.PointingHandCursor)
        menu = QMenu(self)

        # 크기 조정 메뉴 추가
        resize_action = menu.addAction("크기 조정")
        resize_action.triggered.connect(self.show_resize_dialog)

        # 닫기 메뉴 추가
        close_action = menu.addAction("닫기")
        close_action.triggered.connect(self.close)

        menu_btn.setMenu(menu)
        header_layout.addWidget(menu_btn, alignment=Qt.AlignRight)
        main_layout.addLayout(header_layout)

        # 달력 그리드
        calendar_layout = QGridLayout()
        days = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
        for i, day in enumerate(days):
            lbl = QLabel(day)
            lbl.setFont(QFont("ONE 모바일POP", 11))
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("background: transparent; color: gray;")
            calendar_layout.addWidget(lbl, 0, i)

        base_date = QDate.currentDate()
        for week in range(1, 7):
            for day in range(7):
                cell_date = QDate(base_date.year(), base_date.month(), 1).addDays((week-1)*7 + day)
                cell = DateCell(cell_date)
                calendar_layout.addWidget(cell, week, day)

        main_layout.addLayout(calendar_layout)
        self.setLayout(main_layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(1.0)
        painter.setBrush(QColor(255, 255, 255))
        painter.setPen(QPen(Qt.transparent))
        painter.drawRoundedRect(self.rect(), 15, 15)

    def show_resize_dialog(self):
        dialog = ResizeDialog(self.width(), self.height(), self)
        if dialog.exec_():
            w, h = dialog.get_size()
            if w and h and w > 400 and h > 300:
                self.resize(w, h)
