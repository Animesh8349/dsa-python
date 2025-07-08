# Data Structures and Algorithms in Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-blue.svg)](https://python-poetry.org/)

An educational project focused on implementing fundamental data structures and algorithms in Python. This repository serves as a learning resource for understanding how core computer science concepts work under the hood.

## 🎯 Project Objectives

- **Learn by Implementation**: Gain deep understanding of data structures and algorithms through hands-on coding
- **Educational Focus**: Clear, well-documented code that prioritizes learning over performance optimization
- **Test-Driven Development**: Comprehensive test coverage to ensure correctness and reliability
- **Open Source Contribution**: Encourage collaborative learning and contributions from the community

## 📚 What's Included

### Data Structures

- **Linked Lists**
  - Singly Linked List
  - Doubly Linked List
  - Singly Circular Linked List
  - Doubly Circular Linked List
- **More coming soon...**

### Algorithms

- **Coming soon...**

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- Poetry (for dependency management)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/dsa-python.git
   cd dsa-python
   ```

2. **Install dependencies using Poetry**

   ```bash
   poetry install
   ```

3. **Activate the virtual environment**

   ```bash
   poetry shell
   ```

### Running Tests

Run all tests:

```bash
poetry run pytest
```

Run tests with verbose output:

```bash
poetry run pytest -v
```

Run tests for a specific module:

```bash
poetry run pytest tests/test_linked_lists/
```

Run tests with coverage:

```bash
poetry run pytest --cov=src
```

### Code Quality Tools

**Format code with Black:**

```bash
poetry run black src/ tests/
```

**Lint with Flake8:**

```bash
poetry run flake8 src/ tests/
```

**Type checking with mypy:**

```bash
poetry run mypy src/
```

## 📖 Usage Examples

### Singly Linked List

```python
from src.data_structures.linked_lists.singly_linked_list import SinglyLinkedList

# Create a new linked list
ll = SinglyLinkedList()

# Add elements
ll.append(1)
ll.append(2)
ll.append(3)

# Display the list
print(ll)  # Output: 1 -> 2 -> 3 -> None

# Access elements
print(ll.get(1))  # Output: 2

# Remove elements
ll.remove(2)
print(ll)  # Output: 1 -> 3 -> None
```

## 🏗️ Project Structure

```text
dsa-python/
├── src/
│   ├── data_structures/
│   │   └── linked_lists/
│   │       ├── singly_linked_list/
│   │       ├── doubly_linked_list/
│   │       ├── singly_circular_linked_list/
│   │       └── doubly_circular_linked_list/
│   └── algorithms/
├── tests/
│   └── test_linked_lists/
├── pyproject.toml
├── poetry.lock
└── README.md
```

## 🛠️ Development

### Adding New Data Structures

1. Create a new module in `src/data_structures/`
2. Implement the data structure with clear documentation
3. Add comprehensive tests in `tests/`
4. Update this README with usage examples

### Adding New Algorithms

1. Create a new module in `src/algorithms/`
2. Implement the algorithm with clear documentation
3. Add comprehensive tests in `tests/`
4. Update this README with usage examples

## 🧪 Testing Philosophy

This project follows test-driven development principles:

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test how components work together
- **Property-Based Testing**: Use Hypothesis for testing with random inputs
- **Performance Tests**: Benchmark critical operations

## 📊 Dependencies

### Core Dependencies

- **Python 3.13+**: Latest Python features and performance improvements
- **graphviz**: For visualizing data structures
- **ipython**: Enhanced interactive Python shell
- **jupyter**: For interactive notebooks and demonstrations
- **matplotlib**: For plotting algorithm performance and visualizations

### Development Dependencies

- **pytest**: Testing framework
- **pytest-benchmark**: Performance benchmarking
- **hypothesis**: Property-based testing
- **black**: Code formatting
- **flake8**: Linting
- **mypy**: Type checking

## 🤝 Contributing

Contributions are welcome! This is an educational project, so clarity and learning value are prioritized over performance optimizations.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Implement your changes with tests
4. Ensure all tests pass and code is formatted
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Contribution Guidelines

- Write clear, self-documenting code
- Include comprehensive tests for new features
- Follow the existing code style (use Black for formatting)
- Add docstrings for all public methods and classes
- Update the README if you add new features

## 📋 TODO

- [ ] Implement stack and queue data structures
- [ ] Add tree structures (Binary Tree, BST, AVL, etc.)
- [ ] Implement graph data structures and algorithms
- [ ] Add sorting algorithms (Quick Sort, Merge Sort, etc.)
- [ ] Add searching algorithms (Binary Search, etc.)
- [ ] Create visualization tools for data structures
- [ ] Add complexity analysis documentation
- [ ] Create Jupyter notebook tutorials

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Educational resources and algorithm books that inspired this project
- The open-source community for providing excellent tools and libraries
- Contributors who help improve this educational resource

## 📞 Contact

**Author**: Animesh  
**Email**: [reachanimesh8349@gmail.com](mailto:reachanimesh8349@gmail.com)

---

*This project is created for educational purposes. The implementations prioritize clarity and understanding over performance optimization.*
