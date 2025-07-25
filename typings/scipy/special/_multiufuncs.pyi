"""
This type stub file was generated by pyright.
"""

from ._special_ufuncs import assoc_legendre_p, legendre_p, sph_harm_y, sph_legendre_p
from ._gufuncs import assoc_legendre_p_all, legendre_p_all, sph_harm_y_all, sph_legendre_p_all

__all__ = ["assoc_legendre_p", "assoc_legendre_p_all", "legendre_p", "legendre_p_all", "sph_harm_y", "sph_harm_y_all", "sph_legendre_p", "sph_legendre_p_all"]
class MultiUFunc:
    def __init__(self, ufunc_or_ufuncs, doc=..., *, force_complex_output=..., **default_kwargs) -> None:
        ...
    
    @property
    def __doc__(self): # -> None:
        ...
    
    def __call__(self, *args, **kwargs): # -> Any:
        ...
    


sph_legendre_p = ...
@sph_legendre_p._override_key
def _(diff_n): # -> int:
    ...

@sph_legendre_p._override_finalize_out
def _(out): # -> NDArray[Any]:
    ...

sph_legendre_p_all = ...
@sph_legendre_p_all._override_key
def _(diff_n): # -> int:
    ...

@sph_legendre_p_all._override_ufunc_default_kwargs
def _(diff_n): # -> dict[str, list[tuple[Literal[0], Literal[1], Literal[-1]] | tuple[()]]]:
    ...

@sph_legendre_p_all._override_resolve_out_shapes
def _(n, m, theta_shape, nout, diff_n): # -> tuple[Any]:
    ...

@sph_legendre_p_all._override_finalize_out
def _(out): # -> NDArray[Any]:
    ...

assoc_legendre_p = ...
@assoc_legendre_p._override_key
def _(branch_cut, norm, diff_n): # -> tuple[Any, int]:
    ...

@assoc_legendre_p._override_ufunc_default_args
def _(branch_cut, norm, diff_n): # -> tuple[Any]:
    ...

@assoc_legendre_p._override_finalize_out
def _(out): # -> NDArray[Any]:
    ...

assoc_legendre_p_all = ...
@assoc_legendre_p_all._override_key
def _(branch_cut, norm, diff_n): # -> tuple[Any, Integral]:
    ...

@assoc_legendre_p_all._override_ufunc_default_args
def _(branch_cut, norm, diff_n): # -> tuple[Any]:
    ...

@assoc_legendre_p_all._override_ufunc_default_kwargs
def _(branch_cut, norm, diff_n): # -> dict[str, list[tuple[Literal[0], Literal[1], Literal[-1]] | tuple[()]]]:
    ...

@assoc_legendre_p_all._override_resolve_out_shapes
def _(n, m, z_shape, branch_cut_shape, nout, **kwargs): # -> tuple[tuple[_ComplexLike, Any, *tuple[int, ...], Any]]:
    ...

@assoc_legendre_p_all._override_finalize_out
def _(out): # -> NDArray[Any]:
    ...

legendre_p = ...
@legendre_p._override_key
def _(diff_n): # -> Integral:
    ...

@legendre_p._override_finalize_out
def _(out): # -> NDArray[Any]:
    ...

legendre_p_all = ...
@legendre_p_all._override_key
def _(diff_n): # -> int:
    ...

@legendre_p_all._override_ufunc_default_kwargs
def _(diff_n): # -> dict[str, list[Any]]:
    ...

@legendre_p_all._override_resolve_out_shapes
def _(n, z_shape, nout, diff_n):
    ...

@legendre_p_all._override_finalize_out
def _(out): # -> NDArray[Any]:
    ...

sph_harm_y = ...
@sph_harm_y._override_key
def _(diff_n): # -> int:
    ...

@sph_harm_y._override_finalize_out
def _(out): # -> tuple[Any, Any] | tuple[Any, Any, Any] | None:
    ...

sph_harm_y_all = ...
@sph_harm_y_all._override_key
def _(diff_n): # -> int:
    ...

@sph_harm_y_all._override_ufunc_default_kwargs
def _(diff_n): # -> dict[str, list[tuple[Literal[0], Literal[1], Literal[-2], Literal[-1]] | tuple[()]]]:
    ...

@sph_harm_y_all._override_resolve_out_shapes
def _(n, m, theta_shape, phi_shape, nout, **kwargs): # -> tuple[tuple[_ComplexLike, Any, *tuple[int, ...], Any, Any]]:
    ...

@sph_harm_y_all._override_finalize_out
def _(out): # -> tuple[Any, Any] | tuple[Any, Any, Any] | None:
    ...

