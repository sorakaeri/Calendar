from PyQt5.QtWidgets import QFrame, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from widgets.event_dialog import EventInputDialog
from google_calendar import add_event_to_google_calendar, get_events_from_google_calendar

class DateCell(QFrame):
    def __init__(self, date, parent=None):
        super().__init__(parent)
        self.date = date  # 셀에 해당하는 날짜
        self.event_text = ""  # 일정 텍스트 저장
        self.setStyleSheet("background: #222; border: 1px solid #333;")
        self.setMinimumSize(50, 40)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 날짜 숫자 라벨 (셀 우측 상단에 표시)
        self.date_label = QLabel(str(self.date.day()), self)
        self.date_label.setFont(QFont("ONE 모바일POP", 9, QFont.Bold))
        self.date_label.setStyleSheet("color: #bbb; background: transparent;")
        self.date_label.setAlignment(Qt.AlignRight | Qt.AlignTop)

        # 일정 표시 라벨 (셀 내부에 표시)
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
        # 셀을 더블클릭하면 일정 입력 다이얼로그 표시
        if event.button() == Qt.LeftButton:
            dialog = EventInputDialog(self.date, self)
            if dialog.exec_():
                self.event_text = dialog.get_event_text()  # 입력된 일정 저장
                self.update_display()  # 화면에 일정 표시
                add_event_to_google_calendar(self.date, self.event_text)  # 구글 캘린더에 일정 추가

    def update_display(self):
        # 일정 텍스트를 라벨에 표시
        self.label.setText(self.event_text)
        
    def resizeEvent(self, event):
        # 셀 크기 변경 시 라벨 위치/크기 조정
        w, h = self.width(), self.height()
        self.date_label.setGeometry(w-32, 2, 30, 16)  # 날짜 숫자 위치
        self.label.setGeometry(8, 22, w-16, h-30)     # 일정 텍스트 위치
        super().resizeEvent(event)
