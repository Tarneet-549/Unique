import tkinter as tk
import random
import time

from PIL import ImageTk, Image






def main_menu():
    main_menu_frame.pack(fill="both", expand=True)

    welcome_label = tk.Label(main_menu_frame, text="Welcome to the Learning and Relaxation Game", font=("Arial", 16,"bold"),bg="blue")
    welcome_label.pack(pady=10)

    menu_label = tk.Label(main_menu_frame, text="Please select an activity:", font=("Arial", 12),bg="cyan")
    menu_label.pack(pady=5)

    activities = [
        ("Math Quiz", start_math_quiz),
        ("Memory Game", start_memory_game),
        ("Word Scramble", start_word_scramble),
        ("Number Sorting Game", start_number_sorting_game),
        ("Logic Puzzle", start_logic_puzzle),
        ("Relaxation Exercise", start_relaxation_exercise),
        ("Typing Challenge", start_typing_challenge),  # Added Typing Challenge
    ]

    for activity_name, activity_function in activities:
        button = tk.Button(main_menu_frame, text=activity_name, width=25,height=2,font=("Comic Sans MS",14,"bold") ,command=activity_function,bg="pink")
        button.pack(pady=5)


def start_typing_challenge():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "A stitch in time saves nine.",
        "Actions speak louder than words.",
        "The early bird catches the worm.",
        "Fortune favors the bold.",
        "Time and tide wait for none.",
        "When in Rome, do as the Romans do."
    ]

    def get_sentence():
        return random.choice(sentences)

    def start_challenge():
        nonlocal current_sentence, start_time
        current_sentence = get_sentence()
        sentence_label.config(text=f"Type this sentence: {current_sentence}")
        user_entry.delete(0, tk.END)
        start_time = time.time()
        result_label.config(text="")

    def check_sentence():
        user_input = user_entry.get().strip()
        elapsed_time = time.time() - start_time
        if user_input == current_sentence:
            result_label.config(text=f"Correct! Time taken: {elapsed_time:.2f} seconds", fg="green")
            root.after(1000, start_challenge)
        else:
            result_label.config(text="Incorrect. Try again.", fg="red")

    def back_to_menu():
        typing_challenge_frame.destroy()
        main_menu_frame.pack()

    main_menu_frame.pack_forget()
    typing_challenge_frame = tk.Frame(root)
    typing_challenge_frame.pack(fill="both", expand=True, pady=20)

    current_sentence = ""
    start_time = 0

    sentence_label = tk.Label(typing_challenge_frame, text="", font=("Arial", 14))
    sentence_label.pack(pady=10)

    user_entry = tk.Entry(typing_challenge_frame, font=("Arial", 20))
    user_entry.pack(pady=5)

    check_button = tk.Button(typing_challenge_frame, text="Check Sentence", command=check_sentence,font=("Arial",20,"bold"),bg="yellow" )
    check_button.pack(pady=5)

    result_label = tk.Label(typing_challenge_frame, text="", font=("Arial", 12))
    result_label.pack(pady=5)

    back_button = tk.Button(typing_challenge_frame, text="Back to Menu", command=back_to_menu, font=("Arial",20,"bold"),bg="pink")
    back_button.pack(pady=10)

    start_challenge()


def start_math_quiz():
    def generate_question():
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        question_text = f"{num1} {operation} {num2}"
        answer = str(eval(question_text))
        return question_text, answer

    def check_answer():
        user_answer = answer_input.get().strip()
        if user_answer == answer:
            result_label.config(text="Correct!", fg="green")
            update_score(1)
        else:
            result_label.config(text=f"Incorrect! The correct answer was {answer}.", fg="red")
        next_question()

    def next_question():
        nonlocal question, answer
        question, answer = generate_question()
        question_label.config(text=f"Solve: {question}")
        answer_input.delete(0, tk.END)

    def update_score(points):
        nonlocal score
        score += points
        score_label.config(text=f"Score: {score}")

    def back_to_menu():
        math_quiz_frame.destroy()
        main_menu_frame.pack()

    main_menu_frame.pack_forget()
    math_quiz_frame = tk.Frame(root)
    math_quiz_frame.pack(fill="both", expand=True, pady=20)

    score = 0
    question, answer = generate_question()

    question_label = tk.Label(math_quiz_frame, text=f"Solve: {question}", font=("Arial", 14))
    question_label.pack(pady=10)

    answer_input = tk.Entry(math_quiz_frame, font=("Arial", 12))
    answer_input.pack(pady=5)

    submit_button = tk.Button(math_quiz_frame, text="Submit Answer", command=check_answer,font=("Arial",20,"bold"),bg="cyan")
    submit_button.pack(pady=5)

    result_label = tk.Label(math_quiz_frame, text="", font=("Arial", 12))
    result_label.pack(pady=5)

    score_label = tk.Label(math_quiz_frame, text=f"Score: {score}", font=("Arial", 12))
    score_label.pack(pady=5)

    back_button = tk.Button(math_quiz_frame, text="Back to Menu", command=back_to_menu,font=("Arial",20,"bold"),bg="pink")
    back_button.pack(pady=10)


def start_memory_game():
    def generate_sequence(length):
        return [random.randint(0, 9) for _ in range(length)]

    def show_sequence():
        sequence = generate_sequence(sequence_length[0])
        sequence_label.config(text=" ".join(map(str, sequence)))
        root.after(2000, lambda: sequence_label.config(text="Enter the sequence:"))
        check_button.config(state="normal")
        return sequence

    def check_sequence():
        user_input = user_entry.get().strip().split()
        if user_input == list(map(str, sequence)):
            result_label.config(text="Correct!", fg="green")
            sequence_length[0] += 1
        else:
            result_label.config(text=f"Incorrect! The sequence was {' '.join(map(str, sequence))}", fg="red")
            sequence_length[0] = 3
        user_entry.delete(0, tk.END)
        root.after(2000, start_round)

    def start_round():
        nonlocal sequence
        result_label.config(text="")
        sequence = show_sequence()

    def back_to_menu():
        memory_game_frame.destroy()
        main_menu_frame.pack()

    main_menu_frame.pack_forget()
    memory_game_frame = tk.Frame(root)
    memory_game_frame.pack(fill="both", expand=True, pady=20)

    sequence_length = [3]
    sequence = []

    instruction_label = tk.Label(memory_game_frame, text="Memorize the sequence of numbers displayed.",
                                 font=("Arial", 12))
    instruction_label.pack(pady=10)

    sequence_label = tk.Label(memory_game_frame, text="", font=("Arial", 16))
    sequence_label.pack(pady=10)

    user_entry = tk.Entry(memory_game_frame, font=("Arial", 14))
    user_entry.pack(pady=5)

    check_button = tk.Button(memory_game_frame, text="Check Sequence", state="disabled", command=check_sequence,font=("Arial",20,"bold"),bg="orange")
    check_button.pack(pady=5)

    result_label = tk.Label(memory_game_frame, text="", font=("Arial", 12))
    result_label.pack(pady=5)

    back_button = tk.Button(memory_game_frame, text="Back to Menu", command=back_to_menu,font=("Arial",20,"bold"),bg="pink")
    back_button.pack(pady=10)

    start_round()


def start_word_scramble():
    # List of words with their scrambled versions and categories
    words = [
        {"word": "elephant", "scrambled": "nalehpte", "category": "Animal"},
        {"word": "giraffe", "scrambled": "raegiff", "category": "Animal"},
        {"word": "penguin", "scrambled": "gniepun", "category": "Animal"},
        {"word": "rose", "scrambled": "sreo", "category": "Flower"},
        {"word": "lily", "scrambled": "ylli", "category": "Flower"},
        {"word": "daisy", "scrambled": "ayisd", "category": "Flower"},
        {"word": "paris", "scrambled": "rispa", "category": "Place"},
        {"word": "london", "scrambled": "donlon", "category": "Place"},
        {"word": "tokyo", "scrambled": "oktoy", "category": "Place"},
        {"word": "orange", "scrambled": "rageon", "category": "Fruit"},
        {"word": "banana", "scrambled": "nanaab", "category": "Fruit"},
        {"word": "mango", "scrambled": "goman", "category": "Fruit"},
        {"word": "piano", "scrambled": "nopai", "category": "Object"},
        {"word": "laptop", "scrambled": "patlop", "category": "Object"},
        {"word": "bottle", "scrambled": "telbot", "category": "Object"},
        {"word": "school", "scrambled": "hcolso", "category": "Place"},
        {"word": "teacher", "scrambled": "rehcaet", "category": "Person"},
        {"word": "doctor", "scrambled": "tcrood", "category": "Person"},
        {"word": "zebra", "scrambled": "rabze", "category": "Animal"},
        {"word": "tiger", "scrambled": "giret", "category": "Animal"},
        {"word": "lion", "scrambled": "oinl", "category": "Animal"},
        {"word": "apple", "scrambled": "lpeap", "category": "Fruit"},
        {"word": "grape", "scrambled": "eprag", "category": "Fruit"},
        {"word": "pear", "scrambled": "arep", "category": "Fruit"},
        {"word": "new york", "scrambled": "kory enw", "category": "Place"},
        {"word": "sunflower", "scrambled": "werslonfu", "category": "Flower"},
        {"word": "cherry", "scrambled": "ehrryc", "category": "Fruit"},
        {"word": "rhinoceros", "scrambled": "cereosrhin", "category": "Animal"},
        {"word": "kangaroo", "scrambled": "roongaak", "category": "Animal"}
    ]

    def get_word():
        return random.choice(words)

    def show_hint():
        hint_label.config(text=f"Category: {current_word['category']}")

    def check_answer():
        user_answer = answer_input.get().strip().lower()
        if user_answer == current_word['word']:
            result_label.config(text="Correct!", fg="green")
            update_score(1)
        else:
            result_label.config(text=f"Incorrect! The correct word was '{current_word['word']}'.", fg="red")
        next_word()

    def next_word():
        nonlocal current_word
        current_word = get_word()
        word_label.config(text=f"Scrambled Word: {current_word['scrambled']}")
        answer_input.delete(0, tk.END)
        hint_label.config(text="")

    def update_score(points):
        nonlocal score
        score += points
        score_label.config(text=f"Score: {score}")

    def back_to_menu():
        word_scramble_frame.destroy()
        main_menu_frame.pack()

    main_menu_frame.pack_forget()
    word_scramble_frame = tk.Frame(root)
    word_scramble_frame.pack(fill="both", expand=True, pady=20)

    score = 0
    current_word = get_word()

    word_label = tk.Label(word_scramble_frame, text=f"Scrambled Word: {current_word['scrambled']}", font=("Arial", 14))
    word_label.pack(pady=10)

    answer_input = tk.Entry(word_scramble_frame, font=("Arial", 12))
    answer_input.pack(pady=5)

    hint_button = tk.Button(word_scramble_frame, text="Show Hint", command=show_hint)
    hint_button.pack(pady=5)

    hint_label = tk.Label(word_scramble_frame, text="", font=("Arial", 12))
    hint_label.pack(pady=5)

    submit_button = tk.Button(word_scramble_frame, text="Submit Answer", command=check_answer)
    submit_button.pack(pady=5)

    result_label = tk.Label(word_scramble_frame, text="", font=("Arial", 12))
    result_label.pack(pady=5)

    score_label = tk.Label(word_scramble_frame, text=f"Score: {score}", font=("Arial", 12))
    score_label.pack(pady=5)

    back_button = tk.Button(word_scramble_frame, text="Back to Menu", command=back_to_menu)
    back_button.pack(pady=10)

    next_word()


def start_number_sorting_game():
    def generate_numbers():
        return [random.randint(1, 99) for _ in range(5)]

    def check_answer():
        user_input = user_entry.get().strip().split()
        user_numbers = list(map(int, user_input))
        if user_numbers == sorted_numbers:
            result_label.config(text="Correct!", fg="green")
        else:
            result_label.config(text=f"Incorrect! The correct order is: {' '.join(map(str, sorted_numbers))}", fg="red")
        root.after(3000, start_round)

    def start_round():
        nonlocal numbers, sorted_numbers
        result_label.config(text="")
        numbers = generate_numbers()
        sorted_numbers = sorted(numbers)
        numbers_label.config(text=f"Sort these numbers: {' '.join(map(str, numbers))}")
        user_entry.delete(0, tk.END)

    def back_to_menu():
        number_sorting_frame.destroy()
        main_menu_frame.pack()

    main_menu_frame.pack_forget()
    number_sorting_frame = tk.Frame(root)
    number_sorting_frame.pack(fill="both", expand=True, pady=20)

    numbers = []
    sorted_numbers = []

    instruction_label = tk.Label(number_sorting_frame, text="Arrange the following numbers in ascending order.",
                                 font=("Arial", 12))
    instruction_label.pack(pady=10)

    numbers_label = tk.Label(number_sorting_frame, text="", font=("Arial", 14))
    numbers_label.pack(pady=10)

    user_entry = tk.Entry(number_sorting_frame, font=("Arial", 12))
    user_entry.pack(pady=5)

    check_button = tk.Button(number_sorting_frame, text="Check Answer", command=check_answer,font=("Arial",20,"bold"),bg="green")
    check_button.pack(pady=5)

    result_label = tk.Label(number_sorting_frame, text="", font=("Arial", 12))
    result_label.pack(pady=5)

    back_button = tk.Button(number_sorting_frame, text="Back to Menu", command=back_to_menu,font=("Arial",20,"bold"),bg="pink")
    back_button.pack(pady=10)

    start_round()


def start_logic_puzzle():
    # List of easy logic puzzles with their answers
    puzzles = [
        {"question": "What has to be broken before you can use it?", "answer": "egg",
         "hint": "It's something you eat in breakfast."},
        {"question": "What gets wetter as it dries?", "answer": "towel", "hint": "You use this after a bath."},
        {"question": "What has many keys but can't open a single door?", "answer": "keyboard",
         "hint": "You are probably using this to type right now."},
        {"question": "What has a thumb and four fingers but is not alive?", "answer": "glove",
         "hint": "You wear this on your hand."},
        {"question": "What can you catch but not throw?", "answer": "cold", "hint": "It often comes with a cough."},
        {"question": "What comes down but never goes up?", "answer": "rain",
         "hint": "It's wet and falls from the sky."},
        {"question": "What can travel around the world while staying in a corner?", "answer": "stamp",
         "hint": "You put this on a letter to send it."},
        {"question": "What has one eye but cannot see?", "answer": "needle", "hint": "It's used in sewing."},
        {"question": "What is full of holes but still holds water?", "answer": "sponge",
         "hint": "You use this in the kitchen or bathroom to clean."},
        {"question": "What can be cracked, made, told, and played?", "answer": "joke", "hint": "It makes you laugh."},
        {"question": "What has a head and a tail but no body?", "answer": "coin",
         "hint": "You flip this to make decisions."},
        {"question": "What has a bed but doesn't sleep?", "answer": "river", "hint": "It flows but doesn't sleep."},
        {"question": "What has hands but cannot clap?", "answer": "clock", "hint": "It tells you the time."},
        {"question": "What is so fragile that saying its name breaks it?", "answer": "silence",
         "hint": "It's golden and very fragile."},
        {"question": "What has a neck but no head?", "answer": "bottle", "hint": "You drink from this."},
        {"question": "What has a ring but no finger?", "answer": "telephone",
         "hint": "It rings but isn't worn on your hand."},
        {"question": "What is always in front of you but can’t be seen?", "answer": "future",
         "hint": "It’s something that hasn’t happened yet."},
        {"question": "What is black when it’s clean and white when it’s dirty?", "answer": "chalkboard",
         "hint": "It's used in classrooms by teachers."},
        {"question": "What has a face and two hands but no arms or legs?", "answer": "clock",
         "hint": "It shows the time."},
        {"question": "What can be touched but never held?", "answer": "shadow",
         "hint": "It follows you everywhere when there's light."},
        {"question": "What can fill a room but takes up no space?", "answer": "light",
         "hint": "It’s bright and makes the dark disappear."},
        {"question": "What is light as a feather, yet the strongest person can't hold it for long?", "answer": "breath",
         "hint": "You need it to live."},
        {"question": "What begins with T, ends with T, and has T in it?", "answer": "teapot",
         "hint": "You pour tea from it."},
        {"question": "What has teeth but cannot bite?", "answer": "comb", "hint": "You use it to style your hair."},
        {"question": "What can you keep after giving it to someone?", "answer": "your word",
         "hint": "It's a promise or commitment."},
        {"question": "What has keys but can't listen to the beauty it unlocks?", "answer": "piano",
         "hint": "You play music on this instrument."},
        {"question": "What has legs but doesn’t walk?", "answer": "table", "hint": "You place things on it."},
        {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
         "answer": "the letter M", "hint": "It's part of the alphabet."},
        {"question": "What can’t be seen but is always before you?", "answer": "the future",
         "hint": "It’s yet to come."},
        {"question": "What has a heart that doesn’t beat?", "answer": "artichoke", "hint": "It's a type of vegetable."},
        {"question": "What is tall when it’s young and short when it’s old?", "answer": "candle",
         "hint": "You light it and it melts down."}
    ]

    def get_puzzle():
        return random.choice(puzzles)

    def show_hint():
        hint_label.config(text=f"Hint: {current_puzzle['hint']}")

    def check_answer():
        user_answer = answer_input.get().strip().lower()
        if user_answer == current_puzzle['answer']:
            result_label.config(text="Correct!", fg="green")
            update_score(1)
        else:
            result_label.config(text=f"Incorrect! The correct answer was '{current_puzzle['answer']}'.", fg="red")
        next_puzzle()

    def next_puzzle():
        nonlocal current_puzzle
        current_puzzle = get_puzzle()
        question_label.config(text=f"Puzzle: {current_puzzle['question']}")
        answer_input.delete(0, tk.END)
        hint_label.config(text="")

    def update_score(points):
        nonlocal score
        score += points
        score_label.config(text=f"Score: {score}")

    def back_to_menu():
        logic_puzzle_frame.destroy()
        main_menu_frame.pack()

    main_menu_frame.pack_forget()
    logic_puzzle_frame = tk.Frame(root)
    logic_puzzle_frame.pack(fill="both", expand=True, pady=20)

    score = 0
    current_puzzle = get_puzzle()

    question_label = tk.Label(logic_puzzle_frame, text=f"Puzzle: {current_puzzle['question']}", font=("Arial", 14))
    question_label.pack(pady=10)

    answer_input = tk.Entry(logic_puzzle_frame, font=("Arial", 12))
    answer_input.pack(pady=5)

    hint_button = tk.Button(logic_puzzle_frame, text="Show Hint", command=show_hint,font=("Arial",20,"bold"),bg="blue")
    hint_button.pack(pady=5)

    hint_label = tk.Label(logic_puzzle_frame, text="", font=("Arial", 12))
    hint_label.pack(pady=5)

    submit_button = tk.Button(logic_puzzle_frame, text="Submit Answer", command=check_answer,font=("Arial",20,"bold"),bg="orange")
    submit_button.pack(pady=5)

    result_label = tk.Label(logic_puzzle_frame, text="", font=("Arial", 12))
    result_label.pack(pady=5)

    score_label = tk.Label(logic_puzzle_frame, text=f"Score: {score}", font=("Arial", 12))
    score_label.pack(pady=5)

    back_button = tk.Button(logic_puzzle_frame, text="Back to Menu", command=back_to_menu,font=("Arial",20,"bold"),bg="pink")
    back_button.pack(pady=10)

    next_puzzle()


def start_relaxation_exercise():
    def start_exercise():
        cycles = 3  # Number of times to repeat the exercise
        start_duration = 4  # Starting duration for the first cycle

        def perform_cycle(cycle_index, duration):
            if cycle_index < cycles:
                def countdown(step_name, time_left, next_step):
                    if time_left > 0:
                        exercise_label.config(text=f"{step_name}")
                        clock_label.config(text=f"Time Left: {time_left} seconds")
                        root.after(1000, countdown, step_name, time_left - 1, next_step)
                    else:
                        next_step()

                def next_breathe():
                    countdown("Breathe In", duration, next_hold)

                def next_hold():
                    countdown("Hold", duration, next_release)

                def next_release():
                    countdown("Release", duration, lambda: perform_cycle(cycle_index + 1, duration + 1))

                countdown("Breathe In", duration, next_breathe)
            else:
                exercise_label.config(text="Exercise completed. Feel relaxed!")
                clock_label.config(text="")

        perform_cycle(0, start_duration)

    def back_to_menu():
        relaxation_frame.destroy()
        main_menu_frame.pack()

    main_menu_frame.pack_forget()
    relaxation_frame = tk.Frame(root)
    relaxation_frame.pack(fill="both", expand=True, pady=20)

    exercise_label = tk.Label(relaxation_frame, text="", font=("Arial", 16))
    exercise_label.pack(pady=20)

    clock_label = tk.Label(relaxation_frame, text="", font=("Arial", 16))
    clock_label.pack(pady=10)

    start_button = tk.Button(relaxation_frame, text="Start Relaxation Exercise", command=start_exercise,font=("Arial",20,"bold"),bg="blue")
    start_button.pack(pady=10)

    back_button = tk.Button(relaxation_frame, text="Back to Menu", command=back_to_menu,font=("Arial",20,"bold"),bg="pink")
    back_button.pack(pady=10)


def hag_d():
    global root,main_menu_frame
    root = tk.Toplevel()
    root.title("Student Innovation Game")

    main_menu_frame = tk.Frame(root)
    main_menu_frame.pack(fill="both", expand=True)

    main_menu()

    root.mainloop()