#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CSE_USER
#
# Created:     23-05-2019
# Copyright:   (c) CSE_USER 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

#한글폰트
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)

df = pd.read_csv('final.csv',engine='python')

#프로그램 모드 선택

while True :
    select = int(input("선박 등록 정보 프로그램입니다. 모드를 선택하세요.(년으로 검색 : 1 , 선종으로 검색 : 2 , 종료 : 3)"))

    if select == 1:
        while True:
            year = int(input("조사할 년을 입력하시오.(ex 11 ~ 19) (이전 : 3)")) # 조사 년 선택
            if year in range(11,20):
                df1 = df.loc[df['년']== year]
                print(df1)
                while True:
                    age = input("조사할 선령을 입력하시오. (이전 : 3)")
                    if age in ['5년','5-10년','10-15년','15-20년','20-25년','25-30년','30-25년','35년']:
                        df2 = df1.loc[df1['선령']==age]
                        print(df2)
                        while True:
                            sort = input("조사할 선종을 입력하시오. (이전 : 3)")
                            if sort in ['여객선','화물선','유조선']:
                                df3 = df2[['년','선령',sort]]
                                df31 = df3.loc[df3['선령']==age]
                                print(df31)
                            elif int(sort) == 3:
                                break
                            else:
                                print("error 다시 입력하시오")
                                continue
                        continue

                    elif int(age) == 3:
                        break
                    else:
                        print("error 다시 입력하시오")
                        continue
            elif year == 3:
                break
            else:
                print("error 다시 입력하시오")
                continue

    elif select == 2:
        while True:
            sort = input("조사할 선종을 입력하시오.(여객선, 유조선, 화물선) (이전 : 3)") #조사 선종 선택
            if sort in ['여객선','화물선','유조선']:
                df1 = df[['년','선령',sort]]
                while True:
                    age = input("조사할 선령을 입력하시오. (이전 : 3)")
                    if age in ['5년','5-10년','10-15년','15-20년','20-25년','25-30년','30-25년','35년']:
                        df11 = df1.loc[df1['선령']==age]
                        print(df11)
                        plt.plot(df11['년'],df11[sort])
                        plt.show()
                        continue
                    elif int(age) == 3:
                        break
                    else:
                        print("error 다시 입력하시오")
                        continue
                continue
            elif int(sort) == 3:
                break
            else:
                print("error 다시 입력하시오")
                continue
    elif select == 3:
        print("종료합니다")
        break
    else:
        print("error 다시 입력하시오")
        continue

