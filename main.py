# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as tb
W= 380


def betCalculator():
    a = input("Enter Home Team Name:  \n")
    b = int(input("Enter Home GF (Goals For): \n"))
    c = int(input("Enter Home GA (Goals Against): \n"))
    d = int(input("Enter Total Numer of Games Played \n"))
    e = input("Enter Away Team Name \n")
    f = int(input("Enter Away GF (Goals For): \n"))
    g = int(input("Enter Away GA (Goals Against): \n"))
    h = int(input("Enter Total Numer of Games Played \n"))

    i = int(input("Enter League`s Total Home GF \n"))
    j = int(input("Enter League`s Total A Home GA \n"))

    l = int(input("Enter League`s Total Away GF \n"))
    k = int(input("Enter League`s Total Away GA \n"))
# HOme avarage for games played.
    Hvariable1 = b / d
    Hvariable2 = c / d
    # Away avarage for games played.
    Avariable1 = f / h
    Avariable2 = d / h

    # Serie a Avarage ga and gf
    Indvariable1 = i / W
    Indvariable2 = j / W
    Indvariable3 = l / W
    Indvariable4 = k / W

    homeOutput = Hvariable1 / Indvariable1
    homeOutput1 = Hvariable2 / Indvariable2

    Awayoutput = Avariable1 / Indvariable3
    Awayoutput1 = Avariable2 / Indvariable4

    HomeResult = round((homeOutput / homeOutput1), 1)
    AwayResults = round((Awayoutput / Awayoutput1), 1)

    header = ["Team Names", "Goal Prediction Scores HT", "GP Scores AwayTeam"]

    data = [[a, e], [HomeResult, AwayResults]]
    df = tb.DataFrame(data, columns=[' ', ' ', ],
                      index=["", "Scores"])
    print(df)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    betCalculator()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
