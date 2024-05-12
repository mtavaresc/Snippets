import csv


class LargeFileIterator:
    """
    Provides a standard way to traverse through elements in a pipeline. 
    Useful for processing data streams where you do not have all the 
    data at once.

    Problem: Handling datasets too large for memory, or data streams require processing 
            in chunks.

    Solution: The Iterator pattern enables sequential access to elements in a collection 
            without exposing its underlying structure.
    """

    def __init__(self, filename, chunk_size=1024):
        self.file = open(filename)
        self.chunk_size = chunk_size
    
    def __iter__(self):
        return self
    
    def __next__(self):
        data = self.file.read(self.chunk_size)
        if not data:
            raise StopIteration
        return data


class CSVFileIterator:
    """
    Problem: Handling large datasets that do not fit readily in memory, or working with 
            data streams.

    Solution: Iterators let you process data in chunks.
    """

    def __init__(self, filename):
        self.file = open(filename)
        self.reader = csv.reader(self.file)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        row = next(self.reader)
        if not row:
            raise StopIteration
        return row


# Usage
for row in CSVFileIterator("large_data.csv"):
    # Process each row individually
    ...
