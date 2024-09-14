class QuestionClusterPart34:
    def __init__(self, audioSrc, imgSrc, questions : list):
        self.questionCluster = {}
        self.questionCluster["audio_src"] = audioSrc
        self.questionCluster["img_src"] = imgSrc
        self.questionCluster["questions"] = questions
    def to_dict(self):
        return self.questionCluster