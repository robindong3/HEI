import json
import numpy as np
import math
import matplotlib.pyplot as plt
import csv

#(a)
def load_json(fileName, start = 1937, end = 2012):
    '''
    load data from .csv file, 
    '''
    total = {}
    with open(fileName, 'r') as csvf:
        reader = csv.reader(csvf)
        next(reader)
        for row in reader:
            year = int(row[0])
            if start <= year <= end:
                if year not in total.keys():
                    total[year] = [float(row[2])]
                else:
                    total[year].append(float(row[2]))
    
    with open('new_file.json', 'w') as file:
        json.dump(total, file, indent=4)

load_json('python_language_1_data.csv')

#(b)
def plot_json(fileName, year, colour = 'r'):
    '''
    plot the rainfall of the year
    '''
    with open(fileName, 'r') as f:
        year_dict = json.load(f)
    rain = year_dict[str(year)]
    days = range(1, len(rain) + 1)
    plt.plot(days, rain, colour)
    plt.ylabel('Rainfall (mm/day)')
    plt.xlabel('Day')
    plt.title('Daily rainfall measurement in {0}'.format(year))
    plt.savefig('Rainfall_plot_1998.png')
    plt.clf()

plot_json('new_file.json', 1998, colour = 'r')

#(c)
def plot_average(fileName, start, end):
    '''
    plot the rainfall of the year
    '''
    start_year = start
    mean_list = []
    year_list = []
    with open(fileName, 'r') as f:
        year_dict = json.load(f)
    while start <= end:
        rain =  year_dict[str(start)]
        mean = sum(rain)/len(rain)
        mean_list.append(mean)
        year_list.append(start)
        start += 1


    plt.plot(year_list, mean_list)
    plt.ylabel('Daily Average Rainfall of The Year (mm/day)')
    plt.xlabel('Year')
    plt.title('Average rainfall measurement in the year {0} to The Year {1}'.format(start_year, end))
    plt.savefig('Average_Rainfall.png')
    plt.clf()

plot_average('new_file.json', 1988, 2000)

#(d)
def calculate_correction(data):
    correction = data * (1.2 ** np.sqrt(2))
    return correction

def solve_with_loop(fileName, year):
    with open(fileName, 'r') as f:
        year_dict = json.load(f)
    Original_list = year_dict[str(year)]
    new_list = []
    for i in Original_list:
        new_list.append(calculate_correction(i))
    return new_list

new_list = solve_with_loop('new_file.json', 2000)
print(new_list)

def solve_with_comp(fileName, year):
    """
    Advantages of using comprehension - considered more readable, achieves the same output in less lines of
                                        code, faster in terms of performance.
    Disadvantages of using comprehension - Does not increase the capabilities of the language

    Advantages of using loop - Perhaps easier to understand
    Disadvantage of using loop - less readable, takes more lines of code, slower in terms of performance.
    """
    with open(fileName, 'r') as f:
        year_dict = json.load(f)
    new_list = [calculate_correction(i) for i in year_dict[str(year)]]
    return new_list

new_list = solve_with_comp('new_file.json', 2000)
print(new_list)