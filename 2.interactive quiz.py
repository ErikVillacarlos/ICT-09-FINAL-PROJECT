
import random

# Quiz data structure: list of tuples containing (question, options, correct_answer)
quiz_questions = [
    ("What is the capital of France?", ["A. London", "B. Paris", "C. Rome", "D. Madrid"], "B"),
    ("Who wrote 'Hamlet'?", ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Leo Tolstoy"], "A"),
    ("Which planet is known as the Red Planet?", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "B"),
    
    ("What is the capital of France?", ["A. London", "B. Paris", "C. Rome", "D. Madrid"], "B"),
    ("Who wrote 'Hamlet'?", ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Leo Tolstoy"], "A"),
    ("Which planet is known as the Red Planet?", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "B"),
    ("What is the largest ocean on Earth?", ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"], "C"),
    ("What is the capital of Australia?", ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"], "C"),
    ("Who painted the Mona Lisa?", ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"], "C"),
    ("Which country won the FIFA World Cup in 2018?", ["A. Germany", "B. Brazil", "C. France", "D. Argentina"], "C"),
    ("Which element has the chemical symbol 'H'?", ["A. Hydrogen", "B. Helium", "C. Carbon", "D. Gold"], "A"),
    ("What is the powerhouse of the cell?", ["A. Nucleus", "B. Ribosome", "C. Mitochondrion", "D. Golgi Apparatus"], "C"),
    ("Who is credited with discovering gravity after seeing an apple fall from a tree?", ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"], "A"),
        ("What is the powerhouse of the cell?", ["A. Nucleus", "B. Ribosome", "C. Mitochondrion", "D. Golgi Apparatus"], "C"),
    ("Who is credited with discovering gravity after seeing an apple fall from a tree?", ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"], "A"),
    ("What is the national animal of China?", ["A. Panda", "B. Dragon", "C. Tiger", "D. Elephant"], "A"),
    ("Which planet is closest to the Sun?", ["A. Venus", "B. Earth", "C. Mercury", "D. Mars"], "C"),
    ("Which artist painted the famous painting 'Starry Night'?", ["A. Claude Monet", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Leonardo da Vinci"], "B"),
    ("What is the longest river in the world?", ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"], "A"),
    ("Who wrote 'Pride and Prejudice'?", ["A. Jane Austen", "B. Emily Brontë", "C. Charlotte Brontë", "D. George Eliot"], "A"),
    ("Which mammal can fly?", ["A. Bat", "B. Rat", "C. Rabbit", "D. Squirrel"], "A"),
    ("What year did the Titanic sink?", ["A. 1912", "B. 1905", "C. 1920", "D. 1898"], "A"),
    ("Who invented the telephone?", ["A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Isaac Newton"], "A"),
    ("What is the chemical symbol for gold?", ["A. Au", "B. Ag", "C. Fe", "D. Hg"], "A"),
    ("Who wrote '1984'?", ["A. George Orwell", "B. Aldous Huxley", "C. J.R.R. Tolkien", "D. H.G. Wells"], "A"),
    ("Which country is known as the Land of the Rising Sun?", ["A. China", "B. Japan", "C. South Korea", "D. Thailand"], "B"),
    ("Who painted 'The Last Supper'?", ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo"], "B"),
    ("What is the largest organ in the human body?", ["A. Liver", "B. Brain", "C. Skin", "D. Heart"], "C"),
    ("Which gas do plants absorb from the atmosphere?", ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "C"),
    ("What is the largest animal on Earth?", ["A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Crocodile"], "A"),
    ("Who wrote 'To Kill a Mockingbird'?", ["A. Mark Twain", "B. Harper Lee", "C. F. Scott Fitzgerald", "D. Ernest Hemingway"], "B"),
    ("Which country is famous for the Great Wall?", ["A. India", "B. China", "C. Egypt", "D. Italy"], "B"),
    ("Who was the first man to step on the moon?", ["A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. Alan Shepard"], "A"),
    ("What is the largest desert in the world?", ["A. Sahara Desert", "B. Gobi Desert", "C. Arabian Desert", "D. Kalahari Desert"], "A"),
    ("Which is the largest continent by land area?", ["A. Africa", "B. Asia", "C. North America", "D. Europe"], "B"),
    ("Who is known as the 'Father of Computers'?", ["A. Alan Turing", "B. Charles Babbage", "C. Steve Jobs", "D. Bill Gates"], "B"),
    ("What is the chemical symbol for water?", ["A. Wo", "B. Wt", "C. H2O", "D. Ag"], "C"),
    ("What is the tallest mountain in the world?", ["A. Mount Everest", "B. K2", "C. Kilimanjaro", "D. Mount Fuji"], "A"),
    ("Who is the author of 'The Catcher in the Rye'?", ["A. J.D. Salinger", "B. F. Scott Fitzgerald", "C. Ernest Hemingway", "D. Mark Twain"], "A"),
    ("Which city is known as the 'Eternal City'?", ["A. Athens", "B. Rome", "C. Paris", "D. London"], "B"),
    ("Which animal is known as the 'Ship of the Desert'?", ["A. Camel", "B. Horse", "C. Elephant", "D. Giraffe"], "A"),
    ("Who painted 'The Starry Night'?", ["A. Pablo Picasso", "B. Vincent van Gogh", "C. Leonardo da Vinci", "D. Michelangelo"], "B"),
    ("Which planet is known as the 'Morning Star' or 'Evening Star'?", ["A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"], "A"),
    ("Who wrote 'The Great Gatsby'?", ["A. F. Scott Fitzgerald", "B. Ernest Hemingway", "C. Mark Twain", "D. J.D. Salinger"], "A"),
    ("What is the largest bird in the world?", ["A. Ostrich", "B. Penguin", "C. Eagle", "D. Vulture"], "A"),
    ("Who discovered penicillin?", ["A. Alexander Fleming", "B. Marie Curie", "C. Louis Pasteur", "D. Robert Koch"], "A"),
    ("What is the currency of Japan?", ["A. Yen", "B. Yuan", "C. Dollar", "D. Euro"], "A"),
    ("Which is the smallest ocean in the world?", ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"], "D"),
    ("Who is known as the 'Maid of Orleans'?", ["A. Catherine of Aragon", "B. Joan of Arc", "C. Anne Boleyn", "D. Cleopatra"], "B"),
    ("What is the chemical symbol for silver?", ["A. Si", "B. Ag", "C. Au", "D. Pt"], "B"),
    ("Who wrote 'Romeo and Juliet'?", ["A. William Shakespeare", "B. Jane Austen", "C. Leo Tolstoy", "D. Charles Dickens"], "A"),
    ("Which is the largest species of big cats?", ["A. Leopard", "B. Lion", "C. Tiger", "D. Cheetah"], "C"),
    ("Who painted 'The Persistence of Memory'?", ["A. Salvador Dalí", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Leonardo da Vinci"], "A"),
    ("What is the largest moon in the Solar System?", ["A. Titan", "B. Europa", "C. Ganymede", "D. Callisto"], "C"),
    ("Who is known as the 'Father of Medicine'?", ["A. Hippocrates", "B. Aristotle", "C. Galen", "D. Socrates"], "A"),
    ("What is the capital of France?", ["A. London", "B. Paris", "C. Rome", "D. Madrid"], "B"),
    ("Who wrote 'Hamlet'?", ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Leo Tolstoy"], "A"),
    ("Which planet is known as the Red Planet?", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "B"),
    ("What is the largest ocean on Earth?", ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"], "C"),
    ("What is the capital of Australia?", ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"], "C"),
    ("Who painted the Mona Lisa?", ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"], "C"),
    ("Which country won the FIFA World Cup in 2018?", ["A. Germany", "B. Brazil", "C. France", "D. Argentina"], "C"),
    ("Which element has the chemical symbol 'H'?", ["A. Hydrogen", "B. Helium", "C. Carbon", "D. Gold"], "A"),
    ("What is the powerhouse of the cell?", ["A. Nucleus", "B. Ribosome", "C. Mitochondrion", "D. Golgi Apparatus"], "C"),
    ("Who is credited with discovering gravity after seeing an apple fall from a tree?", ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"], "A"),
    ("What is the national animal of China?", ["A. Panda", "B. Dragon", "C. Tiger", "D. Elephant"], "A"),
    ("Which planet is closest to the Sun?", ["A. Venus", "B. Earth", "C. Mercury", "D. Mars"], "C"),
    ("Which artist painted the famous painting 'Starry Night'?", ["A. Claude Monet", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Leonardo da Vinci"], "B"),
    ("What is the longest river in the world?", ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"], "A"),
    ("Who wrote 'Pride and Prejudice'?", ["A. Jane Austen", "B. Emily Brontë", "C. Charlotte Brontë", "D. George Eliot"], "A"),
    ("Which mammal can fly?", ["A. Bat", "B. Rat", "C. Rabbit", "D. Squirrel"], "A"),
    ("What year did the Titanic sink?", ["A. 1912", "B. 1905", "C. 1920", "D. 1898"], "A"),
    ("Who invented the telephone?", ["A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Isaac Newton"], "A"),
    ("What is the chemical symbol for gold?", ["A. Au", "B. Ag", "C. Fe", "D. Hg"], "A"),
    ("Who wrote '1984'?", ["A. George Orwell", "B. Aldous Huxley", "C. J.R.R. Tolkien", "D. H.G. Wells"], "A"),
    ("Which country is known as the Land of the Rising Sun?", ["A. China", "B. Japan", "C. South Korea", "D. Thailand"], "B"),
    ("Who painted 'The Last Supper'?", ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo"], "B"),
    ("What is the largest organ in the human body?", ["A. Liver", "B. Brain", "C. Skin", "D. Heart"], "C"),
    ("Which gas do plants absorb from the atmosphere?", ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "C"),
    ("What is the largest animal on Earth?", ["A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Crocodile"], "A"),
    ("Who wrote 'To Kill a Mockingbird'?", ["A. Mark Twain", "B. Harper Lee", "C. F. Scott Fitzgerald", "D. Ernest Hemingway"], "B"),
    ("Which country is famous for the Great Wall?", ["A. India", "B. China", "C. Egypt", "D. Italy"], "B"),
    ("Who was the first man to step on the moon?", ["A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. Alan Shepard"], "A"),
    ("What is the largest desert in the world?", ["A. Sahara Desert", "B. Gobi Desert", "C. Arabian Desert", "D. Kalahari Desert"], "A"),
    ("Which is the largest continent by land area?", ["A. Africa", "B. Asia", "C. North America", "D. Europe"], "B"),
    ("Who is known as the 'Father of Computers'?", ["A. Alan Turing", "B. Charles Babbage", "C. Steve Jobs", "D. Bill Gates"], "B"),
    ("What is the chemical symbol for water?", ["A. Wo", "B. Wt", "C. H2O", "D. Ag"], "C"),
    ("What is the tallest mountain in the world?", ["A. Mount Everest", "B. K2", "C. Kilimanjaro", "D. Mount Fuji"], "A"),
    ("Who is the author of 'The Catcher in the Rye'?", ["A. J.D. Salinger", "B. F. Scott Fitzgerald", "C. Ernest Hemingway", "D. Mark Twain"], "A"),
    ("Which city is known as the 'Eternal City'?", ["A. Athens", "B. Rome", "C. Paris", "D. London"], "B"),
    ("Which animal is known as the 'Ship of the Desert'?", ["A. Camel", "B. Horse", "C. Elephant", "D. Giraffe"], "A"),
    ("Who painted 'The Starry Night'?", ["A. Pablo Picasso", "B. Vincent van Gogh", "C. Leonardo da Vinci", "D. Michelangelo"], "B"),
    ("Which planet is known as the 'Morning Star' or 'Evening Star'?", ["A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"], "A"),
    ("Who wrote 'The Great Gatsby'?", ["A. F. Scott Fitzgerald", "B. Ernest Hemingway", "C. Mark Twain", "D. J.D. Salinger"], "A"),
    ("What is the largest bird in the world?", ["A. Ostrich", "B. Penguin", "C. Eagle", "D. Vulture"], "A"),
    ("Who discovered penicillin?", ["A. Alexander Fleming", "B. Marie Curie", "C. Louis Pasteur", "D. Robert Koch"], "A"),
    ("What is the currency of Japan?", ["A. Yen", "B. Yuan", "C. Dollar", "D. Euro"], "A"),
    ("Which is the smallest ocean in the world?", ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"], "D"),
    ("Who is known as the 'Maid of Orleans'?", ["A. Catherine of Aragon", "B. Joan of Arc", "C. Anne Boleyn", "D. Cleopatra"], "B"),
    ("What is the chemical symbol for silver?", ["A. Si", "B. Ag", "C. Au", "D. Pt"], "B"),
    ("Who wrote 'Romeo and Juliet'?", ["A. William Shakespeare", "B. Jane Austen", "C. Leo Tolstoy", "D. Charles Dickens"], "A"),
    ("Which is the largest species of big cats?", ["A. Leopard", "B. Lion", "C. Tiger", "D. Cheetah"], "C"),
    ("Who painted 'The Persistence of Memory'?", ["A. Salvador Dalí", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Leonardo da Vinci"], "A"),
    ("What is the largest moon in the Solar System?", ["A. Titan", "B. Europa", "C. Ganymede", "D. Callisto"], "C"),
    ("Who is known as the 'Father of Medicine'?", ["A. Hippocrates", "B. Aristotle", "C. Galen", "D. Socrates"], "A"),

    # Add more questions here...
]

def run_quiz():
    print("Welcome to the Interactive Quiz!")
    print("You will be presented with 100 questions. Each question has multiple-choice answers.")
    print("Enter the letter corresponding to your answer (A, B, C, or D).\n")

    score = 0
    user_answers = []

    # Shuffle the quiz questions to randomize the order
    random.shuffle(quiz_questions)

    for i, (question, options, correct_answer) in enumerate(quiz_questions, start=1):
        print(f"Question {i}: {question}")
        for option in options:
            print(option)
        
        user_answer = input("Your answer: ").strip().upper()

        # Validate user input
        while user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Your answer: ").strip().upper()

        user_answers.append((question, user_answer))
        
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.\n")
    
    print("Quiz completed!")
    print(f"You got {score} out of {len(quiz_questions)} questions correct.")

    # Allow user to review their answers
    review_answers = input("Do you want to review your answers? (yes/no): ").lower()
    if review_answers == "yes":
        print("\nReview of Your Answers:")
        for i, (question, user_answer) in enumerate(user_answers, start=1):
            print(f"Question {i}: {question}")
            print(f"Your answer: {user_answer}")
            for q, options, correct_answer in quiz_questions:
                if q == question:
                    print(f"Correct answer: {correct_answer}")
            print()
    else:
        print("Thank you for taking the quiz!")

    # Prompt to continue or exit
    continue_quiz = input("Do you want to continue with another quiz? (yes/no): ").lower()
    if continue_quiz == "yes":
        run_quiz()
    else:
        print("Goodbye!")

# Run the quiz
run_quiz()
