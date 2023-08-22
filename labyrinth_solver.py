from pyamaze import maze
from typing import cast, Union, TypeAlias

Node_pos:TypeAlias = tuple[int, int]


def calculate_h_cost(node_pos:Node_pos) -> int:
    return node_pos[0] + node_pos[1]


class Node:
    @classmethod
    def calculate_h_cost(cls, node:'Node') -> int:
        return calculate_h_cost(node.pos)

    def __init__(self, pos:Node_pos, g_cost:int, h_cost:int) -> None:
        self.pos:Node_pos = pos
        self.g_cost:int = g_cost
        self.h_cost:int = h_cost
        self.parent:Union[Node, None] = None
    
    def get_f_cost(self) -> int:
        return self.g_cost + self.h_cost

    def get_h_cost(self) -> int:
        return self.h_cost

    def get_g_cost(self) -> int:
        return self.g_cost

    def get_neighboors(self, present_neighboors:dict[str, int])\
    -> list['Node']:
        node_neighboors:list[Node] = []
        for (cardinal_point, present) in present_neighboors.items():
            if present:
                neighboor_pos:Node_pos = (0, 0)
                if cardinal_point == 'N':
                    neighboor_pos = (self.pos[0] - 1, self.pos[1])
                    node_neighboors.append(
                        Node(neighboor_pos, self.g_cost + 1,
                             calculate_h_cost(neighboor_pos)))
                elif cardinal_point == 'S':
                    neighboor_pos = (self.pos[0] + 1, self.pos[1])
                    node_neighboors.append(
                        Node(neighboor_pos, self.g_cost + 1,
                             calculate_h_cost(neighboor_pos)))
                elif cardinal_point == 'E':
                    neighboor_pos = (self.pos[0], self.pos[1] + 1)
                    node_neighboors.append(
                        Node(neighboor_pos, self.g_cost + 1,
                             calculate_h_cost(neighboor_pos)))
                elif cardinal_point == 'W':
                    neighboor_pos = (self.pos[0], self.pos[1] - 1)
                    node_neighboors.append(
                        Node(neighboor_pos, self.g_cost + 1,
                             calculate_h_cost(neighboor_pos)))
        return node_neighboors

class LabyrinthSolver:
    def __init__(self, maze:maze) -> None:
        self.open_set:list[Node_pos] = []
        self.closed_set:list[Node_pos] = []
        maze.CreateMaze()
        self.labyrinth = maze

        start_pos = (maze.cols, maze.rows)
        self.start_node = Node(start_pos, 0, calculate_h_cost(start_pos))
    
    def get_start_node(self) -> Node:
        return self.start_node

    def get_labyrinth(self) -> maze:
        return self.labyrinth

    def h_cost(self, node:Node_pos) -> int:
        return node[0] + node[1]

    def g_cost(self, node:Node_pos) -> int:
        return 0

    def expand_node(self, node:Node) -> list[Node]:
        present_neighboors = self.labyrinth.maze_map[node.pos]
        return node.get_neighboors(present_neighboors)