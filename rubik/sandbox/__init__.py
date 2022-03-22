   
import rubik.cube as rubik
import re


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
        # P2-1) Bottom cross solve
        solveFlag = True;
        solveFlag2 = True;
        
        solution = ''
        while(solveFlag):
            if (cLists[49] == cLists[46] and cLists[49] == cLists[48] and cLists[49] == cLists[50] and cLists[49] == cLists[52] and cLists[13] == cLists[16] and cLists[22] == cLists[25] and cLists[31] == cLists[34] and cLists[4] == cLists[7]):
                result['status'] = 'ok'
                
                for i in solRot:
                    solution += i
                
                result['solution'] = solution
                
                return result

            else:
                #top daisey
                while(solveFlag2):

                    print(cLists[37] + cLists[39] + cLists[41] + cLists[43])
                    print(cLists)
                    if (cLists[49] == cLists[37] and cLists[49] == cLists[39] and cLists[49] == cLists[41] and cLists[49] == cLists[43] and cLists[37] == cLists[39] and cLists[37] == cLists[41] and cLists[41] == cLists[43]):
                        solveFlag2 = False

                    elif(cLists[49] == cLists[10]):
                        solRot += 'RBU'
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                        cLists = lists     
                               
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                        cLists = lists
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists    
                        
                                                              
                    elif(cLists[49] == cLists[12]):
                        solRot += 'RRBU' 
                         
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                        cLists = lists 
                            
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                        cLists = lists    
                                                   
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                        cLists = lists
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists   
                                                                                                           
                    elif(cLists[49] == cLists[14]):
                        solRot += 'BU'   
                          
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                        cLists = lists
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists     
                        
                                                               
                    elif(cLists[49] == cLists[16]):
                        solRot += 'rBU'
                        
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                        cLists = lists  

                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                        cLists = lists
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists                        
                        
                                 
                    elif(cLists[49] == cLists[19]):   
                        solRot += 'br'
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists 
                        
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                        cLists = lists                         
                                               
                    elif(cLists[49] == cLists[21]):
                        solRot += 'r'
                        
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                        cLists = lists   
                                               
                    elif(cLists[49] == cLists[23]):  
                        solRot += 'bbr'
                        
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists 
                        
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists   
                                              
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                        cLists = lists       
                                          
                    elif(cLists[49] == cLists[25]):  
                        solRot += 'Br'
                        
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                        cLists = lists  
                        
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                        cLists = lists  
                                                
                    elif(cLists[49] == cLists[28]):   
                        solRot += 'lbU'
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists   
                        
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists 
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists     
                                                                   
                    elif(cLists[49] == cLists[30]):
                        solRot += 'llFu'
                        
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists   
                        
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists                        
                        
                        lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                        cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                        cLists = lists
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists    

                                                
                    elif(cLists[49] == cLists[32]):   
                        solRot += 'llbU'
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists   
                        
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists                        
                        
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists 
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists     
                                              
                    elif(cLists[49] == cLists[34]):                         
                        solRot += 'LbU'
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                        cLists = lists       
                        
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists 
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists                           
                        
                                         
                    elif(cLists[49] == cLists[46]):   
                        solRot += 'FFu'
                        lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                        cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                        cLists = lists 
                        
                        lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                        cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                        cLists = lists 
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                        cLists = lists       
                                                                                       
                    elif(cLists[49] == cLists[48]):
                        solRot += 'llUU'
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists   
                        
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists  
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists   
                                              
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists                         
                        

                                              
                    elif(cLists[49] == cLists[50]):   
                        solRot += 'RR'
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                        cLists = lists
                
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                        cLists = lists                
                                        
                    elif(cLists[49] == cLists[52]):                         
                        solRot += 'bbU'
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists 
                                                 
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists 
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists  
                                
                                            
                    elif(cLists[49] == cLists[1]):                         
                        solRot += 'UlbU'
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists   
                                
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists        
                                        
                        lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                        cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                        cLists = lists 
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists                          
                                     
                    elif(cLists[49] == cLists[3]):                         
                        solRot += 'lUU'
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists   
                                           
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists  
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists  
                                                                    
                    elif(cLists[49] == cLists[5]):                         
                        solRot += 'R'
                        lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                        cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                        cLists = lists
                                                  
                    elif(cLists[49] == cLists[7]):                         
                        solRot += 'DlFu'
                        
                        lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[45], lists[46], lists[47], lists[48], lists[49], lists[50], lists[51], lists[52], lists[53] = \
                        cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[51], cLists[48], cLists[45], cLists[52], cLists[49], cLists[46], cLists[53], cLists[50], cLists[47]
                        cLists = lists
                        
                        lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                        cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                        cLists = lists
                        
                        lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                        cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                        cLists = lists    
                        
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                        cLists = lists  
                                                              
                    while(True):
                        solRot += 'U'
                        lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                        cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                        cLists = lists
                        if not (cLists[41] != cLists[49]):
                            break
                        
                  


                    
                # make bottom cross
                while(cLists[10] != cLists[13]):
                    solRot += 'U'
                    lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                    cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                    cLists = lists

                solRot += 'rr'
                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                cLists = lists
                
                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = \
                cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                cLists = lists                
                                
                while(cLists[1] != cLists[4]):
                    solRot += 'U'
                    lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                    cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                    cLists = lists
   
                solRot += 'FF'                
                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                cLists = lists
                
                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = \
                cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                cLists = lists                
                
                
                                    
                while(cLists[28] != cLists[31]):
                    solRot += 'U'
                    lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                    cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                    cLists = lists
                  
                solRot += 'LL'     
                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                cLists = lists
                
                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[48], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = \
                cLists[20], cLists[23], cLists[26], cLists[51], cLists[48], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                cLists = lists                
                
                                               
                while(cLists[19] != cLists[22]):
                    solRot += 'U'
                    lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = \
                    cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                    cLists = lists
           
                solRot += 'bb' 
                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                cLists = lists
                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = \
                cLists[33], cLists[30], cLists[27], cLists[36], cLists[37], cLists[38], cLists[11], cLists[14], cLists[17], cLists[53], cLists[52], cLists[51], cLists[20], cLists[23], cLists[26], cLists[19], cLists[22], cLists[25], cLists[18], cLists[21], cLists[24]
                cLists = lists                                
                
                               
                # side color
                
                
                
                
        return result