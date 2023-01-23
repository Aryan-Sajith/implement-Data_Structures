from singly_linked_list import SinglyLinkedList


def main():
    """The main method of the Singly Linked List."""
    singly_linked_list = SinglyLinkedList()

    # insertion
    singly_linked_list.append(5)
    singly_linked_list.append(10)
    singly_linked_list.prepend(3)
    singly_linked_list.prepend(0)
    singly_linked_list.traverse()


if __name__ == '__main__':
    main()
