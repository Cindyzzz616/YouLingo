"""
This type stub file was generated by pyright.
"""

"""shgo: The simplicial homology global optimisation algorithm."""
__all__ = ['shgo']
def shgo(func, bounds, args=..., constraints=..., n=..., iters=..., callback=..., minimizer_kwargs=..., options=..., sampling_method=..., *, workers=...): # -> OptimizeResult:
    """
    Finds the global minimum of a function using SHG optimization.

    SHGO stands for "simplicial homology global optimization".

    Parameters
    ----------
    func : callable
        The objective function to be minimized.  Must be in the form
        ``f(x, *args)``, where ``x`` is the argument in the form of a 1-D array
        and ``args`` is a tuple of any additional fixed parameters needed to
        completely specify the function.
    bounds : sequence or `Bounds`
        Bounds for variables. There are two ways to specify the bounds:

        1. Instance of `Bounds` class.
        2. Sequence of ``(min, max)`` pairs for each element in `x`.

    args : tuple, optional
        Any additional fixed parameters needed to completely specify the
        objective function.
    constraints : {Constraint, dict} or List of {Constraint, dict}, optional
        Constraints definition. Only for COBYLA, COBYQA, SLSQP and trust-constr.
        See the tutorial [5]_ for further details on specifying constraints.

        .. note::

           Only COBYLA, COBYQA, SLSQP, and trust-constr local minimize methods
           currently support constraint arguments. If the ``constraints``
           sequence used in the local optimization problem is not defined in
           ``minimizer_kwargs`` and a constrained method is used then the
           global ``constraints`` will be used.
           (Defining a ``constraints`` sequence in ``minimizer_kwargs``
           means that ``constraints`` will not be added so if equality
           constraints and so forth need to be added then the inequality
           functions in ``constraints`` need to be added to
           ``minimizer_kwargs`` too).
           COBYLA only supports inequality constraints.

        .. versionchanged:: 1.11.0

           ``constraints`` accepts `NonlinearConstraint`, `LinearConstraint`.

    n : int, optional
        Number of sampling points used in the construction of the simplicial
        complex. For the default ``simplicial`` sampling method 2**dim + 1
        sampling points are generated instead of the default ``n=100``. For all
        other specified values `n` sampling points are generated. For
        ``sobol``, ``halton`` and other arbitrary `sampling_methods` ``n=100`` or
        another specified number of sampling points are generated.
    iters : int, optional
        Number of iterations used in the construction of the simplicial
        complex. Default is 1.
    callback : callable, optional
        Called after each iteration, as ``callback(xk)``, where ``xk`` is the
        current parameter vector.
    minimizer_kwargs : dict, optional
        Extra keyword arguments to be passed to the minimizer
        ``scipy.optimize.minimize``. Some important options could be:

        method : str
            The minimization method. If not given, chosen to be one of
            BFGS, L-BFGS-B, SLSQP, depending on whether or not the
            problem has constraints or bounds.
        args : tuple
            Extra arguments passed to the objective function (``func``) and
            its derivatives (Jacobian, Hessian).
        options : dict, optional
            Note that by default the tolerance is specified as
            ``{ftol: 1e-12}``

    options : dict, optional
        A dictionary of solver options. Many of the options specified for the
        global routine are also passed to the ``scipy.optimize.minimize``
        routine. The options that are also passed to the local routine are
        marked with "(L)".

        Stopping criteria, the algorithm will terminate if any of the specified
        criteria are met. However, the default algorithm does not require any
        to be specified:

        maxfev : int (L)
            Maximum number of function evaluations in the feasible domain.
            (Note only methods that support this option will terminate
            the routine at precisely exact specified value. Otherwise the
            criterion will only terminate during a global iteration)
        f_min : float
            Specify the minimum objective function value, if it is known.
        f_tol : float
            Precision goal for the value of f in the stopping
            criterion. Note that the global routine will also
            terminate if a sampling point in the global routine is
            within this tolerance.
        maxiter : int
            Maximum number of iterations to perform.
        maxev : int
            Maximum number of sampling evaluations to perform (includes
            searching in infeasible points).
        maxtime : float
            Maximum processing runtime allowed
        minhgrd : int
            Minimum homology group rank differential. The homology group of the
            objective function is calculated (approximately) during every
            iteration. The rank of this group has a one-to-one correspondence
            with the number of locally convex subdomains in the objective
            function (after adequate sampling points each of these subdomains
            contain a unique global minimum). If the difference in the hgr is 0
            between iterations for ``maxhgrd`` specified iterations the
            algorithm will terminate.

        Objective function knowledge:

        symmetry : list or bool
            Specify if the objective function contains symmetric variables.
            The search space (and therefore performance) is decreased by up to
            O(n!) times in the fully symmetric case. If `True` is specified
            then all variables will be set symmetric to the first variable.
            Default
            is set to False.

            E.g.  f(x) = (x_1 + x_2 + x_3) + (x_4)**2 + (x_5)**2 + (x_6)**2

            In this equation x_2 and x_3 are symmetric to x_1, while x_5 and
            x_6 are symmetric to x_4, this can be specified to the solver as::

                symmetry = [0,  # Variable 1
                            0,  # symmetric to variable 1
                            0,  # symmetric to variable 1
                            3,  # Variable 4
                            3,  # symmetric to variable 4
                            3,  # symmetric to variable 4
                            ]

        jac : bool or callable, optional
            Jacobian (gradient) of objective function. Only for CG, BFGS,
            Newton-CG, L-BFGS-B, TNC, SLSQP, dogleg, trust-ncg. If ``jac`` is a
            boolean and is True, ``fun`` is assumed to return the gradient
            along with the objective function. If False, the gradient will be
            estimated numerically. ``jac`` can also be a callable returning the
            gradient of the objective. In this case, it must accept the same
            arguments as ``fun``. (Passed to `scipy.optimize.minimize`
            automatically)

        hess, hessp : callable, optional
            Hessian (matrix of second-order derivatives) of objective function
            or Hessian of objective function times an arbitrary vector p.
            Only for Newton-CG, dogleg, trust-ncg. Only one of ``hessp`` or
            ``hess`` needs to be given. If ``hess`` is provided, then
            ``hessp`` will be ignored. If neither ``hess`` nor ``hessp`` is
            provided, then the Hessian product will be approximated using
            finite differences on ``jac``. ``hessp`` must compute the Hessian
            times an arbitrary vector. (Passed to `scipy.optimize.minimize`
            automatically)

        Algorithm settings:

        minimize_every_iter : bool
            If True then promising global sampling points will be passed to a
            local minimization routine every iteration. If True then only the
            final minimizer pool will be run. Defaults to True.

        local_iter : int
            Only evaluate a few of the best minimizer pool candidates every
            iteration. If False all potential points are passed to the local
            minimization routine.

        infty_constraints : bool
            If True then any sampling points generated which are outside will
            the feasible domain will be saved and given an objective function
            value of ``inf``. If False then these points will be discarded.
            Using this functionality could lead to higher performance with
            respect to function evaluations before the global minimum is found,
            specifying False will use less memory at the cost of a slight
            decrease in performance. Defaults to True.

        Feedback:

        disp : bool (L)
            Set to True to print convergence messages.

    sampling_method : str or function, optional
        Current built in sampling method options are ``halton``, ``sobol`` and
        ``simplicial``. The default ``simplicial`` provides
        the theoretical guarantee of convergence to the global minimum in
        finite time. ``halton`` and ``sobol`` method are faster in terms of
        sampling point generation at the cost of the loss of
        guaranteed convergence. It is more appropriate for most "easier"
        problems where the convergence is relatively fast.
        User defined sampling functions must accept two arguments of ``n``
        sampling points of dimension ``dim`` per call and output an array of
        sampling points with shape `n x dim`.

    workers : int or map-like callable, optional
        Sample and run the local serial minimizations in parallel.
        Supply -1 to use all available CPU cores, or an int to use
        that many Processes (uses `multiprocessing.Pool <multiprocessing>`).

        Alternatively supply a map-like callable, such as
        `multiprocessing.Pool.map` for parallel evaluation.
        This evaluation is carried out as ``workers(func, iterable)``.
        Requires that `func` be pickleable.

        .. versionadded:: 1.11.0

    Returns
    -------
    res : OptimizeResult
        The optimization result represented as a `OptimizeResult` object.
        Important attributes are:
        ``x`` the solution array corresponding to the global minimum,
        ``fun`` the function output at the global solution,
        ``xl`` an ordered list of local minima solutions,
        ``funl`` the function output at the corresponding local solutions,
        ``success`` a Boolean flag indicating if the optimizer exited
        successfully,
        ``message`` which describes the cause of the termination,
        ``nfev`` the total number of objective function evaluations including
        the sampling calls,
        ``nlfev`` the total number of objective function evaluations
        culminating from all local search optimizations,
        ``nit`` number of iterations performed by the global routine.

    Notes
    -----
    Global optimization using simplicial homology global optimization [1]_.
    Appropriate for solving general purpose NLP and blackbox optimization
    problems to global optimality (low-dimensional problems).

    In general, the optimization problems are of the form::

        minimize f(x) subject to

        g_i(x) >= 0,  i = 1,...,m
        h_j(x)  = 0,  j = 1,...,p

    where x is a vector of one or more variables. ``f(x)`` is the objective
    function ``R^n -> R``, ``g_i(x)`` are the inequality constraints, and
    ``h_j(x)`` are the equality constraints.

    Optionally, the lower and upper bounds for each element in x can also be
    specified using the `bounds` argument.

    While most of the theoretical advantages of SHGO are only proven for when
    ``f(x)`` is a Lipschitz smooth function, the algorithm is also proven to
    converge to the global optimum for the more general case where ``f(x)`` is
    non-continuous, non-convex and non-smooth, if the default sampling method
    is used [1]_.

    The local search method may be specified using the ``minimizer_kwargs``
    parameter which is passed on to ``scipy.optimize.minimize``. By default,
    the ``SLSQP`` method is used. In general, it is recommended to use the
    ``SLSQP``, ``COBYLA``, or ``COBYQA`` local minimization if inequality
    constraints are defined for the problem since the other methods do not use
    constraints.

    The ``halton`` and ``sobol`` method points are generated using
    `scipy.stats.qmc`. Any other QMC method could be used.

    References
    ----------
    .. [1] Endres, SC, Sandrock, C, Focke, WW (2018) "A simplicial homology
           algorithm for lipschitz optimisation", Journal of Global
           Optimization.
    .. [2] Joe, SW and Kuo, FY (2008) "Constructing Sobol' sequences with
           better  two-dimensional projections", SIAM J. Sci. Comput. 30,
           2635-2654.
    .. [3] Hock, W and Schittkowski, K (1981) "Test examples for nonlinear
           programming codes", Lecture Notes in Economics and Mathematical
           Systems, 187. Springer-Verlag, New York.
           http://www.ai7.uni-bayreuth.de/test_problem_coll.pdf
    .. [4] Wales, DJ (2015) "Perspective: Insight into reaction coordinates and
           dynamics from the potential energy landscape",
           Journal of Chemical Physics, 142(13), 2015.
    .. [5] https://docs.scipy.org/doc/scipy/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize

    Examples
    --------
    First consider the problem of minimizing the Rosenbrock function, `rosen`:

    >>> from scipy.optimize import rosen, shgo
    >>> bounds = [(0,2), (0, 2), (0, 2), (0, 2), (0, 2)]
    >>> result = shgo(rosen, bounds)
    >>> result.x, result.fun
    (array([1., 1., 1., 1., 1.]), 2.920392374190081e-18)

    Note that bounds determine the dimensionality of the objective
    function and is therefore a required input, however you can specify
    empty bounds using ``None`` or objects like ``np.inf`` which will be
    converted to large float numbers.

    >>> bounds = [(None, None), ]*4
    >>> result = shgo(rosen, bounds)
    >>> result.x
    array([0.99999851, 0.99999704, 0.99999411, 0.9999882 ])

    Next, we consider the Eggholder function, a problem with several local
    minima and one global minimum. We will demonstrate the use of arguments and
    the capabilities of `shgo`.
    (https://en.wikipedia.org/wiki/Test_functions_for_optimization)

    >>> import numpy as np
    >>> def eggholder(x):
    ...     return (-(x[1] + 47.0)
    ...             * np.sin(np.sqrt(abs(x[0]/2.0 + (x[1] + 47.0))))
    ...             - x[0] * np.sin(np.sqrt(abs(x[0] - (x[1] + 47.0))))
    ...             )
    ...
    >>> bounds = [(-512, 512), (-512, 512)]

    `shgo` has built-in low discrepancy sampling sequences. First, we will
    input 64 initial sampling points of the *Sobol'* sequence:

    >>> result = shgo(eggholder, bounds, n=64, sampling_method='sobol')
    >>> result.x, result.fun
    (array([512.        , 404.23180824]), -959.6406627208397)

    `shgo` also has a return for any other local minima that was found, these
    can be called using:

    >>> result.xl
    array([[ 512.        ,  404.23180824],
           [ 283.0759062 , -487.12565635],
           [-294.66820039, -462.01964031],
           [-105.87688911,  423.15323845],
           [-242.97926   ,  274.38030925],
           [-506.25823477,    6.3131022 ],
           [-408.71980731, -156.10116949],
           [ 150.23207937,  301.31376595],
           [  91.00920901, -391.283763  ],
           [ 202.89662724, -269.38043241],
           [ 361.66623976, -106.96493868],
           [-219.40612786, -244.06020508]])

    >>> result.funl
    array([-959.64066272, -718.16745962, -704.80659592, -565.99778097,
           -559.78685655, -557.36868733, -507.87385942, -493.9605115 ,
           -426.48799655, -421.15571437, -419.31194957, -410.98477763])

    These results are useful in applications where there are many global minima
    and the values of other global minima are desired or where the local minima
    can provide insight into the system (for example morphologies
    in physical chemistry [4]_).

    If we want to find a larger number of local minima, we can increase the
    number of sampling points or the number of iterations. We'll increase the
    number of sampling points to 64 and the number of iterations from the
    default of 1 to 3. Using ``simplicial`` this would have given us
    64 x 3 = 192 initial sampling points.

    >>> result_2 = shgo(eggholder,
    ...                 bounds, n=64, iters=3, sampling_method='sobol')
    >>> len(result.xl), len(result_2.xl)
    (12, 23)

    Note the difference between, e.g., ``n=192, iters=1`` and ``n=64,
    iters=3``.
    In the first case the promising points contained in the minimiser pool
    are processed only once. In the latter case it is processed every 64
    sampling points for a total of 3 times.

    To demonstrate solving problems with non-linear constraints consider the
    following example from Hock and Schittkowski problem 73 (cattle-feed)
    [3]_::

        minimize: f = 24.55 * x_1 + 26.75 * x_2 + 39 * x_3 + 40.50 * x_4

        subject to: 2.3 * x_1 + 5.6 * x_2 + 11.1 * x_3 + 1.3 * x_4 - 5    >= 0,

                    12 * x_1 + 11.9 * x_2 + 41.8 * x_3 + 52.1 * x_4 - 21
                        -1.645 * sqrt(0.28 * x_1**2 + 0.19 * x_2**2 +
                                      20.5 * x_3**2 + 0.62 * x_4**2)      >= 0,

                    x_1 + x_2 + x_3 + x_4 - 1                             == 0,

                    1 >= x_i >= 0 for all i

    The approximate answer given in [3]_ is::

        f([0.6355216, -0.12e-11, 0.3127019, 0.05177655]) = 29.894378

    >>> def f(x):  # (cattle-feed)
    ...     return 24.55*x[0] + 26.75*x[1] + 39*x[2] + 40.50*x[3]
    ...
    >>> def g1(x):
    ...     return 2.3*x[0] + 5.6*x[1] + 11.1*x[2] + 1.3*x[3] - 5  # >=0
    ...
    >>> def g2(x):
    ...     return (12*x[0] + 11.9*x[1] +41.8*x[2] + 52.1*x[3] - 21
    ...             - 1.645 * np.sqrt(0.28*x[0]**2 + 0.19*x[1]**2
    ...                             + 20.5*x[2]**2 + 0.62*x[3]**2)
    ...             ) # >=0
    ...
    >>> def h1(x):
    ...     return x[0] + x[1] + x[2] + x[3] - 1  # == 0
    ...
    >>> cons = ({'type': 'ineq', 'fun': g1},
    ...         {'type': 'ineq', 'fun': g2},
    ...         {'type': 'eq', 'fun': h1})
    >>> bounds = [(0, 1.0),]*4
    >>> res = shgo(f, bounds, n=150, constraints=cons)
    >>> res
     message: Optimization terminated successfully.
     success: True
         fun: 29.894378159142136
        funl: [ 2.989e+01]
           x: [ 6.355e-01  1.137e-13  3.127e-01  5.178e-02] # may vary
          xl: [[ 6.355e-01  1.137e-13  3.127e-01  5.178e-02]] # may vary
         nit: 1
        nfev: 142 # may vary
       nlfev: 35 # may vary
       nljev: 5
       nlhev: 0

    >>> g1(res.x), g2(res.x), h1(res.x)
    (-5.062616992290714e-14, -2.9594104944408173e-12, 0.0)

    """
    ...

class SHGO:
    def __init__(self, func, bounds, args=..., constraints=..., n=..., iters=..., callback=..., minimizer_kwargs=..., options=..., sampling_method=..., workers=...) -> None:
        ...
    
    def init_options(self, options): # -> None:
        """
        Initiates the options.

        Can also be useful to change parameters after class initiation.

        Parameters
        ----------
        options : dict

        Returns
        -------
        None

        """
        ...
    
    def __enter__(self): # -> Self:
        ...
    
    def __exit__(self, *args): # -> None:
        ...
    
    def iterate_all(self): # -> None:
        """
        Construct for `iters` iterations.

        If uniform sampling is used, every iteration adds 'n' sampling points.

        Iterations if a stopping criteria (e.g., sampling points or
        processing time) has been met.

        """
        ...
    
    def find_minima(self): # -> None:
        """
        Construct the minimizer pool, map the minimizers to local minima
        and sort the results into a global return object.
        """
        ...
    
    def find_lowest_vertex(self): # -> None:
        ...
    
    def finite_iterations(self): # -> bool:
        ...
    
    def finite_fev(self): # -> bool:
        ...
    
    def finite_ev(self): # -> None:
        ...
    
    def finite_time(self): # -> None:
        ...
    
    def finite_precision(self): # -> bool:
        """
        Stop the algorithm if the final function value is known

        Specify in options (with ``self.f_min_true = options['f_min']``)
        and the tolerance with ``f_tol = options['f_tol']``
        """
        ...
    
    def finite_homology_growth(self): # -> bool | None:
        """
        Stop the algorithm if homology group rank did not grow in iteration.
        """
        ...
    
    def stopping_criteria(self): # -> bool:
        """
        Various stopping criteria ran every iteration

        Returns
        -------
        stop : bool
        """
        ...
    
    def iterate(self): # -> None:
        ...
    
    def iterate_hypercube(self): # -> None:
        """
        Iterate a subdivision of the complex

        Note: called with ``self.iterate_complex()`` after class initiation
        """
        ...
    
    def iterate_delaunay(self): # -> None:
        """
        Build a complex of Delaunay triangulated points

        Note: called with ``self.iterate_complex()`` after class initiation
        """
        ...
    
    def minimizers(self): # -> NDArray[Any]:
        """
        Returns the indexes of all minimizers
        """
        ...
    
    def minimise_pool(self, force_iter=...): # -> None:
        """
        This processing method can optionally minimise only the best candidate
        solutions in the minimiser pool

        Parameters
        ----------
        force_iter : int
                     Number of starting minimizers to process (can be specified
                     globally or locally)

        """
        ...
    
    def sort_min_pool(self): # -> None:
        ...
    
    def trim_min_pool(self, trim_ind): # -> None:
        ...
    
    def g_topograph(self, x_min, X_min):
        """
        Returns the topographical vector stemming from the specified value
        ``x_min`` for the current feasible set ``X_min`` with True boolean
        values indicating positive entries and False values indicating
        negative entries.

        """
        ...
    
    def construct_lcb_simplicial(self, v_min): # -> list[list[Any]]:
        """
        Construct locally (approximately) convex bounds

        Parameters
        ----------
        v_min : Vertex object
                The minimizer vertex

        Returns
        -------
        cbounds : list of lists
            List of size dimension with length-2 list of bounds for each
            dimension.

        """
        ...
    
    def construct_lcb_delaunay(self, v_min, ind=...): # -> list[list[Any]]:
        """
        Construct locally (approximately) convex bounds

        Parameters
        ----------
        v_min : Vertex object
                The minimizer vertex

        Returns
        -------
        cbounds : list of lists
            List of size dimension with length-2 list of bounds for each
            dimension.
        """
        ...
    
    def minimize(self, x_min, ind=...):
        """
        This function is used to calculate the local minima using the specified
        sampling point as a starting value.

        Parameters
        ----------
        x_min : vector of floats
            Current starting point to minimize.

        Returns
        -------
        lres : OptimizeResult
            The local optimization result represented as a `OptimizeResult`
            object.
        """
        ...
    
    def sort_result(self): # -> OptimizeResult:
        """
        Sort results and build the global return object
        """
        ...
    
    def fail_routine(self, mes=...): # -> None:
        ...
    
    def sampled_surface(self, infty_cons_sampl=...): # -> None:
        """
        Sample the function surface.

        There are 2 modes, if ``infty_cons_sampl`` is True then the sampled
        points that are generated outside the feasible domain will be
        assigned an ``inf`` value in accordance with SHGO rules.
        This guarantees convergence and usually requires less objective
        function evaluations at the computational costs of more Delaunay
        triangulation points.

        If ``infty_cons_sampl`` is False, then the infeasible points are
        discarded and only a subspace of the sampled points are used. This
        comes at the cost of the loss of guaranteed convergence and usually
        requires more objective function evaluations.
        """
        ...
    
    def sampling_custom(self, n, dim): # -> ndarray[Any, Any]:
        """
        Generates uniform sampling points in a hypercube and scales the points
        to the bound limits.
        """
        ...
    
    def sampling_subspace(self): # -> None:
        """Find subspace of feasible points from g_func definition"""
        ...
    
    def sorted_samples(self): # -> tuple[NDArray[intp], ndarray[_Shape, dtype[Any]] | Any | ndarray[_Shape, Any]]:
        """Find indexes of the sorted sampling points"""
        ...
    
    def delaunay_triangulation(self, n_prc=...): # -> Tri | Delaunay:
        ...
    


class LMap:
    def __init__(self, v) -> None:
        ...
    


class LMapCache:
    def __init__(self) -> None:
        ...
    
    def __getitem__(self, v):
        ...
    
    def add_res(self, v, lres, bounds=...): # -> None:
        ...
    
    def sort_cache_result(self): # -> dict[Any, Any]:
        """
        Sort results and build the global return object
        """
        ...
    


