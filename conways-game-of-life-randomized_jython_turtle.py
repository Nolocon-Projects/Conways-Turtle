# Conways Game of Life - Jython Turtle Version (Randomized Start)
# © 2026 XeraoXX & Github Contributors | Licensed under GNU GPL v3
# https://github.com/Nolocon-Projects/Conways-Turtle
# This project requires Jython. Get it on https://www.jython.org/download.html
from gturtle import *
import time
import random

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
        self.activatedFields = set(
            (x, y)
            for x in range(-(512 // boxSize), 512 // boxSize + 1)
            for y in range(-(384 // boxSize), 384 // boxSize + 1)
            if random.random() < 0.3
        )
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
