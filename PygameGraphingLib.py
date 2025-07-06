# Example file showing a circle moving on screen
import datetime
import random
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


class PygameGraph:
    screen = None
    locX = 0
    locY = 0
    sizeX = 0
    sizeY = 0
    pickColor = ["red", "blue", "yellow", "green", "purple", "white"]
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    p7 = 0
    parr = []
    labelarr = ["this", "is", "for", "testing", "purposes", "only!!"]

    def __init__(self, iscreen, ilocX: int, ilocY: int, isizeX: int, isizeY: int):
        self.screen = iscreen
        self.locX = ilocX
        self.locY = ilocY
        self.sizeX = isizeX
        self.sizeY = isizeY

        # Demo Values
        self.p1 = random.randint(1, 26)
        random.seed(datetime.datetime.now().microsecond)
        self.p2 = random.randint(1, 26)
        random.seed(datetime.datetime.now().microsecond)
        self.p3 = random.randint(1, 16)
        random.seed(datetime.datetime.now().microsecond)
        self.p4 = random.randint(1, 16)
        random.seed(datetime.datetime.now().microsecond)
        self.p5 = random.randint(1, 10)
        random.seed(datetime.datetime.now().microsecond)
        self.p6 = random.randint(2, 6)
        self.p7 = random.randint(10, 100)
        self.parr = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6]

    def __DisplayChartGridLines(self, xLines: bool, yLines: bool, lineDistance: int = 25,
                                chartColor: str = 'white', shortLines: bool = False):
        axisThickness = 4
        markerThickness = 1
        startingY = self.locY + self.sizeY

        pygame.draw.line(screen, chartColor, [self.locX, startingY], [self.locX + self.sizeX, startingY],
                         axisThickness)  # X Axis
        if (xLines):
            for y in range(self.sizeY):
                if (y % lineDistance == 0):
                    if (shortLines):
                        pygame.draw.line(screen, chartColor, [self.locX, startingY - y],
                                         [self.locX + 20, startingY - y], markerThickness)
                    else:
                        pygame.draw.line(screen, chartColor, [self.locX, startingY - y],
                                         [self.locX + self.sizeX, startingY - y],
                                         markerThickness)

        pygame.draw.line(screen, chartColor, [self.locX, startingY], [self.locX, self.locY],
                         axisThickness)  # Y Axis
        if (yLines):
            for x in range(self.sizeX):
                if (x % lineDistance == 0):
                    if (shortLines):
                        pygame.draw.line(screen, chartColor, [self.locX + x, self.locY],
                                         [self.locX + x, startingY], markerThickness)
                    else:
                        pygame.draw.line(screen, chartColor, [self.locX + x, self.locY],
                                         [self.locX + x, startingY],
                                         markerThickness)

    def AddLegend(self, colorIds, labels, legendPosition="r", font=None, labelColor="white", size=10, spacing=35):
        labelFont = pygame.font.Font(font, size)  # None means the default font will be used
        labelRectArr = []
        colorRectArr = []
        labelRectTemplate = []
        colorRectTemplate = []
        longestLabel = 0

        adjustInc = size + 10
        adjustY = 0
        for col in labels:
            if (longestLabel < len(col)):
                longestLabel = round(len(col))

        for col in labels:
            if (legendPosition.lower() == "right" or legendPosition.lower() == "r"):
                labelRectTemplate = [self.locX + self.sizeX + size + spacing + 10, self.locY + adjustY, size, size]
                colorRectTemplate = [self.locX + self.sizeX + spacing, self.locY + adjustY, size, size]
            elif (legendPosition.lower() == "left" or legendPosition.lower() == "l"):
                labelRectTemplate = [self.locX - ((size * 2) + longestLabel) - spacing - 10, self.locY + adjustY, size,
                                     size]
                colorRectTemplate = [self.locX - ((size * 3.5) + longestLabel) - spacing, self.locY + adjustY, size,
                                     size]

            colorRectArr.append(colorRectTemplate)
            labelRectArr.append(labelRectTemplate)
            adjustY = adjustY + adjustInc

        for index in range(0, len(colorIds), 1):
            pygame.draw.rect(screen, colorIds[index], colorRectArr[index], size)

            labelText = labelFont.render(labels[index], True, labelColor)
            screen.blit(labelText, labelRectArr[index])

    def AddTitle(self, titleText, size=25, xAdjust=25, yAdjust=10, font=None, titleColor="white", isUnderlined=True):
        titleFont = pygame.font.Font(font, size)  # None means the default font will be used
        titleFont.set_underline(isUnderlined)
        titleText = titleFont.render(titleText, True, titleColor)

        titleRect = [self.locX + xAdjust, self.locY - size - yAdjust, size, size]
        screen.blit(titleText, titleRect)

    def DrawPieChart(self, pieSlices, pieColors=None):
        rect = [self.locX, self.locY, self.sizeX, self.sizeY]
        maxRads = 6.28
        piecePercents = []
        counter = 0
        index = 0
        lastValue = 0
        maxPieVal = 0

        if (pieColors is not None):
            self.pickColor = pieColors

        for piece in pieSlices:
            maxPieVal += piece

        for piece in pieSlices:
            piecePercents.append(piece / maxPieVal)

        for piece in piecePercents:
            pygame.draw.arc(screen, self.pickColor[index], rect, lastValue, lastValue + (piece * maxRads), self.sizeX)
            lastValue += piece * maxRads
            # print(str(lastValue))
            counter += 1
            index = counter % len(self.pickColor)
            # print(pickColor[index] + "-" + str(index))

    def DrawProgressBar(self, value: int, maxValue: int, barColor: str = "red",
                        bracketColor: str = "white", vertical: bool = False):
        barPercent = value / maxValue
        startingY = self.locY + self.sizeY

        if (vertical):
            pygame.draw.line(screen, bracketColor,
                             [self.locX - 2, startingY],
                             [self.locX - 2, self.locY],
                             2)  # Y Axis
            pygame.draw.line(screen, bracketColor,
                             [self.locX + (self.sizeX*0.1), startingY],
                             [self.locX - 2, startingY],
                             2)  # X Axis

            rect = [self.locX, self.locY + (self.sizeY - (self.sizeY * barPercent)),
                    ((self.locX + (self.sizeX*0.1)) - (self.locX - 2)), (self.sizeY * barPercent)]
            pygame.draw.rect(screen, barColor, rect)
        else:  # Horizontal
            pygame.draw.line(screen, bracketColor,
                             [self.locX - 2, startingY + 2],
                             [self.locX - 2, startingY - (5 + self.sizeY * 0.1)],
                             2)  # Y Axis
            pygame.draw.line(screen, bracketColor,
                             [self.locX, startingY + 2],
                             [self.locX + self.sizeX, startingY + 2],
                             2)  # X Axis

            rect = [self.locX, startingY - (self.sizeY * 0.1),
                    self.sizeX * barPercent, self.sizeY * 0.1]
            # print(self.sizeX*barPercent)
            pygame.draw.rect(screen, barColor, rect, round(self.sizeX * barPercent))

    def DrawLineChart(self, lineArray, xLabels, ylabels,
                      chartColor: str = "white", lineColors=None):
        counter = 0
        pickColor = ["red", "blue", "yellow", "green", "purple", "white"]
        biggestX = 0
        biggestY = 0
        startingY = self.locY + self.sizeY

        if (lineColors is not None):
            pickColor = lineColors

        self.__DisplayChartGridLines(True, True, chartColor=chartColor, shortLines=False)

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
                pygame.draw.circle(screen, pickColor[index],
                                   [self.locX + (percentX * self.sizeX),
                                    startingY - (percentY * self.sizeY)], 6)
                if (lastDot != []):
                    pygame.draw.line(screen, pickColor[index],
                                     [self.locX + (percentX * self.sizeX),
                                      startingY - (percentY * self.sizeY)],
                                     [lastDot[0], lastDot[1]], 4)
                lastDot = [self.locX + (percentX * self.sizeX),
                           startingY - (percentY * self.sizeY)]
            counter += 1

    def DrawBarChart(self, valueArray, xLabels: str = "test", ylabels: str = "test",
                     barColors=None, chartColor: str = "white", vertical: bool = True):
        pickColor = ["red", "blue", "yellow", "green", "purple", "white"]
        maxVal = 0
        counter = 0
        index = 0
        barsize = round(self.sizeX / (len(valueArray) + 4))
        startingY = self.locY + self.sizeY

        if (barColors is not None):
            pickColor = barColors

        for bar in valueArray:
            if (bar > maxVal):
                maxVal = bar

        if (vertical):
            self.__DisplayChartGridLines(True, False, chartColor=chartColor, shortLines=False)

            for bar in valueArray:
                barPercent = bar / maxVal
                if (counter == 0):
                    rect = [self.locX + (counter * barsize) + 10,
                            (self.locY) + (self.sizeY * (1 - barPercent)),
                            barsize,
                            self.sizeY * barPercent]
                else:
                    rect = [self.locX + (counter * barsize) + (10 * counter) + 10,
                            (self.locY) + (self.sizeY * (1 - barPercent)),
                            barsize,
                            self.sizeY * barPercent]
                pygame.draw.rect(screen, pickColor[index], rect, barsize)
                counter += 1
                index = counter % len(pickColor)
        else:  # Horizontal Bars
            self.__DisplayChartGridLines(False, True, chartColor=chartColor, shortLines=False)

            for bar in valueArray:
                barPercent = bar / maxVal
                if (counter == 0):
                    rect = [self.locX + 3,
                            startingY - (counter * barsize) - 40,
                            self.sizeX * barPercent,
                            barsize]
                else:
                    rect = [self.locX + 3,
                            startingY - (counter * barsize) - (10 * counter) - 40,
                            self.sizeX * barPercent,
                            barsize]
                pygame.draw.rect(screen, pickColor[index], rect, barsize)
                counter += 1
                index = counter % len(pickColor)

    def DrawScatterPlot(self, pointArray, xLabels, ylabels, pointColor: str = "white", chartColor: str = "white"):
        biggestX = 0
        biggestY = 0
        startingY = self.locY + self.sizeY

        self.__DisplayChartGridLines(True, True, chartColor=chartColor, shortLines=False)

        for dot in pointArray:
            if (dot[0] > biggestX):
                biggestX = dot[0]
            if (dot[1] > biggestY):
                biggestY = dot[1]

        for dot in pointArray:
            percentX = dot[0] / biggestX
            percentY = dot[1] / biggestY
            pygame.draw.circle(screen, pointColor,
                               [self.locX + (percentX * self.sizeX), startingY - (percentY * self.sizeY)], 6)

    def DrawValueDisplay(self, label: str, value: str, size: int, Symbol: str = None,
                         valueColor: str = "black", labelColor: str = "black", font: str = None):
        labelFont = pygame.font.Font(font, size)  # None means the default font will be used
        valueFont = pygame.font.Font(font, size * 2)

        labelText = labelFont.render(label, True, labelColor)
        valueText = valueFont.render(value, True, valueColor)

        labelRect = [self.locX, self.locY, size, size]
        valueRect = [self.locX - 25, self.locY + 32, size * 2, size * 2]

        screen.blit(labelText, labelRect)
        screen.blit(valueText, valueRect)

    def DemoCharts(self, chartType):
        if (chartType.lower() == 'pie'):
            self.DrawPieChart([self.p1, self.p2, self.p3, self.p4, self.p5, self.p6])

        if (chartType.lower() == 'vprogress'):
            self.DrawProgressBar(self.p1 + self.p2 + self.p3, self.p1 + self.p2 + self.p3 + self.p4, "red", "white",
                                 True)
        if (chartType.lower() == 'hprogress'):
            self.DrawProgressBar(self.p1 + self.p2, self.p1 + self.p2 + self.p3, "red", "white", False)

        if (chartType.lower() == 'value'):
            self.DrawValueDisplay("TEST", "100%", 35, None, "white", "white")

        if (chartType.lower() == 'scatter'):
            dotsExample = [[10, 15], [5, 95], [80, 85], [62, 33], [25, 25], [35, 50]]
            self.DrawScatterPlot(dotsExample, "", "", "red", "white")

        if (chartType.lower() == 'vbar'):
            self.DrawBarChart([45, 55, 10, 90, 33, 25], "xLabels", "ylabels", vertical=True)

        if (chartType.lower() == 'hbar'):
            self.DrawBarChart([45, 55, 10, 90, 33, 25], "xLabels", "ylabels", vertical=False)

        if (chartType.lower() == 'line'):
            lineExample = [
                [[0, 0], [50, self.p1], [100, self.p2]],
                [[0, 10], [50, self.p7/2], [100, 50]],
                [[0, 0], [22, 60], [75, self.p7], [100,100]],
                [[0, 100], [50, self.p5], [65, self.p6*2]]
            ]
            self.DrawLineChart(lineExample, "xLabels", "ylabels", "white")


###############################################################################################################
chart1 = PygameGraph(screen, 100, 100, 250, 250)
chart2 = PygameGraph(screen, 600, 100, 250, 250)
chart3 = PygameGraph(screen, 820, 440, 250, 250)
chart4 = PygameGraph(screen, 100, 400, 250, 250)
chart5 = PygameGraph(screen, 475, 400, 250, 250)
chart6 = PygameGraph(screen, 400, 400, 250, 250)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    chart1.DemoCharts("line")
    chart1.AddTitle("TEST TITLE", size=35)
    chart1.AddLegend(chart1.pickColor, chart1.labelarr, "right", size=35)
    chart2.DemoCharts("vbar")
    chart3.DemoCharts("pie")
    chart3.AddTitle("TEST TITLE", size=35)
    chart3.AddLegend(chart1.pickColor, chart1.labelarr, "right", size=35)
    chart4.DemoCharts("scatter")
    chart5.DemoCharts("hprogress")
    chart6.DemoCharts("vprogress")
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
