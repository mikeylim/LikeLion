import random
import time


## 화면에 출력한다
print(random.choice(["된장찌개", "피자", "제육볶음"]))

## 랜덤으로 하나를 출력하자 -> 라이브러리 (특별한 기능)
random.choice(["된장찌개", "피자", "제육볶음"])

## 리스트와 반복구 (for loop)
lunchList = ["된장찌개", "피자", "제육볶음"]
print("점심 리스트: ", lunchList)
lunchList.append("냉장고")
print("냉장고 추가: ", lunchList)
lunch = random.choice(lunchList)
print("오늘먹을 점심: ", lunch)

# Dictionary
information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수", "특기":"피아노", "사는곳":"서울"}
for x in information:
    print("{}: {}".format(x, information[x]))


## Append / Delete Dictionary 
information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# Append
information["특기"] = "피아노"
information["사는곳"] = "서울"
print(information)
# Delete
del information["좋아하는 음식"]
print(information)

## Append / Delete Lists
foods = ["된장찌개", "피자", "제육볶음"]
# Append
foods.append("김밥")
print(foods)
# Delete by index
del foods[3]
print(foods)
# Delete by value
foods.append("김밥")
print(foods)
foods.remove("김밥")
print(foods)

## Iterate dictionary
information = {"고향":"수원", "취미":"피아노", "사는곳":"서울"}
# iterating directly
for key in information:
    print(key, '->', information[key])

# iterating through .items() 
for x, y in information.items():
    print(x, "->", y)

# iterating through .keys()
for key in information.keys():
    print(key)

## 집합(Set) - 순서 없음 => changes the order everytime we run the code
foods = ["된장찌개", "피자", "제육볶음"]
foods_set1 = set(foods)
foods_set2 = set(["된장찌개", "피자", "제육볶음"])
print(foods_set1)
print(foods_set2)

## 합집합-Union (|), 교집합-Intersection (&), 차집합-Diffrence (-), 대칭자집합-Symmetric difference (^)
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
print("메뉴1: ", menu1)
print("메뉴2: ", menu2)
menu3 = print("합집합: ", menu1 | menu2) # 합집합
menu3 = print("교집합: ", menu1 & menu2) # 교집합
menu3 = print("차집합 A-B: ", menu1 - menu2) # 차집합 A-B
menu3 = print("차집합 B-A: ", menu2 - menu1) # 차집합 B-A
menu3 = print("대칭자집합: ", menu2 ^ menu1) # 대칭자집합 B-A

## 만약에-If // 그렇지않다면-else 
foodList = ["된장찌개", "피자", "제육볶음"]
food = random.choice(foodList)
if(food == "제육볶음"):
    print(food, "곱배기 주세요")
elif(food == "피자"):
    print("파인애플 빼고", food, "주세요")
else:    
    print("그냥", food, "주세요")


## input - storing and appending user's Input
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
print("메뉴:", lunch)
shouldWeAddMenu = input("음식을 추가 하시겠습니까? (Y/N): ")
while True:
    if(shouldWeAddMenu == "Y" or shouldWeAddMenu == "y"):
        newMenu = input("음식을 추가 해주세요: ")
        lunch.append(newMenu)
        break
    elif(shouldWeAddMenu == "N" or shouldWeAddMenu == "n"):
        break
    else:
        print("Y/N 둘 중에 하나를 입력해주세요. ")
        shouldWeAddMenu = input("음식을 추가 하시겠습니까? (Y/N): ")
print("메뉴:", lunch)