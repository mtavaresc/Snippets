class LoadCommand:
    """
    Encapsulates actions or operations as objects. Makes it easy to queue, log, or undo 
    steps in a pipeline.

    Problem: You need to track pipeline actions to enable features like logging, 
            undo/redo, or asynchronous execution.

    Solution: The Command pattern turns requests into standalone objects, containing 
            all information necessary to execute the action.
    
    Impact and Benefits:
        - Decoupled Operations: Actions become independent of the pipeline code that 
        triggers them.
        - History and Queuing: Commands are logged, queued, or retried.
        - Undo/Redo Support: Commands can keep state to reverse their actions.
    """

    def __init__(self, target, data):
        self.target = target
        self.data = data
    
    def execute(self):
        self.target.load(self.data)
