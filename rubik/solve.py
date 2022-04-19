import rubik.cube as rubik
import re
from flask.cli import cli

def _solve(parms):
    
    # P1) get parms ['cube'] and ['rotate'] and encodedCube and rotations will have these values
    # This portion will check if encodedCube is validated or not. If it is not, will return error on ['status']
    # After checking all error, encodedCube and rotations will convert into lists to use on each cube and rotations values
    # lists <- encodedCube    rLists <- rotations
    encodedCube = parms.get('cube', None)
    rotations = parms.get('rotate', None)

    rLists = []
   
    count={}
    result={}
    
    pattern = re.compile("[A-Za-z0-9]+")   
    if (encodedCube == None):
        result['status'] = 'error: cube is none'
        return result
    
    elif (encodedCube == ''):
        result['status'] = 'error: there is empty cube input'
        return result
    
    elif ((str(type(encodedCube)) != "<class 'str'>")):
        result['status'] = 'error: Invalid cube input type'
        return result
    
    elif (pattern.fullmatch(encodedCube) is None):
        result['status'] = 'error: Illegal characeter'
        return result
    
    else:
        lists = list(encodedCube) 

    numCnt = False
    
    for i in lists:
        
        try: count[i] += 1
        except: count[i]=1
              
    for j in count.values():
        if (9 != j):
            numCnt = True
            break
    
    k = 4
    l = k + 9
    faceCheck = False
    
    while k <= len(lists):
        while l < len(lists):
            if lists[k] == lists[l]:
                faceCheck = True
            l += 9
        l = k + 18
        k += 9    
  
    if(len(lists) != 54):
        result['status'] = 'error: Invalid number of total cube elements' 
        return result
    elif(len(count) != 6):
        result['status'] = 'error: Cube does not have 6 colors.'
        return result
    elif(numCnt):
        result['status'] = 'error: Some cube color may not have 9 occurrences'  
        return result
    elif(faceCheck):
        result['status'] = 'error: Invalid cube middle face color'    
        return result
    # End P1
    
    cLists = list(encodedCube)

    # P2) Entering solve mode for no rotation or empty
    solRot = [];
    if rotations is None or not rotations:   
        
        solveFlag = True;
        solveFlag2 = True;
        btmCross = True
        solution = ''
        btmLayer = True        
        while(solveFlag):
            #Return solution
            if (cLists[45] == cLists[46] and cLists[47] == cLists[48] and cLists[49] == cLists[50] and cLists[51] == cLists[52] and cLists[53] == cLists[45]):
                
                result['status'] = 'ok'
            
                for i in solRot:
                    solution += i
            
                result['solution'] = solution
                return result
            else:
                
                # P2-1) Bottom cross solve
                #top daisey
                while(solveFlag2):
                    
                    if (cLists[49] == cLists[37] and cLists[49] == cLists[39] and cLists[49] == cLists[41] and cLists[49] == cLists[43] and cLists[37] == cLists[39] and cLists[37] == cLists[41] and cLists[41] == cLists[43]):
                        solveFlag2 = False
                        Flag1 = True
                        Flag2 = True
                        Flag3 = True
                        Flag4 = True  

                    else:
                        if(cLists[37] == cLists[49]):
                            solRot += 'U'
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                            cLists = lists                        
                            
                        else:
                            if(cLists[10] == cLists[49]):
                                solRot += 'RB'  
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists       
                                                             
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists   
                                                             
                                                          
                            if(cLists[12] == cLists[49]):
                                solRot += 'RRB'     
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists
                                
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists   
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists   
                                                                                                                            
                            if(cLists[14] == cLists[49]):
                                solRot += 'B'   
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists                                  
                                                                
                            if(cLists[16] == cLists[49]):
                                solRot += 'RRRB'
                                
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists                                
                                    
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists
                                
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists   
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists   
                                
                                
                                                                
                            if(cLists[19] == cLists[49]):
                                solRot += 'BBDRRRB'    
                                       
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists     
                                                            
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists   
                                                              
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists
                                 
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists                                
                                    
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists
                                
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists   
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists                                                                  
                                       
                                                         
                            if(cLists[21] == cLists[49]):
                                solRot += 'BBBDRRRB'                                    
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists     
                            
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists     
                                                            
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists   
                                                              
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists
                                 
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists                                
                                    
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists
                                
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists   
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists                                 
                             
                            if(cLists[23] == cLists[49]):
                                solRot += 'BDRRRB' 
                                                                   
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists   
                                                              
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists
                                 
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists                                
                                    
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists
                                
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists   
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists  
                            
                            if(cLists[25] == cLists[49]):
                                solRot += 'DRRRB'
                                  
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists
                                 
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists                                
                                    
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists
                                
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists   
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists   
                                
                                                                                             
                            if(cLists[28] == cLists[49]):
                                solRot += 'LLLBBB'                                     
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists     
                                       
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists 
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists  
                                                               
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists                                
                                
                            if(cLists[30] == cLists[49]):
                                solRot += 'BBB' 
                                                                  
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists 
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists  
                                                               
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists    

                            if(cLists[32] == cLists[49]):
                                solRot += 'LLBBB'                                     
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists     
                                       
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists 
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists  
                                                               
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists    
                            
                            if(cLists[34] == cLists[49]):
                                solRot += 'LBBB'  
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists     
                                       
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists 
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists  
                                                               
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists    
                                                                                                 
                            if(cLists[1] == cLists[49]):
                                solRot += 'FFFLLLU'       
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                                cLists = lists                                
                                                
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                                cLists = lists  
                                                              
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                                cLists = lists           
                                                     
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists    
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                                  
                                                                                    
                            if(cLists[3] == cLists[49]):
                                solRot += 'LLLU'    
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists    
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                                  
                                
                                
                                                                 
                            if(cLists[5] == cLists[49]):
                                solRot += 'FFLLLU'     
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                                cLists = lists  
                                                              
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                                cLists = lists           
                                                     
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists    
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                                 
                                                            
                            if(cLists[7] == cLists[49]):
                                solRot += 'FLLLU'                                   
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                                cLists = lists           
                                                     
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists    
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists   
                                                               
                            if(cLists[46] == cLists[49]):
                                solRot += 'DLLU'   
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists    
                                                            
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                                 
                                
                                
                                                             
                            if(cLists[48] == cLists[49]):
                                solRot += 'LLU'   
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                                 
                                
                                
                                                                  
                            if(cLists[50] == cLists[49]):
                                solRot += 'DDLLU'        
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists    
                                
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists       
                                                                                      
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                                 
                                
                                
                                
                                                           
                            if(cLists[52] == cLists[49]):
                                solRot += 'DDDLLU' 
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists  
                                
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists    
                                
                                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                                cLists = lists       
                                                                                      
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                  
                
                
                
                while(btmCross): 
                    # make bottom cross
                    if(cLists[10] == cLists[13] and Flag1 == True):
                        solRot += 'rr'
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                        cLists = lists
                    
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                        cLists = lists  
                        
                        Flag1 = False              
                                    
                    elif(cLists[1] == cLists[4] and Flag2 == True):
                        solRot += 'FF'                
                        lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                        cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                        cLists = lists
                    
                        lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                        cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                        cLists = lists 
                        Flag2 = False               
                                                 
                    elif(cLists[28] == cLists[31] and Flag3 == True):
                        solRot += 'LL'     
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                        cLists = lists
                        
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                        cLists = lists                
                        Flag3 = False
                                                   
                    elif(cLists[19] == cLists[22] and Flag4 == True):           
                        solRot += 'bb' 
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists                                
                        Flag4 = False
                    else:
                        solRot += 'U'  
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists     
                        
                    if (Flag1 == False and Flag2 == False and Flag3 == False and Flag4 == False):
                        btmCross = False    
                        
                                                    
                
                               
                # P2-2) Make bottom layer
                
                count = 0
                
                while(btmLayer):    
                      
                    count = 0
                    
                    if (cLists[0] == cLists[49] or cLists[2] == cLists[49] or cLists[9] == cLists[49] or cLists[11] == cLists[49] or cLists[18] == cLists[49] or cLists[20] == cLists[49] or cLists[27] == cLists[49] or cLists[29] == cLists[49]):                            
                    
                        
                        if (cLists[2] == cLists[4]):
                            
                            if(cLists[9] == cLists[49]):
                                solRot += 'RUr'
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists
                                
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists  
                                                              
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                                cLists = lists    
                                
                                count += 1 
                                
                                                           
                        if (cLists[18] == cLists[22]):
                            if(cLists[11] == cLists[49]):
                                solRot += 'ruR'       
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                                cLists = lists 
                                
                                
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                                cLists = lists
                                
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists      
                                
                                count += 1                           
                                                                                       
                        if (cLists[0] == cLists[4]):
                            if(cLists[29] == cLists[49]):

                                solRot += 'luL'
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                                cLists = lists
                                
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                                cLists = lists    
                                                            
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                
                                count += 1                               
                                                                
                        if (cLists[20] == cLists[22]):
                            if(cLists[27] == cLists[49]):
                                solRot += 'LUl' 
                                   
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists  
                                 
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists  
                                 
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                                cLists = lists   
                                
                                count += 1               
                                                                                                                                        
                        if (cLists[9] == cLists[13]):

                            if(cLists[2] == cLists[49]):

                                solRot += 'fuF'   
                                
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[2], cLists[5], cLists[8], cLists[1], cLists[4], cLists[7], cLists[0], cLists[3], cLists[6]
                                cLists = lists 
                                
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                                cLists = lists   
                                                              
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                                cLists = lists 
                                
                                count += 1                                
                                                               
                        if (cLists[29] == cLists[31]):
                            

                            if(cLists[0] == cLists[49]):

                                
                                solRot += 'FUf'   
                                
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                                cLists = lists  
                                  
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists  
                                
                                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                                cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[2], cLists[5], cLists[8], cLists[1], cLists[4], cLists[7], cLists[0], cLists[3], cLists[6]
                                cLists = lists    
                                
                                count += 1                                                               
                                
                                                                                                        
                        if (cLists[11] == cLists[13]):
                            if(cLists[18] == cLists[49]):
                                solRot += 'BUb'  
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists  
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists  
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                                cLists = lists 
                                
                                count += 1 
                                                                                                                                   
                        if (cLists[27] == cLists[31]):
                            if(cLists[20] == cLists[49]):
                                solRot += 'buB'   
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                                cLists = lists    
                                                              
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                                cLists = lists   
                                
                                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                                cLists = lists 
                                
                                count += 1 
                                                          
                        if (count == 0):
                            solRot += 'U'
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                            cLists = lists
                            print('On')
                            count = 0
                            
                    else:
                        
                        # when colors are in bottom sides
                        if (cLists[15] == cLists[49]):
                            solRot += 'fUF'
                            lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                            cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[2], cLists[5], cLists[8], cLists[1], cLists[4], cLists[7], cLists[0], cLists[3], cLists[6]
                            cLists = lists 
                                                              
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                            cLists = lists 
                                                            
                            lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                            cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                            cLists = lists                            
                            
                        elif (cLists[17] == cLists[49]):
                            solRot += 'Bub'
                            lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                            cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                            cLists = lists   
                                                     
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                            cLists = lists          
                                              
                            lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                            cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                            cLists = lists                                        
                                        
                            
                        elif (cLists[24] == cLists[49]):
                            solRot += 'rUR'
                            lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                            cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                            cLists = lists                            
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                            cLists = lists  
                            lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                            cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                            cLists = lists     
                                                                            
                        elif (cLists[26] == cLists[49]):
                            solRot += 'Lul'
                            lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                            cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                            cLists = lists    
                                                    
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                            cLists = lists  
                            
                            lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                            cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                            cLists = lists 
                                                                                 
                        elif (cLists[33] == cLists[49]):
                            solRot += 'bUB'
                            lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                            cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                            cLists = lists 
                                                        
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                            cLists = lists  
                            
                            lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                            cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                            cLists = lists                             
                                                       
                        elif (cLists[35] == cLists[49]):
                            solRot += 'Fuf'
                            lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                            cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                            cLists = lists     
                                                     
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                            cLists = lists  
                            
                            lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                            cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[2], cLists[5], cLists[8], cLists[1], cLists[4], cLists[7], cLists[0], cLists[3], cLists[6]
                            cLists = lists   
                                                                                 
                        elif (cLists[6] == cLists[49]):
                            solRot += 'lUL'
                            lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                            cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                            cLists = lists      
                                                   
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                            cLists = lists 
                            
                            lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                            cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                            cLists = lists      
                                                                                
                        elif (cLists[8] == cLists[49]):
                            solRot += 'Rur'
                            lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                            cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                            cLists = lists  
                                                       
                            lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                            cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                            cLists = lists 
                                                        
                            lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                            cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                            cLists = lists 
                                                    
                        else:
                            if (cLists[42] == cLists[49]):
                                solRot += 'luLluL'
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                                cLists = lists                                 
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                                cLists = lists                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                                cLists = lists                                 
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                                cLists = lists                                
                                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                                cLists = lists                                
                                
                                                                 
                            elif(cLists[44] == cLists[49]):
                                solRot += 'RUrRUr'
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists  
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                             
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                                cLists = lists                             
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                                cLists = lists  
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists                             
                                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                                cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                                cLists = lists  
                                                                                              
                            else:
                                solRot += 'U'
                                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                                cLists = lists
 
                    
                    print('^^^^^')
                    print(cLists[45])
                    print(cLists[46])
                    print(cLists[47])
                    print(cLists[48])
                    print(cLists[49])
                    print(cLists[50])
                    print(cLists[51])
                    print(cLists[52])
                    print(cLists[53])
                    print('^^^^')
                    
                    if (cLists[45] == cLists[46] and cLists[46] == cLists[47] and cLists[47] == cLists[48] and cLists[48] == cLists[49] and cLists[50] == cLists[49] and cLists[50] == cLists[51] and cLists[51] == cLists[52] and cLists[52] == cLists[53]):
                        btmLayer = False

    
    # End P2
    
    
    # P3) Entering rotate mode, put rotations in rlist and show error if rotation is invalid 
    else:
        rLists = rotations

    
    
    k = 0
    while k < len(rLists):
        if (rLists[k] != 'F' and rLists[k] != 'f' and rLists[k] != 'R' and rLists[k] != 'r' and rLists[k] != 'B' and rLists[k] != 'b' and rLists[k] != 'L' and rLists[k] != 'l' and rLists[k] != 'U' and rLists[k] != 'u' and rLists[k] != 'D' and rLists[k] != 'd'):
            result['status'] = 'error: Invalid rotation inputs' 
            return result
    
        k += 1
    # P3) End P3





    # P4) Do rotation based on rLists
    # All rotated values is on lists after this

    
    k = 0
    while k < len(rLists):
            
            if (rLists[k] == 'F'):
                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                cLists = lists

            
            if (rLists[k] == 'f'): 
                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[2], cLists[5], cLists[8], cLists[1], cLists[4], cLists[7], cLists[0], cLists[3], cLists[6]
                cLists = lists                                                                                                                                                                                                                                                                                                                 
            
            if (rLists[k] == 'R'):
                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                cLists = lists
            
            if (rLists[k] == 'r'):
                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                cLists = lists
                
            if (rLists[k] == 'B'):
                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                cLists = lists

            if (rLists[k] == 'b'):
                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                cLists = lists

            if (rLists[k] == 'L'): 
                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                cLists = lists

            if (rLists[k] == 'l'): 
                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                cLists = lists
            
            if (rLists[k] == 'U'): 
                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                cLists = lists
            
            if (rLists[k] == 'u'): 
                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                cLists = lists
            ##
            if (rLists[k] == 'D'): 
                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                cLists = lists
            ##
            if (rLists[k] == 'd'): 
                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[47], cLists[50], cLists[53], cLists[46], cLists[49], cLists[52], cLists[45], cLists[48], cLists[51]
                cLists = lists
            k += 1
    # End P4
    
    # P5) all the rotated values on lists array will be on fLists as string
    # Then return fLists as ['Cube'] and status['ok']
    fLists = ''
    k = 0
    while k < 54:
        fLists += lists[k]
        k += 1
        
    result['cube'] = fLists
    result['status'] = 'ok'
    
    return result
    # End P5
