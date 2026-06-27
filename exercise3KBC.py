question="Who is the prime minister of india?"
print(question)
answer=input().lower().strip() 
correct_answer=["narendra modi","narendra damodardas modi","modi"]
if answer in correct_answer:
    print("correct answer!")
else:
    print("wrong answer!!")


