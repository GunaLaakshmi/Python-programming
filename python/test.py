class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for idx, option in enumerate(question['options'], 1):
            print(f"{idx}. {option}")

    def get_user_answer(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.questions[0]['options']):
                    return choice
                else:
                    print("Invalid choice. Please enter a number within the given range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question, user_answer):
        correct_answer = question['answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer is:", question['options'][correct_answer - 1])

    def run_quiz(self):
        for question in self.questions:
            self.display_question(question)
            user_choice = self.get_user_answer()
            self.check_answer(question, user_choice)
        print("Quiz completed!")
        print("Your final score is:", self.score)


if __name__ == "__main__":
    questions = [
        {
            "question": "Who developed Python Programming Language?",
            "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum","Niene Stom"],
            "answer": 3
        },
        {
            "question": "Which of the following is the correct extension of the Python file?",
            "options": [".python", ".pl", ".py",".p"],
            "answer": 2
        },
        {
            "question": "Which of the following functions is a built-in function in python?",
            "options": ["factorial()", "print()", "seed()","sqrt()"],
            "answer": 2
        },
        {
            "question": "Which of the following is not a core data type in Python programming?",
            "options": ["Tuples", "Lists", "Class","Dictionary"],
            "answer": 3
        },
        {
            "question": "What are the two main types of functions in Python?",
            "options": [" System function", "Custom function", " Built-in function & User defined function","User function"],
            "answer": 3
        }
    ]

    quiz = Quiz(questions)
    quiz.run_quiz()

