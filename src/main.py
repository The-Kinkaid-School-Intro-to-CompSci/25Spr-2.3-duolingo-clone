import flet as ft
import random
import functools


global page_global

# Colors - No Need to Edit
Duolingo_Colors = {
    "FEATHER_GREEN": "#58cc02",
    "SNOW": "#FFFFFF",
    "EEL": "#4B4B4B",
    "HARE": "#AFAFAF",
    "CARDINAL": "#FF4B4B"
}


global word_chosen, target_language
word_chosen = "____"
target_language = "Portuguese"
# exercise type 1 data
# eng to portuguese dictionary
data_ex_1 = {
    "horse": "cavalo",
    "bat": "morcego",
    "monkey": "macaco",
    "mouse": "rato",
    "squirrel": "esquilo",
    "spider": "aranha",
    "frog": "sapo"
}

# exercise type 2 data
# dictionary of matching pairs
data_ex_2 = {
    "mãe": "mother",
    "pai": "father",
    "irmão": "brother",
    "irmã": "sister",
    "filho": "son",
    "filha": "daughter",
}

# global variables for Type 2 exercise
global buttons_clicked, first_choice, second_choice

buttons_clicked = 0
first_choice = ""
second_choice = ""

num_correct = None

def clear_the_page():
    global page_global
    page_global.controls.clear()
    page_global.update()



def check_answer_ex_2():
    global first_choice, second_choice, num_correct, page_global

    # Step 11
    # choice_that_is_a_key and choice_that_is_a_value will change depending on which choice is in the dictionary

    # Use key to index into the dictionary and get the 'correct_choice'

    # check if the 'correct_choice' matches the value
        # if so, update the number that are correct (referring to num_correct.data)

    # Step 12
    #  if the number that are correct is equal to the number of matching pairs
        # show a snackbar that says so, copying from exercise 1



def exercise_2_callback(event, button_itself):
    global buttons_clicked, first_choice, second_choice
    # Step 10. 
    # if no buttons have been clicked
        # increase the number of buttons clicked
        # save the first choice (button_itself.text)
        # change the button's color to a lighter grey ("HARE")
    # otherwise, if one button has been clicked
        # save the second choice (like first_choice)
        # check for the answer (a function call)
        # change the button's color to a lighter grey ("HARE")
        # reset num_selections back to 0




def make_col_of_buttons_of_list(list_of_words):
    buttons_to_return = []
    for word in list_of_words:
        word_button = ft.Button(
            text=word,
            bgcolor=Duolingo_Colors["EEL"],
            color=Duolingo_Colors["SNOW"], 
            
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=20),
                padding=15
            ),
        )
        word_button.on_click = functools.partial(
            exercise_2_callback, 
            word=word, 
            button_itself=word_button
        )
        buttons_to_return.append(word_button)
    return buttons_to_return


def exercise_type_2(e):
    global page_global, num_correct
    clear_the_page()
    # Step 7. get the data and shuffle the keys and values (in separate lists)



    target_language_buttons = []
    # Step 8. Make the target language buttons
   
   
    column1 = ft.Column(controls=target_language_buttons, alignment=ft.MainAxisAlignment.START)

    known_language_buttons = []
    #Step 9. Make the known language buttons


    column2 = ft.Column(controls=known_language_buttons, alignment=ft.MainAxisAlignment.START)


    
    # starting to add to the page (No need to edit below)
    # Main thing to add
    page_global.add(
        ft.Text("Match the pairs below",  
                color=Duolingo_Colors["EEL"], 
                size=40
        )
    )
    # The number that are correct (Do Not Edit)
    num_correct = ft.Text(
        value =f"Number Correct: 0", 
        data=0, 
        size=20, 
        color=Duolingo_Colors["EEL"]
    )
    page_global.add(num_correct)

    # The columns of buttons -- DO NOT EDIT
    row = ft.Row(
        controls=[column1, column2],  
        alignment=ft.MainAxisAlignment.CENTER
    )
    page_global.add(row)


def exercise1_callback(event, word_of_button):
    global page_global
    print(word_of_button)
    text_to_display = "Feedback on the answer"
    # Check the word against the dictionary for the right answer

    text_item = ft.Text(text_to_display, size=20)
    snackbar = ft.SnackBar(
        text_item, 
        action="Next Question", 
        action_color=Duolingo_Colors["FEATHER_GREEN"],
        on_action=exercise_type_2
    )
    page_global.open(snackbar)
    

def exercise_type_1():
    global page_global, target_language, word_chosen
    # Step 2. 
    # get the keys of the data; convert them to a list

    # get the values of the data; convert them to a list

    # Step 3A. get a random word (word_chosen) from the list of keys

    # Step 3B. Save the right answer
    
    

    # Step 3C. Make a list of options, include the right answer

    # Step 3D. Pick two more options    
    



    option_buttons = []
    # Step 4A. Create option buttons for each of the options
    








    # adding the widgets to the page -- Do not the function below this line
    question_text = ft.Text(
        value=f"How do you say {word_chosen} in {target_language}?", 
        size=50,
        color=Duolingo_Colors["EEL"]
    )

    page_global.add(question_text)

    # Step 4B. Make a column, passing the option_buttons as the controls



    # Step 4B. Add the column to the page
    


def example_callback(event, word_of_button):
    print("This button was clicked")
    print(f"This button's word is {word_of_button}")

def start_game(e):
    clear_the_page()
    exercise_type_1()


def list_examples():
    words = ["monkey", "bull", "horse"]
    # Example on getting a random choice
    random_choice = random.choice(words)
    print(random_choice)

    # initializing a list options with only one variable inside it
    some_variable = "cow"
    options = [some_variable]

    some_other_variable = "horse"
    options.append(some_other_variable)
    print(options) # Prints: ["cow", "horse"]

    # shuffling a list
    random.shuffle(words) # this actually changes the ordering randomly

def dictionary_examples():
    # example on dictionary and how to get keys/values
    my_example_dict = {
        "monkey": "macaco",
        "bull": "touro",
        "horse": "cavalo",
        "butterfly": "borboleta"
    }
    my_chosen_word = "monkey"
    translation_of_monkey = my_example_dict[my_chosen_word]

    print(translation_of_monkey) # Prints: "macaco"


    # checking if a key is in the dictionary
    if my_chosen_word in my_example_dict:
        print("Yes, the word is in the dict")

    # getting the eng words, aka the keys, aka the left side in the pair
    my_dict_keys = list(my_example_dict.keys())
    print(my_dict_keys) # Prints: ["monkey", "bull", "horse"]

    # getting the portuguese words, aka the values, aka the right side,
    my_dict_values = list(my_example_dict.values())
    print(my_dict_values) # Prints: ["macaco", "touro", "cavalo"]

def example():
    global page_global


    # Example on how to create buttons 
    options = ["monkey", "cow", "horse", "butterfly"]

    word_buttons = []
    for curr_word in options:
        word_button = ft.ElevatedButton(
            text=curr_word,
            bgcolor=Duolingo_Colors["FEATHER_GREEN"],
            color=Duolingo_Colors["SNOW"], 
            on_click = functools.partial(
                example_callback, 
                word_of_button=curr_word, # bind the curr_word to the callback
            ),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=40),
                padding=15
            ),
        )
        # adding to the list
        word_buttons.append(word_button)
    # adding the list to a column
    my_example_column = ft.Column(
        controls=word_buttons,
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )

    example_text = ft.Text("Example buttons to try out", size=40, color=Duolingo_Colors["EEL"])

    clear_btn = ft.ElevatedButton(
        text="Clear & Start",
        bgcolor=Duolingo_Colors["CARDINAL"],
        color=Duolingo_Colors["SNOW"], 
        on_click = start_game,
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=40),
            padding=15
        ),
    )

    page_global.add(example_text)
    page_global.add(my_example_column)
    page_global.add(clear_btn)



def main(page: ft.Page):
    global page_global
    page_global = page
    page.title = "Duolingo Clone"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme_seed=Duolingo_Colors["FEATHER_GREEN"]) 
    page.bgcolor = Duolingo_Colors["SNOW"]
    page.update()

    example()
    # If you want to just get started,comment example above and 
    # uncomment the line below

    # exercise_type_1()


ft.app(main)
