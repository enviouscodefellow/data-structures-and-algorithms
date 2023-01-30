import pytest
from data_structures.linked_list import LinkedList, Node


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")

@pytest.mark.skip("TODO")
def test_findMiddle_odd_nodes():
    # Test case 1: Odd number of nodes
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    assert ll.findMiddle() == 3

@pytest.mark.skip("TODO")
def test_findMiddle_even_nodes():
    # Test case 2: Even number of nodes
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    assert ll.findMiddle() == 2

@pytest.mark.skip("TODO")
def test_findMiddle_one_node():
    # Test case 3: List with only one node
    ll = LinkedList()
    ll.insert(1)
    assert ll.findMiddle() == 1

@pytest.mark.skip("TODO")
def test_findMiddle_no_node():
    # Test case 4: List with no nodes
    ll = LinkedList()
    ll.insert(None)
    assert ll.findMiddle() == None

