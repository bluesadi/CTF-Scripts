"""
输入求解未知数与约束条件表达式
解出方程组的解，并将可行解打印成ASCII字符串
2020/8/21 by bluesadi
"""
from z3 import *
import os

class EquationsSolver:

    vars = []
    constraints = []
    temp = '__temp.py'

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
        target = open(self.temp,"w")
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
        os.system(f'python {self.temp}')
        os.remove(self.temp)

solver = EquationsSolver()