class QuestionPart1:
    def __init__(self, questionIndex, audioSrc, imgSrc, answers, correctAnswer):
        self.question = {}
        self.question["question_index"] = questionIndex
        self.question["audio_src"] = audioSrc
        self.question["img_src"] = imgSrc
        self.question["answers"] = answers
        self.question["correct_answer"] = correctAnswer
    def to_dict(self):
        return self.question