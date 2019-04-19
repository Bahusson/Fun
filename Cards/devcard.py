
arkana = {"1": "Głupiec", "2": "Mag", "3": "Kapłanka", "4": "Cesarzowa", "5": "Cesarz",
 "6": "Kapłan", "7": "Kochankowie", "8": "Rydwan", "9": "Sprawiedliwość", "10": "Pustelnik",
"11": "Koło Fortuny", "12": "Moc", "13": "Wisielec", "14": "Śmierć", "15": "Umiarkowanie",
"16": "Diabeł", "17": "Wieża", "18": "Gwiazda", "19": "Księżyc", "20": "Słońce",
"21": "Sąd Ostateczny", "22": "Świat"}
#Skrót do powtórzenia w pętli
def short2 ():
    while True:
        x1 = input('Którego dnia się urodziłeś/aś? [dd]')
        if len(x1) == 2:
            try:
                d1 = int(x1[0])
                d2 = int(x1[1])
            except:
                print ('Poproszę 2 cyfry w formacie: [dd]')
                continue
        else:
            print ('Spróbuj podać dwie cyfry w formacie: [dd].')
            continue

        x2 = input('W którym miesiącu się urodziłeś/aś? [mm]')
        if len(x2) == 2:
            try:
                m1 = int(x2[0])
                m2 = int(x2[1])
            except:
                print ('Poproszę 2 cyfry w formacie: [mm]')
                continue
        else:
            print ('Spróbuj podać dwie cyfry w formacie: [mm].')
            continue

        x3 = input('W którym roku się urodziłeś/aś? [yyyy]')
        if len(x3) == 4:
            try:
                y1 = int(x3[0])
                y2 = int(x3[1])
                y3 = int(x3[2])
                y4 = int(x3[3])
            except:
                print('Poproszę 4 cyfry w formacie:  [yyyy]')
                continue
        else:
            print ('Spróbuj podać cztery cyfry w formacie: [yyyy].')
            continue
        x4 = input('Na który rok mam wyliczyć kartę rozwoju? [yyyy]')
        if len(x4) == 4:
            try:
                c1 = int(x4[0])
                c2 = int(x4[1])
                c3 = int(x4[2])
                c4 = int(x4[3])
            except:
                print('Poproszę 4 cyfry w formacie:  [yyyy]')
                continue
        else:
            print ('Spróbuj podać cztery cyfry w formacie: [yyyy].')
            continue
        break

    daymonth = d1+d2+m1+m2
    yearborn = y1+y2+y3+y4
    yearnow = c1+c2+c3+c4
    lifecard_raw = daymonth+yearborn
    devcard_raw = yearnow+daymonth

    if lifecard_raw > 22:
        l1 = int(str(lifecard_raw)[0])
        l2 = int(str(lifecard_raw)[1])
        lifecard = l1+l2
    else:
        lifecard = lifecard_raw

    if lifecard > 9:
        s1 = int(str(lifecard)[0])
        s2 = int(str(lifecard)[1])
        soulcard = s1+s2
    else:
        soulcard = lifecard

    if devcard_raw > 22:
        v1 = int(str(devcard_raw)[0])
        v2 = int(str(devcard_raw)[1])
        devcard1 = v1+v2
    else:
        devcard1 = devcard_raw

    if len(str(devcard1)) > 1:
        v3 = int(str(devcard1)[0])
        v4 = int(str(devcard1)[1])
        devcard2 = v3+v4
    else:
        pass

#Tu się cholernie dużo powtarza. Weź to spróbuj przepisać żeby nie było tu tyle kodu...

    print('Twoja karta życia to ' + arkana[str(lifecard)])
    print('Twoja karta duszy to ' + arkana[str(soulcard)])

    if len(str(devcard1)) < 2:
        print('Twoja karta rozwoju to ' + arkana[str(devcard1)])
    else:
        print('Twoja karta rozwoju to ' + arkana[str(devcard1)] + ' lub ' + arkana[str(devcard2)])


#Skopiuj jeszcze "short1 żeby powtarzał czynność aż każesz mu skończyć"


#Tu zaczyna się program
print("Witaj w TAROCIE!")
print("Ten poręczny program wyliczy Ci kartę życia, duszy i rozwoju!")
short2()
