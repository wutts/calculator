"""
Basic arithmetic operations for the terminal calculator.

This module provides the core mathematical operations (+, -, *, /) with proper
error handling and metadata for precedence and associativity.
"""

from typing import Dict, Callable, Tuple
from dataclasses import dataclass


@dataclass
class OperationMetadata:
    """Metadata for mathematical operations."""
    precedence: int
    associativity: str  # 'left' or 'right'
    symbol: str


class ArithmeticError(Exception):
    """Custom exception for arithmetic operation errors."""
    pass


def add(a: float, b: float) -> float:
    """
    Perform addition operation.
    
    Args:
        a: First operand
        b: Second operand
        
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Perform subtraction operation.
    
    Args:
        a: First operand (minuend)
        b: Second operand (subtrahend)
        
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Perform multiplication operation.
    
    Args:
        a: First operand
        b: Second operand
        
    Returns:
        Product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Perform division operation with zero division error handling.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Quotient of a and b
        
    Raises:
        ArithmeticError: When attempting to divide by zero
    """
    if b == 0:
        raise ArithmeticError("Division by zero is not allowed")
    return a / b


# Operation registry with metadata
OPERATIONS: Dict[str, Tuple[Callable[[float, float], float], OperationMetadata]] = {
    '+': (add, OperationMetadata(precedence=1, associativity='left', symbol='+')),
    '-': (subtract, OperationMetadata(precedence=1, associativity='left', symbol='-')),
    '*': (multiply, OperationMetadata(precedence=2, associativity='left', symbol='*')),
    '/': (divide, OperationMetadata(precedence=2, associativity='left', symbol='/')),
}


def get_operation(symbol: str) -> Tuple[Callable[[float, float], float], OperationMetadata]:
    """
    Get operation function and metadata by symbol.
    
    Args:
        symbol: Operation symbol (+, -, *, /)
        
    Returns:
        Tuple of (operation_function, operation_metadata)
        
    Raises:
        KeyError: If operation symbol is not supported
    """
    if symbol not in OPERATIONS:
        raise KeyError(f"Unsupported operation: {symbol}")
    return OPERATIONS[symbol]


def get_supported_operations() -> Dict[str, OperationMetadata]:
    """
    Get all supported operations and their metadata.
    
    Returns:
        Dictionary mapping operation symbols to their metadata
    """
    return {symbol: metadata for symbol, (_, metadata) in OPERATIONS.items()}


def execute_operation(symbol: str, a: float, b: float) -> float:
    """
    Execute an operation by symbol.
    
    Args:
        symbol: Operation symbol (+, -, *, /)
        a: First operand
        b: Second operand
        
    Returns:
        Result of the operation
        
    Raises:
        KeyError: If operation symbol is not supported
        ArithmeticError: For mathematical errors (e.g., division by zero)
    """
    operation_func, _ = get_operation(symbol)
    return operation_func(a, b)