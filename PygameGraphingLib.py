import pygame

def __DisplayChartGridLines(xLines: bool, yLines: bool, locX: int, locY: int, sizeX: int, sizeY: int,
                           lineDistanc: int = 25, chartColor: str = 'white', shortLines: bool = False):
    axisThickness = 4
    markerThickness = 1

    pygame.draw.line(screen, chartColor, [locX, locY], [locX + sizeX, locY], axisThickness)  # X Axis
    if (xLines):
        for y in range(sizeY):
            if (y % lineDistanc == 0):
                if (shortLines):
                    pygame.draw.line(screen, chartColor, [locX, locY - y], [locX + 20, locY - y], markerThickness)
                else:
                    pygame.draw.line(screen, chartColor, [locX, locY - y], [locX + sizeX, locY - y], markerThickness)

    pygame.draw.line(screen, chartColor, [locX, locY], [locX, locY - sizeY], axisThickness)  # Y Axis
    if (yLines):
        for x in range(sizeX):
            if (x % lineDistanc == 0):
                if (shortLines):
                    pygame.draw.line(screen, chartColor, [locX + x, locY], [locX + x, locY - 20], markerThickness)
                else:
                    pygame.draw.line(screen, chartColor, [locX + x, locY], [locX + x, locY - sizeY], markerThickness)


def DrawPieChart(screen, locX: int, locY: int, size: int, pieSlices, pieColors=None):
    rect = [locX, locY, size, size]
    maxRads = 6.28
    piecePercents = []
    pickColor = ["red", "blue", "yellow", "green", "purple", "white"]
    counter = 0
    index = 0
    lastValue = 0
    maxPieVal = 0

    if (pieColors is not None):
        pickColor = pieColors

    for piece in pieSlices:
        maxPieVal += piece

    for piece in pieSlices:
        piecePercents.append(piece / maxPieVal)

    for piece in piecePercents:
        pygame.draw.arc(screen, pickColor[index], rect, lastValue, lastValue + (piece * maxRads), size)
        lastValue += piece * maxRads
        # print(str(lastValue))
        counter += 1
        index = counter % len(pickColor)
        # print(pickColor[index] + "-" + str(index))


def DrawProgressBar(screen, locX: int, locY: int, sizeX: int, sizeY: int, value: int, maxValue: int,
                    barColor: str = "red",
                    bracketColor: str = "white", vertical: bool = False):
    barPercent = value / maxValue

    pygame.draw.line(screen, bracketColor, [locX - 2, locY + 2], [locX - 2, locY - sizeY], 2)  # Y Axis
    pygame.draw.line(screen, bracketColor, [locX - 2, locY + 2], [locX + sizeX, locY + 2], 2)  # X Axis

    if (vertical):
        rect = [locX, (locY - sizeY) + (sizeY * (1 - barPercent)), sizeX, sizeY * barPercent]
        pygame.draw.rect(screen, barColor, rect, sizeY - 50)
    else:  # Horizontal
        rect = [locX, locY - sizeY, sizeX * barPercent, sizeY]
        pygame.draw.rect(screen, barColor, rect)


def DrawLineChart(screen, locX: int, locY: int, lineArray, sizeX: int, sizeY: int, xLabels, ylabels,
                  chartColor: str = "white", lineColors=None):
    counter = 0
    pickColor = ["red", "blue", "yellow", "green", "purple", "white"]
    biggestX = 0
    biggestY = 0

    if(lineColors is not None):
        pickColor= lineColors

    __DisplayChartGridLines(True, True, locX, locY, sizeX, sizeY, chartColor= chartColor, shortLines=False)

    # example= [
    # [[0,0],[50,10],[100,100]],
    # [[0,10],[50,13],[100,50]],
    # [[0,0],[50,15],[75,2]],
    # [[0,100],[50,50],[52,33]]
    # ]
    for line in lineArray:
        for dot in line:
            if (dot[0] > biggestX):
                biggestX = dot[0]
            if (dot[1] > biggestY):
                biggestY = dot[1]

    for line in lineArray:
        lastDot = []
        index = counter % len(pickColor)
        for dot in line:
            percentX = dot[0] / biggestX
            percentY = dot[1] / biggestY
            pygame.draw.circle(screen, pickColor[index], [locX + (percentX * sizeX), locY - (percentY * sizeY)], 6)
            if (lastDot != []):
                pygame.draw.line(screen, pickColor[index],
                                 [locX + (percentX * sizeX), locY - (percentY * sizeY)],
                                 [lastDot[0], lastDot[1]], 4)
            lastDot = [locX + (percentX * sizeX), locY - (percentY * sizeY)]
        counter += 1


def DrawBarChart(screen, locX: int, locY: int, valueArray, sizeX: int, sizeY: int, xLabels: str = "test",
                 ylabels: str = "test", barColors=None, chartColor: str = "white", vertical: bool = True):
    pickColor = ["red", "blue", "yellow", "green", "purple", "white"]
    maxVal = 0
    counter = 0
    index = 0
    barsize = round(sizeX / (len(valueArray) + 4))

    if(barColors is not None):
        pickColor= barColors

    for bar in valueArray:
        if (bar > maxVal):
            maxVal = bar

    if (vertical):
        __DisplayChartGridLines(True, False, locX, locY, sizeX, sizeY, chartColor=chartColor, shortLines=False)

        for bar in valueArray:
            barPercent = bar / maxVal
            if (counter == 0):
                rect = [locX + (counter * barsize) + 10,
                        (locY - sizeY) + (sizeY * (1 - barPercent)),
                        barsize,
                        sizeY * barPercent]
            else:
                rect = [locX + (counter * barsize) + (10 * counter) + 10,
                        (locY - sizeY) + (sizeY * (1 - barPercent)),
                        barsize,
                        sizeY * barPercent]
            pygame.draw.rect(screen, pickColor[index], rect, barsize)
            counter += 1
            index = counter % len(pickColor)
    else:  # Horizontal Bars (TO DO)
        __DisplayChartGridLines(False, True, locX, locY, sizeX, sizeY, chartColor=chartColor, shortLines=False)

        for bar in valueArray:
            barPercent = bar / maxVal
            if (counter == 0):
                rect = [locX + 3,
                        locY - (counter * barsize) - 40,
                        sizeX * barPercent,
                        barsize]
            else:
                rect = [locX + 3,
                        locY - (counter * barsize) - (10 * counter) - 40,
                        sizeX * barPercent,
                        barsize]
            pygame.draw.rect(screen, pickColor[index], rect, barsize)
            counter += 1
            index = counter % len(pickColor)


def DrawScatterPlot(screen, locX: int, locY: int, pointArray, sizeX: int, sizeY: int, xLabels, ylabels,
                    pointColor: str = "black", chartColor: str = "black"):
    biggestX = 0
    biggestY = 0

    __DisplayChartGridLines(True, True, locX, locY, sizeX, sizeY, chartColor=chartColor, shortLines=False)

    for dot in pointArray:
        if (dot[0] > biggestX):
            biggestX = dot[0]
        if (dot[1] > biggestY):
            biggestY = dot[1]

    for dot in pointArray:
        percentX = dot[0] / biggestX
        percentY = dot[1] / biggestY
        pygame.draw.circle(screen, pointColor, [locX + (percentX * sizeX), locY - (percentY * sizeY)], 6)


def DrawValueDisplay(screen, locX: int, locY: int, label: str, value: str, size: int, Symbol: str = None,
                     valueColor: str = "black", labelColor: str = "black", font: str = None):
    labelFont = pygame.font.Font(font, size)  # None means the default font will be used
    valueFont = pygame.font.Font(font, size * 2)

    labelText = labelFont.render(label, True, labelColor)
    valueText = valueFont.render(value, True, valueColor)

    labelRect = [locX, locY, size, size]
    valueRect = [locX - 25, locY + 32, size * 2, size * 2]

    screen.blit(labelText, labelRect)
    screen.blit(valueText, valueRect)


def DemoCharts(screen):
    DrawPieChart(screen, 60, 25, 300, [15, 10, 30, 25, 10, 10])

    DrawProgressBar(screen, 100, 600, 200, 20, 20, 100, "red", "white", False)
    DrawProgressBar(screen, 350, 600, 20, 200, 68, 100, "red", "white", True)

    DrawValueDisplay(screen, 150, 425, "TEST", "100%", 35, None, "white", "white")

    dotsExample = [[10, 15], [5, 95], [80, 85], [62, 33], [25, 25], [35, 50]]
    DrawScatterPlot(screen, 500, 325, dotsExample, 300, 300, "", "", "red", "white")

    DrawBarChart(screen, 900, 325, [45, 55, 10, 90, 33, 25], 300, 300, "xLabels", "ylabels")
    DrawBarChart(screen, 900, 675, [45, 55, 10, 90, 33, 25], 300, 300, "xLabels", "ylabels", vertical=False)

    lineExample = [
        [[0, 0], [50, 10], [100, 100]],
        [[0, 10], [50, 13], [100, 50]],
        [[0, 0], [22, 60], [75, 2]],
        [[0, 100], [50, 50], [52, 33]]
    ]
    DrawLineChart(screen, 500, 675, lineExample, 300, 300, "xLabels", "ylabels", "white")