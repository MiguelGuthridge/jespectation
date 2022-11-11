"""
Tests / List containing test

Tests for whether the ListContaining type
"""
import pytest
from jestspectation import (
    DictContainingItems,
    DictContainingKeys,
    DictContainingValues,
    ListContaining,
    SetContaining,
)


@pytest.mark.parametrize(
    ('item', 'matcher'),
    [
        ({1: 'a', 2: 'b', 3: 'c'}, DictContainingKeys({1, 2})),
        ({1: 'a', 2: 'b', 3: 'c'}, DictContainingValues(['a', 'b'])),
        ({1: 'a', 2: 'b', 3: 'c'}, DictContainingItems({1: 'a', 2: 'b'})),
        ([1, 2, 3], ListContaining([1, 2])),
        ({1, 2, 3}, SetContaining({1, 2})),
    ]
)
def test_matches(item, matcher):
    assert item == matcher


@pytest.mark.parametrize(
    ('item', 'matcher'),
    [
        ({1: 'a', 2: 'b', 3: 'c'}, DictContainingKeys({1, 2, 4})),
        ({1: 'a', 2: 'b', 3: 'c'}, DictContainingValues(['a', 'b', 'd'])),
        (
            {1: 'a', 2: 'b', 3: 'c'},
            DictContainingItems({1: 'a', 2: 'b', 3: 'd'}),
        ),
        ([1, 2, 3], ListContaining([1, 2, 4])),
        ({1, 2, 3}, SetContaining({1, 2, 4})),
    ]
)
def test_no_match(item, matcher):
    assert item != matcher


def test_diff_match_list_containing():
    list = ListContaining([1, 2, 3, 4, 5])
    assert list.get_diff([1, 2, 3]) == [
        "Missing properties",
        f"Expected a {list}, but was missing properties",
        f"- {4}",
        f"- {5}",
    ]


def test_diff_match_set_containing():
    set = SetContaining({1, 2, 3, 4, 5})
    assert set.get_diff({1, 2, 3}) == [
        "Missing properties",
        f"Expected a {set}, but was missing properties",
        f"- {4}",
        f"- {5}",
    ]


def test_diff_match_dict_containing_keys():
    dict = DictContainingKeys({1, 2, 3, 4, 5})
    assert dict.get_diff({1: '1', 2: '2', 3: '3'}) == [
        "Missing properties",
        f"Expected a {dict}, but was missing properties",
        f"- {4}",
        f"- {5}",
    ]


def test_diff_match_dict_containing_values():
    dict = DictContainingValues(['1', '2', '3', '4', '5'])
    assert dict.get_diff({1: '1', 2: '2', 3: '3'}) == [
        "Missing properties",
        f"Expected a {dict}, but was missing properties",
        f"- '{4}'",
        f"- '{5}'",
    ]


def test_diff_match_dict_containing_items():
    dict = DictContainingItems({1: '1', 2: '2', 3: '3', 4: '4', 5: '5'})
    assert dict.get_diff({1: '1', 2: '2', 3: '3'}) == [
        "Missing properties",
        f"Expected a {dict}, but was missing properties",
        f"- {(4, '4')}",
        f"- {(5, '5')}",
    ]
