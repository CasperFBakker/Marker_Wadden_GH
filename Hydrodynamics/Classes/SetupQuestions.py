class SetupQuestions():

    def Q_Filter_WindSpeed(WindKracht_Dic):
        FilterWindSpeed = False

        while FilterWindSpeed == False:
            WindSpeed = 69
            try: 
                WindSpeed = int(input('Welke windkracht wil je filteren? '))
            except ValueError: 
                print('Geef een getal van 0 tot 10')


            if WindSpeed >= 0 and WindSpeed <= 10:
                print('De data wordt gefilterd op windkracht:', WindSpeed, ' Bft')
                word = ' Bft'
                WindSpeed = str(WindSpeed) + word
                FilterWindSpeed = True
            else:
                FilterWindSpeed = False

            Windkracht = WindKracht_Dic[WindSpeed]
        return Windkracht 


    def Q_Filter_WindDirection(WindKracht_Dic):
        WantSecondFilter = False
        while WantSecondFilter == False:
            try: 
                Antwoord = str(input('Wil je ook op windrichting filteren? [Ja/Nee]'))
            except TypeError(): 
                print('Kies uit: N, NO, O, ZO, Z, ZW, W, NW')

            checkListJa = ['Ja', 'ja', 'J', 'j', 'Y', 'y']
            checkListNee =  ['Nee', 'nee', 'N', 'n']
            if Antwoord in checkListJa or Antwoord in checkListNee:
                if Antwoord in checkListJa: 
                    FilterWindDirect = False
                    while FilterWindDirect == False:
                        FilterWindDirect = 69
                        try: 
                            WindDirect = str(input('Welke windrichting wil je filteren? '))
                        except TypeError(): 
                            print('Kies uit: N, NO, O, ZO, Z, ZW, W, NW')

                        checkList = ['N', 'NO', 'O',  'ZO', 'Z', 'ZW', 'W',  'NW']
                        if WindDirect in checkList:
                            print('De data wordt gefilterd op windrichting:', WindDirect)
                            FilterWindDirect = True
                        else:
                            print('Kies uit: N, NO, O, ZO, Z, ZW, W, NW')
                            FilterWindDirect = False
                    WantSecondFilter = True
                elif Antwoord in checkListNee:
                    print('Start filter: ')
                    WantSecondFilter = True
            else:
                WantSecondFilter = False