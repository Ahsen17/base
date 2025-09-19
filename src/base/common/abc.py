from collections.abc import Awaitable, Callable
from typing import Any


type JsonString = str
type JsonBytes = bytes

type AnyCallable = Callable[..., Any]
type AnyAsyncCallable = Callable[..., Awaitable[Any]]
