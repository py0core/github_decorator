from modules import html_deco, write_file

# questions list
q_list: tuple = ("Please insert link for main img: ", "Full Name: ",
                 "Sub Title: ", "LinkedIn Link: ", "GitHub Username: ")

if __name__ == "__main__":
    # empty list to store user input
    a: list = []
    # loop in range of max args in function get_input from html_deco
    for q in range(html_deco.get_input.__code__.co_argcount):
        # ask for input give q_list where index == q and store answer in the list
        a.append(input(q_list[q]))
    # call write_file while getting return from get_input
    try:
        write_file.write_file(html_deco.get_input(*a))
        print("README.md was created!")
    except:
        print("Something went wrong, please try again.")
