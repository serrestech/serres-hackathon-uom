import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable, Any
from shape import Shape

class Canvas():

    empty_cell_char = '-'
    hole_cell_char = 'B'

    # to megethos den mas apasxolei sto backend
    def __init__(self,lines:int,rows:int, holes:List[Tuple[int, int]]):#y:lines,x:rows
        self.dimentions: Tuple[int, int] = (lines,rows)
        self.shapes_placed:List[Shape] = []
        self.holes: List[Tuple[int, int]] = holes
        enough_empty_cells = [self.empty_cell_char for i in range(lines*rows)]
        # den einai swsto auto
        # self.matrix = np.arange(lines * rows).reshape(lines,rows) NOT WORKING
        #self.matrix = np.full((lines,rows),self.empty_cell_char)
        #print("MATRIX OF:",self.matrix)

    def check_for_stepping_in_hole_when_placed_in(self,s:Shape,position:Tuple[int,int]):
        position_x, position_y = position
        pass
    def check_for_out_of_bounds_when_placed_in(self,s:Shape,position:Tuple[int,int])->bool:
        position_x,position_y = position
        coords = s.get_coords_list()
        all_x = list(map(lambda coord: coord[0], coords))
        all_x_sorted = sorted(all_x)
        #print(all_x_sorted)
        all_y = list(map(lambda coord: coord[1], coords))
        all_y_sorted = sorted(all_y)

        min_x = all_x_sorted[0]
        min_y = all_y_sorted[0]

        max_x = all_y_sorted[len(all_x_sorted)-1]
        max_y = all_y_sorted[len(all_y_sorted)-1]

        # everything is signed so just add it
        max_position_x = position_x + max_x
        max_position_y = position_y + max_y

        min_position_x = position_x + min_x
        min_position_y = position_y + min_y

        if min_position_y< 0 or min_position_x < 0 or max_position_x > self.dimentions[0] -1 or max_position_y > self.dimentions[1] - 1:
            return False
        return True

    def place_shape_unchecked(self,s:Shape,position:Tuple[int,int]):
        pass
    def find_perimeter_os_shapes(self, shapes:List[Shape])->int:
        G:nx.Graph = nx.Graph()


    def place_shape(self,s:Shape,position:Tuple[int,int]):
        position_x,position_y = position
        coords = s.get_coords_list()
        self.shapes_placed.append(s)
        s.change_cords_by_a_position(position)

        #draw the board appropriately
        # for coord_tuple in coords:
        #     # position_y,position_x to origin kai thelw na efarmosw ta transforms
        # #    print(coord_tuple)
        #     x,y = coord_tuple
        #
        #     place_in_x = position_x + x
        #     place_in_y = position_y + y
        #     #print("Placement",place_in_x,place_in_y)
        #     self.matrix[place_in_x][place_in_y] = s.value
        # print(self.matrix)
    def draw_shape_in(self,s:Shape,position:Tuple[int,int]):
        position_x,position_y = position
    def get_matrix(self):
        matrix = np.full((self.dimentions[0], self.dimentions[1]), self.empty_cell_char)
        for shape in self.shapes_placed:
            coords = shape.get_coords_list()
            for coord_tuple in coords:
                x, y = coord_tuple
                matrix[x][y] = shape.value

        #place the holes in the matrix
        for hole in self.holes:
            hole_x,hole_y = hole
            matrix[hole_x][hole_y] = self.hole_cell_char
        return matrix
    def __str__(self):
        my_string:str = ""
        for elem in self.matrix:
            pass



    def count_empty_cells(self) -> int:
        # the_sum = 0
        # for row in self.matrix:
        #     for elem in row:
        #         if elem == self.empty_cell_char:
        #         #    print(elem)
        #             the_sum += 1
        #
        # return the_sum
        pass
    def count_filled_cells(self) -> int:
        # the_sum = 0
        # for row in self.matrix:
        #     for elem in row:
        #         if elem != self.empty_cell_char and elem != self.hole_cell_char:
        #             #print(elem)
        #             the_sum += 1

        #return the_sum
        pass
    def count_holes(self) -> int:
        # the_sum = 0
        # for row in self.matrix:
        #     for elem in row:
        #         if elem == self.hole_cell_char:
        #             #print(elem)
        #             the_sum += 1
        #
        # return the_sum
        pass
    def get_holes(self) -> List[Tuple[int,int]]:
        holes = []
        rows,cols = self.matrix.shape
        for row_index in range(rows):
            for col_index in range(cols):
                elem = self.matrix[row_index][col_index]
                if elem == self.hole_cell_char:
                    #print(elem)
                    holes.append((row_index,col_index))


        return holes

    # Calculate Parameter of shape
    def calculate_parameter_of_shape(self,s1:Shape) -> int:
        pass

    def get_empty_cells(self)->List[Tuple[int,int]]:
        pass

    def place_hole_in(self,x,y):
        pass

    def shapes_touch(self,s1:Shape,s2:Shape) -> bool:
        pass
    def merge_shapes(self,s1:Shape,s2:Shape):
        # this will return a shape that has the coordinates of both
        # shapes should touch --> be a Congruent Group/Group
        # !!! there will be a problem with defining its origin
        # we might just make it a different Class
        pass