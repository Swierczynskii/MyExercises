import numpy as np


class Solution:

    def __init__(self):
        with open(r"2024\4\input.txt") as f:
            file_content = f.read()

        self.letter_x = 0
        self.letter_y = 0

        self._word_length = 4

        self._puzzle_matrix = [list(row.strip()) for row in file_content.split()]
        self.max_x = len(self._puzzle_matrix[0])-1
        self.max_y = len(self._puzzle_matrix)-1

        self._hit = []
        self._output = []

    def _find_horizontal(self, letter):
        _desire = 'XMAS'
        _desire_backwards = 'SAMX'

        if self.letter_x <= self.max_x+1 - self._word_length:
            second = self._puzzle_matrix[self.letter_y][self.letter_x+1] 
            third = self._puzzle_matrix[self.letter_y][self.letter_x+2]
            fourth = self._puzzle_matrix[self.letter_y][self.letter_x+3]
            __output = letter + second + third + fourth

            if __output == _desire or __output == _desire_backwards:
                self._hit.append([
                    (self.letter_y, self.letter_x), 
                    (self.letter_y,self.letter_x+1),
                    (self.letter_y,self.letter_x+2),
                    (self.letter_y,self.letter_x+3)
                ])

    def _find_vertical(self, letter):
        _desire = 'XMAS'
        _desire_backwards = 'SAMX'

        if self.letter_y <= self.max_y+1 - self._word_length:
            second = self._puzzle_matrix[self.letter_y+1][self.letter_x] 
            third = self._puzzle_matrix[self.letter_y+2][self.letter_x]
            fourth = self._puzzle_matrix[self.letter_y+3][self.letter_x]
            __output = letter + second + third + fourth

            if __output == _desire or __output == _desire_backwards:
                self._hit.append([
                    (self.letter_y, self.letter_x), 
                    (self.letter_y+1,self.letter_x),
                    (self.letter_y+2,self.letter_x),
                    (self.letter_y+3,self.letter_x)
                ])

    def _find_diagonal(self, letter):
        _desire = 'XMAS'
        _desire_backwards = 'SAMX'

        if self.letter_y <= self.max_y+1 - self._word_length:
            if self.letter_x <= self.max_x+1 - self._word_length:
                second = self._puzzle_matrix[self.letter_y+1][self.letter_x+1] 
                third = self._puzzle_matrix[self.letter_y+2][self.letter_x+2]
                fourth = self._puzzle_matrix[self.letter_y+3][self.letter_x+3]
                __output = letter + second + third + fourth

                if __output == _desire or __output == _desire_backwards:
                    self._hit.append([
                        (self.letter_y, self.letter_x), 
                        (self.letter_y+1,self.letter_x+1),
                        (self.letter_y+2,self.letter_x+2),
                        (self.letter_y+3,self.letter_x+3)
                    ])

    def _find_diagonal_backwards(self, letter):
        _desire = 'XMAS'
        _desire_backwards = 'SAMX'

        if self.letter_y <= self.max_y+1 - self._word_length:
            if self.letter_x >= self._word_length-1:
                second = self._puzzle_matrix[self.letter_y+1][self.letter_x-1] 
                third = self._puzzle_matrix[self.letter_y+2][self.letter_x-2]
                fourth = self._puzzle_matrix[self.letter_y+3][self.letter_x-3]
                __output = letter + second + third + fourth

                if __output == _desire or __output == _desire_backwards:
                    self._hit.append([
                        (self.letter_y, self.letter_x), 
                        (self.letter_y+1,self.letter_x-1),
                        (self.letter_y+2,self.letter_x-2),
                        (self.letter_y+3,self.letter_x-3)
                    ])

    def solve(self):
        for curr_letter_y in self._puzzle_matrix:

            for curr_letter_x in curr_letter_y:
                self._find_horizontal(curr_letter_x)
                self._find_vertical(curr_letter_x)
                self._find_diagonal(curr_letter_x)
                self._find_diagonal_backwards(curr_letter_x)

                self.letter_x += 1
            self.letter_y += 1
            self.letter_x = 0
    
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