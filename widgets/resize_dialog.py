from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class ResizeDialog(QDialog):
    def __init__(self, current_width, current_height, parent=None):
        super().__init__(parent)
        self.setWindowTitle("크기 조정")
        self.setFixedSize(220, 120)
        layout = QVBoxLayout(self)

        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("가로(px):"))
        self.width_edit = QLineEdit(str(current_width))
        self.width_edit.setFixedWidth(60)
        size_layout.addWidget(self.width_edit)
        size_layout.addWidget(QLabel("세로(px):"))
        self.height_edit = QLineEdit(str(current_height))
        self.height_edit.setFixedWidth(60)
        size_layout.addWidget(self.height_edit)
        layout.addLayout(size_layout)

        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("확인")
        ok_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("취소")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def get_size(self):
        try:
            w = int(self.width_edit.text())
            h = int(self.height_edit.text())
            return w, h
        except ValueError:
            return None, None
