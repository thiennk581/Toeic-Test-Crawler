

class Test:
    def __init__(self, questionsTest):
        self.parts = {}
        self.parts['part_1'] = questionsTest[1]
        self.parts['part_2'] = questionsTest[2]
        self.parts['part_3'] = questionsTest[3]
        self.parts['part_4'] = questionsTest[4]
        self.parts['part_5'] = questionsTest[5]
        self.parts['part_6'] = questionsTest[6]
        self.parts['part_7'] = questionsTest[7]
    def to_dict(self):
        return self.parts