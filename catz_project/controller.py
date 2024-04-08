"""
Controller

This code gets facts from cat facts api and gives you a little image too

This code contains the following functions:
  * funct(var), description
  * command_input(str = "", process = 0), call for an input while 
    allowing EXIT whenever
"""

# Imports
import requests as re
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *

def api_call(endpoint: str) -> str:
    """
    Gets the api call 

    Args:
        endpoint (str): where to direct the api, in this case either fact or 
        breed, with facts as an unused and unsupported
    
    Return:
        results (str): the api return
    """
    domain = "https://catfact.ninja/"
    url = domain + endpoint
    response = re.get(url) 
    clean_api_response(response)
    if response.ok:
        results = response.text
    else:
        results = "Api failure"
    return results

def clean_api_response(response: str) -> str:
    """
    Cleans the api's response dumbly

    Args:
        response (str): the unfiltered response from the api
    
    Return:
        cleaned (str): a cleaned version with just the fact
    """
    cleaned = str(response)[9:]
    cleaned = cleaned.split("\"")[0]
    return cleaned

# Qt
class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cat Factz")

        self.text = "Welcome to Cat Factz!"

        # Create our Layouts
        layout_main = QVBoxLayout()

        # Title 
        lable_title = QLabel(" Cat Factz ")
        font = lable_title.font()
        font.setPointSize(30)
        lable_title.setFont(font)
        lable_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)
        layout_main.addWidget(lable_title)

        # Text
        lable_text = QLabel()
        layout_main.addWidget(lable_text)

        # Buttons
        layout_buttons = QHBoxLayout()

        button_fact = QPushButton("Fact")
        button_fact.setCheckable(True)
        button_fact.clicked.connect(self.new_fact)
        layout_buttons.addWidget(button_fact)

        button_breed = QPushButton("Breed")
        button_breed.setCheckable(True)
        button_breed.clicked.connect(self.new_breed)
        layout_buttons.addWidget(button_breed)

        # Add main
        layout_main.addLayout(layout_buttons)

        # Set the main layout
        gui = QWidget()
        gui.setLayout(layout_main)
        self.setCentralWidget(gui)

        # Display
        lable_text.setText(self.text)

    def new_fact(self):
        self.text = "fact"

    def new_breed(self):
        self.text = "breed"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = main_window()
    window.show()

    app.exec()