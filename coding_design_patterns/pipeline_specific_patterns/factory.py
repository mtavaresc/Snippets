class DataLoaderFactory:
    """
    Handles the creation of data pipeline components (like sources, transformations, 
    sinks). Employ this when creating multiple similar pipelines or dynamically 
    choosing components at runtime.

    Problem: Creating pipeline components involves complex logic, or component 
            selection needs to happen at runtime.

    Solution: The Factory pattern encapsulates object creation, letting you choose 
            components based on configuration or input.
        
    Impact and Benefits:
        - Centralized Creation: Component creation logic is managed in one place.
        - Flexibility: Different components can be selected without altering core 
        pipeline code.
    """

    def get_loader(self, loader_type):
        if loader_type == "csv":
            ...
            # return CSVLoader()
        elif loader_type == "json":
            ...
            # return JSONLoader()
        # ... Add more loaders