class DataPipelineFacade:
    """
    Simplifies the interface to a complex subsystem, like interacting with multiple
    data sources, transformations, and targets. It makes your data pipeline easier
    to use and maintain.

    Problem: Your pipeline interacts with a database, an external API, and a file
            system. The complexity of these interactions makes your core pipeline
            logic intricate.

    Solution: The Facade pattern provides a unified interface to this subsystem.
    
    Impact and Benefits:
        - Enhanced Usability: Makes your pipeline easier to use by hiding internal
        complexities.
        - Improved Maintainability: Modifications to subsystems are isolated behind
        the facade.
    """

    def __init__(self, db_client, api_client, file_system):
        self.db_client = db_client
        self.api_client = api_client
        self.file_system = file_system
    
    def extract_transform_load(self, source_type, source_config, transformations):
        if source_type == "database":
            data = self.db_client.extract_data(**source_config)
        elif source_type == "api":
            data = self.api_client.get_data(**source_config)
        if source_type == "file":
            data = self.file_system.load_csv(**source_config)
        else:
            raise ValueError("Invali source type")
        
        transformed_data = self.apply_transformation(data, transformations)
        self.db_client.load_data(transformed_data)
    
    def apply_transformation(self, data, transformations):
        # ... Logic to apply transformations
        ...
        