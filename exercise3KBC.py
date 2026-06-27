# question="Who is the prime minister of india?"
# print(question)
# answer=input().lower().strip() 
# correct_answer=["narendra modi","narendra damodardas modi","modi"]
# if answer in correct_answer:
#     print("correct answer!")
# else:
#     print("wrong answer!!")


questions=["Who is the prime minister of india?","Which is the national fruit of india?","Which is the national bird of india?"]
correct_answers=[["modi","narendra damodardas modi","narendra modi"],["mango"],["peacock"]]
score=0
for i,question in enumerate(questions):
    print(question)
    answer=input().lower().strip()
    if answer in correct_answers[i]:
        print("Correct Answer!👍")
        score+=10
    else:
        print("Game Over!!😓")
        break
print("SCORE=",score)

                #DAY 27