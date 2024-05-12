class DataPipelineTemplate:
    """
    Defines the skeleton of an algorithm in a base class (e.g., a base data pipeline 
    class) and lets subclasses provide specific implementations for certain steps.

    Problem: Pipelines share a general structure, but implementations of specific steps 
            may vary.

    Solution: The Template Method defines an algorithm skeleton in a base class, letting 
            subclasses redefine certain steps without affecting the overall flow.
        
    Impact and Benefits:
        - Code Reuse: Enforces structure, encouraging reuse of the common pipeline process.
        - Controlled Customization: Subclasses tailor only specific parts of the algorithm.
    """

    def run(self):
        self.extract()
        self.transform()
        self.load()
    
    def extract(self):
        raise NotImplementedError()
    
    def transform(self):
        raise NotImplementedError()
    
    def load(self):
        raise NotImplementedError()
