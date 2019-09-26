from graph import *
def ellipse( a, b, x0, y0):
    x = a
    y = 0
    s = [(x0 + a, y0)]
    for i in range(2 * a):
        x -= 1
        y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        s.append((x + x0, y + y0))
    for i in range(2 * a):
        x += 1
        y = -(((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
        s.append((x + x0, y + y0))
    polygon(s)

windowSize(1760, 769)
canvasSize(1760, 769)



penColor('orange')
brushColor('orange')
circle(463, 769, 300)

brushColor(233, 200, 176)
penColor(200, 200, 200)
circle(463, 384, 200)
penColor(0, 0, 0)

brushColor(100, 100, 255)
penColor('black')
ellipse(48,30,528, 349)
ellipse(48,30,398,349)
brushColor('black')
circle(528, 349, 10)
circle(398 , 349, 10)

brushColor('brown')
polygon([(483, 394), (443, 394), (463, 424)])

brushColor('red')
polygon([(333, 454), (613, 454), (463, 534)])



brushColor(233, 200, 176)
penColor(200, 200, 200)
polygon([(230, 569), (270, 549), (180, 150), (140, 130)])
polygon([(630, 549), (670, 569), (880, 150), (840, 130)])

penColor('white')
circle(160, 115, 40)
circle(870, 115, 40)


penColor('black')
brushColor('orange')
circle(260,549,60)
circle(665,549,60)

brushColor('purple')
polygon([(293,275), (336,219), (267,205)])
polygon([(316,230), (378,200), (329,166)])
polygon([(362,201), (431,186), (377,149)])
polygon([(417,184), (476,180), (436,144)])
polygon([(457,187), (509,186), (486,143)])
polygon([(498,178), (543,200), (525,151)])
polygon([(532,187), (586,220), (573,152)])
polygon([(576,206), (621,253), (615,182)])
polygon([(608,235), (644,289), (674,218)])


#copy start
penColor('orange')
brushColor('green')
circle(1263, 769, 300)

brushColor(233, 200, 176)
penColor(200, 200, 200)
circle(1263, 384, 200)
penColor(0, 0, 0)

brushColor(191, 200, 183)
penColor('black')
ellipse(48,30,1328, 349)
ellipse(48,30,1198 , 349)
brushColor('black')
circle(1328, 349, 10)
circle(1198 , 349, 10)

brushColor('brown')
polygon([(1283, 394), (1243, 394), (1263, 424)])

brushColor('red')
polygon([(1133, 454), (1413, 454), (1263, 534)])



brushColor(233, 200, 176)
penColor(200, 200, 200)
polygon([(1030, 569), (1070, 549), (980, 150), (940, 130)])
polygon([(1430, 549), (1470, 569), (1680, 150), (1640, 130)])

penColor('white')
circle(960, 115, 40)
circle(1670, 115, 40)


penColor('black')
brushColor('green')
circle(1060,549,60)
circle(1465,549,60)

brushColor('yellow')
polygon([(1093,275), (1136,219), (1067,205)])
polygon([(1116,230), (1178,200), (1129,166)])
polygon([(1162,201), (1231,186), (1177,149)])
polygon([(1217,184), (1276,180), (1236,144)])
polygon([(1257,187), (1309,186), (1286,143)])
polygon([(1298,178), (1343,200), (1325,151)])
polygon([(1332,187), (1386,220), (1373,152)])
polygon([(1376,206), (1421,253), (1415,182)])
polygon([(1408,235), (1444,289), (1474,218)])
#copy end
brushColor('black')


label('PYTHON is REALLY AMAZING!', 00, 00, font=('Arial 32', 90, 'bold'), bg='green', foreground='black')

run()


