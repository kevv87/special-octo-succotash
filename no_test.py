# import unittest
# from unittest import TestCase, main
# from pyamaze import maze
# from typing import cast

# from node import Node, get_cardinal_point_modifier
# from graph import Graph


# class NodeTest(TestCase):
#     def setUp(self) -> None:
#         self.m = maze()

#     def test_create_node_out_of_maze_map_entry(self) -> None:
#         pos = (1,1)
#         maze_map_entry = self.m.maze_map[pos]
#         node:Node = Node.from_maze_map_entry(maze_map_entry, pos)
#         self.assertTrue(node)
    
#     def test_node_should_have_its_place_in_grid(self) -> None:
#         pos = (1,1)
#         maze_map_entry = self.m.maze_map[pos]

#         node:Node = Node.from_maze_map_entry(maze_map_entry, pos)
#         self.assertEqual(node.pos, pos)
    
#     def test_node_should_have_neighboors(self) -> None:
#         pos = (1,1)
#         maze_map_entry = self.m.maze_map[pos]

#         node:Node = Node.from_maze_map_entry(maze_map_entry, pos)
#         self.assertIsInstance(node.neighboors, list)
    
#     def test_is_neighboor(self) -> None:
#         pos = (1,1)
#         neighbor_pos = (1,2)

#         neighboor_node:Node = Node(neighbor_pos)
#         node:Node = Node(pos, [neighboor_node])

#         self.assertTrue(node.is_neighboor_of(neighboor_node))
    
#     def test_should_add_neighboor(self) -> None:
#         pos = (1,1)
#         neighbor_pos = (1,2)

#         neighboor_node:Node = Node(neighbor_pos)
#         node:Node = Node(pos)
#         node.add_neighboor(neighboor_node)

#         self.assertTrue(node.is_neighboor_of(neighboor_node))

#     def test_neighboors_should_be_reciprocal(self) -> None:
#         pos = (1,1)
#         neighbor_pos = (1,2)

#         neighboor_node:Node = Node(neighbor_pos)
#         node:Node = Node(pos, [neighboor_node])

#         self.assertTrue(neighboor_node.is_neighboor_of(node),
#                         "Neighboors are not being added correctly")
#         self.assertTrue(node.is_neighboor_of(neighboor_node), 
#                         "Neighboors are not being correctly updated")

#     def test_node_neighboors_should_be_the_same_as_map_entry(self) -> None:
#         pos = (1,1)
#         maze_map_entry = self.m.maze_map[pos]
#         maze_map_entry = {'N': True, 'S': True, 'E': True, 'W': True}

#         node:Node = Node.from_maze_map_entry(maze_map_entry, pos)
#         for (cardinal_point, present) in maze_map_entry.items():
#             if present:
#                 cardinal_point_modifier:tuple[int, int] =\
#                     get_cardinal_point_modifier(cardinal_point)
#                 neighboor_pos = (pos[0] + cardinal_point_modifier[0],
#                                  pos[1] + cardinal_point_modifier[1])
#                 # check if neighboor_pos is in any neighboor of node
#                 neighboor_found = False
#                 for neighboor in node.neighboors:
#                     if neighboor.pos == neighboor_pos:
#                         neighboor_found = True
#                         break
#                 self.assertTrue(neighboor_found, 
#                                 f"Neighboor with pos {neighboor_pos} was not" 
#                                 "found inside neighboors of the node")
    
#     def test_should_throw_if_adding_fifth_neighboor(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (3,2), (4,3), (2,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         with self.assertRaises(Exception):
#             node.add_neighboor(Node((3,5)))
    
#     def test_node_should_give_north_neighboor_when_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (3,2), (4,3), (2,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         north_neighboor = node.get_neighboor('N')
#         self.assertTrue(north_neighboor)
#         self.assertEqual(cast(Node, north_neighboor).pos, (2,3))
    
#     def test_node_should_give_None_if_north_neighbor_not_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (4,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         north_neighboor = node.get_neighboor('N')
#         self.assertIsNone(north_neighboor)

#     def test_node_should_give_south_neighboor_when_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (3,2), (4,3), (2,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         south_neighboor = node.get_neighboor('S')
#         self.assertTrue(south_neighboor)
#         self.assertEqual(cast(Node, south_neighboor).pos, (4,3))
    
#     def test_node_should_give_None_if_south_neighbor_not_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,2), (2,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         south_neighboor = node.get_neighboor('S')
#         self.assertIsNone(south_neighboor)
    
#     def test_node_should_give_east_neighboor_when_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (3,2), (4,3), (2,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         east_neighboor = node.get_neighboor('E')
#         self.assertTrue(east_neighboor)
#         self.assertEqual(cast(Node, east_neighboor).pos, (3,4))
    
#     def test_node_should_give_None_if_east_neighbor_not_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,2), (2,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         east_neighboor = node.get_neighboor('E')
#         self.assertIsNone(east_neighboor)
    
#     def test_node_should_give_west_neighboor_when_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (3,2), (4,3), (2,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         west_neighboor = node.get_neighboor('W')
#         self.assertTrue(west_neighboor)
#         self.assertEqual(cast(Node, west_neighboor).pos, (3,2))
    
#     def test_node_should_give_None_if_west_neighbor_not_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (4,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)
#         west_neighboor = node.get_neighboor('W')
#         self.assertIsNone(west_neighboor)
    
#     def test_node_should_give_neighbor_given_position(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (3,2), (4,3), (2,3)]
#         desired_pos = (4, 3)
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)

#         neighboor = node.get_neighboor_by_pos(desired_pos)
#         self.assertTrue(neighboor)
#         self.assertEqual(cast(Node, neighboor).pos, desired_pos)
    
#     def test_node_should_give_None_if_neighbor_not_present(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (3,2), (4,3), (2,3)]
#         desired_pos = (3, 1)
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)

#         neighboor = node.get_neighboor_by_pos(desired_pos)
#         self.assertIsNone(neighboor)

#     def test_should_get_node_neighboors_pos(self) -> None:
#         pos = (3,3)
#         neighbors_pos = [(3,4), (3,2), (4,3), (2,3)]
#         neighbors = [Node(pos) for pos in neighbors_pos]
#         node:Node = Node(pos, neighbors)

#         neighboors_pos = node.get_neighboors_pos()
#         self.assertEqual(neighboors_pos, neighbors_pos)

#     @unittest.skip("Not implemented yet")
#     def test_should_create_node_from_maze_map(self) -> None:
#         pass
#         #new_node = Node.from_maze_map(self.m.maze_map)
#         #self.assertTrue(new_node)

# class LabyrinthTest(TestCase):
    
#     def setUp(self) -> None:
#         self.m = maze()

#     def test_labyrinth_is_created(self) -> None:
#         self.assertTrue(self.m)
    
#     def test_extract_labyrinth_as_dict(self) -> None:
#         self.assertIsInstance(self.m.maze_map, dict)

#     def test_from_labyrinth_maze_map_create_a_graph(self) -> None:
#         labyrinth_graph:Graph = Graph.from_maze_map(self.m.maze_map)
#         self.assertIsInstance(labyrinth_graph.get_head(), Node)
#         self.assertIsInstance(labyrinth_graph.get_head().neighboors, list)
    
#     def test_head_of_graph_should_be_starting_position(self) -> None:
#         labyrinth_graph:Graph = Graph.from_maze_map(self.m.maze_map)
#         starting_pos = (self.m.rows, self.m.cols)
#         self.assertEqual(labyrinth_graph.get_head().pos, starting_pos,
#                          "Head of graph is not the starting position")

#     @unittest.skip("Not implemented yet")
#     def test_labyrinth_solution_is_followable_by_the_graph(self) -> None:
#         self.m.CreateMaze()
#         labyrinth_graph:Graph = Graph.from_maze_map(self.m.maze_map)
#         labyrinth_solution = self.m.path

#         current_node = labyrinth_graph.get_head()
#         first_pos = current_node.pos
#         current_pos = first_pos
#         while current_pos != (1,1):
#             next_pos = labyrinth_solution[current_pos]
#             next_node = current_node.get_neighboor_by_pos(next_pos)
#             print(f"Checking current pos: {current_pos}, next pos: {next_pos}")
#             self.assertTrue(next_node,
#                             f"Node {current_pos} gives way to {next_pos} but "
#                             "there is no node in that position")
#             self.assertEqual(cast(Node, next_node).pos, next_pos,
#                              "The neighboor was not expected")


# if __name__ == '__main__':
#     main()