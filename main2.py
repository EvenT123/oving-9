# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 12:14:29 2021

@author: Bruker
"""

class Questions:
    def __init__(self, tasktext, answer_options, correct_answer):
        self.tasktext = tasktext
        self.answer_options = answer_options
        self.correct_answer = correct_answer  
    
    def answer_options(self, option1, option2, option3, option4, option5):
        self.answer_options = [option1, option2, option3, option4, option5]
        
    def __str__(self):
        return f"{self.tasktext} \n 1: {self.answer_options[0]} 2: {self.answer_options[1]} 3: {self.answer_options[2]} 4: {self.answer_options[3]}"
    
    def task_text(self, task):
        self.tasktext = task
    
    def check_answer_user1(self, answer1, correct):
        self.answer1 = answer1
        if self.answer1 == correct:
            print("User 1: Correct!")
        else:
            print("User 1: Wrong!")
            
       
    def check_answer_user2(self, answer2, correct):
        self.answer2 = answer2
        if self.answer2 == correct:
            print("User 2: Correct! \n")
        else:
            print("User 2: Wrong! \n")
    
    def correct_answer_text(self):
        correctAnswerTxt = f"The correct answer was alternative {self.correct_answer} \n"
        print(correctAnswerTxt)
        
QuestionList = []
Alternatives = []
with open("sporsmaalsfil.txt", "r", encoding="UTF-8") as file:
    
    for line in file:
        if line.find(":"):
            spm = line.split(":")
            QuestionList.append(spm[0])
            alt = spm[-1]
            Alternatives.append(alt)

if __name__ == "__main__":
    p1 = 0
    p2 = 0
    
    task_text1 = QuestionList[0]
    answer_options1 = Alternatives[0][1:4] + "\n", Alternatives[0][6:14] + "\n", Alternatives[0][16:19] + "\n", Alternatives[0][21:34] + "\n", ""
    correct_answer1 = 3
    
    qOne = Questions(task_text1, answer_options1, correct_answer1)
    print(str(qOne))
    User1 = int(input("Answer user 1:"))
    User2 = int(input("Answer user 2:"))
    qOne.correct_answer_text()
    qOne.check_answer_user1(User1, correct_answer1)
    qOne.check_answer_user2(User2, correct_answer1)
    if User1 == 3:
        p1 += 1
    if User2 == 3:
        p2 += 1
    
    task_text2 = QuestionList[1]
    answer_options2 = Alternatives[1][2:5] + "\n", Alternatives[1][7:11] + "\n", Alternatives[1][13:19] + "\n", Alternatives[1][21:31] + "\n", ""
    correct_answer2 = 1
    
    qTwo = Questions(task_text2, answer_options2, correct_answer2)
    print(str(qTwo))
    User1 = int(input("Answer user 1:"))
    User2 = int(input("Answer user 2:"))
    qTwo.correct_answer_text()
    qTwo.check_answer_user1(User1, correct_answer2)
    qTwo.check_answer_user2(User2, correct_answer2)
    if User1 == 1:
        p1 += 1
    if User2 == 1:
        p2 += 1
    
    task_text3 = QuestionList[2]
    answer_options3 = Alternatives[2][2:6] + "\n", Alternatives[2][8:21] + "\n", Alternatives[2][23:32] + "\n", Alternatives[2][34:40] + "\n", ""
    correct_answer3 = 1
    
    qThree = Questions(task_text3, answer_options3, correct_answer3)
    print(str(qThree))
    User1 = int(input("Answer user 1:"))
    User2 = int(input("Answer user 2:"))
    qThree.correct_answer_text()
    qThree.check_answer_user1(User1, correct_answer3)
    qThree.check_answer_user2(User2, correct_answer3)
    if User1 == 1:
        p1 += 1
    if User2 == 1:
        p2 += 1
    
    
    task_text4 = QuestionList[3]
    answer_options4 = Alternatives[3][2:14] + "\n", Alternatives[3][16:21] + "\n", Alternatives[3][23:28] + "\n", Alternatives[3][30:37] + "\n", ""
    correct_answer4 = 3
    
    qFour = Questions(task_text4, answer_options4, correct_answer4)
    print(str(qFour))
    User1 = int(input("Answer user 1:"))
    User2 = int(input("Answer user 2:"))
    qFour.correct_answer_text()
    qFour.check_answer_user1(User1, correct_answer4)
    qFour.check_answer_user2(User2, correct_answer4)
    if User1 == 3:
        p1 += 1
    if User2 == 3:
        p2 += 1
    
    print(f"Points: \n User1: {p1} \n User2: {p2}")
            

    
    
    


            
            


    