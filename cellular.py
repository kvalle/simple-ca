class Cell:
    def __init__(self, state=0):
        self.state = state
    def update(self, state):
        self.state = state
    def __str__(self):
        if int(self.state) == 1:
            return 'x'
        else:
            return ' '

class SimpleCA:
    def __init__(self, initial_states, rule_code):
        self._cells = [Cell(s) for s in initial_states]
        self.transition_function = self.wolfram_rule_code(rule_code)

    def update(self):
        """Update cell states synchronously"""
        states = []
        for cell in self._cells:
            cell
            neighbors = self.get_neighbors(cell)
            state = self.transition_function(cell, neighbors)
            states.append(state)
        for i, cell in enumerate(self._cells):
            cell.update(states[i])

    def get_neighbors(self, cell):
        """Fetch list of neighbor cells"""
        if cell not in self._cells:
            raise Exception('Cell not present!')
        i = self._cells.index(cell)
        # neighborhood wraps the cellular space!
        prev = self._cells[i-1]
        next = self._cells[(i+1)%len(self._cells)]
        return [prev, next]

    def run(self, iterations):
        """Iteratively update cell states and print results"""
        w = len(str(iterations))
        print '0'.rjust(w), self
        for itr in range(1,iterations+1):
            self.update()
            print str(itr).rjust(w), self

    def __str__(self):
        rep = [str(cell) for cell in self._cells]
        return '|'+''.join(rep)+'|'

    @staticmethod
    def wolfram_rule_code(code=184):
        """Returns transition function for given wolfram rule"""
        code = str(bin(code))[2:]
        code = code[::-1]
        def fun(cell, neighbors):
            inp = str(neighbors[0].state)+str(cell.state)+str(neighbors[1].state)
            return code[int(inp,2)]
        return fun

if __name__=='__main__':
    states = '110000010001000'
    rule_code = 184
    ca = SimpleCA(states, rule_code)
    ca.run(10)
