#PROGRAM MEMORY QUIZ



# Lists to store usernames and passwords

uname_list = []
passwords_list = []

# register a new user
def register():
    print("Register a new account.")
    uname = input("Enter a username: ")
    password = input("Enter a password: ")
    
    
    # Add username and password to the lists
    uname_list.append(uname)
    passwords_list.append(password)
    
    print("Registration successful! You can now log in.")



#  log in with existing users
def login():
    print("Log in to your account.")
    uname = input("Enter your username: ")
    password = input("Enter your password: ")
    
    #username exists and the password matches
    if uname in uname_list:
        index = uname_list.index(uname)
        if passwords_list[index] == password:
            print("Login successful! Welcome,", uname)
            return True  # Successful login
        else:
            print("Incorrect password.")
            return False
    else:
        print("Username not found. Please register first.")
        return False


# Quiz questions##


dsa_ques = [
    {"question": "Which of the following is a linear data structure?", "options": ["A) Stack", "B) Tree", "C) Graph"], "correct_answer": "A"},
    {"question": "Which sorting algorithm has the best worst-case time complexity?", "options": ["A) Bubble Sort", "B) Merge Sort", "C) Selection Sort"], "correct_answer": "B"},
    {"question": "Which data structure uses LIFO (Last In First Out) order?", "options": ["A) Queue", "B) Stack", "C) Linked List"], "correct_answer": "B"},
    {"question": "Which of the following is a non-linear data structure?", "options": ["A) Array", "B) Linked List", "C) Tree"], "correct_answer": "C"},
    {"question": "In a BST, the left child of a node must be ____.","options": ["A) Greater than the node", "B) Less than the node", "C) Equal to the node"], "correct_answer": "B"}
]

dbms_ques = [
    {"question": "What is the primary key of a table used for?", "options": ["A) To uniquely identify each record", "B) To store data in the table", "C) To create a relationship between tables"], "correct_answer": "A"},
    {"question": "What does SQL stand for?", "options": ["A) Structured Query Language", "B) Simple Query Language", "C) Standard Query Language"], "correct_answer": "A"},
    {"question": "In a relational database, a table is also called a:", "options": ["A) Relation", "B) Query", "C) Attribute"], "correct_answer": "A"},
    {"question": "Which of the following is not a type of JOIN in SQL?", "options": ["A) INNER JOIN", "B) LEFT JOIN", "C) RIGHT JOIN", "D) LINK JOIN"], "correct_answer": "D"},
    {"question": "Which of the following prevents record duplication in a table?", "options": ["A) FOREIGN KEY", "B) UNIQUE constraint", "C) CHECK constraint"], "correct_answer": "B"}
]

python_ques = [
    {"question": "Which of these data types is immutable in Python?", "options": ["A) List", "B) Dictionary", "C) Tuple"], "correct_answer": "C"},
    {"question": "What is the output of this code: print(3 * 2 + 1)?", "options": ["A) 7", "B) 8", "C) 6"], "correct_answer": "A"},
    {"question": "How do you define a function in Python?", "options": ["A) def function_name():", "B) function function_name():", "C) function_name def():"], "correct_answer": "A"},
    {"question": "How to create an empty list in Python?", "options": ["A) []", "B) {}", "C) ()"], "correct_answer": "A"},
    {"question": "How to access the first element of a list?", "options": ["A) list[1]", "B) list(1)", "C) list[0]"], "correct_answer": "C"}
]

# Function to take a quiz

def take_quiz():
    print("\nChoose a quiz category:")
    print("1. DSA")
    print("2. DBMS")
    print("3. Python")
    
    chh = input("Enter your choice: ")
    if chh == '1':
        ques = dsa_ques
    elif chh == '2':
        ques = dbms_ques
    elif chh == '3':
        ques = python_ques
    else:
        print("Invalid choice. Exiting the quiz.")
        return
    
    score = 0

    # Loop through the quiz questions
    for q in ques:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().upper()
        
        if answer == q["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {q['correct_answer']}\n")
    
    print(f"You scored {score} out of {len(ques)}.")

# Main function TO COMBINE ALL FUNCTIONS


def main():
    while True:
        print("\nWelcome to the system!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        chh = input("Choose an option (1/2/3): ")
        
        if chh == '1':
            register()
        elif chh == '2':
            if login():  # Proceed only if login is successful
                take_quiz()  # Start the quiz after successful login
        elif chh == '3':
            print("Thank you")
            break
        else:
            print("Invalid choice, please try again.")


main()
