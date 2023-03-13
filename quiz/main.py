questions={"question1":{"question":"what is your name",
"answer":"Bolu"
                        },
           "question2": {"question": "what is youR letter",
                         "answer": "H"
                         },
"question3":{"question":"what is your friend's name",
"answer":"Tayo"
                        }
           }

score=0

for (key,value)in questions.items():
    print(value['question'])
    answer=input("What is your answer to this question : ")
    if answer.lower()==value['answer'].lower():
        print("correct")
        score=score+1
        print('Your total score is',str(score))

    else:
        print('wrong')
        score=score
        print('Your total score is',str(score))

