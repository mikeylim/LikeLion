# 함수-function 만들기-declaration
def functionName():
    print('this is a function')

functionName()


# dictionary
{"key":"value"}

# 1st way of storing values into objects
{"취미는":"영화보기"}, # 질문-key : 답변-value
{"특기는":"댄스"}

total_dictionary = {}

while True:
    question = input('질문을 입력해주세요 (끝내기 : q) : ')
    if (question == 'q' or question == 'Q'):
        break
    else:
        total_dictionary[question] = ""

for q in total_dictionary:
    print(q)
    answer = input('답변을 입력 해주세요 (끝내기 : q) : ')
    total_dictionary[q] = answer
print(total_dictionary)


# 2nd way of storing values into objects
[
    {"질문":"취미는","답변":"영화보기"}, # inside the list, there is dictionary with  무엇-key 질문-value
    {"질문":"특기는","답변":"댄스"}
]

total_list = []
while True:
    question = input('질문을 입력 해주세요 (끝내기 : q) : ')
    if (question == 'q' or question == 'Q'):
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})
print(total_list)

for i in total_list:
    print(i)
    print(i['질문'])
    # print(total_list[i["질문"]])
    answer = input('답변을 입력 해주세요 : ')
    i['답변'] = answer
print(total_list)