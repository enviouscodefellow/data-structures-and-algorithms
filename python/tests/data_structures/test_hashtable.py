import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected




def test_set_value_exists():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_get_value():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item)

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


def test_get_value_null():
    hashtable = Hashtable()
    actual = hashtable.get("banana")
    expected = None
    assert actual == expected

def test_keys_list():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Used for banana bread")
    actual = hashtable.keys()
    expected = ["apple", "banana"]
    assert set(actual) == set(expected)

def test_collision_handling():
    hashtable = Hashtable(2) # Small size to cause collisions
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Used for banana bread")
    actual = hashtable.get("banana")
    expected = "Used for banana bread"
    assert actual == expected

def test_retrieve_value_from_collision():
    hashtable = Hashtable(2) # Small size to cause collisions
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Used for banana bread")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_hash_key_in_range():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    actual = hashtable._buckets[hashtable.hash("ahmad") % 1024]
    assert actual is not None

