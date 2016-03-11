from exceptions import BlockNotFound


class Blocks:

    def __init__(self, size=None):
        if size is not None:
            self.set_size(size)

    def set_size(self, size):
        self.blocks = range(size)
        self.update_structure()

    def update_structure(self):
        self.blocks = [[i] for i in self.blocks]

    def position(self, block):
        for i, row in enumerate(self.blocks):
            for j, column in enumerate(row):
                if column == block:
                    return (i, j)
        raise BlockNotFound

    def remove_block(self, i, j):
        del self.blocks[i][j]

    def remove_pile(self, block):
        pos = self.position(block)
        pile = self.blocks[pos[0]][pos[1]:]
        self.blocks[pos[0]] = list(set(self.blocks[pos[0]]) - set(pile))
        return pile

    def check_pile_movement(self, a, b):
        pos_a = self.position(a)
        pos_b = self.position(b)
        if pos_a[0] == pos_b[0]:
            if pos_a[1] <= pos_b[1]:
                return False
        return True

    def move_onto(self, a, b):
        pos_a = self.position(a)
        self.remove_block(pos_a[0], pos_a[1])
        pos_b = self.position(b)
        self.blocks[pos_b[0]].insert(pos_b[1] + 1, a)

    def move_over(self, a, b):
        pos_a = self.position(a)
        self.remove_block(pos_a[0], pos_a[1])
        pos_b = self.position(b)
        self.blocks[pos_b[0]].append(a)

    def pile_onto(self, a, b):
        if self.check_pile_movement(a, b):
            pile = self.remove_pile(a)
            pos = self.position(b)
            index = 1
            for i in pile:
                self.blocks[pos[0]].insert(pos[1] + index, i)
                index = index + 1

    def pile_over(self, a, b):
        if self.check_pile_movement(a, b):
            pile = self.remove_pile(a)
            pos = self.position(b)
            self.blocks[pos[0]].extend(pile)
