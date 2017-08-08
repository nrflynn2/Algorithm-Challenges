from LinkedList import *
from nose.tools import assert_equal

class TestLinkedList(object):
    def test_add_to_front(self):
        print('Test: add_to_front to an empty list')
        linked_list = LinkedList(None)
        linked_list.add_to_front(10)
        assert_equal(linked_list.toArray(), [10])

        print('Test: add_to_front a node with value None')
        linked_list.add_to_front(None)
        assert_equal(linked_list.toArray(), [10])

        print('Test: add_to_front general case')
        linked_list.add_to_front('a')
        linked_list.add_to_front('bc')
        assert_equal(linked_list.toArray(), ['bc', 'a', 10])

        print('Success: test_add_to_front\n')

    def test_add(self):
        print('Test: add on an empty list')
        linked_list = LinkedList(None)
        linked_list.add(10)
        assert_equal(linked_list.toArray(), [10])

        print('Test: add a None')
        linked_list.add(None)
        assert_equal(linked_list.toArray(), [10])

        print('Test: add general case')
        linked_list.add('a')
        linked_list.add('bc')
        assert_equal(linked_list.toArray(), [10, 'a', 'bc'])

        print('Success: test_add\n')

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        assert_equal(node, False)

        print('Test: find general case with matches')
        linked_list = LinkedList([10])
        linked_list.add_to_front('a')
        linked_list.add_to_front('bc')
        node = linked_list.find('a')
        assert_equal(node, True)

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        assert_equal(node, False)

        print('Success: test_find\n')

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = LinkedList(None)
        linked_list.delete('a')
        assert_equal(linked_list.toArray(), [])

        print('Test: delete a None')
        linked_list = LinkedList([10])
        linked_list.delete(None)
        assert_equal(linked_list.toArray(), [10])

        print('Test: delete general case with matches')
        linked_list = LinkedList([10])
        linked_list.add_to_front('a')
        linked_list.add_to_front('bc')
        linked_list.delete('a')
        assert_equal(linked_list.toArray(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        assert_equal(linked_list.toArray(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = LinkedList(None)
        assert_equal(len(linked_list), 0)

        print('Test: len general case')
        linked_list = LinkedList([10])
        linked_list.add_to_front('a')
        linked_list.add_to_front('bc')
        assert_equal(len(linked_list), 3)

        print('Success: test_len\n')


def main():
    test = TestLinkedList()
    test.test_add_to_front()
    test.test_add()
    test.test_find()
    test.test_delete()
    test.test_len()


if __name__ == '__main__':
    main()
