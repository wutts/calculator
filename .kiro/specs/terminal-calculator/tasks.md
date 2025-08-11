# Implementation Plan

- [x] 1. Set up project structure and data models
  - Create directory structure: `domain/`, `infrastructure/`, `ui/`, `app/`
  - Add `__init__.py` files to make packages importable
  - Create ExpressionToken and CalculationRecord dataclasses in `domain/models.py`
  - Define OperationHandler protocol for type hints
  - _Requirements: 5.1, 6.1, 6.3_

- [-] 2. Implement basic arithmetic operations
  - Create `domain/operations.py` with basic operation functions (+, -, *, /)
  - Implement division by zero error handling
  - Add operation metadata (precedence, associativity)
  - Write unit tests for all arithmetic operations
  - _Requirements: 2.1-2.5_

- [ ] 3. Build expression parser using AST
  - Create `domain/expression_parser.py` using Python's `ast` module
  - Implement safe expression parsing without `eval()`
  - Add syntax validation and error handling for malformed expressions
  - Handle parentheses and operator precedence through AST
  - Write unit tests for parsing various expression formats
  - _Requirements: 3.1-3.3, 4.1, 4.2_

- [ ] 4. Implement calculation engine
  - Create `domain/calculation_engine.py` with AST visitor pattern
  - Implement safe evaluation of parsed expressions
  - Integrate with arithmetic operations from step 2
  - Add comprehensive mathematical error handling
  - Write unit tests for calculation accuracy and edge cases
  - _Requirements: 2.1-2.5, 3.1-3.2, 4.1-4.4_

- [ ] 5. Create history manager
  - Implement `infrastructure/history_manager.py` using `collections.deque`
  - Add methods for storing and retrieving last 10 calculations
  - Implement automatic cleanup when history exceeds capacity
  - Add clear history functionality
  - Write unit tests for history storage and retrieval
  - _Requirements: 7.1-7.4_

- [ ] 6. Build terminal interface
  - Create `ui/terminal_interface.py` with input/output methods
  - Implement welcome message, user prompting, and result display
  - Add formatted history display functionality
  - Include error message formatting for user-friendly feedback
  - Handle keyboard interrupts (Ctrl+C) gracefully on macOS
  - Write unit tests using `io.StringIO` for I/O simulation
  - _Requirements: 1.1, 4.3, 4.4, 7.1, 8.2_

- [ ] 7. Implement calculator controller
  - Create `app/calculator_controller.py` with main application loop
  - Add input processing for expressions and commands ("history", "quit", "exit")
  - Integrate all components (parser, engine, history, interface)
  - Implement comprehensive error handling with user-friendly messages
  - Add signal handling for graceful shutdown on macOS
  - Write unit tests for controller logic and error scenarios
  - _Requirements: 1.2-1.4, 4.1-4.4, 8.2_

- [ ] 8. Create main entry point and integration tests
  - Create `calculator.py` as main application entry point
  - Implement application initialization and startup
  - Write integration tests testing complete user workflows
  - Test end-to-end scenarios with complex expressions and error cases
  - Verify all requirements through automated testing
  - _Requirements: 1.1-1.4, 8.1-8.5_

- [ ] 9. Final validation and documentation
  - Run comprehensive test suite covering all components
  - Test calculator with various mathematical expressions and edge cases
  - Validate error handling with invalid inputs and system errors
  - Verify history functionality and capacity limits
  - Test macOS Terminal compatibility and signal handling
  - Update README.md with usage instructions and examples
  - _Requirements: All requirements 1-8_