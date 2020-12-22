#weather data
import mtplotlib.pylot as plt

statData = "ex4.csv"
def getAVG(file, N):
    row = 0
    lastN = []
    mean = [0]

    with open(file, "r") as rawData:
        for line in rawData:
            if(row == o):
                row = row +1
                continue
            line = line.strip('\n')
            lineData = float(line.split(',')[1])

            if (row <= N):
                lastN.append(lineData)
                mean[0] = (lineData + mean[0]*(row - 1))/row

            else:
                mean.append( mean[row - N -1] + (lineData - lastN[0]/N)
                lastN = lastN[1:]
                lastN.append(lineData)

            row = row + 1
            return mean
                

def plotData(mean, N):
    mean = [round(x,3) for in mean]
    plt.plot(mean, label = str(N) + ' day average')
    plt.xlabel('Day')
    plt.ylabel('Precipation')
    plt.legend()

plotData(getAVG(statData, 1, 1),1)
plotData([0 for x in range(1,5)] + getAVG(statData, 5),5)
