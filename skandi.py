from random import randint
import csv
import requests

def gen():
    
    szamok1 = []
    szamok2 = []
    
    while True:
        a = randint(1,35)
        if len(szamok1) < 7:
            if a not in szamok1:
                szamok1.append(a)
        else:
            print("A kovetkezo lottoszamokat generaltam #1: ", sorted(szamok1))
            while True:
                b = randint(1,35)
                if len(szamok2) < 7:
                    if b not in szamok2:
                        szamok2.append(b)
                else:
                    print("A kovetkezo lottoszamokat generaltam #2: ", sorted(szamok2))
                    break
            break

    url = 'https://bet.szerencsejatek.hu/cmsfiles/skandi.csv'

    res = requests.get(url)
    content = res.content.decode('iso-8859-1')

    kezi_sorsolas = []
    gepi_sorsolas = []

    for i,line in enumerate(csv.reader(content.splitlines(), delimiter=';')):
                kezi_sorsolas.extend([int(line[11]),int(line[12]),int(line[13]),int(line[14]),int(line[15]),int(line[16]),int(line[17])])
                gepi_sorsolas.extend([int(line[18]),int(line[19]),int(line[20]),int(line[21]),int(line[22]),int(line[23]),int(line[24])])
                print("Kezi sorsolas nyeroszamai:", kezi_sorsolas)
                print("Gepi sorsolas nyeroszamai:",gepi_sorsolas)
                if(i >= 0):
                    break
        
    talalatok_list =[]
    for szamok1szam in szamok1:
        if szamok1szam in kezi_sorsolas:
            talalatok_list.append(szamok1szam)
    print("elso szamsorral a kezi sorsolason a kovetkezo szam(ok) talalt(ak):", talalatok_list)

    talalatok_list3 =[]
    for szamok3szam in szamok1:
        if szamok3szam in gepi_sorsolas:
            talalatok_list3.append(szamok1szam)
    print("elso szamsorral a gepi sorsolason a kovetkezo szam(ok) talalt(ak):", talalatok_list3)

    talalatok_list4 =[]
    for szamok4szam in szamok2:
        if szamok4szam in kezi_sorsolas:
            talalatok_list4.append(szamok1szam)
    print("masodik szamsorral a kezi sorsolason a kovetkezo szam(ok) talalt(ak):", talalatok_list4)
        
    talalatok_list2 =[]
    for szamok2szam in szamok2: 
        if szamok2szam in gepi_sorsolas:
            talalatok_list2.append(szamok2szam)
    print("masodik szamsorral a gepi sorsolason a kovetkezo szam(ok) talalt(ak):", talalatok_list2)
            
gen()