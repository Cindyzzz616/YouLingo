"""
This type stub file was generated by pyright.
"""

QUADRATIC_ASSIGNMENT_METHODS = ...
def quadratic_assignment(A, B, method=..., options=...):
    r"""
    Approximates solution to the quadratic assignment problem and
    the graph matching problem.

    Quadratic assignment solves problems of the following form:

    .. math::

        \min_P & \ {\ \text{trace}(A^T P B P^T)}\\
        \mbox{s.t. } & {P \ \epsilon \ \mathcal{P}}\\

    where :math:`\mathcal{P}` is the set of all permutation matrices,
    and :math:`A` and :math:`B` are square matrices.

    Graph matching tries to *maximize* the same objective function.
    This algorithm can be thought of as finding the alignment of the
    nodes of two graphs that minimizes the number of induced edge
    disagreements, or, in the case of weighted graphs, the sum of squared
    edge weight differences.

    Note that the quadratic assignment problem is NP-hard. The results given
    here are approximations and are not guaranteed to be optimal.


    Parameters
    ----------
    A : 2-D array, square
        The square matrix :math:`A` in the objective function above.

    B : 2-D array, square
        The square matrix :math:`B` in the objective function above.

    method :  str in {'faq', '2opt'} (default: 'faq')
        The algorithm used to solve the problem.
        :ref:`'faq' <optimize.qap-faq>` (default) and
        :ref:`'2opt' <optimize.qap-2opt>` are available.

    options : dict, optional
        A dictionary of solver options. All solvers support the following:

        maximize : bool (default: False)
            Maximizes the objective function if ``True``.

        partial_match : 2-D array of integers, optional (default: None)
            Fixes part of the matching. Also known as a "seed" [2]_.

            Each row of `partial_match` specifies a pair of matched nodes:
            node ``partial_match[i, 0]`` of `A` is matched to node
            ``partial_match[i, 1]`` of `B`. The array has shape ``(m, 2)``,
            where ``m`` is not greater than the number of nodes, :math:`n`.

        rng : `numpy.random.Generator`, optional
            Pseudorandom number generator state. When `rng` is None, a new
            `numpy.random.Generator` is created using entropy from the
            operating system. Types other than `numpy.random.Generator` are
            passed to `numpy.random.default_rng` to instantiate a ``Generator``.

            .. versionchanged:: 1.15.0
                As part of the `SPEC-007 <https://scientific-python.org/specs/spec-0007/>`_
                transition from use of `numpy.random.RandomState` to
                `numpy.random.Generator` is occurring. Supplying
                `np.random.RandomState` to this function will now emit a
                `DeprecationWarning`. In SciPy 1.17 its use will raise an exception.
                In addition relying on global state using `np.random.seed`
                will emit a `FutureWarning`. In SciPy 1.17 the global random number
                generator will no longer be used.
                Use of an int-like seed will raise a `FutureWarning`, in SciPy 1.17 it
                will be normalized via `np.random.default_rng` rather than
                `np.random.RandomState`.

        For method-specific options, see
        :func:`show_options('quadratic_assignment') <show_options>`.

    Returns
    -------
    res : OptimizeResult
        `OptimizeResult` containing the following fields.

        col_ind : 1-D array
            Column indices corresponding to the best permutation found of the
            nodes of `B`.
        fun : float
            The objective value of the solution.
        nit : int
            The number of iterations performed during optimization.

    Notes
    -----
    The default method :ref:`'faq' <optimize.qap-faq>` uses the Fast
    Approximate QAP algorithm [1]_; it typically offers the best combination of
    speed and accuracy.
    Method :ref:`'2opt' <optimize.qap-2opt>` can be computationally expensive,
    but may be a useful alternative, or it can be used to refine the solution
    returned by another method.

    References
    ----------
    .. [1] J.T. Vogelstein, J.M. Conroy, V. Lyzinski, L.J. Podrazik,
           S.G. Kratzer, E.T. Harley, D.E. Fishkind, R.J. Vogelstein, and
           C.E. Priebe, "Fast approximate quadratic programming for graph
           matching," PLOS one, vol. 10, no. 4, p. e0121002, 2015,
           :doi:`10.1371/journal.pone.0121002`

    .. [2] D. Fishkind, S. Adali, H. Patsolic, L. Meng, D. Singh, V. Lyzinski,
           C. Priebe, "Seeded graph matching", Pattern Recognit. 87 (2019):
           203-215, :doi:`10.1016/j.patcog.2018.09.014`

    .. [3] "2-opt," Wikipedia.
           https://en.wikipedia.org/wiki/2-opt

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.optimize import quadratic_assignment
    >>> rng = np.random.default_rng()
    >>> A = np.array([[0, 80, 150, 170], [80, 0, 130, 100],
    ...               [150, 130, 0, 120], [170, 100, 120, 0]])
    >>> B = np.array([[0, 5, 2, 7], [0, 0, 3, 8],
    ...               [0, 0, 0, 3], [0, 0, 0, 0]])
    >>> res = quadratic_assignment(A, B, options={'rng': rng})
    >>> print(res)
         fun: 3260
     col_ind: [0 3 2 1]
         nit: 9

    The see the relationship between the returned ``col_ind`` and ``fun``,
    use ``col_ind`` to form the best permutation matrix found, then evaluate
    the objective function :math:`f(P) = trace(A^T P B P^T )`.

    >>> perm = res['col_ind']
    >>> P = np.eye(len(A), dtype=int)[perm]
    >>> fun = np.trace(A.T @ P @ B @ P.T)
    >>> print(fun)
    3260

    Alternatively, to avoid constructing the permutation matrix explicitly,
    directly permute the rows and columns of the distance matrix.

    >>> fun = np.trace(A.T @ B[perm][:, perm])
    >>> print(fun)
    3260

    Although not guaranteed in general, ``quadratic_assignment`` happens to
    have found the globally optimal solution.

    >>> from itertools import permutations
    >>> perm_opt, fun_opt = None, np.inf
    >>> for perm in permutations([0, 1, 2, 3]):
    ...     perm = np.array(perm)
    ...     fun = np.trace(A.T @ B[perm][:, perm])
    ...     if fun < fun_opt:
    ...         fun_opt, perm_opt = fun, perm
    >>> print(np.array_equal(perm_opt, res['col_ind']))
    True

    Here is an example for which the default method,
    :ref:`'faq' <optimize.qap-faq>`, does not find the global optimum.

    >>> A = np.array([[0, 5, 8, 6], [5, 0, 5, 1],
    ...               [8, 5, 0, 2], [6, 1, 2, 0]])
    >>> B = np.array([[0, 1, 8, 4], [1, 0, 5, 2],
    ...               [8, 5, 0, 5], [4, 2, 5, 0]])
    >>> res = quadratic_assignment(A, B, options={'rng': rng})
    >>> print(res)
         fun: 178
     col_ind: [1 0 3 2]
         nit: 13

    If accuracy is important, consider using  :ref:`'2opt' <optimize.qap-2opt>`
    to refine the solution.

    >>> guess = np.array([np.arange(len(A)), res.col_ind]).T
    >>> res = quadratic_assignment(A, B, method="2opt",
    ...     options = {'rng': rng, 'partial_guess': guess})
    >>> print(res)
         fun: 176
     col_ind: [1 2 3 0]
         nit: 17

    """
    ...

