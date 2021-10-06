import statistics as stats
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv('medium_data.csv')

data = df['reading_time'].tolist()

population_mean = stats.mean(data)
population_stdev = stats.stdev(data)

print(f'The mean of the population is {population_mean}')
print(f'The mean of the standard deviation is {population_mean}')

def randomSetOfData():
    dataset = []
    for i in range(0, 30):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = stats.mean(dataset)

    return mean

def plotGraph(meanList):
    df = meanList
    mean = stats.mean(df)
    fig = ff.create_distplot([df], ['Reading Time'], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode = 'lines', name = 'mean'))
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        setOfMeans = randomSetOfData()
        mean_list.append(setOfMeans)

    plotGraph(mean_list)

    mean = str(stats.mean(mean_list))
    print('Mean of sampling data is ' + mean)

setup()