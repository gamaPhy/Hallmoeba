from pcbnewTransition.pcbnew import BOX2I, VECTOR2I

def mmToNm(mm):
    return int(mm * 1000000)
    
def vec(x, y):
    return VECTOR2I(mmToNm(x), mmToNm(y))
    
def kikitPostprocess(panel, args):
    rows = int(args.split(',')[0])
    cols = int(args.split(',')[1])
    for i in panel.board.GetPads():
        if (i.GetAttribute() == 3 and i.GetDrillSize().x == 500000 and (i.GetPosition().x - 119925000) % 19050000 == 0):
            #panel.addNPTHole(VECTOR2I(i.GetPosition().x, i.GetPosition().y + 8740000), mmToNm(0.5))
            if (i.GetPosition().x  == 119925000):
                panel.addNPTHole(VECTOR2I(i.GetPosition().x - 19050000, i.GetPosition().y), mmToNm(0.5))
                #panel.addNPTHole(VECTOR2I(i.GetPosition().x - 19050000, i.GetPosition().y + 8740000), mmToNm(0.5))
            if (i.GetPosition().x == 119925000 + (cols - 2) * 19050000):
                panel.addNPTHole(VECTOR2I(i.GetPosition().x + 19050000, i.GetPosition().y), mmToNm(0.5))
                #panel.addNPTHole(VECTOR2I(i.GetPosition().x + 19050000, i.GetPosition().y + 8740000), mmToNm(0.5))
    
    for r in range(0, rows):
        y = 29.525 + r * 19.05
        panel.appendBoard('../../tab/tab.kicad_pcb', vec(98.375, y), BOX2I(vec(0, 0), vec(100, 100)), shrink=True, tolerance=mmToNm(5), inheritDrc=False)
        panel.appendBoard('../../tab/tab.kicad_pcb', vec(103.375 + 19.05 * cols, y), BOX2I(vec(100, 0), vec(150, 100)), shrink=True, tolerance=mmToNm(5), inheritDrc=False)
