from typing import List, Tuple


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


class Painter:
    @staticmethod
    def _can_move(jump_point, field, direction):
        # Тут возможны два случая. Само по себе поле закончилось или же уже закрашено
        # 1) Прыгать нельзя, если точка приземления находится вне поля
        # 2) Прыгать нельзя если следующая от точки приземления клетка закрашена:

        # 1
        if jump_point[0] >= len(field[0]) or jump_point[1] >= len(field[0]) or jump_point[0] < 0 or jump_point[1] < 0:
            return False

        # 2
        next_after_jump = [coord_1 + coord_2 for coord_1, coord_2 in zip(jump_point, direction)]

        if next_after_jump[0] == len(field[0]) or next_after_jump[1] == len(field[0]) or next_after_jump[0] < 0 or next_after_jump[1] < 0:
            return True

        if field[next_after_jump[0]][next_after_jump[1]] == "0":
            return False

        return True

    def __init__(self, x: int, y: int, jump_sequence: Tuple[Tuple[int, int]]):
        self.x = x
        self.y = y
        self.jump_sequence = jump_sequence

    def paint(self, field: List[List[str]]) -> None:
        field[self.x][self.y] = '0'

    def move(self, field):
        curr_direction_idx = 0
        have_tried = [0, 0, 0, 0]
        while True:
            self.paint(field)

            while True:
                next_point = (self.x + self.jump_sequence[curr_direction_idx][0],
                              self.y + self.jump_sequence[curr_direction_idx][1])

                if Painter._can_move(next_point, field, self.jump_sequence[curr_direction_idx]):
                    self.x = next_point[0]
                    self.y = next_point[1]
                    break

                have_tried[curr_direction_idx] = 1
                curr_direction_idx += 1

                if curr_direction_idx == len(self.jump_sequence):
                    curr_direction_idx = 0

                if 0 not in have_tried:
                    return




def create_field(l: int):
    field = [['.' for _ in range(l)] for _ in range(l)]
    return field


field = create_field(6)
painter = Painter(0, 0, (RIGHT, DOWN, LEFT, UP))
painter.move(field)

for i in field:
    for j in i:
        print(j, end='')
    print()