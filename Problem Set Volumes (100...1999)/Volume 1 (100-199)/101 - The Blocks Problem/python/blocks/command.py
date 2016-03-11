from blocks import Blocks


class Command(object):

    blocks = None
    finish = False

    def read(self, line):
        if self.blocks is None:
            self.blocks = Blocks(int(line))
        else:
            if line == "quit":
                self.finish = True
                self.output()
            else:
                self.parse(line)

    def parse(self, line):
        action, block, pos, des = line.split(" ")
        if action == "move":
            if pos == "onto":
                self.blocks.move_onto(int(block), int(des))
            elif pos == "over":
                self.blocks.move_over(int(block), int(des))
        elif action == "pile":
            if pos == "onto":
                self.blocks.pile_onto(int(block), int(des))
            elif pos == "over":
                self.blocks.pile_over(int(block), int(des))

    def output(self):
        for i, blocks in enumerate(self.blocks.blocks):
            print "%d:" % i,
            for block in blocks:
                print "%d" % block,
            print

    def start(self):
        while not self.finish:
            self.read(raw_input())
