class QuestionClusterPart67:
    def __init__(self, paragraph, questions):
        self.questionCluster = {}
        self.questionCluster["paragraph"] = paragraph
        self.questionCluster["questions"] = questions
    def to_dict(self):
        return self.questionCluster