from professorspelet.professorspelet import Professor, Tile, Puzzle

if __name__ == '__main__':
    tiles = [
        Tile([Professor('lower', 'green'), Professor('lower', 'brown'), Professor('upper', 'purple'), Professor('upper', 'blue')]),
        Tile([Professor('lower', 'brown'), Professor('lower', 'green'), Professor('upper', 'blue'), Professor('upper', 'purple')]),
        Tile([Professor('lower', 'brown'), Professor('lower', 'purple'), Professor('upper', 'green'), Professor('upper', 'brown')]),
        Tile([Professor('lower', 'brown'), Professor('lower', 'green'), Professor('upper', 'green'), Professor('upper', 'purple')]),
        Tile([Professor('lower', 'blue'), Professor('lower', 'green'), Professor('upper', 'brown'), Professor('upper', 'purple')]),
        Tile([Professor('lower', 'brown'), Professor('lower', 'purple'), Professor('upper', 'green'), Professor('upper', 'blue')]),
        Tile([Professor('lower', 'green'), Professor('lower', 'blue'), Professor('upper', 'green'), Professor('upper', 'purple')]),
        Tile([Professor('lower', 'green'), Professor('lower', 'blue'), Professor('upper', 'brown'), Professor('upper', 'purple')]),
        Tile([Professor('lower', 'blue'), Professor('lower', 'brown'), Professor('upper', 'brown'), Professor('upper', 'blue')]),
        Tile([Professor('lower', 'green'), Professor('lower', 'purple'), Professor('upper', 'blue'), Professor('upper', 'brown')]),
        Tile([Professor('lower', 'green'), Professor('lower', 'green'), Professor('upper', 'brown'), Professor('upper', 'purple')]),
        Tile([Professor('lower', 'green'), Professor('lower', 'purple'), Professor('upper', 'brown'), Professor('upper', 'blue')]),
        Tile([Professor('lower', 'brown'), Professor('lower', 'purple'), Professor('upper', 'green'), Professor('upper', 'blue')]),
        Tile([Professor('lower', 'brown'), Professor('lower', 'blue'), Professor('upper', 'green'), Professor('upper', 'green')]),
        Tile([Professor('lower', 'brown'), Professor('lower', 'purple'), Professor('upper', 'brown'), Professor('upper', 'blue')]),
        Tile([Professor('lower', 'brown'), Professor('lower', 'blue'), Professor('upper', 'purple'), Professor('upper', 'green')])
    ]
    puzzle = Puzzle(tiles)
    for s in puzzle.solution():
        print(*s)
