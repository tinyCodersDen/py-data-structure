# Py Data Structure
Py data stucture makes it easier to use data structures with python. While you can perform these operations in different ways, py data structure makes it much easier to use many data structures which we can use in C++ but not in Python. You can use Stacks, and Queues in this module, however we will be adding more data structures like heaps. <br>

Pypi Page: https://pypi.org/project/py-data-structure/

Github Page: https://github.com/tinyCodersDen/py-data-structure

See documentation below for the functions and how it works. 


## Installation:
```
pip install py-data-structure
```

## Stacks:
```python
from py_data_structure import Stack
```

Create a stack:

```python
stack = Stack()
```

Push an element into a stack:

```python
stack.push(element)
```

Pop/remove the top element from stack:

```python
stack.pop()
```

Get the top element:

```python
print(stack.top())
```

Get bottom element:

```python
print(stack.bottom())
```

Get size of stack:

```python
print(stack.size())
```

Check if stack is empty:

```python
print(stack.isEmpty())
```

Get a list of stack values:

```python
print(stack.get_stack())
```

## Queues:
```python
from py_data_structure import Queue
```

Create a queue:

```python
queue = Queue()
```

Enqueue to a queue:

```python
queue.enqueue(element)
```

Dequeue to a queue:

```python
queue.dequeue()
```

Get the front element of a queue:

```python
print(queue.front())
```

Get the back element of a queue:

```python
print(queue.back())
```

Check if a queue is empty:

```python
print(queue.isEmpty())
```

Get the size of a queue:

```python
print(queue.size())
```

Get the whole queue in a list format:

```python
print(queue.get_queue())
```
## Reporting a Vulnerability

Do you have any suggestions, questions, comments, or concerns? Reach out to the developer at vihan.raval1@gmail.com or at GitHub to report an issue!
