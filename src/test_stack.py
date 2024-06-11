from stack_list import StackList

def test_stack_push():
    stack = StackList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.list == [3, 2, 1]


if __name__ == "__main__":
    test_stack_push()