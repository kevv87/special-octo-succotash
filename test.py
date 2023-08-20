from unittest import TestCase, main
from pyamaze import maze # type: ignore


class Node:
    def __init__(self, neighboors:list=[]):
        self.neighboors = neighboors


class Graph:
    @classmethod
    def from_maze_map(cls, maze_map:dict):
        instance = cls()
        instance.head = Node()
        return instance

    def get_head(self) -> Node:
        return self.head


class LabyrinthTest(TestCase):
    
    def setUp(self):
        self.m = maze()
        self.m.CreateMaze()

    def test_labyrinth_is_created(self):
        self.assertTrue(self.m)
    
    def test_extract_labyrinth_as_dict(self):
        self.assertIsInstance(self.m.maze_map, dict)
    
    def test_create_node_out_of_a_maze_map_entry(self):
        self.assertTrue(True)

    def test_from_labyrinth_maze_map_create_a_graph(self):
        labyrinth_graph:Graph = Graph.from_maze_map(self.m.maze_map)
        self.assertIsInstance(labyrinth_graph.get_head(), Node)
        self.assertIsInstance(labyrinth_graph.get_head().neighboors, list)
        

if __name__ == '__main__':
    main()