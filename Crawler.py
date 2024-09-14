from Question import *
from QuestionPart1 import *
from QuestionPart2 import *
from QuestionClusterPart34 import *
import QuestionPart5
from QuestionClusterPart67 import *


class Crawler:
    def __init__(self):
        pass

    # question, questionPart5
    def questionInfo(question):
        questionIndex = (question.find('div', class_ = 'game-object-view-question-index').text.strip())
        questionText = (question.find('div', class_ = 'game-object-question-text'))
        if questionText != None:
            questionText = questionText.text.strip()
        tempAnswers = question.find_all('div', class_ = 'quiz-choice-item')
        answers = []
        for answer in tempAnswers:
            answers.append(answer.find('div', class_ = 'quiz-choice-item-content').text.strip())
                
        correctAnswer = question.find('span').text.strip()
        return Question(questionIndex, questionText, answers, correctAnswer).to_dict()
    
    def questionClusterInfoPart67(self, questionCluster):
        paragraph = questionCluster.find('div', class_ = 'game-object-question-text').get_text()
        questions = questionCluster.find_all('div', class_ = 'game-object-child-wrap')
        questions = [self.questionInfo(question) for question in questions]
        return QuestionClusterPart67(paragraph, questions).to_dict()
    
    def questionInfoPart5(self, question):
        return self.questionInfo(question)
    
    def questionClusterInfoPart34(self, questionCluster):
        audioSrc = str(questionCluster.find('audio')['src'])
        imgSrc = questionCluster.find('img')
        if imgSrc != None:
            imgSrc = str(imgSrc['src'])
        
        questions = questionCluster.find_all('div', class_ = 'game-object-child-wrap')
        questions = [self.questionInfo(question) for question in questions]
        return QuestionClusterPart34(audioSrc, imgSrc, questions).to_dict()

    def questionInfoPart2(question):
        questionIndex = (question.find('div', class_ = 'game-object-view-question-index').text.strip())
        audioSrc = str(question.find('audio')['src'])

        tempAnswers = question.find_all('div', class_ = 'quiz-choice-item')
        answers = []
        for answer in tempAnswers:
            answers.append(answer.find('div', class_ = 'quiz-choice-item-content').text.strip())
                
        correctAnswer = question.find('div', class_ = "quiz-explanation-correct-answer")
        correctAnswer = correctAnswer.find('span').text.strip()
        return QuestionPart2(questionIndex, audioSrc, answers, correctAnswer).to_dict()

    def questionInfoPart1(question):
        questionIndex = (question.find('div', class_ = 'game-object-view-question-index').text.strip())
        audioSrc = str(question.find('audio')['src'])
        imgSrc = str(question.find('img')['src'])

        tempAnswers = question.find_all('div', class_ = 'quiz-choice-item')
        answers = []
        for answer in tempAnswers:
            answers.append(answer.find('div', class_ = 'quiz-choice-item-content').text.strip())
                
        correctAnswer = question.find('div', class_ = "quiz-explanation-correct-answer")
        correctAnswer = correctAnswer.find('span').text.strip()
        return QuestionPart1(questionIndex, audioSrc, imgSrc, answers, correctAnswer).to_dict()



