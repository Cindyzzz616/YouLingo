"""
This type stub file was generated by pyright.
"""

"""
Contingency table functions (:mod:`scipy.stats.contingency`)
============================================================

Functions for creating and analyzing contingency tables.

.. currentmodule:: scipy.stats.contingency

.. autosummary::
   :toctree: generated/

   chi2_contingency
   relative_risk
   odds_ratio
   crosstab
   association

   expected_freq
   margins

"""
__all__ = ['margins', 'expected_freq', 'chi2_contingency', 'crosstab', 'association', 'relative_risk', 'odds_ratio']
def margins(a): # -> list[Any]:
    """Return a list of the marginal sums of the array `a`.

    Parameters
    ----------
    a : ndarray
        The array for which to compute the marginal sums.

    Returns
    -------
    margsums : list of ndarrays
        A list of length `a.ndim`.  `margsums[k]` is the result
        of summing `a` over all axes except `k`; it has the same
        number of dimensions as `a`, but the length of each axis
        except axis `k` will be 1.

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.stats.contingency import margins

    >>> a = np.arange(12).reshape(2, 6)
    >>> a
    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11]])
    >>> m0, m1 = margins(a)
    >>> m0
    array([[15],
           [51]])
    >>> m1
    array([[ 6,  8, 10, 12, 14, 16]])

    >>> b = np.arange(24).reshape(2,3,4)
    >>> m0, m1, m2 = margins(b)
    >>> m0
    array([[[ 66]],
           [[210]]])
    >>> m1
    array([[[ 60],
            [ 92],
            [124]]])
    >>> m2
    array([[[60, 66, 72, 78]]])
    """
    ...

def expected_freq(observed): # -> Any:
    """
    Compute the expected frequencies from a contingency table.

    Given an n-dimensional contingency table of observed frequencies,
    compute the expected frequencies for the table based on the marginal
    sums under the assumption that the groups associated with each
    dimension are independent.

    Parameters
    ----------
    observed : array_like
        The table of observed frequencies.  (While this function can handle
        a 1-D array, that case is trivial.  Generally `observed` is at
        least 2-D.)

    Returns
    -------
    expected : ndarray of float64
        The expected frequencies, based on the marginal sums of the table.
        Same shape as `observed`.

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.stats.contingency import expected_freq
    >>> observed = np.array([[10, 10, 20],[20, 20, 20]])
    >>> expected_freq(observed)
    array([[ 12.,  12.,  16.],
           [ 18.,  18.,  24.]])

    """
    ...

Chi2ContingencyResult = ...
def chi2_contingency(observed, correction=..., lambda_=..., *, method=...): # -> _:
    """Chi-square test of independence of variables in a contingency table.

    This function computes the chi-square statistic and p-value for the
    hypothesis test of independence of the observed frequencies in the
    contingency table [1]_ `observed`.  The expected frequencies are computed
    based on the marginal sums under the assumption of independence; see
    `scipy.stats.contingency.expected_freq`.  The number of degrees of
    freedom is (expressed using numpy functions and attributes)::

        dof = observed.size - sum(observed.shape) + observed.ndim - 1


    Parameters
    ----------
    observed : array_like
        The contingency table. The table contains the observed frequencies
        (i.e. number of occurrences) in each category.  In the two-dimensional
        case, the table is often described as an "R x C table".
    correction : bool, optional
        If True, *and* the degrees of freedom is 1, apply Yates' correction
        for continuity.  The effect of the correction is to adjust each
        observed value by 0.5 towards the corresponding expected value.
    lambda_ : float or str, optional
        By default, the statistic computed in this test is Pearson's
        chi-squared statistic [2]_.  `lambda_` allows a statistic from the
        Cressie-Read power divergence family [3]_ to be used instead.  See
        `scipy.stats.power_divergence` for details.
    method : ResamplingMethod, optional
        Defines the method used to compute the p-value. Compatible only with
        `correction=False`,  default `lambda_`, and two-way tables.
        If `method` is an instance of `PermutationMethod`/`MonteCarloMethod`,
        the p-value is computed using
        `scipy.stats.permutation_test`/`scipy.stats.monte_carlo_test` with the
        provided configuration options and other appropriate settings.
        Otherwise, the p-value is computed as documented in the notes.
        Note that if `method` is an instance of `MonteCarloMethod`, the ``rvs``
        attribute must be left unspecified; Monte Carlo samples are always drawn
        using the ``rvs`` method of `scipy.stats.random_table`.

        .. versionadded:: 1.15.0


    Returns
    -------
    res : Chi2ContingencyResult
        An object containing attributes:

        statistic : float
            The test statistic.
        pvalue : float
            The p-value of the test.
        dof : int
            The degrees of freedom. NaN if `method` is not ``None``.
        expected_freq : ndarray, same shape as `observed`
            The expected frequencies, based on the marginal sums of the table.

    See Also
    --------
    scipy.stats.contingency.expected_freq
    scipy.stats.fisher_exact
    scipy.stats.chisquare
    scipy.stats.power_divergence
    scipy.stats.barnard_exact
    scipy.stats.boschloo_exact
    :ref:`hypothesis_chi2_contingency` : Extended example

    Notes
    -----
    An often quoted guideline for the validity of this calculation is that
    the test should be used only if the observed and expected frequencies
    in each cell are at least 5.

    This is a test for the independence of different categories of a
    population. The test is only meaningful when the dimension of
    `observed` is two or more.  Applying the test to a one-dimensional
    table will always result in `expected` equal to `observed` and a
    chi-square statistic equal to 0.

    This function does not handle masked arrays, because the calculation
    does not make sense with missing values.

    Like `scipy.stats.chisquare`, this function computes a chi-square
    statistic; the convenience this function provides is to figure out the
    expected frequencies and degrees of freedom from the given contingency
    table. If these were already known, and if the Yates' correction was not
    required, one could use `scipy.stats.chisquare`.  That is, if one calls::

        res = chi2_contingency(obs, correction=False)

    then the following is true::

        (res.statistic, res.pvalue) == stats.chisquare(obs.ravel(),
                                                       f_exp=ex.ravel(),
                                                       ddof=obs.size - 1 - dof)

    The `lambda_` argument was added in version 0.13.0 of scipy.

    References
    ----------
    .. [1] "Contingency table",
           https://en.wikipedia.org/wiki/Contingency_table
    .. [2] "Pearson's chi-squared test",
           https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test
    .. [3] Cressie, N. and Read, T. R. C., "Multinomial Goodness-of-Fit
           Tests", J. Royal Stat. Soc. Series B, Vol. 46, No. 3 (1984),
           pp. 440-464.

    Examples
    --------
    A two-way example (2 x 3):

    >>> import numpy as np
    >>> from scipy.stats import chi2_contingency
    >>> obs = np.array([[10, 10, 20], [20, 20, 20]])
    >>> res = chi2_contingency(obs)
    >>> res.statistic
    2.7777777777777777
    >>> res.pvalue
    0.24935220877729619
    >>> res.dof
    2
    >>> res.expected_freq
    array([[ 12.,  12.,  16.],
           [ 18.,  18.,  24.]])

    Perform the test using the log-likelihood ratio (i.e. the "G-test")
    instead of Pearson's chi-squared statistic.

    >>> res = chi2_contingency(obs, lambda_="log-likelihood")
    >>> res.statistic
    2.7688587616781319
    >>> res.pvalue
    0.25046668010954165

    A four-way example (2 x 2 x 2 x 2):

    >>> obs = np.array(
    ...     [[[[12, 17],
    ...        [11, 16]],
    ...       [[11, 12],
    ...        [15, 16]]],
    ...      [[[23, 15],
    ...        [30, 22]],
    ...       [[14, 17],
    ...        [15, 16]]]])
    >>> res = chi2_contingency(obs)
    >>> res.statistic
    8.7584514426741897
    >>> res.pvalue
    0.64417725029295503

    When the sum of the elements in a two-way table is small, the p-value
    produced by the default asymptotic approximation may be inaccurate.
    Consider passing a `PermutationMethod` or `MonteCarloMethod` as the
    `method` parameter with `correction=False`.

    >>> from scipy.stats import PermutationMethod
    >>> obs = np.asarray([[12, 3],
    ...                   [17, 16]])
    >>> res = chi2_contingency(obs, correction=False)
    >>> ref = chi2_contingency(obs, correction=False, method=PermutationMethod())
    >>> res.pvalue, ref.pvalue
    (0.0614122539870913, 0.1074)  # may vary

    For a more detailed example, see :ref:`hypothesis_chi2_contingency`.

    """
    ...

def association(observed, method=..., correction=..., lambda_=...): # -> float:
    """Calculates degree of association between two nominal variables.

    The function provides the option for computing one of three measures of
    association between two nominal variables from the data given in a 2d
    contingency table: Tschuprow's T, Pearson's Contingency Coefficient
    and Cramer's V.

    Parameters
    ----------
    observed : array-like
        The array of observed values
    method : {"cramer", "tschuprow", "pearson"} (default = "cramer")
        The association test statistic.
    correction : bool, optional
        Inherited from `scipy.stats.contingency.chi2_contingency()`
    lambda_ : float or str, optional
        Inherited from `scipy.stats.contingency.chi2_contingency()`

    Returns
    -------
    statistic : float
        Value of the test statistic

    Notes
    -----
    Cramer's V, Tschuprow's T and Pearson's Contingency Coefficient, all
    measure the degree to which two nominal or ordinal variables are related,
    or the level of their association. This differs from correlation, although
    many often mistakenly consider them equivalent. Correlation measures in
    what way two variables are related, whereas, association measures how
    related the variables are. As such, association does not subsume
    independent variables, and is rather a test of independence. A value of
    1.0 indicates perfect association, and 0.0 means the variables have no
    association.

    Both the Cramer's V and Tschuprow's T are extensions of the phi
    coefficient.  Moreover, due to the close relationship between the
    Cramer's V and Tschuprow's T the returned values can often be similar
    or even equivalent.  They are likely to diverge more as the array shape
    diverges from a 2x2.

    References
    ----------
    .. [1] "Tschuprow's T",
           https://en.wikipedia.org/wiki/Tschuprow's_T
    .. [2] Tschuprow, A. A. (1939)
           Principles of the Mathematical Theory of Correlation;
           translated by M. Kantorowitsch. W. Hodge & Co.
    .. [3] "Cramer's V", https://en.wikipedia.org/wiki/Cramer's_V
    .. [4] "Nominal Association: Phi and Cramer's V",
           http://www.people.vcu.edu/~pdattalo/702SuppRead/MeasAssoc/NominalAssoc.html
    .. [5] Gingrich, Paul, "Association Between Variables",
           http://uregina.ca/~gingrich/ch11a.pdf

    Examples
    --------
    An example with a 4x2 contingency table:

    >>> import numpy as np
    >>> from scipy.stats.contingency import association
    >>> obs4x2 = np.array([[100, 150], [203, 322], [420, 700], [320, 210]])

    Pearson's contingency coefficient

    >>> association(obs4x2, method="pearson")
    0.18303298140595667

    Cramer's V

    >>> association(obs4x2, method="cramer")
    0.18617813077483678

    Tschuprow's T

    >>> association(obs4x2, method="tschuprow")
    0.14146478765062995
    """
    ...

