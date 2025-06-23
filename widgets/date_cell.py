from PyQt5.QtWidgets import QFrame, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from widgets.event_dialog import EventInputDialog
from google_calendar import add_event_to_google_calendar, get_events_from_google_calendar

class DateCell(QFrame):
    def __init__(self, date, parent=None):
        super().__init__(parent)
        self.date = date
        self.event_text = ""
        self.setStyleSheet("background: #222; border: 1px solid #333;")
        self.setMinimumSize(50, 40)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 날짜 숫자 (네모칸 없이, 그냥 셀 우측 상단에 표시)
        self.date_label = QLabel(str(self.date.day()), self)
        self.date_label.setFont(QFont("ONE 모바일POP", 9, QFont.Bold))
        self.date_label.setStyleSheet("color: #bbb; background: transparent;")
        self.date_label.setAlignment(Qt.AlignRight | Qt.AlignTop)

        # 일정 표시 (네모칸 없이 셀 내부에 표시)
        self.label = QLabel("", self)
        self.label.setStyleSheet("color: #fff; background: transparent;")
        self.label.setWordWrap(True)
        self.label.setFont(QFont("ONE 모바일POP", 11))

        # 구글 캘린더에서 일정 불러오기
        events = get_events_from_google_calendar(self.date)
        if events:
            self.event_text = "\n".join(events)
            self.update_display()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            dialog = EventInputDialog(self.date, self)
            if dialog.exec_():
                self.event_text = dialog.get_event_text()
                self.update_display()
                add_event_to_google_calendar(self.date, self.event_text)

    def update_display(self):
        self.label.setText(self.event_text)\
        
    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        self.date_label.setGeometry(w-32, 2, 30, 16)
        self.label.setGeometry(8, 22, w-16, h-30)
        super().resizeEvent(event)    
