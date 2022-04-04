'''
Created on Feb 21, 2022

@author: joonh
'''
import unittest
import rubik.solve as solve


class solveTest(unittest.TestCase):

# Analysis : solve
#
#    inputs:
#        parmss:        dictionary; mandatory; arrives validated
#        parmss['op']    string, "solve"; mandatory; arrives validated
#        parmss['cube']    string; len=54, [azAZ09], ..; mandatory, arrives unvalidated
#        parmss['rotate']    string; len>=0, [FfRrBbLlUuDd]; optional, default to F is missing; arrives unvalidated

#    outputs:
#        side-effects:    no state change; no external effects
#        returns: dictionary
#            nominal:
#                dictionary['cube']: string, len-54
#                dictionary['status']: 'ok'
#            abnormal:
#                dictionary['status']: 'error: xxx' where xxx is a dev-selected message
#        confidence level: boundary value analysis 

#        happy path:
#            test 010: nominal valid cube with F rotation
#            test 020: nominal valid cube with F rotation
#            test 030: nominal valid cube with missing rotation
#            test 030: nominal valid cube with "" rotation 
#            test 040 ...
#        sad path:
#            test 910: missing cube
#            test 920: valid cube, invalid rotation
#            test 930 ...

        # @unittest.skip('skipping this test until cube model is complete')
        def test_solve_010_ShouldRotateValidNominalCubeF(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'F'
            inputDict['op'] = 'solve'
            actualResult = solve._solve(inputDict)

            expectedResult = {}
            expectedResult['cube'] = 'wwwwwwwwwobbobbobbrrrrrrrrrggyggyggyoooooogggbbbyyyyyy'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_solve_020_ShouldRotateValidNominalCubef(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'f'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'wwwwwwwwwybbybbybbrrrrrrrrrggoggoggooooooobbbgggyyyyyy'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        
        def test_solve_040_ShouldRotateValidNominalCubeR(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'R'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'wwywwywwybbbbbbbbborrorrorrgggggggggoowoowoowyyryyryyr'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_050_ShouldRotateValidNominalCuber(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'r'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'wwowwowwobbbbbbbbbyrryrryrrgggggggggooroorooryywyywyyw'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_solve_060_ShouldRotateValidNominalCubeU(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'U'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'bbbwwwwwwrrrbbbbbbgggrrrrrrwwwggggggoooooooooyyyyyyyyy'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_070_ShouldRotateValidNominalCubeu(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'u'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'gggwwwwwwwwwbbbbbbbbbrrrrrrrrrggggggoooooooooyyyyyyyyy'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_080_ShouldRotateValidNominalCubeB(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'B'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'wwwwwwwwwbbybbybbyrrrrrrrrroggoggoggbbbooooooyyyyyyggg'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_090_ShouldRotateValidNominalCubeb(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'b'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'wwwwwwwwwbbobbobborrrrrrrrryggyggygggggooooooyyyyyybbb'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_100_ShouldRotateValidNominalCubeL(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'L'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'owwowwowwbbbbbbbbbrryrryrrygggggggggroorooroowyywyywyy'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_110_ShouldRotateValidNominalCubel(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'l'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'ywwywwywwbbbbbbbbbrrorrorrogggggggggwoowoowooryyryyryy'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_120_ShouldRotateValidNominalCubeD(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'D'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'wwwwwwgggbbbbbbwwwrrrrrrbbbggggggrrroooooooooyyyyyyyyy'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_130_ShouldRotateValidNominalCubed(self):
            inputDict = {}
            inputDict['cube'] = 'wwwwwwwwwbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyy'
            inputDict['rotate'] = 'd'
            inputDict['op'] = 'solve'
            
            actualResult = solve._solve(inputDict)
            expectedResult = {}
            expectedResult['cube'] = 'wwwwwwbbbbbbbbbrrrrrrrrrgggggggggwwwoooooooooyyyyyyyyy'
            expectedResult['status'] = 'ok'

            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            

        def test_solve_020_ShouldReturnErrorOnNone(self):
            parm = {'op':'solve',
                    'cube':None}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: cube is none')

        def test_solve_030_ShouldReturnErrorOnEmpty(self):
            parm = {'op':'solve',
                    'cube': ''}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: there is empty cube input')

        def test_solve_040_ShouldReturnErrorOnWrongType(self):
            parm = {'op':'solve',
                    'cube': 12345}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: Invalid cube input type')

        def test_solve_050_ShouldReturnErrorOnTotalNumber(self):
            parm = {'op':'solve',
                    'cube': 'bbbbbbbbbbrrrrrrrrrrggggggggggoooooooooyyyyyyyyywwwwwwwww'}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: Invalid number of total cube elements')

        def test_solve_060_ShouldReturnErrorOnNumberElement(self):
            parm = {'op':'solve',
                    'cube': 'bbbbbbbbbrrrrrvrrrgggzgggggoooooooooyyyyyyyyywwwwwwwww'}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: Cube does not have 6 colors.')

        def test_solve_070_ShouldReturnErrorOnOccurrence(self):
            parm = {'op':'solve',
                    'cube': 'bbbbbbbbbbrrrrrrrrggggggggggooooooooyyyyyyyywwwwwwwwww'}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: Some cube color may not have 9 occurrences')
        
        def test_solve_080_ShouldReturnErrorOnMiddleFace(self):
            parm = {'op':'solve',
                    'cube':'bbbbbbbrbrrrrbrrrrggggoggggogoooooooyyyyyyyyywwwwwwwww'}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: Invalid cube middle face color')
        
        
        def test_solve_010_ShouldReturnErrorOnShortCube(self):
            parm = {'op':'solve',
                    'cube':'123456789'}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: Invalid number of total cube elements')    

        def test_solve_011_ShouldReturnErrorOnNoneCube(self):
            parm = {'op':'solve',
                    }
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: cube is none') 
        
        def test_solve_012_ShouldReturnErrorOnInvalidTypeOfCube(self):
            parm = {'op':'solve',
                    'cube' : 42}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: Invalid cube input type')   
        
        def test_solve_013_IllegalCharacter(self):
            parm = {'op':'solve',
                    'cube' : 'bbbbbbbbbr##rrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
            result = solve._solve(parm)
            self.assertIn('status', result)
            status = result.get('status')
            self.assertEqual(status, 'error: Illegal characeter') 
            
         

        def test_solve_100_cubeRotate(self):
            inputDict = {
                'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
                }
            expectedResult = {'status': 'ok', 
                              'solution': ''}
            actualResult = solve._solve(inputDict)
            self.assertDictEqual(expectedResult, actualResult)
        
        def test_solve_110_cubeRotate(self):
            inputDict = {
                'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy',
                'rotate': ''
                }
            expectedResult = {'status': 'ok', 
                              'solution': ''}
            actualResult = solve._solve(inputDict)
            self.assertDictEqual(expectedResult, actualResult)
        
        def test_solve_120_cubeRotate(self):
            inputDict = {
                'op': 'solve',
                'cube': 'ybwgbyyrgrwyowwoorboorgygwwybbryyoyrggrwrgorbggwbobbow',
                'rotate': ''
                }
            expectedResult = {'status': 'ok', 
                              'solution': 'RRBBDRRRBBBBLBBBURRBBDRRRBLBBBDDDLLULLBBBFLLLUDDLLUrrFFLLbbUURUrruRUluLRUrRUrULUlfuF'}
            actualResult = solve._solve(inputDict)
            self.assertDictEqual(expectedResult, actualResult)
        

        def test_solve_140_cubeRotate(self):
            inputDict = {
                'op': 'solve',
                'cube': 'ybbbbwggboywrrbygwrgoygyroggobrorryowwbwygowwyrrowoybg',
                'rotate': ''
                }
            
            expectedResult = {'status': 'ok', 
                              'solution': 'UUUFFLLLUDLLUDDLLUUBDRRRBLBBBLLLUFFLLLUrrUUbbUFFLLUURUrURUrRUrFUfUfuF'}
            actualResult = solve._solve(inputDict)
            self.assertDictEqual(expectedResult, actualResult)
                
                