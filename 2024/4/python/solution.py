import numpy as np


class Solution:

    def __init__(self):
        with open(r"2024\4\input.txt") as f:
            file_content = f.read()

        self._letter_x = 0
        self._letter_y = 0

        self._word_length = 4

        self._puzzle_matrix = [list(row.strip()) for row in file_content.split()]
        self._max_x = len(self._puzzle_matrix[0])-1
        self._max_y = len(self._puzzle_matrix)-1

        self._hit = []
        self._output = []

    def _find_horizontal(self, letter):
        desire = 'XMAS'
        desire_backwards = 'SAMX'

        if self._letter_x <= self._max_x+1 - self._word_length:
            second = self._puzzle_matrix[self._letter_y][self._letter_x+1] 
            third = self._puzzle_matrix[self._letter_y][self._letter_x+2]
            fourth = self._puzzle_matrix[self._letter_y][self._letter_x+3]
            output = letter + second + third + fourth

            if output == desire or output == desire_backwards:
                self._hit.append([
                    (self._letter_y, self._letter_x), 
                    (self._letter_y,self._letter_x+1),
                    (self._letter_y,self._letter_x+2),
                    (self._letter_y,self._letter_x+3)
                ])

    def _find_vertical(self, letter):
        desire = 'XMAS'
        desire_backwards = 'SAMX'

        if self._letter_y <= self._max_y+1 - self._word_length:
            second = self._puzzle_matrix[self._letter_y+1][self._letter_x] 
            third = self._puzzle_matrix[self._letter_y+2][self._letter_x]
            fourth = self._puzzle_matrix[self._letter_y+3][self._letter_x]
            output = letter + second + third + fourth

            if output == desire or output == desire_backwards:
                self._hit.append([
                    (self._letter_y, self._letter_x), 
                    (self._letter_y+1,self._letter_x),
                    (self._letter_y+2,self._letter_x),
                    (self._letter_y+3,self._letter_x)
                ])

    def _find_diagonal(self, letter):
        desire = 'XMAS'
        desire_backwards = 'SAMX'

        if self._letter_y <= self._max_y+1 - self._word_length:
            if self._letter_x <= self._max_x+1 - self._word_length:
                second = self._puzzle_matrix[self._letter_y+1][self._letter_x+1] 
                third = self._puzzle_matrix[self._letter_y+2][self._letter_x+2]
                fourth = self._puzzle_matrix[self._letter_y+3][self._letter_x+3]
                output = letter + second + third + fourth

                if output == desire or output == desire_backwards:
                    self._hit.append([
                        (self._letter_y, self._letter_x), 
                        (self._letter_y+1,self._letter_x+1),
                        (self._letter_y+2,self._letter_x+2),
                        (self._letter_y+3,self._letter_x+3)
                    ])

    def _find_diagonal_backwards(self, letter):
        desire = 'XMAS'
        desire_backwards = 'SAMX'

        if self._letter_y <= self._max_y+1 - self._word_length:
            if self._letter_x >= self._word_length-1:
                second = self._puzzle_matrix[self._letter_y+1][self._letter_x-1] 
                third = self._puzzle_matrix[self._letter_y+2][self._letter_x-2]
                fourth = self._puzzle_matrix[self._letter_y+3][self._letter_x-3]
                output = letter + second + third + fourth

                if output == desire or output == desire_backwards:
                    self._hit.append([
                        (self._letter_y, self._letter_x), 
                        (self._letter_y+1,self._letter_x-1),
                        (self._letter_y+2,self._letter_x-2),
                        (self._letter_y+3,self._letter_x-3)
                    ])

    def solve(self):
        for curr_letter_y in self._puzzle_matrix:

            for curr_letter_x in curr_letter_y:
                self._find_horizontal(curr_letter_x)
                self._find_vertical(curr_letter_x)
                self._find_diagonal(curr_letter_x)
                self._find_diagonal_backwards(curr_letter_x)

                self._letter_x += 1
            self._letter_y += 1
            self._letter_x = 0
    
        for dots in self._hit:
            # if . not in string in _puzzle_matrix then add .
            if '.' not in self._puzzle_matrix[dots[0][0]][dots[0][1]]:
                self._puzzle_matrix[dots[0][0]][dots[0][1]] = '.'+self._puzzle_matrix[dots[0][0]][dots[0][1]]
            if '.' not in self._puzzle_matrix[dots[1][0]][dots[1][1]]:
                self._puzzle_matrix[dots[1][0]][dots[1][1]] = '.'+self._puzzle_matrix[dots[1][0]][dots[1][1]]
            if '.' not in self._puzzle_matrix[dots[2][0]][dots[2][1]]:
                self._puzzle_matrix[dots[2][0]][dots[2][1]] = '.'+self._puzzle_matrix[dots[2][0]][dots[2][1]]
            if '.' not in self._puzzle_matrix[dots[3][0]][dots[3][1]]:
                self._puzzle_matrix[dots[3][0]][dots[3][1]] = '.'+self._puzzle_matrix[dots[3][0]][dots[3][1]]

        self._output = [
                ['.' if not letter.startswith('.') else letter[1:] for letter in row] for row in self._puzzle_matrix
            ]

    def print_table(self):
        for row in self._output:
            print(row)
        print("Quantity of 'XMAS' strings: ",len(self._hit))



if __name__ == '__main__':
    solution = Solution()
    solution.solve()
    solution.print_table()