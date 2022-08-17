class QuizBrain:
    def __init__(self, questions) -> None:
        self._question_number = 0
        self._score = 0
        self._questions = questions

    def score_string(self):
        return f"{self._score}/{self._question_number}"

    def still_has_questions(self):
        return self._question_number < len(self._questions)

    def next_question(self):
        question = self._questions[self._question_number]._text
        answer = self._questions[self._question_number]._answer
        print(f"\nQ: {question}")
        user_answer = input("True or False?: ").strip().lower()
        if user_answer == answer.lower():
            self._score += 1
            print("You got it right!")
            print(f"The correct answer was: {answer}.")

        else:
            print("That's wrong.")
            print(f"The correct answer was: {answer}.")

        self._question_number += 1
        print(
            f"Your current score is {self.score_string()}")
