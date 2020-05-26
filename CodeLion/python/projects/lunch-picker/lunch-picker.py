# 오늘은 뭐드실.py 
# Date: 05.26.20
# Author: Mike Dohyun Lim
# Language/version: Python 3.8
#
# This program randomly recommends what to eat today for lunch to Korean users. Runs on console/terminal
# Data structures used: Lists, Sets

import random
import time

lunchList = ['된장찌개', '피자', '제육볶음', '짜장면']
print('오늘의 점심 메뉴 후보:', lunchList)

addMenuPrompt = input('\n음식을 추가 하시겠습니까? (y) (끝내기: q) ')
while True:
    if(addMenuPrompt == 'y' or addMenuPrompt == 'Y'):
        addMenuItem = input('\n음식을 추가 해주세요: ')
        if (addMenuItem not in lunchList):
            lunchList.append(addMenuItem)    
            print('\n점심 메뉴 후보:', lunchList)
            addMenuPrompt = input('[{}] 가 추가 되었습니다. 음식을 더 추가 하시겠습니까? (y) (끝내기: q) '.format(addMenuItem))
        else:
            print('\n점심 메뉴 후보:', lunchList)
            addMenuPrompt = input('이미 [{}] 가 메뉴에 있습니다. 다른 음식을 추가 하시겠습니까? (y) (끝내기: q) '.format(addMenuItem))
    elif(addMenuPrompt == 'q' or addMenuPrompt == 'Q'):
        # list to set
        lunchSet = set(lunchList)
        print(lunchSet)
        break
    else:
        print("\n추가 하시려면 'y'를 끝내시려면 'q'를 입력해주세요.")
        print('점심 메뉴 후보:', lunchList)
        addMenuPrompt = input('\n음식을 추가 하시겠습니까? (Y) (끝내기: q) ')

delMenuPrompt = input('\n음식을 삭제하시겠습니까? (y) (끝내기: q) ')
while True:
    if(delMenuPrompt == 'y' or delMenuPrompt == 'Y'):
        delMenuItem = input('\n음식을 삭제 해주세요: ')
        if(delMenuItem in lunchSet):
            lunchSet -= set([delMenuItem])
            # lunchSet.remove(delMenuItem)
            print('\n점심 메뉴 후보:', lunchSet)
            delMenuPrompt = input('[{}] 가 삭제 되었습니다. 음식을 더 삭제 하시겠습니까? (y) (끝내기: q) '.format(delMenuItem))
        else:
            print('\n점심 메뉴 후보:', lunchSet)
            delMenuPrompt = input('점심 메뉴에 [{}] 가 없습니다. 다른 음식을 삭제 하시겠습니까? (y) (끝내기: q) '.format(delMenuItem))
            print('\n점심 메뉴 후보:', lunchSet)
    elif(delMenuPrompt == 'q' or delMenuPrompt == 'Q'):
        print('\n====================================================================')
        break 
    else:
        print("\n삭제 하시려면 'y'를 끝내시려면 'q'를 입력해주세요.")
        print('점심 메뉴 후보:', lunchSet)
        delMenuPrompt = input('\n음식을 삭제 하시겠습니까? (Y) (끝내기: q) ')

print('\n최종 점심 메뉴 후보:', lunchSet, '중에서 선택합니다!\n')
# count down by seconds from 5 to 1 
for i in range(5,0,-1):
   print(i)
   time.sleep(1)

finalMenu = random.choice(list(lunchSet))
# finalMenu = random.choice(tuple(lunchSet))
print('\n~~~~~ 오늘의 점심 메뉴는 [{}] 입니다! 맛있게 드세요 ~~~~~'.format(finalMenu))
print("\
\n  ___ ___                         _____      ________                  .___ .____                        .__     \
\n /   |   \_____ ___  __ ____     /  _  \    /  _____/  ____   ____   __| _/ |    |    __ __  ____   ____ |  |__  \
\n /    ~    \__  \\  \/ // __ \   /  /_\  \  /   \  ___ /  _ \ /  _ \ / __ |  |    |   |  |  \/    \_/ ___\|  |  \ \
\n \    Y    // __ \\   /\  ___/  /    |    \ \    \_\  (  <_> |  <_> ) /_/ |  |    |___|  |  /   |  \  \___|   Y  \ \
\n \___|_  /(____  /\_/  \___  > \____|__  /  \______  /\____/ \____/\____ |  |_______ \____/|___|  /\___  >___|  / \
\n       \/      \/          \/          \/          \/                   \/          \/          \/     \/     \/ \
")