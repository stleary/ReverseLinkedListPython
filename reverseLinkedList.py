# Reverse a simple linked list

'''
Add functionality to the reverse() function that takes a singly linked list as a parameter,
and returns the reversed linked list.
Linked list nodes have a string value property and a reference to the next node property.
The reference will be None at the end of the list
For example, given this linked list:
    A -> B -> C -> D -> None
Return this linked list:
    D -> C -> B -> A -> None

'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        res = ""
        ptr = self
        while ptr:
            res += str(ptr.value) + ", "
            ptr = ptr.next
        res = res.strip(", ")
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"

def reverse(node: Node) -> Node:
    # TODO fill in this functionality
    return node

def reverseRecursive(node: Node) -> Node:

    # termination step
    if node is None:
        return None
    if node.next is None:
        return node

    # recursion step
    retNode = reverseRecursive(node.next)

    # action step
    node.next.next = node
    node.next = None
    return retNode

def reverseNonRecursive(node: Node) -> Node:
    # non-recursive
    if node is None:
        return node
    if node.next is None:
        return node
    head = None
    while (node):
        savenext = node.next
        node.next = head
        head = node
        node = savenext
    return head


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g = Node('G', None)
    f = Node('F', g)
    e = Node('E', f)
    d = Node('D', e)
    c = Node('C', d)
    b = Node('B', c)
    a = Node('A', b)
    print(a)
    r = reverseRecursive(a)
    print(r)
    g = Node('G', None)
    f = Node('F', g)
    e = Node('E', f)
    d = Node('D', e)
    c = Node('C', d)
    b = Node('B', c)
    a = Node('A', b)
    r = reverseNonRecursive(a)
    print(r)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
