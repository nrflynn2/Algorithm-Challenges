# O(N)
import unittest
from collections import Counter

def pal_perm(string):
    c = Counter()
    string = (string.lower()).split()
    num_odd = 0

    for word in string:
        for char in word:
            c[char] += 1
    
    for char in list(c):
        if c[char] % 2 != 0 and num_odd == 0:
            num_odd = 1
            continue
        if c[char] % 2 != 0 and num_odd == 1:
            return False
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
