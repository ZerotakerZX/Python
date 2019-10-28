import unittest
from nose.tools import assert_true, assert_false
from chess import rookmove, bishopmove, kingmove, queenmove, knightmove, move, wpawnmove, bpawnmove


class TestChess(unittest.TestCase):
    def testrookmove(self):
        a = 2
        b = 5
        c = 3
        d = 5
        result = rookmove(a, b, c, d)
        assert_true(result)

        c = 3
        d = 4
        result = rookmove(a, b, c, d)
        assert_false(result)

    def testbishipmove(self):
        a = 5
        b = 5
        c = 4
        d = 6
        result = bishopmove(a, b, c, d)
        assert_true(result)

        c = 5
        d = 4
        result = bishopmove(a, b, c, d)
        assert_false(result)

        c = 1
        d = 1
        result = bishopmove(a, b, c, d)
        assert_true(result)

        c = 2
        d = 8
        result = bishopmove(a, b, c, d)
        assert_true(result)

        c = 8
        d = 8
        result = bishopmove(a, b, c, d)
        assert_true(result)

        c = 8
        d = 2
        result = bishopmove(a, b, c, d)
        assert_true(result)

    def testkingmove(self):
        a = 4
        b = 4
        c = 5
        d = 5
        result = kingmove(a, b, c, d)
        assert_true(result)

        d = 1
        result = kingmove(a, b, c, d)
        assert_false(result)

        c = 6
        d = 6
        result = kingmove(a, b, c, d)
        assert_false(result)

        c = 3
        d = 5
        result = kingmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 5
        result = kingmove(a, b, c, d)
        assert_true(result)

        c = 5
        d = 5
        result = kingmove(a, b, c, d)
        assert_true(result)

        c = 3
        d = 4
        result = kingmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 4
        result = kingmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 5
        result = kingmove(a, b, c, d)
        assert_true(result)

        c = 3
        d = 3
        result = kingmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 3
        result = kingmove(a, b, c, d)
        assert_true(result)

        c = 5
        d = 3
        result = kingmove(a, b, c, d)
        assert_true(result)

    def testqueenmove(self):
        a = 4
        b = 4
        c = 4
        d = 5
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 1
        d = 7
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 1
        d = 1
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 1
        d = 4
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 8
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 8
        d = 8
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 8
        d = 4
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 5
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 1
        result = queenmove(a, b, c, d)
        assert_true(result)

        c = 7
        d = 1
        result = kingmove(a, b, c, d)
        assert_false(result)

    def testknightmove(self):
        a = 5
        b = 4
        c = 4
        d = 6
        result = knightmove(a, b, c, d)
        assert_true(result)

        c = 6
        d = 6
        result = knightmove(a, b, c, d)
        assert_true(result)

        c = 7
        d = 5
        result = knightmove(a, b, c, d)
        assert_true(result)

        c = 7
        d = 3
        result = knightmove(a, b, c, d)
        assert_true(result)

        c = 6
        d = 2
        result = knightmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 2
        result = knightmove(a, b, c, d)
        assert_true(result)

        c = 3
        d = 3
        result = knightmove(a, b, c, d)
        assert_true(result)

        c = 3
        d = 5
        result = knightmove(a, b, c, d)
        assert_true(result)

        c = 4
        d = 5
        result = knightmove(a, b, c, d)
        assert_false(result)

    def testmove(self):
        figure = 'knight'
        a = 5
        b = 4
        c = 4
        d = 6
        result = move(figure, a, b, c, d)
        assert_true(result)

        c = 4
        d = 5
        result = move(figure, a, b, c, d)
        assert_false(result)

        a = 8
        b = 8
        c = 10
        d = 9
        result = move(figure, a, b, c, d)
        assert_false(result)

    def testwpawnmove(self):
        a = 2
        b = 2
        c = 2
        d = 3
        result = wpawnmove(a, b, c, d)
        assert_true(result)

        c = 3
        d = 3
        result = wpawnmove(a, b, c, d)
        assert_true(result)

        c = 8
        d = 8
        result = wpawnmove(a, b, c, d)
        assert_false(result)

    def testbpawnmove(self):
        a = 2
        b = 7
        c = 2
        d = 6
        result = bpawnmove(a, b, c, d)
        assert_true(result)

        c = 3
        d = 6
        result = bpawnmove(a, b, c, d)
        assert_true(result)

        c = 8
        d = 8
        result = bpawnmove(a, b, c, d)
        assert_false(result)