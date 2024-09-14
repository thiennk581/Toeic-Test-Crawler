class Question:
    def __init__(self, questionIndex, questionText, answers, correctAnswer):
        self.questionDict = {}
        self.questionDict["question_index"] = questionIndex
        self.questionDict["question_text"] = questionText
        self.questionDict["answers"] = answers
        self.questionDict["correct_answer"] = correctAnswer
    def to_dict(self):
        return self.questionDict