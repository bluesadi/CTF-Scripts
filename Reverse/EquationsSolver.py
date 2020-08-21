"""
解出输入方程组的解，并将可行解打印成ASCII字符串。
"""
from z3 import *
import os

class EquationsSolver:

    __vars = []
    __constraints = []
    __temp = '__temp.py'

    def addVar(self,var: str):
        self.vars.append(var)
    
    def addVars(self,vars: list):
        self.vars += vars

    def addConstraint(self,constraint: str):
        self.constraints.append(constraint)

    def addConstraints(self,constraint: list):
        self.constraints += constraints

    def solve(self):
        output = 'from z3 import *\n\n'
        target = open(temp,"w")
        for var in self.vars:
            output += f'{var} = Real(\'{var}\')\n'
        output += '\ns = Solver()\n'
        for constraint in self.constraints:
            output += f's.add({constraint})\n'
        output += '\ns.check()\nresult = s.model()\nflag = \'\'\n'
        for var in self.vars:
            output += f'flag += chr(result[{var}].as_long())\n'
        output += 'print(flag)'
        target.write(output)
        target.close()
        os.system(f'python {temp}')
        os.remove(temp)