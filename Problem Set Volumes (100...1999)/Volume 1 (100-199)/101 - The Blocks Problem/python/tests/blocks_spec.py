import unittest
from blocks import Blocks


class TestBlocks(unittest.TestCase):

    def setUp(self):
        self.blocks = Blocks()
        self.result = [
            [0],
            [1, 9, 2, 4],
            [],
            [3],
            [],
            [5, 8, 7, 6],
            [],
            [],
            [],
            []
        ]
        self.example = [
            [0],
            [1, 2, 3, 4],
            [],
            [],
            [],
            [5, 6, 7, 8],
            [],
            [],
            [],
            [9]
        ]

    def test_amount_blocks(self):
        self.blocks.set_size(10)
        self.assertEqual(len(self.blocks.blocks), 10)

    def test_constructor_settings_size(self):
        self.blocks = Blocks(10)
        self.assertEqual(len(self.blocks.blocks), 10)

    def test_update_blocks_structure(self):
        self.blocks = Blocks(10)
        self.assertEqual(type(self.blocks.blocks[0]), type([]))

    def test_position_index(self):
        self.blocks = Blocks(10)
        self.blocks.blocks = self.result
        positions = self.blocks.position(9)
        self.assertEqual(positions, (1, 1))

    def test_remove_block_9(self):
        self.blocks = Blocks(10)
        self.blocks.blocks = self.result
        self.blocks.remove_block(1, 1)
        self.assertEqual(self.blocks.blocks[1][1], 2)

    def test_remove_block_4(self):
        self.blocks = Blocks(10)
        self.blocks.blocks = self.result
        self.blocks.remove_block(1, 3)
        with self.assertRaises(IndexError):
            self.blocks.blocks[1][3]

    def test_check_pile_movement_same_pile(self):
        self.blocks = Blocks(10)
        self.blocks.blocks = self.example
        check = self.blocks.check_pile_movement(2, 3)
        self.assertFalse(check)

    def test_check_pile_movement_different_pile(self):
        self.blocks = Blocks(10)
        self.blocks.blocks = self.example
        check = self.blocks.check_pile_movement(6, 2)
        self.assertTrue(check)

    def test_remove_pile_2(self):
        self.blocks = Blocks(10)
        self.blocks.blocks = self.example
        pile = self.blocks.remove_pile(2)
        self.assertEqual(self.blocks.blocks[1], [1])
        self.assertEqual(pile, [2, 3, 4])

    def test_remove_pile_4(self):
        self.blocks = Blocks(10)
        self.blocks.blocks = self.example
        pile = self.blocks.remove_pile(4)
        self.assertEqual(self.blocks.blocks[1], [1, 2, 3])
        self.assertEqual(pile, [4])

    def test_move_9_onto_1(self):
        self.blocks = Blocks(10)
        self.blocks.move_onto(9, 1)
        self.assertEqual(self.blocks.blocks[1], [1, 9])

    def test_move_9_over_1(self):
        self.blocks = Blocks(10)
        self.blocks.move_over(9, 1)
        self.blocks.move_over(2, 1)
        self.assertEqual(self.blocks.blocks[1], [1, 9, 2])

    def test_pile_8_onto_1(self):
        self.blocks = Blocks(10)
        self.blocks.pile_onto(8, 1)
        self.assertEqual(self.blocks.blocks[1], [1, 8])

    def test_pile_8_onto_1(self):
        self.blocks = Blocks(10)
        self.blocks.move_onto(8, 5)
        self.blocks.move_over(6, 5)
        self.blocks.move_over(7, 5)
        self.blocks.pile_onto(8, 1)
        self.assertEqual(self.blocks.blocks[1], [1, 8, 6, 7])

    def test_pile_8_onto_2_same_column(self):
        self.blocks = Blocks(10)
        self.blocks.move_onto(8, 5)
        self.blocks.move_over(2, 8)
        self.blocks.move_over(7, 8)
        self.blocks.pile_onto(8, 2)
        self.assertEqual(self.blocks.blocks[5], [5, 8, 2, 7])

    def test_pile_8_onto_1_with_9(self):
        self.blocks = Blocks(10)
        self.blocks.move_onto(8, 5)
        self.blocks.move_onto(9, 1)
        self.blocks.move_over(6, 5)
        self.blocks.move_over(7, 5)
        self.blocks.pile_onto(8, 1)
        self.assertEqual(self.blocks.blocks[1], [1, 8, 6, 7, 9])

    def test_pile_8_over_1(self):
        self.blocks = Blocks(10)
        self.blocks.move_onto(8, 5)
        self.blocks.move_over(6, 5)
        self.blocks.move_over(7, 5)
        self.blocks.pile_over(8, 1)
        self.assertEqual(self.blocks.blocks[1], [1, 8, 6, 7])

    def test_pile_8_over_1_with_9(self):
        self.blocks = Blocks(10)
        self.blocks.move_onto(8, 5)
        self.blocks.move_onto(9, 1)
        self.blocks.move_over(6, 5)
        self.blocks.move_over(7, 5)
        self.blocks.pile_onto(8, 1)
        self.assertEqual(self.blocks.blocks[1], [1, 8, 6, 7, 9])

    def test_final(self):
        self.blocks = Blocks(10)
        self.blocks.move_onto(9, 1)
        self.blocks.move_over(8, 1)
        self.blocks.move_over(7, 1)
        self.blocks.move_over(6, 1)
        self.blocks.pile_over(8, 6)
        self.blocks.pile_over(8, 5)
        self.blocks.move_over(2, 1)
        self.blocks.move_over(4, 9)
        self.assertEqual(self.blocks.blocks, self.result)
