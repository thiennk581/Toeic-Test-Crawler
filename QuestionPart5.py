import Question

class QuestionPart5:
    def __init__(self, question: Question):
        self.question = question.to_dict()
    def to_dict(self):
        return self.question