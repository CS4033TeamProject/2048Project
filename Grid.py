import Tile
import math
import random
class Grid():
    def __init__(self, size, previousState = None) -> None:
        self.size = size
        self.cells = self.fromState(previousState) if previousState else self.empty()


    # Build a grid of the specified size
    def empty(self):
        cells = []

        for x in range(self.size):
            cells.append([])
            row = cells[x]

            for y in range(self.size):
                row.append(None)

        return cells

    def fromState(self, state):
        cells = []

        for x in range(self.size):
            row = cells[x] = []

            for y in range(self.size):
                tile = state[x][y]
                row.push(tile if Tile(tile.position, tile.value) else None)

        return cells

    # Find the first available random position
    def randomAvailableCell(self):
        cells = self.availableCells()

        if (len(cells)):
            return cells[math.floor(random.random() * len(cells))]

    def availableCells(self):
        cells = []

        def callback(x, y, tile):
            if (not tile): 
                cells.append({ "x": x, "y": y })

        self.eachCell(callback)
        return cells

    # Call callback for every cell
    def eachCell(self, callback):
        for x in range(self.size):
            for y in range(self.size):
                callback(x, y, self.cells[x][y])

    # Check if there are any cells available
    def cellsAvailable(self):
        return bool(len(self.availableCells()))

    # Check if the specified cell is taken
    def cellAvailable(self, cell):
        return not self.cellOccupied(cell)

    def cellOccupied(self, cell):
        return bool(self.cellContent(cell))

    def cellContent(self, cell):
        if (self.withinBounds(cell)):
            return self.cells[cell["x"]][cell["y"]]
        else:
            return None

    # Inserts a tile at its position
    def insertTile(self, tile):
        self.cells[tile.x][tile.y] = tile

    def removeTile(self, tile):
        self.cells[tile.x][tile.y] = None

    def withinBounds(self, position):
        return (position["x"] >= 0) and (position["x"] < self.size) and (position["y"] >= 0) and (position["y"] < self.size)

    def printToTerminal(self):
        for y in range(self.size):
            row = "["
            for x in range(self.size):
                if self.cells[x][y] == None: row = row + "0 "
                else: row = row + str(self.cells[x][y].value) + " "
            row = row[:-1] + "]"
            print(row)

    def serialize(self):
        cellState = []

        for x in range(self.size):
            cellState.append([])
            row = cellState[x]

            for y in range(self.size):
                row.append(self.cells[x][y].serialize() if self.cells[x][y] else None)

        return {
            "size": self.size,
            "cells": cellState}