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

if __name__ == "__main__":
    test_stack_push()
    test_stack_is_empty()
    test_stack_pop()