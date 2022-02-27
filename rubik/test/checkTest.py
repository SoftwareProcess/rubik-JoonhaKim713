from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):

    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')

    def test_check_020_ShouldReturnErrorOnNone(self):
        parm = {'op':'check',
                'cube':None}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: cube is none')

    def test_check_030_ShouldReturnErrorOnEmpty(self):
        parm = {'op':'check',
                'cube': ''}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: there is empty cube input')

    def test_check_040_ShouldReturnErrorOnWrongType(self):
        parm = {'op':'check',
                'cube': 12345}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: Invalid cube input type')

    def test_check_050_ShouldReturnErrorOnTotalNumber(self):
        parm = {'op':'check',
                'cube': 'bbbbbbbbbbrrrrrrrrrrggggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: Invalid number of total cube elements')

    def test_check_060_ShouldReturnErrorOnNumberElement(self):
        parm = {'op':'check',
                'cube': 'bbbbbbbbbrrrrrvrrrgggzgggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: Cube does not have 6 colors.')

    def test_check_070_ShouldReturnErrorOnOccurrence(self):
        parm = {'op':'check',
                'cube': 'bbbbbbbbbbrrrrrrrrggggggggggooooooooyyyyyyyywwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: Some cube color may not have 9 occurrences')
        
    def test_check_080_ShouldReturnErrorOnMiddleFace(self):
        parm = {'op':'check',
                'cube':'bbbbbbbrbrrrrbrrrrggggoggggogoooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: Invalid cube middle face color')
        
    def test_check_090_ShouldReturnOkOnCube(self):
        parm = {'op':'check',
                'cube':'11w11w11wrrrrrrrrryggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        
    def test_check_010_ShouldReturnErrorOnShortCube(self):
        parm = {'op':'check',
                'cube':'123456789'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: Invalid number of total cube elements')    

    def test_check_011_ShouldReturnErrorOnNoneCube(self):
        parm = {'op':'check',
                }
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: cube is none') 
        
    def test_check_012_ShouldReturnErrorOnInvalidTypeOfCube(self):
        parm = {'op':'check',
                'cube' : 42}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: Invalid cube input type')   
        
    def test_check_013_IllegalCharacter(self):
        parm = {'op':'check',
                'cube' : 'bbbbbbbbbr##rrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: Illegal characeter') 

