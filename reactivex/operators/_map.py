from typing import TypeVar, cast

from reactivex import Observable, abc, typing
from reactivex import operators as ops
from reactivex.internal import curry_flip
from reactivex.internal.basic import identity
from reactivex.internal.utils import infinite
from reactivex.typing import Mapper, MapperIndexed

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")


@curry_flip
def map_(
    source: Observable[_T1],
    mapper: Mapper[_T1, _T2] | None = None,
) -> Observable[_T2]:
    """Project each element of an observable sequence into a new form.

    Example:
        >>> result = source.pipe(map(lambda x: x * 2))
        >>> result = map(lambda x: x * 2)(source)

    Args:
        source: The observable source to transform.
        mapper: A transform function to apply to each element.

    Returns:
        Returns an observable sequence whose elements are the
        result of invoking the transform function on each element
        of the source.
    """
    pass


@curry_flip
def map_indexed_(
    source: Observable[_T1],
    mapper_indexed: MapperIndexed[_T1, _T2] | None = None,
) -> Observable[_T2]:
    """Project each element of an observable sequence into a new form by
    incorporating the element's index.

    Example:
        >>> result = source.pipe(map_indexed(lambda x, i: (x, i)))
        >>> result = map_indexed(lambda x, i: (x, i))(source)

    Args:
        source: The observable source to transform.
        mapper_indexed: A transform function to apply to each element with its index.

    Returns:
        An observable sequence whose elements are the result of invoking
        the transform function on each element with its index.
    """

    def _identity(value: _T1, _: int) -> _T2:
        pass

    _mapper_indexed = mapper_indexed or cast(typing.MapperIndexed[_T1, _T2], _identity)

    return source.pipe(
        ops.zip_with_iterable(infinite()),
        ops.starmap_indexed(_mapper_indexed),  # type: ignore
    )


__all__ = ["map_", "map_indexed_"]
