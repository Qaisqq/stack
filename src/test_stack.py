from stack_list import StackList

def test_stack_push():
    stack = StackList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.list == [3, 2, 1]

def test_stack_pop():
    stack = StackList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == None

def test_stack_is_empty():
    stack = StackList() 
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False

def test_size():
    stack = StackList()
    assert stack.size() == 0
    stack.push(5)
    assert stack.size() == 1
    stack.push(10)
    stack.push(15)
    assert stack.size() == 3
    stack.pop()
    assert stack.size() == 2

def test_peek():
    stack = StackList()
    assert stack.peek() is None
    stack.push(5)
    assert stack.peek() == 5
    stack.push(10)
    stack.push(15)
    assert stack.peek() == 15
    stack.pop()
    assert stack.peek() == 10

if __name__ == "__main__":
    test_stack_push()
    test_stack_is_empty()
    test_stack_pop()
    test_size()
    test_peek()