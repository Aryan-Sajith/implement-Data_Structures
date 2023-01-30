import fastenum
import unittest

from circular_doubly_linked_list import CircularDoublyLinkedList


class Error(fastenum.Enum):
    """An enum class for commonly recurring error messages."""
    SENTINEL = 'Sentinel nodes not set up properly.'
    HEAD = 'Head reference not updated.'
    TAIL = 'Tail reference not updated.'
    LENGTH = 'Length not updated.'


class TestCircularDoublyLinkedList(unittest.TestCase):
    """Tests the Circular Doubly Linked List Class(CDLL)."""

    def setUp(self):
        """Initializes an empty CDLL instance."""
        self.cdll = CircularDoublyLinkedList()

    def tearDown(self):
        """Deletes CDLL instance."""
        del self.cdll

    def test_empty_CDLL(self):
        """Tests whether a newly initialized CDLL works properly."""
        self.assertEqual(self.cdll.head.next, self.cdll.tail, Error.SENTINEL)
        self.assertEqual(self.cdll.head.prev, self.cdll.tail, Error.SENTINEL)
        self.assertEqual(self.cdll.tail.next, self.cdll.head, Error.SENTINEL)
        self.assertEqual(self.cdll.tail.prev, self.cdll.head, Error.SENTINEL)
        self.assertIsNone(self.cdll.head.value, Error.SENTINEL)
        self.assertIsNone(self.cdll.tail.value, Error.SENTINEL)
        self.assertEqual(self.cdll.length, 0, Error.LENGTH)

    def test_prepend_empty_CDLL(self):
        """Tests whether prepending to an empty CDLL works properly."""
        self.cdll.prepend(0)
        self.assertEqual(self.cdll.head.next.value, 0, Error.HEAD)
        self.assertEqual(self.cdll.tail.prev.value, 0, Error.TAIL)
        self.assertEqual(self.cdll.length, 1, Error.LENGTH)

    def test_prepend_non_empty_CDLL(self):
        """Tests whether prepending to a non-empty CDLL works properly."""
        self.cdll.prepend(1)
        self.cdll.prepend(0)
        self.assertEqual(self.cdll.head.next.value, 0, Error.HEAD)
        self.assertEqual(self.cdll.tail.prev.value, 1, Error.TAIL)
        self.assertEqual(self.cdll.length, 2, Error.LENGTH)


if __name__ == '__main__':
    unittest.main()
