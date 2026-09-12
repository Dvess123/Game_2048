import random


class Logic:
    def __init__(self):
        self.board_size = 4
        self.matrix = [
            [0] * self.board_size
            for _ in range(self.board_size)
        ]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()

    def slide(self, direction):
        old_matrix = [row[:] for row in self.matrix]
        lines = self.get_lines(direction)

        if lines is None:
            return False, []

        new_matrix = [
            [0] * self.board_size
            for _ in range(self.board_size)
        ]

        moves = []

        for line in lines:
            tiles = []

            for y, x in line:
                value = self.matrix[y][x]

                if value != 0:
                    tiles.append({
                        "y": y,
                        "x": x,
                        "value": value
                    })

            result_index = 0
            i = 0

            while i < len(tiles):
                current = tiles[i]
                target_y, target_x = line[result_index]

                if (
                    i + 1 < len(tiles)
                    and current["value"] == tiles[i + 1]["value"]
                ):
                    second = tiles[i + 1]
                    new_value = current["value"] * 2

                    new_matrix[target_y][target_x] = new_value

                    moves.append({
                        "old_y": current["y"],
                        "old_x": current["x"],
                        "new_y": target_y,
                        "new_x": target_x,
                        "value": current["value"],
                        "merged": True
                    })

                    moves.append({
                        "old_y": second["y"],
                        "old_x": second["x"],
                        "new_y": target_y,
                        "new_x": target_x,
                        "value": second["value"],
                        "merged": True
                    })

                    self.score += new_value
                    i += 2

                else:
                    new_matrix[target_y][target_x] = current["value"]

                    moves.append({
                        "old_y": current["y"],
                        "old_x": current["x"],
                        "new_y": target_y,
                        "new_x": target_x,
                        "value": current["value"],
                        "merged": False
                    })

                    i += 1

                result_index += 1

        changed = old_matrix != new_matrix

        if not changed:
            return False, []

        self.matrix = new_matrix

        return True, moves

    def get_lines(self, direction):
        if direction == "left":
            return [
                [(y, x) for x in range(self.board_size)]
                for y in range(self.board_size)
            ]

        if direction == "right":
            return [
                [
                    (y, x)
                    for x in range(self.board_size - 1, -1, -1)
                ]
                for y in range(self.board_size)
            ]

        if direction == "top":
            return [
                [(y, x) for y in range(self.board_size)]
                for x in range(self.board_size)
            ]

        if direction == "bottom":
            return [
                [
                    (y, x)
                    for y in range(self.board_size - 1, -1, -1)
                ]
                for x in range(self.board_size)
            ]

        return None

    def spawn_tile(self):
        empty_cells = []

        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.matrix[y][x] == 0:
                    empty_cells.append((y, x))

        if not empty_cells:
            return None

        y, x = random.choice(empty_cells)

        if random.randint(1, 10) >= 6:
            value = 4
        else:
            value = 2

        self.matrix[y][x] = value

        return {
            "y": y,
            "x": x,
            "value": value
        }

    def is_game_over(self):
        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.matrix[y][x] == 0:
                    return False

        for y in range(self.board_size):
            for x in range(self.board_size - 1):
                if self.matrix[y][x] == self.matrix[y][x + 1]:
                    return False

        for y in range(self.board_size - 1):
            for x in range(self.board_size):
                if self.matrix[y][x] == self.matrix[y + 1][x]:
                    return False

        return True