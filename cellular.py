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
    def __init__(self, initial_states):
        self._cells = [Cell(s) for s in initial_states]

    def update(self, transition_rule):
        # synchronous update of cells
        states = []
        for cell in self._cells:
            cell
            neighbors = self.get_neighbors(cell)
            state = transition_rule(cell, neighbors)
            states.append(state)
        for i, cell in enumerate(self._cells):
            cell.update(states[i])

    def get_neighbors(self, cell):
        # neighborhood wraps the cellular space!
        if cell not in self._cells:
            raise Exception('Cell not present!')
        i = self._cells.index(cell)
        prev = self._cells[i-1]
        next = self._cells[(i+1)%len(self._cells)]
        return [prev, next]

    def __str__(self):
        cells = [str(cell) for cell in self._cells]
        return '|'+''.join(cells)+'|'

    def run(self, iterations):
        print self
        for itr in range(iterations):
            self.update(TransitionRuleFactory.wolfram_code(184))
            print self

class TransitionRuleFactory:
    @staticmethod
    def wolfram_code(code=184):
        code = str(bin(code))[2:]
        code = code[::-1]
        def fun(cell, neighbors):
            inp = str(neighbors[0].state)+str(cell.state)+str(neighbors[1].state)
            return code[int(inp,2)]
        return fun

if __name__=='__main__':
    states = '110000010001000110011100000101010100010010000010001000'
    ca = SimpleCA(states)
    ca.run(10)
