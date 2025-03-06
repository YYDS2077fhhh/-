import sys
from PyQt6.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit,QVBoxLayout
 
class BUTTON(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.Buttonclick = 0

        self.setWindowTitle("qwq藏起来了")
        self.resize(160,100)
        
        button = QPushButton("按鈕",clicked = self.Buttonpush)
        self.textline = QLineEdit()

        layout.addWidget(button)
        layout.addWidget(self.textline)

    def Buttonpush(self):
        self.Buttonclick += 1
        self.textline.setText(f"您点击了{self.Buttonclick}下按鈕")
        if self.Buttonclick == 1000:
            self.textline.setText(f"你没有事情可做吗")

app = QApplication(sys.argv)

buttonwindow = BUTTON()

buttonwindow.setStyleSheet("""
    QPushButton {
        font-size: 16px;
    }
    QLineEdit {
        font-size: 14px;
    }
""")

buttonwindow.show()

app.exec()