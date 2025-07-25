"""
This type stub file was generated by pyright.
"""

from scipy.stats._distribution_infrastructure import ContinuousDistribution, DiscreteDistribution

__all__ = ['Normal', 'Uniform', 'Binomial']
class Normal(ContinuousDistribution):
    r"""Normal distribution with prescribed mean and standard deviation.

    The probability density function of the normal distribution is:

    .. math::

        f(x) = \frac{1}{\sigma \sqrt{2 \pi}} \exp {
            \left( -\frac{1}{2}\left( \frac{x - \mu}{\sigma} \right)^2 \right)}

    """
    _mu_domain = ...
    _sigma_domain = ...
    _x_support = ...
    _mu_param = ...
    _sigma_param = ...
    _x_param = ...
    _parameterizations = ...
    _variable = ...
    _normalization = ...
    _log_normalization = ...
    def __new__(cls, mu=..., sigma=..., **kwargs): # -> Self:
        ...
    
    def __init__(self, *, mu=..., sigma=..., **kwargs) -> None:
        ...
    


class StandardNormal(Normal):
    r"""Standard normal distribution.

    The probability density function of the standard normal distribution is:

    .. math::

        f(x) = \frac{1}{\sqrt{2 \pi}} \exp \left( -\frac{1}{2} x^2 \right)

    """
    _x_support = ...
    _x_param = ...
    _variable = ...
    _parameterizations = ...
    _normalization = ...
    _log_normalization = ...
    mu = ...
    sigma = ...
    def __init__(self, **kwargs) -> None:
        ...
    


class _LogUniform(ContinuousDistribution):
    r"""Log-uniform distribution.

    The probability density function of the log-uniform distribution is:

    .. math::

        f(x; a, b) = \frac{1}
                          {x (\log(b) - \log(a))}

    If :math:`\log(X)` is a random variable that follows a uniform distribution
    between :math:`\log(a)` and :math:`\log(b)`, then :math:`X` is log-uniformly
    distributed with shape parameters :math:`a` and :math:`b`.

    """
    _a_domain = ...
    _b_domain = ...
    _log_a_domain = ...
    _log_b_domain = ...
    _x_support = ...
    _a_param = ...
    _b_param = ...
    _log_a_param = ...
    _log_b_param = ...
    _x_param = ...
    _parameterizations = ...
    _variable = ...
    def __init__(self, *, a=..., b=..., log_a=..., log_b=..., **kwargs) -> None:
        ...
    


class Uniform(ContinuousDistribution):
    r"""Uniform distribution.

    The probability density function of the uniform distribution is:

    .. math::

        f(x; a, b) = \frac{1}
                          {b - a}

    """
    _a_domain = ...
    _b_domain = ...
    _x_support = ...
    _a_param = ...
    _b_param = ...
    _x_param = ...
    _parameterizations = ...
    _variable = ...
    def __init__(self, *, a=..., b=..., **kwargs) -> None:
        ...
    


class _Gamma(ContinuousDistribution):
    _a_domain = ...
    _x_support = ...
    _a_param = ...
    _x_param = ...
    _parameterizations = ...
    _variable = ...


class Binomial(DiscreteDistribution):
    r"""Binomial distribution with prescribed success probability and number of trials

    The probability density function of the binomial distribution is:

    .. math::

        f(x) = {n \choose x} p^x (1 - p)^{n-x}

    """
    _n_domain = ...
    _p_domain = ...
    _x_support = ...
    _n_param = ...
    _p_param = ...
    _x_param = ...
    _parameterizations = ...
    _variable = ...
    def __init__(self, *, n, p, **kwargs) -> None:
        ...
    


_module = ...
