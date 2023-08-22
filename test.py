import unittest
from unittest import TestCase, main
from pyamaze import maze
from typing import cast
from labyrinth_solver import LabyrinthSolver, Node

class LabyrinthTest(TestCase):
    def setUp(self) -> None:
        self.m = maze()
        self.labyrinth_solver = LabyrinthSolver(self.m)

    def test_create_labyrinth(self) -> None:
        self.assertTrue(self.labyrinth_solver.labyrinth)
    
    def test_open_set_should_exist(self) -> None:
        self.assertEqual(self.labyrinth_solver.open_set, [])
    
    def test_closed_set_should_exist(self) -> None:
        self.assertEqual(self.labyrinth_solver.closed_set, [])
    
    def test_h_cost_from_starting_node_should_be_rows_plus_cols(self) -> None:
        expected_h = self.m.cols + self.m.rows
        starting_node:Node = self.labyrinth_solver.get_start_node()

        self.assertEqual(starting_node.get_h_cost(), expected_h)
    
    def test_g_cost_from_starting_node_should_be_zero(self) -> None:
        starting_node:Node = self.labyrinth_solver.get_start_node()

        self.assertEqual(starting_node.get_g_cost(), 0)
    
    def test_when_expanding_start_node_should_give_its_neighboors(self)\
    -> None:
        self.m.maze_map[self.m.cols,self.m.rows] = {
            'N': 0, 'S': 0, 'E': 0, 'W': 1 }
        expected_neighboors_pos = [(self.m.cols, self.m.rows - 1)]

        self.assertEqual(
            self.labyrinth_solver.expand_node(
                self.labyrinth_solver.get_start_node())[0].pos,
            expected_neighboors_pos[0] ) 