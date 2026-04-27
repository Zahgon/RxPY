from datetime import datetime, timezone
from typing import Any, NoReturn, TypeVar

_T = TypeVar("_T")


def noop(*args: Any, **kw: Any) -> None:
    """No operation. Returns nothing"""


def identity(x: _T) -> _T:
    """Returns argument x"""
    pass


def default_now() -> datetime:
    return datetime.now(timezone.utc)


def default_comparer(x: _T, y: _T) -> bool:
    pass


def default_sub_comparer(x: Any, y: Any) -> Any:
    pass


def default_key_serializer(x: Any) -> str:
    pass


def default_error(err: Exception | str) -> NoReturn:
    pass
