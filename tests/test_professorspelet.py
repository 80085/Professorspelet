import unittest
from professorspelet.professorspelet import Professor, Tile, Puzzle

class TestProfessor(unittest.TestCase):
    def test_create_is_case_insensitve(self):
        professor = Professor('Upper', 'Blue')
        self.assertEqual(professor.body, 'upper')
        self.assertEqual(professor.color, 'blue')

    def test_create_raises_for_invalid_body_part(self):
        with(self.assertRaisesRegex(ValueError, 'body')):
            Professor('middle', 'blue')

    def test_create_raises_for_invalid_color(self):
        with(self.assertRaisesRegex(ValueError, 'color')):
            Professor('upper', 'red')

    def test_has_a_meaningful_str_representation(self):
        professor = Professor('Upper', 'Blue')
        self.assertEqual(str(professor), 'upper - blue')

    def test_matches(self):
        first = Professor('upper', 'blue')
        second = Professor('lower', 'blue')
        self.assertTrue(first.matches(second))

    def test_matches_body_part_mismatch(self):
        first = Professor('lower', 'blue')
        second = Professor('lower', 'blue')
        self.assertFalse(first.matches(second))

    def test_matches_color_mismatch(self):
        first = Professor('upper', 'purple')
        second = Professor('lower', 'blue')
        self.assertFalse(first.matches(second))


class TestTile(unittest.TestCase):
    def test_create_too_few_professors(self):
        professor = Professor('lower', 'green')
        with(self.assertRaisesRegex(ValueError, 'Expected four professor')):
            Tile([professor] * 3)

    def test_create_too_many_professors(self):
        professor = Professor('lower', 'purple')
        with(self.assertRaisesRegex(ValueError, 'Expected four professor')):
            Tile([professor] * 5)

    def test_create_not_equal_number_of_upper_and_lower_body(self):
        professor = Professor('lower', 'purple')
        with(self.assertRaisesRegex(ValueError, 'Expected equal number of upper and lower body parts')):
            Tile([professor] * 4)

    def test_stores_correct_professor_in_correct_place(self):
        professors = [Professor('lower', 'purple'), Professor('lower', 'blue'), Professor('upper', 'green'), Professor('upper', 'brown')]
        tile = Tile(professors)
        self.assertEqual(tile.top(), professors[0])
        self.assertEqual(tile.right(), professors[1])
        self.assertEqual(tile.bottom(), professors[2])
        self.assertEqual(tile.left(), professors[3])

    def test_rotate_clockwise(self):
        professors = [Professor('lower', 'purple'), Professor('lower', 'blue'), Professor('upper', 'green'), Professor('upper', 'brown')]
        tile = Tile(professors)
        tile.rotate()
        self.assertEqual(tile.top(), professors[3])
        self.assertEqual(tile.right(), professors[0])
        self.assertEqual(tile.bottom(), professors[1])
        self.assertEqual(tile.left(), professors[2])

    def test_rotate_counter_clockwise(self):
        professors = [Professor('lower', 'purple'), Professor('lower', 'blue'), Professor('upper', 'green'), Professor('upper', 'brown')]
        tile = Tile(professors)
        tile.rotate(-1)
        self.assertEqual(tile.top(), professors[1])
        self.assertEqual(tile.right(), professors[2])
        self.assertEqual(tile.bottom(), professors[3])
        self.assertEqual(tile.left(), professors[0])

    def test_tile_has_a_meaningful_str_representation(self):
        professors = [Professor('lower', 'purple'), Professor('lower', 'blue'), Professor('upper', 'green'), Professor('upper', 'brown')]
        tile_str = str(Tile(professors))
        for p in professors:
            self.assertTrue(str(p) in tile_str, f'Expected {p} to be in tile string representation')


class TestPuzzle(unittest.TestCase):
    def test_constructor_raises_when_too_many_tiles_given(self):
        tiles = [Tile([Professor('lower', 'green')] * 2 + [Professor('upper', 'green')] * 2)] * 17
        with(self.assertRaisesRegex(ValueError, 'Maximum number of Professor tiles that can be placed is 16, was: 17')):
            Puzzle(tiles)

    def test_can_place_tile_when_grid_is_empty(self):
        tile = Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])
        puzzle = Puzzle([])
        self.assertTrue(puzzle._can_place_tile(tile, 0))

    def test_can_place_tile_raises_when_position_is_occupied(self):
        tile = Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])
        puzzle = Puzzle([])
        puzzle.grid[0] = tile
        with(self.assertRaisesRegex(ValueError, 'Index.*is not empty')):
            puzzle._can_place_tile(tile, 0)

    def test_can_place_tile_true_when_match(self):
        first_tile = Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])
        second_tile = Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])
        puzzle = Puzzle([])
        puzzle.grid[0] = first_tile
        self.assertTrue(puzzle._can_place_tile(second_tile, 1))

    def test_can_place_tile_false_when_body_mismatch(self):
        first_tile = Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])
        second_tile = Tile([Professor('upper', 'green'), Professor('upper', 'green'), Professor('lower', 'green'), Professor('lower', 'green')])
        puzzle = Puzzle([])
        puzzle.grid[0] = first_tile
        self.assertFalse(puzzle._can_place_tile(second_tile, 1))

    def test_can_place_tile_false_when_color_mismatch(self):
        all_green_tile = Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])
        all_blue_tile = Tile([Professor('lower', 'blue'), Professor('lower', 'blue'), Professor('upper', 'blue'), Professor('upper', 'blue')])
        puzzle = Puzzle([])
        puzzle.grid[0] = all_green_tile
        self.assertFalse(puzzle._can_place_tile(all_blue_tile, 1))

    def test_can_place_tile_if_all_neighboring_tiles_match(self):
        puzzle = Puzzle([])
        puzzle.grid[1] = Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])
        puzzle.grid[6] = Tile([Professor('lower', 'blue'), Professor('lower', 'blue'), Professor('upper', 'blue'), Professor('upper', 'blue')])
        puzzle.grid[9] = Tile([Professor('lower', 'purple'), Professor('lower', 'purple'), Professor('upper', 'purple'), Professor('upper', 'purple')])
        puzzle.grid[4] = Tile([Professor('lower', 'brown'), Professor('lower', 'brown'), Professor('upper', 'brown'), Professor('upper', 'brown')])
        matching_tile = Tile([Professor('lower', 'green'), Professor('lower', 'blue'), Professor('upper', 'purple'), Professor('upper', 'brown')])
        self.assertTrue(puzzle._can_place_tile(matching_tile, 5))

    def test_can_place_tile_if_rotated_correct(self):
        puzzle = Puzzle([])
        puzzle.grid[1] = Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])
        puzzle.grid[6] = Tile([Professor('lower', 'blue'), Professor('lower', 'blue'), Professor('upper', 'blue'), Professor('upper', 'blue')])
        puzzle.grid[9] = Tile([Professor('lower', 'purple'), Professor('lower', 'purple'), Professor('upper', 'purple'), Professor('upper', 'purple')])
        puzzle.grid[4] = Tile([Professor('lower', 'brown'), Professor('lower', 'brown'), Professor('upper', 'brown'), Professor('upper', 'brown')])
        tile = Tile([Professor('lower', 'blue'), Professor('upper', 'purple'), Professor('upper', 'brown'), Professor('lower', 'green')])
        self.assertFalse(puzzle._can_place_tile(tile, 5))
        tile.rotate()
        self.assertTrue(puzzle._can_place_tile(tile, 5))

    def test_solve_two_tiles(self):
        tiles = [Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')]),
                 Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')])]
        self.assertTrue(Puzzle(tiles).solution())

    def test_solve_two_tiles_with_different_color_does_not_solve(self):
        tiles = [Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'green')]),
                 Tile([Professor('lower', 'blue'), Professor('lower', 'blue'), Professor('upper', 'blue'), Professor('upper', 'blue')])]
        self.assertFalse(Puzzle(tiles).solution())

    def test_solve_two_tiles_are_solved_when_rotate(self):
        tiles = [Tile([Professor('lower', 'blue'), Professor('lower', 'purple'), Professor('upper', 'green'), Professor('upper', 'green')]),
                 Tile([Professor('upper', 'green'), Professor('upper', 'blue'), Professor('lower', 'purple'), Professor('lower', 'purple')])]
        self.assertTrue(Puzzle(tiles).solution())

    def test_solve_three_tiles(self):
        tiles = [Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'brown')]),
                 Tile([Professor('lower', 'purple'), Professor('lower', 'purple'), Professor('upper', 'purple'), Professor('upper', 'purple')]),
                 Tile([Professor('lower', 'brown'), Professor('lower', 'purple'), Professor('upper', 'purple'), Professor('upper', 'purple')])]
        puzzle = Puzzle(tiles)
        self.assertTrue(puzzle.solution())

if __name__ == '__main__':
    unittest.main()

