import unittest
from wc import wc


class TestCase(unittest.TestCase):

    def test_Flagl(self):
        parser = wc.create_parser()
        args = parser.parse_args(['-l'])
        self.assertTrue(args.l)

    def test_Flagw(self):
        parser = wc.create_parser()
        args = parser.parse_args(['-w'])
        self.assertTrue(args.w)

    def test_Flagc(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-'])
        t = wc.arguments_split(None, args, unknown)
        self.assertTrue(args.c)

    def test_Flagdash(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-'])
        t = wc.arguments_split(None, args, unknown)
        for i in t:
            self.assertEqual(i,"wc: - open: No such file or directory")

    def test_NoFileFound(self):
        parser = wc.create_parser()
        args,unknown = parser.parse_known_args(['testinputs/testcase0.txt'])
        t = wc.arguments_split(None, args,unknown)
        for a in t:
            self.assertEqual(a, "wc: testinputs/testcase0.txt open: No such file or directory")

    def test_EmptyFile(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['testinputs/testcase1.txt'])
        t = wc.arguments_split(None, args,unknown)
        for a in t:
            self.assertEqual(a, "\t0\t0\t0 testinputs/testcase1.txt")

    def test_WithoutFlagOnlyFile(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['testinputs/testcase2.txt'])
        t = wc.arguments_split(None, args, unknown)
        for a in t:
            self.assertEqual(a, "\t9\t10\t20 testinputs/testcase2.txt")

    def test_WithFlagwOnly(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-w', 'testinputs/testcase3.py'])
        t = wc.arguments_split(None, args, unknown)
        for a in t:
            self.assertEqual(a, "\t31 testinputs/testcase3.py")

    def test_WithFlaglOnly(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-l', 'testinputs/testcase3.py'])
        t = wc.arguments_split(None, args, unknown)
        for a in t:
            self.assertEqual(a, "\t8 testinputs/testcase3.py")

    def test_WithFlagcOnly(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-c', 'testinputs/testcase3.py'])
        t = wc.arguments_split(None, args, unknown)
        for a in t:
            self.assertEqual(a, "\t177 testinputs/testcase3.py")

    def test_WithFlagwOnly(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-w', 'testinputs/testcase3.py'])
        t = wc.arguments_split(None, args, unknown)
        for a in t:
            self.assertEqual(a, "\t31 testinputs/testcase3.py")

    def test_WithAllFlagsOnly(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-wlc', 'testinputs/testcase4.txt'])
        t = wc.arguments_split(None, args, unknown)
        for a in t:
            self.assertEqual(a, "\t6\t133\t795 testinputs/testcase4.txt")

    def test_HelloWorldwithFlagw(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-w', 'testinputs/testcase5.txt'])
        t = wc.arguments_split(None, args, unknown)
        for a in t:
            self.assertEqual(a, "\t2 testinputs/testcase5.txt")

    def test_MultpleFileswithFlagw(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['-w', 'testinputs/testcase5.txt', 'testinputs/testcase6.txt'])
        t = wc.arguments_split(None, args, unknown)
        self.assertSequenceEqual(t,['\t2 testinputs/testcase5.txt','\t1 testinputs/testcase6.txt','\t3 total'])


    def test_MultpleFileswithAllflags(self):
        parser = wc.create_parser()
        args, unknown = parser.parse_known_args(['testinputs/testcase5.txt', 'testinputs/testcase6.txt'])
        t = wc.arguments_split(None, args, unknown)
        self.assertSequenceEqual(t,['\t1\t2\t14 testinputs/testcase5.txt','\t0\t1\t4 testinputs/testcase6.txt','\t1\t3\t18 total'])

if __name__ == '__main__':
    unittest.main()