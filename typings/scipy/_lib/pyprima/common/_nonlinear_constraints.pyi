"""
This type stub file was generated by pyright.
"""

def transform_constraint_function(nlc): # -> Callable[..., NDArray[Any]]:
    '''
    The Python interfaces receives the constraints as lb <= constraint(x) <= ub, 
    but the Fortran backend expects the nonlinear constraints to be constraint(x) <= 0.
    Thus a conversion is needed.
    
    In addition to the conversion, we add a check to ensure that the provided lower/upper bounds
    have a shape consistent with the output of the constraint function.
    '''
    ...

def process_nl_constraints(nlcs): # -> Callable[..., _Array1D[float64] | NDArray[float64]]:
    ...

