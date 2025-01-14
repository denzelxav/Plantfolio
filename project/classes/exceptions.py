"""
Here are custom exceptions that Plantfolio uses
"""

class ContainerNotEmpty(ValueError):
    """
    Exception to raise when a container is not yet empty that should be.
    """


class NothingSelected(ValueError):
    """
    When nothing in the UI is selected.
    """


class NameTakenError(ValueError):
    """
    When a name is already used.
    """
