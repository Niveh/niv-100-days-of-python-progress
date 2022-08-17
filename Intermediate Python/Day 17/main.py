from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def load_questions_data():
    questions_list = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        questions_list.append(Question(question_text, question_answer))

    return questions_list


def run_quiz():
    questions = load_questions_data()
    quiz = QuizBrain(questions)

    while quiz.still_has_questions():
        quiz.next_question()

    return quiz


def main():
    quiz = run_quiz()

    print("\nYou've completed the quiz!")
    print(f"Your final score was: {quiz.score_string()}")


if __name__ == "__main__":
    main()
