from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class ResizeDialog(QDialog):
    def __init__(self, current_width, current_height, parent=None):
        super().__init__(parent)
        self.setWindowTitle("크기 조정")
        self.setFixedSize(220, 120)
        layout = QVBoxLayout(self)

        # 크기 입력 레이아웃
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("가로(px):"))
        self.width_edit = QLineEdit(str(current_width))  # 현재 가로값 입력란
        self.width_edit.setFixedWidth(60)
        size_layout.addWidget(self.width_edit)
        size_layout.addWidget(QLabel("세로(px):"))
        self.height_edit = QLineEdit(str(current_height))  # 현재 세로값 입력란
        self.height_edit.setFixedWidth(60)
        size_layout.addWidget(self.height_edit)
        layout.addLayout(size_layout)

        # 버튼 레이아웃 (확인/취소)
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("확인")
        ok_btn.clicked.connect(self.accept)    # 확인 클릭 시 다이얼로그 종료(accept)
        cancel_btn = QPushButton("취소")
        cancel_btn.clicked.connect(self.reject)  # 취소 클릭 시 다이얼로그 종료(reject)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def get_size(self):
        """
        입력된 가로, 세로 값을 정수로 반환
        숫자가 아니면 (None, None) 반환
        """
        try:
            w = int(self.width_edit.text())
            h = int(self.height_edit.text())
            return w, h
        except ValueError:
            return None, None
