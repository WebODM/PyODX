class GenericError(Exception):
    """Generic catch-all exception. All exceptions in pyodx inherit from it."""
    pass

class NodeServerError(GenericError):
    """The server replied in a manner which we did not expect. Usually this indicates
    a temporary malfunction of the node."""
    pass

class NodeConnectionError(GenericError):
    """A connection problem (such as a timeout or a network error) has occurred."""
    pass

class NodeResponseError(GenericError):
    """The node responded with an error message indicating that the requested operation failed."""
    pass

class TaskFailedError(GenericError):
    """A task did not complete successfully."""
    pass

class RangeNotAvailableError(GenericError):
    """A download attempt to use Range requests failed."""
    pass