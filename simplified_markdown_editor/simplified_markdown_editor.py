"""Markdown Editor"""


def help_option():
    """DISPLAYS ON THE SCREEN ALL AVAILABLE COMMANDS OF THIS PROGRAM"""
    print('Available formatters: "plain" "bold" "italic" "header" "link" "inline-code" "ordered-list" '
          '"unordered-list" "new-line" \nSpecial commands: "!help" "!done"')


def plain_option(text_all: str) -> str:
   """
       FUNCTION TO INPUT REGULAR TEXT WITHOUT FORMATTING
       Parameters:
       -------
           text_all (str): String.
       Returns:
       -------
           text_all (str): String.
   """
   plain_text = input("Text:")
   print(plain_text)
   text_all += plain_text
   return text_all + "\n"


def bold_option(text_all: str) -> str:
    """
        BOLD TEXT FUNCTION
        Parameters:
        -------
            text_all (str): String.
        Returns:
        -------
            text_all (str): String.
    """
    user_text = input("Text:")
    bold_text = "**" + user_text + "**"
    print(bold_text)
    text_all += bold_text
    return text_all + "\n"


def italic_option(text_all: str) -> str:
    """
        FUNCTION FOR ITALIC TEXT ENTRY
        Parameters:
        -------
            text_all (str): String.
        Returns:
        -------
            text_all (str): String.
    """
    user_text = input("Text:")
    italic_text = "*" + user_text + "*"
    print(italic_text)
    text_all += italic_text
    return text_all + "\n"


def inline_code_option(text_all: str) -> str:
    """
        FUNCTION FOR ENTERING BUILT-IN CODE AS TEXT
        Parameters:
        -------
            text_all (str): String.
        Returns:
        -------
            text_all (str): String.
    """
    user_text = input("Text:")
    code_text = f"`{user_text}`"
    print(code_text)
    text_all += code_text
    return text_all + "\n"


def link_option(text_all: str) -> str:
    """
        FUNCTION TO ENTER THE LINK AND THE SUBJECT OF THIS LINK
        Parameters:
        -------
            text_all (str): String.
        Returns:
        -------
            text_all (str): String.
    """
    user_title = input("Title:")
    user_link = input("URL:")
    link_text = "[" + user_title + "](" + user_link + ")"
    print(link_text)
    text_all += link_text
    return text_all + "\n"


def header_option(text_all: str) -> str:
    """
        FUNCTION TO ENTER TITLE WITH LEVEL 1 TO 6
        Parameters:
        -------
            text_all (str): String.
        Returns:
        -------
            text_all (str): String.
    """
    while True:
        level = input("Level:")
        try:
            level = int(level)
        except ValueError:
            print("Inputted level should be numeric")
            continue
        if 1 < level > 6:
            print("The level should be within the range of 1 to 6")
        else:
            user_text = input("Text:")
            header_text = level * "#" + " " + user_text
            print(header_text)
            text_all += header_text
            return text_all + "\n"


def unordered_list_option(text_all: str) -> str:
    """
        FUNCTION FOR CREATING A UNORDERED LIST WITH DATA WHICH ENTERS THE USER
        Parameters:
        -------
            text_all (str): String.
        Returns:
        -------
            text_all (str): String.
    """
    while True:
        users_rows = input("Number of rows:")
        try:
            users_rows = int(users_rows)
        except ValueError:
            print("Inputted level should be numeric")
            continue
        if users_rows in range(1, 100):
            row_text = ""
            for index in range(users_rows):
                row_text += "- " + input(f"Row #{index + 1}:") + "\n"
            print(row_text)
            text_all += row_text
            return text_all + "\n"
        print("The number of rows should be greater than zero")


def ordered_list_option(text_all: str) -> str:
    """
        FUNCTION FOR CREATING AN ORDERED LIST WITH DATA WHICH ENTERS THE USER
        Parameters:
        -------
            text_all (str): String.
        Returns:
        -------
            text_all (str): String.
    """
    while True:
        users_rows = input("Number of rows:")
        try:
            users_rows = int(users_rows)
        except ValueError:
            print("Inputted level should be numeric")
            continue
        if users_rows in range(1, 100):
            row_text = ""
            for index in range(users_rows):
                row_text += str(index + 1) + ". " + input(f"Row #{index + 1}:") + "\n"
            print(row_text)
            text_all += row_text
            return text_all + "\n"
        print("The number of rows should be greater than zero")


def new_line_option(text_all: str) -> str:
    """
        FUNCTION FOR JAVING TO A NEW LINE
        Parameters:
        -------
            text_all (str): String.
        Returns:
        -------
            text_all (str): String.
    """
    new_line = "\n"
    text_all += new_line
    return text_all


def write_file(text_all: str) -> None:
    """
        FUNCTION FOR SAVING THE ENTERED DATA OF THE USER IN A SEPARATE MD FILE
        Parameters:
        -------
            text_all (str): String.
        -------
        THIS FUNCTION DOES NOT RETURN ANYTHING
    """
    with open("output.md", 'w', encoding='utf-8') as file:
        file.write(text_all)


text = ""  # VARIABLE THAT STORES RETURN DATA FROM FUNCTIONS

# PROGRAM MENU
if __name__ == '__main__':
    while True:
        option = str(input('Choose a formatter:'))
        if option == "!help":
            help_option()
        elif option == "plain":
            text = plain_option(text)
        elif option == "bold":
            text = bold_option(text)
        elif option == "italic":
            text = italic_option(text)
        elif option == "inline-code":
            text = inline_code_option(text)
        elif option == "link":
            text = link_option(text)
        elif option == "header":
            text = header_option(text)
        elif option == "unordered-list":
            text = unordered_list_option(text)
        elif option == "ordered-list":
            text = ordered_list_option(text)
        elif option == "new-line":
            text = new_line_option(text)
        elif option == "!done":
            write_file(text)
            print('Thanks message before exiting')
            exit()
        else:
            print('Unknown formatting type or command')
