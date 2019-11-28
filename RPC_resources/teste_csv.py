import csv


def urlListInput(file_input):
    urlList = []
    with open(file_input, 'rt') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in file_reader:
            urlList.append(row)

    return urlList

List = urlListInput('urlList.csv')

for row in List:
    print(row)