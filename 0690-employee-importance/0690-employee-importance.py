"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
      
        def calculate_total_importance(employee_id: int) -> int:
            
            employee = employee_map[employee_id]
          
            subordinates_importance = sum(
                calculate_total_importance(subordinate_id) 
                for subordinate_id in employee.subordinates
            )
          
            return employee.importance + subordinates_importance
      
        employee_map = {employee.id: employee for employee in employees}
      
        return calculate_total_importance(id)