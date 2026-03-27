class BrowserHistory:
    def __init__(self, homepage: str):
      
        self.history_stack = []
        self.forward_stack = []
        self.visit(homepage)

    def visit(self, url: str) -> None:

        self.history_stack.append(url)
        
        self.forward_stack.clear()

    def back(self, steps: int) -> str:
     
        while steps > 0 and len(self.history_stack) > 1:

            self.forward_stack.append(self.history_stack.pop())
            steps -= 1
      
        return self.history_stack[-1]

    def forward(self, steps: int) -> str:
  
        while steps > 0 and self.forward_stack:
            self.history_stack.append(self.forward_stack.pop())
            steps -= 1
      
        return self.history_stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)