"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Create new serial generator that begins at start variable"""
        self.start = start
        self.curr_serial = start
        
    def generate(self):
        """Incraments current serial number (curr_serial) by one and returns it"""
        output = self.curr_serial
        self.curr_serial += 1
        return output
        
    def reset(self):
        """Resets current serial number (curr_serial) to start value of instance"""
        self.curr_serial = self.start
