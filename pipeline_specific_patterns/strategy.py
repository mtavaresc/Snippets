"""
Encapsulates different algorithms or behaviors (like different data loading 
strategies) and lets you select one at runtime.

Problem: You need to switch between different data transformation or cleaning 
        algorithms at runtime.

Solution: Encapsulate these algorithms as interchangeable strategies.
"""
class DataCleaningStrategy:
    def clean_data(self, data):
        raise NotImplementedError()


class BasicCleaning(DataCleaningStrategy):
    def clean_data(self, data):
        # ... Basic cleaning logic
        return data


class AdvancedCleaning(DataCleaningStrategy):
    def clean_data(self, data):
        # ... Complex cleaning logic
        return data


class DataPipeline:
    def __init__(self, cleaning_strategy):
        self.cleaning_strategy = cleaning_strategy
    
    def process_data(self, data):
        cleaned_data = self.cleaning_strategy.clean_data(data)
        # ... Further processing
        return cleaned_data