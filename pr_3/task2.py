class C32:
    def __init__(self):
        self.state = 'A'
        self.trans = {
            'A' : {
                'scan': ['B', 0]
            },
            'B' : {
                'hurry' : ['C', 1]
            },
            'C' : {
                'hurry' : ['D', 2]
            },
            'D' : {
                'scan' : ['B',4],
                'pluck' : ['E', 3]
            },
            'E' : {
                'hurry' : ['F',5]
            },
            'F' : {
                'scan' : ['G',6]
            },
            'G' : {
                'pluck' : ['E',9],
                'scan' : ['D', 7],
                'hurry': ['A', 8]
            }
        }

    def goto_next(self,command):
        trans = self.trans[self.state].get(command, None)
        if trans is None:
            return None

        self.state = trans[0]
        return trans[1]

    def scan(self):
        return self.goto_next('scan')

    def hurry(self):
        return self.goto_next('hurry')

    def pluck(self):
        return self.goto_next('pluck')
