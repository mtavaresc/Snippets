"""
Defines a way for data pipeline components to notify each other about changes in 
state. Use for coordinating steps that depend on each other's output.

Problem: Pipeline components need to react to changes or events occurring in other 
        components (e.g., step completion, errors).

Solution: The Observer pattern lets objects (observers) subscribe to notifications 
        from other objects (subjects).

Impact and Benefits:
    - Loose Coupling: Components interact without direct knowledge of each other.
    - Coordination: Steps react to events seamlessly, enhancing workflow logic.
"""

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)


class PipelineStepObserver:
    def update(self, event):
        # React to the event
        ...
