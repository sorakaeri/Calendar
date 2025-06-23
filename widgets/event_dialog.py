from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QDialogButtonBox

class EventInputDialog(QDialog):
    def __init__(self, date, parent=None):
        super().__init__(parent)
        self.setWindowTitle(date.toString("yyyy년 M월 d일"))
        self.setFixedSize(250, 180)
        layout = QVBoxLayout(self)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_event_text(self):
        return self.text_edit.toPlainText()
