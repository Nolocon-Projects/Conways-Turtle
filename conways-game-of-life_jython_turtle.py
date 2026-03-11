# Conways Game of Life - Jython Turtle Version
# © 2026 XeraoXX & Github Contributors | Licensed under GNU GPL v3

# This project requires Jython. Get it on https://www.jython.org/download.html
from gturtle import *
import time

boxSize = inputInt("Box Size: ")
waitingDuration = inputFloat("Time between generations (in s): ")

class visualManager():
    def drawField(self, field):
        coord_x = field[0]*boxSize
        coord_y = field[1]*boxSize
        setPos(coord_x, coord_y)
        penDown()
        repeat 4:
            forward(boxSize)
            right(90)
        fill()
        penUp()
        
    def visualize(self, fields):
        for field in fields:
            self.drawField(field)

class logicManager():
    def __init__(self):
        setPlaygroundSize(1024, 768)
        makeTurtle()
        self.activatedFields = set([
            # Glider 1
            (0,0),(1,0),(2,0),(2,-1),(1,-2),
            # Glider 2
            (10,5),(11,5),(12,5),(12,4),(11,3),
            # LWSS
            (20,10),(20,11),(20,12),(20,13),(21,9),(21,13),(22,9),(22,13),(23,9),(23,10),(23,11),(23,12),
            # Blinker
            (5,20),(6,20),(7,20),
            # Toad
            (15,18),(16,18),(17,18),(14,19),(15,19),(16,19),
            # Beacon
            (30,0),(31,0),(30,1),(31,1),(32,2),(33,2),(32,3),(33,3),
            # Block
            (0,30),(1,30),(0,31),(1,31),
            # Beehive
            (5,35),(6,35),(4,36),(7,36),(5,37),(6,37),
            # Loaf
            (10,30),(11,30),(9,31),(12,31),(10,32),(12,32),(11,33),
            # Boat
            (20,25),(21,25),(20,26),(22,26),(21,27),
            # Tub
            (25,30),(24,31),(26,31),(25,32),
            # Glider Gun
            (40,5),(40,6),(41,5),(41,6),
            (50,5),(50,6),(50,7),(51,4),(51,8),(52,3),(52,9),(53,3),(53,9),(54,6),
            (55,4),(55,8),(56,5),(56,6),(56,7),(57,6)
        ])
        setTitle("Conways Game Of Life")
        setPenColor("black")
        setFillColor("black") 
        hideTurtle()
        penUp()
        # List of possible neighbor (offsets)
        self.neighborOffsets = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)
        ]
        self.visual = visualManager()
    
    def getNeighborAmount(self, field, fieldsSet):
        coord_x = field[0]
        coord_y = field[1]
        amountNeighbors = 0

        for dx, dy in self.neighborOffsets:
            if (coord_x+dx, coord_y+dy) in fieldsSet:
                amountNeighbors += 1
        return amountNeighbors
        
    def updateGeneration(self, currentFieldsSet):
        newFieldsSet = set()
        neighborCounts = {}

        # 1. Survival of fields
        for field in currentFieldsSet:
            neighbors = self.getNeighborAmount(field, currentFieldsSet)
            if neighbors == 2 or neighbors == 3:
                newFieldsSet.add(field)
            
            # Count neighbors
            for dx, dy in self.neighborOffsets:
                neighbor = (field[0]+dx, field[1]+dy)
                if neighbor not in currentFieldsSet:
                    if neighbor not in neighborCounts:
                        neighborCounts[neighbor] = 1
                    else:
                        neighborCounts[neighbor] += 1

        # 2. Birth
        for cell, count in neighborCounts.items():
            if count == 3:
                newFieldsSet.add(cell)
        # If not added, they died.
        return newFieldsSet
            
    def run(self):
        while True:
            clear()
            self.visual.visualize(self.activatedFields)
            self.activatedFields = self.updateGeneration(self.activatedFields)
            time.sleep(waitingDuration)
        
if __name__ == "__main__":
    logicManager().run()