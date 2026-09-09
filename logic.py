import random

class Logic:
    matrix = []

    def __init__(self):
        self.matrix =  [[0] * 4 for _ in range(4)]

        self.start()

    def start(self):
        cell_value = 0

        if random.randint(1, 10) >= 6:
            cell_value = 4
        else:
            cell_value = 2
            
        array = []

        for y in self.matrix:
            for x in y:
                if self.matrix[y][x] == 0:
                    array.append("" + y + x)
        
        coords = array[random.randint(0, len(array) - 1)]

        self.matrix[coords[0]][coords[1]] = cell_value

    def move(self, direction):
        dx = 0
        dy = 0

        if direction == "left": dx = -1
        if direction == "top": dy = -1
        if direction == "rigth": dx = 1
        if direction == "bottom": dy = 1

        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if self.matrix[y][x] != 0:
                    coords = self.utalite_move(y, x, dy, dx)

                    self.matrix[coords.y][coords.x] = self.matrix[y][x]
                    self.matrix[y][x] = 0
                    



    def utalite_move(self,y, x, dy, dx):
        if dy > 0:
            for index_y in range(y + 1, len(self.matrix)):
                if self.matrix[index_y, x] != 0: return {y: index_y, x: x}
            return {y: len(self.matrix), x: x}

        if dy < 0:
            for index_y in range(y - 1, -1):
                if self.matrix[index_y, x] != 0: return {y: index_y, x: x}
            return {y: 0, x: x}

        if dx > 0:
            for index_x in range(x + 1, len(self.matrix)):
                if self.matrix[y, index_x] != 0: return {y: y, x: index_x}
            return {y: y, x: len(self.matrix) - 1}

        if dx < 0:
            for index_y in range(x - 1, -1):
                if self.matrix[y, index_x] != 0: return {y: y, x: index_x}
            return {y: y, x: 0}