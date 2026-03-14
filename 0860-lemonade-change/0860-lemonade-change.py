from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Determines if you can provide change to every customer in a queue.
        Customers pay with $5, $10, or $20 bills. Lemonade costs $5.

        Args:
            bills: A list of integers representing the bill each customer pays with.

        Returns:
            True if you can provide change to every customer, False otherwise.
        """
        five_dollar_bills = 0  
        ten_dollar_bills = 0   
      
        for bill in bills:
            if bill == 5:
                
                five_dollar_bills += 1
            elif bill == 10:
                
                if five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    
                    return False
            elif bill == 20:
                
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    ten_dollar_bills -= 1
                    five_dollar_bills -= 1
                
                elif five_dollar_bills >= 3:
                    five_dollar_bills -= 3
                else:
                    
                    return False
           
            
        return True
