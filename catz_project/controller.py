"""
Catz Controller

This code gets facts from cat facts api and displays it in a PyQt6 window

This code contains the following functions:
  * api_call(str), gets from the api
  * factify_response(str), converts api response to str
  * new_fact(), manages the Qt button
"""

# Imports
import requests as re
import sys
import time
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *

# Constants
title = """
 /'''\   /\  ''|''   .">'''''>
|       /__\   |     |  _  _ |
 \___/ /    \  |    / '~=_X_='

|''''  /\   /'''\ ''|'' ''''\\
|---  /__\ |        |   .---'
|    /    \ \___/   |   \____
"""

decor = """
  ,~,   |
{,(@),} |
   Y    |
  (~    |
   )    |
 ~{     |
   }    |
"""

introduce = """Welcome to Cat Factz!

To use, press \"Fact\" for a random cat fact, or press \"Breed\" for a random breed!

You can also search for a breed by typing in either the index number (0 to 97), or you can enter a cat breed's name! Press the breed button to search. Leave it blank or as \"Search\" for a random cat.
"""

# API
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
    if response.ok:
        results = response.text
    else:
        results = "Api failure"
    return results

def factify_response(response: str) -> str:
    """
    Cleans the api's response

    Args:
        response (str): the unfiltered response from the api
    
    Return:
        cleaned (str): a cleaned version with just the fact
    """
    cleaned = str(response)[9:]
    cleaned = cleaned.split("\"")[0]
    return cleaned

def breedify_response(response: str, search) -> str:
    """
    Cleans the api's response and turns it into a cat description

    Args:
        response (str): the unfiltered response from the api
    
    Return:
        (str): a cleaned version with just the breed
    """
    # This is execedingly inefficent, but i'm sick and tired and this is all i
    # can bring myself to do right now
    breeds = response[26:10585].split("},{")
    
    if search != "Search" and search != "":
        if (search.isnumeric() and int(search) < 98 and int(search) > -1)
            search = int(search)
            cat = breeds[search].split(",")

            # Console Debug
            print("\nCat = " + str(search))
            print(cat[0][9:(len(cat[0]) - 1)])
            print(breeds[search].split(","))

            return(madlib(cat, search))
        elif search in ["Donksoy", "Don Sphynx"]:
        
        else:    
            # See madlib comment for why this is like this
            if :
                
            elif search in ["Dwarf cat", "Dwelf"]:

            elif search == "Perfold":
                # This one is just because

            else:
                for i in range(len(breeds)):
                    search_cat = breeds[i].split(",")
                    searching = search_cat[0][9:(len(search_cat[0]) - 1)].lower()
                    if searching == search.lower():
                        cat = breeds[i].split(",")

                        # Console Debug
                        print("\nCat = " + str(i))
                        print(cat[0][9:(len(cat[0]) - 1)])

                        return(madlib(cat, i))
        return "This cat couldn't be found." 
    else:
        random = (round(time.time() * 1000) % 98)
        cat = breeds[random].split(",")

        # Console Debug
        print("\nCat = " + str(random))
        print(cat[0][9:(len(cat[0]) - 1)])
        print(breeds[random].split(","))

        return(madlib(cat, random))
    
def a_an(item: str) -> str:
    """
    Determines if an item should use a or an
    
    Args:
        item (str): the item
    
    Return:
        (str): a or an plus the item
    """
    if item[0] in ["a", "e", "i", "o", "u"]:
        return "an " + item
    else:
        return "a " + item
    
def check_unknown(feature: str) -> str:
    """
    Determines if a cat feature is blank, then replaces it with "unknown"
    
    Args:
        feature (str): the feature to check for
    
    Return:
        (str): either the feature, or "unknown"
    """
    if feature == "":
        return "unknown"
    else:
        return feature

def format_nationality(nationality: str) -> str:
    """
    Determines what intro to use given on where the cat's from
    
    Args:
        nationality (str): the nationality of a cat
    
    Return:
        (str): the nationality, plus a correct introduction
    """
    splited = nationality.split()
    if splited[0] in ["United", "Arabian",  ]:
        return "from the " + nationality
    elif splited[0] == "developed":
        return "that was " + nationality
    else:
        return "from " + nationality
    
def check_if_that_cat(name: str) -> str:
    """
    Checks if the cat in question is *that* one, specifically our good friend
    66 who has special unicode characters in its name
    
    Args:
        name (str): the name of a cat
    
    Return:
        (str): the name just without that special charcter
    """    
    if name[:7] == "PerFold":
        return name[:7] + name[13:]
    else:
        return name
    
def madlib(breed_list: list, id: int) -> str:
    """
    Converts a list of cat features into a sentance.

    Args:
        breed_list (str list): the features list in name, nation, origin, coat, 
                               order
    
    Return:
        lib (str): the list converted into a clean, human readable sentance
    """
    # this data is a nightmare to work with ok, i have finished ALL of the 
    # important logic and have just now realized that a few cats just fail 
    # because they have commas in their names, this is not what i want to do 
    # but i cannot bring myself to rewrite everything for two edge cases

    if id == 31:
        lib = ("The Donskoy, or Don Sphynx is a cat from Russia.\n\nThey are" 
               + " a unknown breed with a hairless coat and an unknown" +
               "pattern.")
    elif id == 33:
        lib = ("The Dwarf cat, or Dwelf is a cat from unknown.\n\nThey are a" + 
               " crossbreed breed with an unknown coat and a hairless pattern.")
    else:
        # also before you mark me down for this abomination of a function plz 
        # remember that it was WORSE than this before i did all the +=

        lib = "The " + check_if_that_cat(breed_list[0][9:(len(breed_list[0]) - 1)])
        lib += " is a cat " 
        lib += format_nationality(check_unknown(breed_list[1][11:(
                                len(breed_list[1]) - 1)])) 
        lib += "." 
        lib += "\n\nThey are "
        lib += a_an(check_unknown(breed_list[2][10:(
                    len(breed_list[2]) - 1)].lower())) 
        lib += " breed with " 
        lib += a_an(check_unknown(breed_list[3][8:(
                    len(breed_list[3]) - 1)].lower()))
        lib += " coat and " 
        lib += a_an(check_unknown(breed_list[4][11:(
                    len(breed_list[4]) - 1)].lower())) 
        lib += " pattern."

        # literally in the last commit (before i even added a ton of the word 
        # logic functions), this was a single line of code 410 characters long

    return lib

# Qt
class main_window(QMainWindow):
    """
    The class that makes the visual element of the program
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cat Factz")

        self.display_text = introduce

        # Create our Layouts
        layout_main = QVBoxLayout()

        # Title 
        label_title = QLabel(title)

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

        button_fact = QPushButton("Fact")
        button_fact.setFont(QFont("Courier"))
        button_fact.setCheckable(True)
        button_fact.clicked.connect(self.new_fact)
        layout_input.addWidget(button_fact)

        button_breed = QPushButton("Breed")
        button_breed.setFont(QFont("Courier"))
        button_breed.setCheckable(True)
        button_breed.clicked.connect(self.new_breed)
        layout_input.addWidget(button_breed)

        self.text_search = QLineEdit("Search")
        self.text_search.setFont(QFont("Courier"))
        self.text_search.setFixedWidth(100)
        layout_input.addWidget(self.text_search)

        label_decor = QLabel(decor)
        label_decor.setFont(QFont("Courier"))
        label_decor.setAlignment(Qt.AlignmentFlag.AlignRight | 
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

    def new_fact(self):
        """
        Gets a fact, processes it, and displays it
        """
        self.display_text = "Fact : " + factify_response(api_call("fact"))
        self.label_text.setText(self.display_text)

    def new_breed(self):
        """
        Gets a breed, processes it, and displays it
        """
        self.display_text = ("Cat : " + 
                             breedify_response(api_call("breeds?limit=98"), 
                             self.text_search.text()))
        self.label_text.setText(self.display_text)
 
if __name__ == "__main__":
    print(a_an("unkownhelp"))
    app = QApplication(sys.argv)

    window = main_window()
    window.show()

    app.exec()