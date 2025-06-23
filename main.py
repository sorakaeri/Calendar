from PyQt5.QtWidgets import QApplication
import sys
from calendar_ui import CalendarUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CalendarUI()
    win.show()
    sys.exit(app.exec_())
