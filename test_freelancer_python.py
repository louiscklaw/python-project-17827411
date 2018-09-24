#!/usr/bin/env python
"""

Helloworld boilder plate

Naming style guideline
    https://google.github.io/styleguide/pyguide.html

unittest documentation
    https://docs.python.org/3/library/unittest.html

"""

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

import freelancer_python

class testing(unittest.TestCase):
    def test_display_name(self):
        # try call
        test_free = freelancer_python
        test_free.print_on_screen=MagicMock()

        test_set = {
            "":"no name to display",
            "llaw": "username: llaw",
            "llaw 1":"username: llaw 1"
        }

        for question, answer in test_set.items():
            test_free.display_name(question)
            test_free.print_on_screen.assert_called_with(answer)


    @patch('builtins.input', return_value='testing_username')
    def test_ask_name(self, test_input):
        test_free = freelancer_python
        test_result = test_free.ask_name()
        self.assertEqual('testing_username', test_result, 'username not match')


    def test_smallest(self):
        test_free = freelancer_python
        test_set = [
            [1,[1,2,3,4,5]],
            [2802, [23237,21429,39465,39661,18723,78536,49925,64728,97262,34117,8449,30710,80333,84074,94609,50954,7490,13373,73456,33392,60457,21357,82278,61642,8112,74510,29360,43985,40666,67703,71083,4085,99029,71412,38153,94303,44424,38794,25836,81019,64686,67894,32638,35371,45262,64842,97266,42993,59741,59123,54077,8246,18879,15056,9498,44645,68550,2900,73351,41080,81680,21905,48311,37018,45546,66286,62418,19406,94808,66839,97014,48457,52394,17484,17929,69312,70199,9920,72157,58615,48787,85136,2802,90783,18170,36045,74034,20276,13491,54706,43242,11555,13166,52117,84213,80021,86895,52079,20345]],
            [2.1,[2.5,3.0,4.8,2.1,5.2]],
            [
                test_free.ERR_CONST,[1,'a',2,'b',3,'c']
            ]
        ]

        for ans, question in test_set:
            self.assertEqual(ans, test_free.smallest(question))

        for ans, question in test_set:
            self.assertEqual(ans, test_free.smallest_detailed(question))

    @patch('builtins.input', return_value=1)
    @patch('builtins.print')
    def test_ask5num(self,patched_print, patched_input ):
        test_free = freelancer_python
        test_free.ask5num()

    @patch('builtins.print')
    def test_question_5_display(self, patched_print):
        test_free = freelancer_python

        test_free.display_a()
        patched_print.assert_called_with('display a:1010')

        test_free.display_b()
        patched_print.assert_called_with(
            'display b:2000'
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)
