answer=''
question=''
answer_dic={'как дела?':"Хорошо!","что делаешь?":"Программирую",
            "пойдешь на занятие в субботу?":"Конечно!"}

def ask_user(answer, question):
    while True:
        answer = input('Привет! Как дела? ')
        if answer.lower() =='хорошо':
            break 


    while True:
        try:        
            question = input("Задай мне вопрос: ")
            for key, val in answer_dic.items():
            #print('print',key.lower(), question)
                if key.lower() == question.lower():
                    print(val)
                    break
        except KeyboardInterrupt:
            print('\n','Пока!')
            break
print(ask_user(answer, question))