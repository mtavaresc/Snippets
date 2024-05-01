class ProcessingStep:
    """
    Links processing steps together. Each step processes the data or passes it to the 
    next step if it cannot handle it. Use it for flexible pipelines where the order of 
    processing steps might need to change dynamically.

    Problem: Your pipeline has processing steps that must sometimes occur in a flexible 
            order, depending on input data or other conditions.

    Solution: Each step attempts to handle the data. If it cannot, it passes it to the 
            next step in the chain.

    Impact and Benefits:
        - Dynamic Processing Order: The chain is built at runtime, not strictly at 
        design time.
        - Decoupling: Processing steps do not need specific knowledge of each other.
    """

    def __init__(self, successor=None):
        self.successor = successor
    
    def handle(self, data):
        if self.can_handle(data):
            return self.process(data)
        elif self.successor:
            return self.successor.handle(data)
        else:
            raise Exception("No suitable handler found")
    
    def can_handle(self, data):
        # Logic to determine if this step can process data
        ...
    
    def process(self, data):
        # Actual processing logic
        ...