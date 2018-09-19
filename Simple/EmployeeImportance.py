"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        rs = 0
        employee = [x for x in employees if x.id == id]
        while employee:
            person = employee.pop()
            rs += person.importance
            employee.extend([x for x in employees if x.id in person.subordinates])
        return rs

    
        """        employee = [x for x in employees if x.id == id][0]
        if not employee.subordinates:
            return employee.importance
        print (employee.id)
        sub = [x for x in employees if x.id in employee.subordinates]
        return employee.importance + sum([self.getImportance(employees, x.id) for x in sub])"""
