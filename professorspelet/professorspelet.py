import copy


class Puzzle:
    """
        Professorspelet consists of a 4x4 grid that shall be filled with tiles,
        each of which has 4 body parts in different colors on each edge.
        The tiles must be place in such a way that all edges must create one
        complete Professor.
    """

    def __init__(self, tiles: list):
        """
            Initialize a puzzle with a list of tiles that shall be placed. The list can be empty or
            contain only a few Professors, but must not exceed 16.
        """
        if len(tiles) > 16:
            raise ValueError(f'Maximum number of Professor tiles that can be placed is 16, was: {len(tiles)}')
        self.grid = [None] * 16
        self._solve(copy.deepcopy(tiles))

    def solution(self):
        """
            Return a list of tiles placement for a valid solution. The tiles are indexed 0-15 and should be placed
            starting from top left corner with a column width of 4.
        """
        return [(e, str(tile)) for e, tile in enumerate(self.grid) if tile is not None]

    def _solve(self, tiles: list, current_index: int=0):
        if not tiles:
            return True
        for tile in tiles:
            for i in range(4):
                if self._can_place_tile(tile, current_index):
                    self.grid[current_index] = tile
                    tiles.remove(tile)
                    if self._solve(tiles, current_index + 1):
                        return True
                    self.grid[current_index] = None
                    tiles.append(tile)
                tile.rotate()
        return False

    def _can_place_tile(self, tile, ind):
        if self.grid[ind] is not None:
            raise ValueError(f'Index={ind} is not empty')
        if ind > 3:
            other = self.grid[ind - 4]
            if other is not None and not other.bottom().matches(tile.top()):
                return False
        if ind < 12:
            other = self.grid[ind + 4]
            if other is not None and not other.top().matches(tile.bottom()):
                return False
        if ind % 4 != 0:
            other = self.grid[ind - 1]
            if other is not None and not other.right().matches(tile.left()):
                return False
        if ind % 4 != 3:
            other = self.grid[ind + 1]
            if other is not None and not other.left().matches(tile.right()):
                return False
        return True


class Tile:
    """
        A tile consisting of four professor halves - two upper and two lower
    """

    def __init__(self, professors):
        """
            Create a card with four professors, starting at the top in a clockwise direction
        """
        if len(professors) != 4:
            raise ValueError('Expected four professor parts')
        bodies = list(map(lambda x: x.body, professors))
        if bodies.count('upper') != bodies.count('lower'):
            raise ValueError('Expected equal number of upper and lower body parts')
        self.professors = professors
        self.rotation = 0

    def __str__(self):
        return f'Top: {self.top()}, Right: {self.right()}, Bottom: {self.bottom()}, Left: {self.left()}'

    def top(self):
        """
            Get the professor in top position
        """
        return self.professors[self.rotation % 4]

    def right(self):
        """
            Get the professor in right position
        """
        return self.professors[(self.rotation + 1) % 4]

    def bottom(self):
        """
            Get the professor in bottom position
        """
        return self.professors[(self.rotation + 2) % 4]

    def left(self):
        """
            Get the professor in left position
        """
        return self.professors[(self.rotation + 3) % 4]

    def rotate(self, steps=1) -> None:
        """
            Rotate this tile a number of steps clockwise.
            Number may be negative to indicate counter clockwise.
        """
        self.rotation -= steps


class Professor:
    """
        Representation of a professor who consists of a body half in a particular color
    """

    _VALID_BODY_PARTS = ['upper', 'lower']
    _VALID_COLORS = ['blue', 'purple', 'green', 'brown']

    def __init__(self, body, color):
        if body.lower() not in Professor._VALID_BODY_PARTS:
            raise ValueError(f'Invalid body part {body}. Valid alternatives: {Professor._VALID_BODY_PARTS}')
        if color.lower() not in Professor._VALID_COLORS:
            raise ValueError(f'Invalid color {color}. Valid alternatives: {Professor._VALID_COLORS}')
        self.body = body.lower()
        self.color = color.lower()

    def __str__(self):
        return f'{self.body} - {self.color}'

    def matches(self, professor) -> bool:
        """
            Test if a professor can be placed next to another one
            by comparing body parts and color.
        """
        return self.body != professor.body and self.color == professor.color

