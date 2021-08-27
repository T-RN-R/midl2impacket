from .base import Generator

class InvocationGenerator(Generator):
    """Generates RPC Procedure invocations.
    
    If a procedure has a dependency on a context_handle as input, make sure it is illegal to call those functions until a context_handle has been created.
    """
    pass