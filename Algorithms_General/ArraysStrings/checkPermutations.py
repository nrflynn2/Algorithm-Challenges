# O(N)
import unittest
from collections import Counter

def permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    cnt = Counter()
    for char in str1:
        cnt[char] += 1
    for char in str2:
        if cnt[char] == 0:
            return False
        cnt[char] -= 1
    return True

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'dcba'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_permutation(self):
        # true check
        for test_strings in self.dataT:
            actual = permutation(*test_strings)
            self.assertTrue(actual)
        # false check
        for test_strings in self.dataF:
            actual = permutation(*test_strings)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
