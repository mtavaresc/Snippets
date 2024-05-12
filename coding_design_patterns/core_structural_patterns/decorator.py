"""
Dynamically adds new functionality to existing pipeline steps (like processing steps)
without modifying their structure. Ideal for adding logging, caching, or validation 
on the fly.

Problem: You need to extend the behavior of pipeline steps (logging, caching, validation) 
        without drastically modifying their structure.

Solution: The Decorator pattern dynamically adds new functionality to existing objects 
        by wrapping them.

Impact and Benefits:
    - Flexibility: Behavior enhancements are added or removed easily at runtime.
    - Open/Closed Principle: Extends functionality without modifying the original classes.
"""

def logging_decorator(func):
    def inner(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print("Function completed.")
        return result
    return inner


@logging_decorator
def processing_step(data):
    # ... processing logic
    ...