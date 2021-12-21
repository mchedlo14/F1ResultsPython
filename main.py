import requests
from bs4 import BeautifulSoup

def F1_RESULT_2021():


    r = requests.get('https://www.formula1.com/en/results.html/2021/races.html')

    c = r.content

    soup = BeautifulSoup(c, 'html.parser')

    data = soup.find('tbody')

    grand_prix_name = data.find_all('a', {'class': 'dark bold ArchiveLink'})
    winner = data.find_all('span', {'class': 'hide-for-tablet'})
    time = data.find_all('td', {'class': 'dark bold hide-for-tablet'})
    laps = data.find_all('td', {'class': 'bold hide-for-mobile'})
    arr = []
    winners_arr = []
    timearr = []
    laparr = []
    count = 1
    for item in winner:
        winners_arr.append(item.text.strip())

    for item in grand_prix_name:
        arr.append(item.text.strip())

    for item in time:
        timearr.append(item.text.strip())

    for lap in laps:
        laparr.append(lap.text.strip())
    print(f"2021 RACE RESULTS")
    print('\n')
    for item1, item2, item3, item4 in zip(arr, winners_arr, timearr, laparr):
        print(f"{count}) Grand Prix Name --> {item1} ")
        print(f"    Laps --> {item4}")
        print(f"    Winner --> {item2}")
        print(f"    Race time --> {item3}")
        print('\n')
        count += 1



# F1_RESULT_2021()


def F1_RESULT_2020():
    r = requests.get('https://www.formula1.com/en/results.html/2021/races.html')

    c = r.content

    soup = BeautifulSoup(c, 'html.parser')

    data = soup.find('tbody')

    grand_prix_name = data.find_all('a', {'class': 'dark bold ArchiveLink'})
    winner = data.find_all('span', {'class': 'hide-for-tablet'})
    time = data.find_all('td', {'class': 'dark bold hide-for-tablet'})
    laps = data.find_all('td', {'class': 'bold hide-for-mobile'})
    arr = []
    winners_arr = []
    timearr = []
    laparr = []
    count = 1
    for item in winner:
        winners_arr.append(item.text.strip())

    for item in grand_prix_name:
        arr.append(item.text.strip())

    for item in time:
        timearr.append(item.text.strip())

    for lap in laps:
        laparr.append(lap.text.strip())
    print(f"2021 RACE RESULTS")
    print('\n')
    for item1, item2, item3, item4 in zip(arr, winners_arr, timearr, laparr):
        print(f"{count}) Grand Prix Name --> {item1} ")
        print(f"    Laps --> {item4}")
        print(f"    Winner --> {item2}")
        print(f"    Race time --> {item3}")
        print('\n')
        count += 1




def F1_RESULT_2019():
    r = requests.get('https://www.formula1.com/en/results.html/2019/races.html')

    c = r.content

    soup = BeautifulSoup(c, 'html.parser')

    data = soup.find('tbody')

    grand_prix_name = data.find_all('a', {'class': 'dark bold ArchiveLink'})
    winner = data.find_all('span', {'class': 'hide-for-tablet'})
    time = data.find_all('td', {'class': 'dark bold hide-for-tablet'})
    laps = data.find_all('td', {'class': 'bold hide-for-mobile'})
    arr = []
    winners_arr = []
    timearr = []
    laparr = []
    count = 1
    for item in winner:
        winners_arr.append(item.text.strip())

    for item in grand_prix_name:
        arr.append(item.text.strip())

    for item in time:
        timearr.append(item.text.strip())

    for lap in laps:
        laparr.append(lap.text.strip())
    print(f"2021 RACE RESULTS")
    print('\n')
    for item1, item2, item3, item4 in zip(arr, winners_arr, timearr, laparr):
        print(f"{count}) Grand Prix Name --> {item1} ")
        print(f"    Laps --> {item4}")
        print(f"    Winner --> {item2}")
        print(f"    Race time --> {item3}")
        print('\n')
        count += 1


def F1_RESULT_2018():
    r = requests.get('https://www.formula1.com/en/results.html/2018/races.html')

    c = r.content

    soup = BeautifulSoup(c, 'html.parser')

    data = soup.find('tbody')

    grand_prix_name = data.find_all('a', {'class': 'dark bold ArchiveLink'})
    winner = data.find_all('span', {'class': 'hide-for-tablet'})
    time = data.find_all('td', {'class': 'dark bold hide-for-tablet'})
    laps = data.find_all('td', {'class': 'bold hide-for-mobile'})
    arr = []
    winners_arr = []
    timearr = []
    laparr = []
    count = 1
    for item in winner:
        winners_arr.append(item.text.strip())

    for item in grand_prix_name:
        arr.append(item.text.strip())

    for item in time:
        timearr.append(item.text.strip())

    for lap in laps:
        laparr.append(lap.text.strip())
    print(f"2021 RACE RESULTS")
    print('\n')
    for item1, item2, item3, item4 in zip(arr, winners_arr, timearr, laparr):
        print(f"{count}) Grand Prix Name --> {item1} ")
        print(f"    Laps --> {item4}")
        print(f"    Winner --> {item2}")
        print(f"    Race time --> {item3}")
        print('\n')
        count += 1



def F1_RESULT_2017():
    r = requests.get('https://www.formula1.com/en/results.html/2017/races.html')

    c = r.content

    soup = BeautifulSoup(c, 'html.parser')

    data = soup.find('tbody')

    grand_prix_name = data.find_all('a', {'class': 'dark bold ArchiveLink'})
    winner = data.find_all('span', {'class': 'hide-for-tablet'})
    time = data.find_all('td', {'class': 'dark bold hide-for-tablet'})
    laps = data.find_all('td', {'class': 'bold hide-for-mobile'})
    arr = []
    winners_arr = []
    timearr = []
    laparr = []
    count = 1
    for item in winner:
        winners_arr.append(item.text.strip())

    for item in grand_prix_name:
        arr.append(item.text.strip())

    for item in time:
        timearr.append(item.text.strip())

    for lap in laps:
        laparr.append(lap.text.strip())
    print(f"2021 RACE RESULTS")
    print('\n')
    for item1, item2, item3, item4 in zip(arr, winners_arr, timearr, laparr):
        print(f"{count}) Grand Prix Name --> {item1} ")
        print(f"    Laps --> {item4}")
        print(f"    Winner --> {item2}")
        print(f"    Race time --> {item3}")
        print('\n')
        count += 1




def F1_RESULT_2016():
    r = requests.get('https://www.formula1.com/en/results.html/2016/races.html')

    c = r.content

    soup = BeautifulSoup(c, 'html.parser')

    data = soup.find('tbody')

    grand_prix_name = data.find_all('a', {'class': 'dark bold ArchiveLink'})
    winner = data.find_all('span', {'class': 'hide-for-tablet'})
    time = data.find_all('td', {'class': 'dark bold hide-for-tablet'})
    laps = data.find_all('td', {'class': 'bold hide-for-mobile'})
    arr = []
    winners_arr = []
    timearr = []
    laparr = []
    count = 1
    for item in winner:
        winners_arr.append(item.text.strip())

    for item in grand_prix_name:
        arr.append(item.text.strip())

    for item in time:
        timearr.append(item.text.strip())

    for lap in laps:
        laparr.append(lap.text.strip())
    print(f"2021 RACE RESULTS")
    print('\n')
    for item1, item2, item3, item4 in zip(arr, winners_arr, timearr, laparr):
        print(f"{count}) Grand Prix Name --> {item1} ")
        print(f"    Laps --> {item4}")
        print(f"    Winner --> {item2}")
        print(f"    Race time --> {item3}")
        print('\n')
        count += 1

print("In the program you can see the results of F1")
print('Please choose year in range(2015-2021)')
print('If you want to close the program enter quit')
print('\n')

while True:
    question = str(input('Please Enter Year --> '))
    if question =='quit' or question == 'QUIT' or question == 'Quit':
        break

    if question == str(2016):
        F1_RESULT_2016()
    elif question == str(2017):
        F1_RESULT_2017()
    elif question == str(2018):
        F1_RESULT_2018()
    elif question == str(2019):
        F1_RESULT_2019()
    elif question == str(2020):
        F1_RESULT_2020()
    elif question == str(2021):
        F1_RESULT_2021()
    else:
        print("Sorry...there's no information")

input()