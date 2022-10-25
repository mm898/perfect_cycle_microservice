import unittest

from isCycle import isListCycle

class TestCycle(unittest.TestCase):
    def test_cycle_list(self):
        """
        Test that list is a cycle
        """
        list_ = [3,0,1,2]
        self.assertTrue(isListCycle(list_))
    
    def test_empty_list_not_cycle(self):
        """
        Test that list is empty and not a cycle
        """
        list_ = []
        self.assertFalse(isListCycle(list_))

    def test_list_has_one_item_cycle(self):
        """
        Test that list has one item and it is a cycle
        """
        list_ = [0]
        self.assertTrue(isListCycle(list_))

    def test_list_has_one_item_not_cycle(self):
        """
        Test that list has one item and it is not cycle
        """
        list_ = [1]
        self.assertFalse(isListCycle(list_))

    def test_list_does_not_have_zero(self):
        """
        Test that list does not have a zero
        """
        list_ = [1,3,2]
        self.assertFalse(isListCycle(list_))

    def test_list_has_duplicates(self):
        """
        Test that list has duplicates
        """
        list_ = [0,3,4,3,4]
        self.assertFalse(isListCycle(list_))

    def test_list_invalid(self):
        """
        Test that list has duplicates
        """
        list_ = [0,'hello',3,4]
        self.assertFalse(isListCycle(list_))


if __name__ == '__main__':
    unittest.main()
