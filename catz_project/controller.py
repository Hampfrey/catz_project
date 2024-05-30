"""
Catz Controller

This is the controller for the Cat Factz app, it runs all of the API and text processing

This code contains the following functions:
  * api_call(str), requests info from the api
  * factify_response(response), trims a fact into something displayable
  * breedify_response(response), processes the breed list for madlib
  * madlib(str list, int), converts a list of cat features into the cat
  * format(str), a merger of check_unknown() and slashes()
  * check_unknown(str), converts blank strings into "unknown"
  * slashes(str), removes backslashes from strings
  * a_an(str), figures out if a str should use a or an and adds it
  * format_nationality(str), figures out how to segway into the nationality
  * check_if_that_cat(str), removes special characters from the cat with them
"""

# Imports
import requests as re
import time

# Texts
title = """
 /'''\   /\  ''|''   .">'''''>
|       /__\   |     |  _  _ |
 \___/ /    \  |    / '~=_X_='

|''''  /\   /'''\ ''|'' ''''\\
|---  /__\ |        |   .---'
|    /    \ \___/   |   \____
"""

decor = """
                .-''\/''=-_
               /          /
      . ' ' ' |/.   _  _  | 
    .             "=__x_.'
    '               ---_ 
 .--|          ]'''''-___)
/ -  '.         \\
\  ---  "--""'\__)    Cat Factz
  "''''''
"""

introduce = """Welcome to Cat Factz!

To use, press \"Fact\" for a random 
cat fact, or press \"Enter\" with
\"Search\" or nothing as the query 
for a random breed!

To search for a breed by type in 
either the index number (0 to 97), 
or you can enter a cat breed's 
name! Press \"Enter\" to search

Enter \"Intro\", if you'd like to 
refrence this :3
"""

# API
def api_call(endpoint: str) -> str:
    """
    Gets the api call 

    Args:
        endpoint (str): where to direct the api, in this case either fact or 
                        breeds?limit=98
    
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
        if (search.isnumeric() and int(search) < 98 and int(search) > -1):
            search = int(search)
            cat = breeds[search].split(",")

            # Console Debug
            print("\nCat = " + str(search))
            print(cat[0][9:(len(cat[0]) - 1)])

            return(madlib(cat, search))
        else:    
            # See madlib comment for why these are here
            if search.lower() in ["donksoy", "don sphynx"]:
                return(madlib("woo", 31))
            elif search.lower() in ["dwarf cat", "dwelf"]:
                return(madlib("woo", 33))
            elif search.lower() in ["kurilian bobtail", 
                                    "kuril islands bobtail"]:
                return(madlib("woo", 49))
            elif search.lower() == "perfold":
                # This one is just because
                cat = breeds[66].split(",")
                return(madlib(cat, 66))
            elif search.lower() == "intro":
                return introduce
            else:
                for i in range(len(breeds)):
                    search_cat = breeds[i].split(",")
                    searching = search_cat[0][9:(len(search_cat[0]) - 1
                                                 )].lower()
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

        return(madlib(cat, random))
    
def madlib(breed_list: list, id: int) -> str:
    """
    Converts a list of cat features into a sentance.

    Args:
        breed_list (str list): the features list in name, nation, origin, coat, 
                               order
        id (int): the id of the inputted cat, this is so that the madlib can    
                  easily take over if one of the broken cats gets inputted

    Return:
        lib (str): the list converted into a clean, human readable sentance
    """
    # this data is a nightmare to work with ok, i have finished ALL of the 
    # important logic and have just now realized that a few cats just fail 
    # because they have commas in their names, this is not what i want to do 
    # but i cannot bring myself to rewrite everything for two (now three) edge 
    # cases

    if id == 0:
        # for some reason cat 0 has just decided that it wants an extra " in it
        # and even though i think i know how to fix it, i can just put it here
        lib = ("Cat : The Abyssian is a cat from Ethiopia.\n\nThey " 
               + "are a natural/standard breed with a short coat and a ticked" +
               "pattern.")

    elif id == 31:
        lib = ("Cat : The Donskoy, or Don Sphynx is a cat from Russia.\n\nThey" 
               + " are an unknown breed with a hairless coat and an unknown" +
               " pattern.")
    elif id == 33:
        lib = ("Cat : The Dwarf cat, or Dwelf is a cat from unknown.\n\nThey" 
               + "are a crossbreed breed with an unknown coat and a hairless" + 
               " pattern.")
    elif id == 49:
        lib = ("Cat : The Kurilian Bobtail, or Kuril Islands Bobtail is a cat"  
               + "from Eastern Russia/Japan.\n\nThey are a natural breed " +
               "with an short/long coat and an unknown pattern.")
    else:
        # also before you mark me down for this abomination of a function plz 
        # remember that it was WORSE than this before i did all the +=

        lib = "Cat : The " + check_if_that_cat(breed_list[0][9:(
                                         len(breed_list[0]) - 1)])
        lib += " is a cat " 
        lib += format_nationality(format(breed_list[1][11:(
                                len(breed_list[1]) - 1)])) 
        lib += "." 
        lib += "\n\nThey are "
        lib += a_an(format(breed_list[2][10:(len(breed_list[2]) - 1)].lower())) 
        lib += " breed with " 
        lib += a_an(format(breed_list[3][8:(len(breed_list[3]) - 1)].lower()))
        lib += " coat and " 
        lib += a_an(format(breed_list[4][11:(len(breed_list[4]) - 1)].lower())) 
        lib += " pattern."

        # literally in the last commit (before i even added a ton of the word 
        # logic functions), this was a single line of code 410 characters long
    return lib

def format(item: str) -> str:
    """
    Trys to improve the madlib function by reducing repetition
    
    Args:
        item (str): the item
    
    Return:
        (str): the item after being run through check_unknown and slashes
    """
    return slashes(check_unknown(item))

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

def slashes(item: str) -> str:
    """
    Finds unwanted slash characters and removes them
    
    Args:
        item (str): the item
    
    Return:
        (str): the item without the unwanted slashes
    """    
    slashless = ""
    for i in item:
        if i != "\\":
            slashless += i
    return slashless

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
    66 who has special unicode characters in its name, then removes those 
    special characters
    
    Args:
        name (str): the name of a cat
    
    Return:
        (str): the name just without that special charcter
    """    
    if name[:7] == "PerFold":
        return name[:7] + name[13:]
    else:
        return name
 
