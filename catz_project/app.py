"""
Cat Factz App

This is the App for Cat Factz, it runs the window and pyqt aspects of the code, 
while leaving the processing to controller

This code contains the following functions:
  * random_color(), provides the window with a random color
  * new_fact(), starts up the fact logic and displays it when done
  * new_breed(), starts up the breed logic, looks at search, and displays it
                 when finished
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *
import time
import controller
import sys

# Qt
class main_window(QMainWindow):
    """
    The class that makes the visual pyqt6 elements of the program
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cat Factz")

        self.display_text = controller.introduce

        # Create our Layouts
        layout_main = QVBoxLayout()

        # Title 
        label_title = QLabel(controller.title)

        label_title.setFont(QFont("Courier"))
        label_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)
        layout_main.addWidget(label_title)

        # Content
        layout_content = QHBoxLayout()

        # Text
        self.label_text = QLabel()
        self.label_text.setFont(QFont("Courier"))
        layout_content.addWidget(self.label_text)

        # Input
        layout_input = QVBoxLayout()

        # Fact
        button_fact = QPushButton("Fact")
        button_fact.setFont(QFont("Courier"))
        button_fact.setCheckable(False)
        button_fact.clicked.connect(self.new_fact)
        layout_input.addWidget(button_fact)

        # Line Edit
        self.text_search = QLineEdit("Search")
        self.text_search.setFont(QFont("Courier"))
        layout_input.addWidget(self.text_search)

        # Enter
        button_breed = QPushButton("Enter")
        button_breed.setFont(QFont("Courier"))
        button_breed.setCheckable(False)
        button_breed.clicked.connect(self.new_breed)
        layout_input.addWidget(button_breed)

        # Decor
        label_decor = QLabel(controller.decor)
        label_decor.setFont(QFont("Courier"))
        label_decor.setAlignment(Qt.AlignmentFlag.AlignLeft | 
                                 Qt.AlignmentFlag.AlignBottom)
        layout_input.addWidget(label_decor)

        # Add main
        layout_content.addLayout(layout_input)
        layout_main.addLayout(layout_content)

        # Set the main layout
        gui = QWidget()
        gui.setLayout(layout_main)
        self.setCentralWidget(gui)
        
        # Display
        self.label_text.setText(self.display_text)
        self.label_text.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label_text.setWordWrap(True)
        self.label_text.setMargin(1)

    def random_color() -> str:
        """
        Provides a random color for the program

        Return:
            color (str): the color to use
        """
        color = ["red", "orange", "yellow", "lime", "cyan", "pink", "white"]
        random = (round(time.time() * 1000) % 6)
        return color[random]

    def new_fact(self):
        """
        Gets a fact, processes it, and displays it
        """
        self.display_text = ("Fact : " + controller.factify_response(
                             controller.api_call("fact")))
        self.label_text.setText(self.display_text)

    def new_breed(self):
        """
        Gets a breed, processes it, and displays it
        """
        self.display_text = (controller.breedify_response(
                             controller.api_call("breeds?limit=98"), 
                             self.text_search.text()))
        self.label_text.setText(self.display_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.setStyleSheet("background-color: black;" +
                         "border: 1px solid " + 
                         main_window.random_color() + ";" +
                         "color: " + main_window.random_color() + ";")
    window.show()
    app.exec()