import fastenum
import unittest

from circular_doubly_linked_list import CircularDoublyLinkedList


class Error(fastenum.Enum):
    """An enum class for commonly recurring error messages."""
    SENTINEL = 'Sentinel nodes not set up properly.'
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


if __name__ == '__main__':
    unittest.main()
