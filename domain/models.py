"""Data models for the terminal calculator application."""

from dataclasses import dataclass
from datetime import datetime
from typing import Union, Literal, Protocol, Callable


@dataclass
class ExpressionToken:
    """Represents a token in a mathematical expression."""
    type: Literal['number', 'operator', 'parenthesis']
    value: Union[str, float]
    position: int


@dataclass
class CalculationRecord:
    """Represents a completed calculation with its result and metadata."""
    expression: str
    result: float
    timestamp: datetime


class OperationHandler(Protocol):
    """Protocol defining the interface for mathematical operation handlers."""
    symbol: str
    precedence: int
    execute: Callable[[float, float], float]