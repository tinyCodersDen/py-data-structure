# Py Data Structure
Py data stucture makes it easier to use data structures with python. While you can perform these operations in different ways, py data structure makes it much easier to use many data structures which we can use in C++ but not in Python. You can use Stacks, and Queues in this module, however we will be adding more data structures like heaps. Download py_data_structure.py into your directory. See documentation below for the functions and how it works. 

## Stacks:
`from py_data_structure import Stack`<br>

Create a stack:

`stack = Stack()`<br>

Push an element into a stack:

`
stack.push(element)
`

Pop/remove the top element from stack:

`
stack.pop()
`

Get the top element:

`
print(stack.top())
`

Get bottom element:

`
print(stack.bottom())
`

Get size of stack:

`
print(stack.size())
`

Check if stack is empty:

`
print(stack.isEmpty())
`

Get a list of stack values:

`
print(stack.get_stack())
`

## Queues:
`from py_data_structure import Queue`<br>

Create a queue:

`queue = Queue()`

Enqueue to a queue:

`queue.enqueue(element)`

Dequeue to a queue:

`queue.dequeue()`

Get the front element of a queue:

`print(queue.front())`

Get the back element of a queue:

`print(queue.back())`

Check if a queue is empty:

`print(queue.isEmpty())`

Get the size of a queue:

`print(queue.size())`

Get the whole queue in a list format:

`print(queue.get_queue())`
