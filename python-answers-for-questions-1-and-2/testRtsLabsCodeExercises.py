
import unittest
from io import StringIO
from unittest.mock import patch
import rtsLabsCodeExercises

class TestRtsLabsCodeExercises(unittest.TestCase):

    def testElementsAboveAndBelowN(self):
        
        arr = [9,34,-100,56,-8,0,49,116,-102,16,24,0,-2,6]

        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.elementsAboveAndBelowN(arr, 17)
            self.assertEqual(string.getvalue(), "above: 5, below: 9\n")

        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.elementsAboveAndBelowN(arr, 0)
            self.assertEqual(string.getvalue(), "above: 8, below: 4\n")

        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.elementsAboveAndBelowN(arr, 1000)
            self.assertEqual(string.getvalue(), "above: 0, below: 14\n")

        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.elementsAboveAndBelowN(arr, -1000)
            self.assertEqual(string.getvalue(), "above: 14, below: 0\n")

    def testRotateByN(self):

        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.rotateByN('Pittsburgh Steelers', 4)
            self.assertEqual(string.getvalue(), "lersPittsburgh Stee\n")

        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.rotateByN('Pittsburgh Steelers', -4)
            self.assertEqual(string.getvalue(), "sburgh SteelersPitt\n")

        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.rotateByN('Pittsburgh Steelers', 19)
            self.assertEqual(string.getvalue(), "Pittsburgh Steelers\n")

        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.rotateByN('Pittsburgh Steelers', 42)
            self.assertEqual(string.getvalue(), "lersPittsburgh Stee\n")
        
        with patch('sys.stdout', new = StringIO()) as string:
            rtsLabsCodeExercises.rotateByN('Pittsburgh Steelers', -48)
            self.assertEqual(string.getvalue(), " SteelersPittsburgh\n")       

        


if __name__ == '__main__':
    unittest.main()