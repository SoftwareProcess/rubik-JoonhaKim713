import unittest
import rubik.cube as cube

class Test(unittest.TestCase):

# Analysis:    Cube    class
#                methods:    instantiate
#                            load
#                            get
#
# Analysis:    Cube._init_
#    inputs:    no input parameter
#    outputs:    
#        side effects: none
#        nominal:    empty instance of cube
#        abnormal:    NA

    def test_init_010_ShouldCreateEmptyCube(self):
        myCube = cube.Cube()
        self.assertIsInstance(myCube, cube.Cube)
        