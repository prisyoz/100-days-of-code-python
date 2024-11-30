class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        #initialise the question_list to an input
        self.question_list = q_list
        self.score = 0

    # check if quiz list still has questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Retrieve the item at the current question_number from the question_list
    # input Question text and ask for user's answer

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True or False? ")
        self.check_answer(user_answer, current_question.answer)
        return user_answer

    # check answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")



