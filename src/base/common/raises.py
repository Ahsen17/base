from returns.result import Result, safe

from .abc import AnyCallable


def raises[T](*exception: type[Exception]) -> AnyCallable:
    """Declare exceptions function may raise."""

    def decorator(function: AnyCallable) -> AnyCallable:
        function.__raises__ = exception  # pyright: ignore[reportFunctionMemberAccess]

        @safe
        def wrapper(*args, **kwargs) -> T | Result[T, Exception]:
            return function(*args, **kwargs)

        return wrapper

    return decorator
