import rubik.cube as rubik
import re


def _solve(parms):
    
    # P1) get parms ['cube'] and ['rotate'] and encodedCube and rotations will have these values
    # This portion will check if encodedCube is validated or not. If it is not, will return error on ['status']
    # After checking all error, encodedCube and rotations will convert into lists to use on each cube and rotations values
    # lists <- encodedCube    rLists <- rotations
    encodedCube = parms.get('cube', None)
    rotations = parms.get('rotate', None) 
   
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
    
\
    # P2) Check rList which has rotations, if there are values which is not FfRrBbLlUuDd, will return error
    
    rLists = list(rotations)
    cLists = list(encodedCube)
    
    if (len(rLists) == 0 or rLists[0] == ' '):
            rLists += 'F'
    
    
    k = 0
    while k < len(rLists):
        if (rLists[k] != 'F' and rLists[k] != 'f' and rLists[k] != 'R' and rLists[k] != 'r' and rLists[k] != 'B' and rLists[k] != 'b' and rLists[k] != 'L' and rLists[k] != 'l' and rLists[k] != 'U' and rLists[k] != 'u' and rLists[k] != 'D' and rLists[k] != 'd'):
            result['status'] = 'error: Invalid rotation inputs' 
            return result
    
        k += 1
    # End P2


    # P3) Do rotation based on rLists
    # All rotated values is on lists after this

    
    k = 0
    while k < len(rLists):
            
            if (rLists[k] == 'F'):
                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[6], cLists[3], cLists[0], cLists[7], cLists[4], cLists[1], cLists[8], cLists[5], cLists[2]
                cLists = lists
            
            if (rLists[k] == 'f'): 
                lists[42], lists[43], lists[44], lists[9], lists[12], lists[15], lists[47], lists[46], lists[45], lists[35], lists[32], lists[29], lists[0], lists[1], lists[2], lists[3], lists[4], lists[5], lists[6], lists[7], lists[8] = cLists[9], cLists[12], cLists[15], cLists[47], cLists[46], cLists[45], cLists[35], cLists[32], cLists[29], cLists[42], cLists[43], cLists[44], cLists[2], cLists[5], cLists[8], cLists[1], cLists[4], cLists[7], cLists[0], cLists[3], cLists[6]
                cLists = lists                                                                                                                                                                                                                                                                                                                 
            
            if (rLists[k] == 'R'):
                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[15], cLists[12], cLists[9], cLists[16], cLists[13], cLists[10], cLists[17], cLists[14], cLists[11]
                cLists = lists
            
            if (rLists[k] == 'r'):
                lists[44], lists[41], lists[38], lists[18], lists[21], lists[24], lists[53], lists[50], lists[47], lists[8], lists[5], lists[2], lists[9], lists[10], lists[11], lists[12], lists[13], lists[14], lists[15], lists[16], lists[17] = cLists[18], cLists[21], cLists[24], cLists[53], cLists[50], cLists[47], cLists[8], cLists[5], cLists[2], cLists[44], cLists[41], cLists[38], cLists[11], cLists[14], cLists[17], cLists[10], cLists[13], cLists[16], cLists[9], cLists[12], cLists[15]         
                cLists = lists
            
            if (rLists[k] == 'B'):
                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = cLists[17], cLists[14], cLists[11], cLists[38], cLists[37], cLists[36], cLists[27], cLists[30], cLists[33], cLists[51], cLists[52], cLists[53], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                cLists = lists
            
            if (rLists[k] == 'b'):
                lists[36], lists[37], lists[38], lists[11], lists[14], lists[17], lists[53], lists[52], lists[51], lists[33], lists[30], lists[27], lists[18], lists[19], lists[20], lists[21], lists[22], lists[23], lists[24], lists[25], lists[26] = cLists[17], cLists[14], cLists[11], cLists[38], cLists[37], cLists[36], cLists[27], cLists[30], cLists[33], cLists[51], cLists[52], cLists[53], cLists[24], cLists[21], cLists[18], cLists[25], cLists[22], cLists[19], cLists[26], cLists[23], cLists[20]
                cLists = lists
            
            if (rLists[k] == 'L'): 
                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[47], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = cLists[20], cLists[23], cLists[26], cLists[51], cLists[47], cLists[45], cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[33], cLists[30], cLists[27], cLists[34], cLists[31], cLists[28], cLists[35], cLists[32], cLists[29]
                cLists = lists
            
            if (rLists[k] == 'l'): 
                lists[42], lists[39], lists[36], lists[20], lists[23], lists[26], lists[51], lists[47], lists[45], lists[6], lists[3], lists[0], lists[27], lists[28], lists[29], lists[30], lists[31], lists[32], lists[33], lists[34], lists[35] = cLists[6], cLists[3], cLists[0], cLists[42], cLists[39], cLists[36], cLists[20], cLists[23], cLists[26], cLists[51], cLists[47], cLists[45], cLists[29], cLists[32], cLists[35], cLists[28], cLists[31], cLists[34], cLists[27], cLists[30], cLists[33]
                cLists = lists
            
            if (rLists[k] == 'U'): 
                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[42], cLists[39], cLists[36], cLists[43], cLists[40], cLists[37], cLists[44], cLists[41], cLists[38]
                cLists = lists
            
            if (rLists[k] == 'u'): 
                lists[0], lists[1], lists[2], lists[9], lists[10], lists[11], lists[18], lists[19], lists[20], lists[27], lists[28], lists[29], lists[36], lists[37], lists[38], lists[39], lists[40], lists[41], lists[42], lists[43], lists[44] = cLists[27], cLists[28], cLists[29], cLists[0], cLists[1], cLists[2], cLists[9], cLists[10], cLists[11], cLists[18], cLists[19], cLists[20], cLists[38], cLists[41], cLists[44], cLists[37], cLists[40], cLists[43], cLists[36], cLists[39], cLists[42]
                cLists = lists
            
            if (rLists[k] == 'D'): 
                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[51], lists[52], lists[53], lists[48], lists[49], lists[50], lists[45], lists[46], lists[47] = cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[45], cLists[48], cLists[51], cLists[46], cLists[49], cLists[52], cLists[47], cLists[50], cLists[53]
                cLists = lists
            
            if (rLists[k] == 'd'): 
                lists[6], lists[7], lists[8], lists[15], lists[16], lists[17], lists[24], lists[25], lists[26], lists[33], lists[34], lists[35], lists[51], lists[52], lists[53], lists[48], lists[49], lists[50], lists[45], lists[46], lists[47] = cLists[33], cLists[34], cLists[35], cLists[6], cLists[7], cLists[8], cLists[15], cLists[16], cLists[17], cLists[24], cLists[25], cLists[26], cLists[53], cLists[50], cLists[47], cLists[52], cLists[49], cLists[46], cLists[51], cLists[48], cLists[45]
                cLists = lists
            k += 1
    # End P3
    
    
    # P4) all the rotated values on lists array will be on fLists as string
    # Then return fLists as ['Cube'] and status['ok']
    fLists = ''
    k = 0
    while k < 54:
        fLists += lists[k]
        k += 1
        
    result['cube'] = fLists
    result['status'] = 'ok'
    
    return result
    # End P4
    
    
    
    # print(rLists)
    #
    #
    #
    #
    #
    #
    #
    # i = 0
    # while i < len(lists):
    #     fLists += lists[i]
    #     i = i + 1
    #
    # result['status'] = 'ok'
    # result['cube'] = fLists
    # return result
    #
    #
    #

    
    #FfRrBbLlUuDd
    #F : 42 43 44 9 12 15 47 46 45 35 32 29 0 1 2 3 4 5 6 7 8 -> 35 32 29 42 43 44 9 12 15 47 46 45 6 3 0 7 4 1 8 5 2
    #f : 42 43 44 9 12 15 47 46 45 35 32 29 0 1 2 3 4 5 6 7 8 -> 9 12 15 47 46 45 35 32 29 42 43 44 2 5 8 1 4 7 0 3 6
    
    #R : 44 41 38 18 21 24 53 50 47 8 5 2 9 10 11 12 13 14 15 16 17 -> 8 5 2 44 41 38 18 21 24 53 50 47 15 12 9 16 13 10 17 14 11
    #r : 44 41 38 18 21 24 53 50 47 8 5 2 9 10 11 12 13 14 15 16 17 -> 18 21 24 53 50 47 8 5 2 44 41 38 11 14 17 10 13 16 9 12 15
    
    #B : 36 37 38 11 14 17 53 52 51 33 30 27 18 19 20 21 22 23 24 25 26 -> 11 14 17 53 52 51 33 30 27 36 37 38 24 21 18 25 22 19 26 23 20 
    #b : 36 37 38 11 14 17 53 52 51 33 30 27 18 19 20 21 22 23 24 25 26 -> 33 30 27 36 37 38 11 14 17 53 52 51 20 23 26 19 22 25 18 21 24
    
    #L : 42 39 36 20 23 26 51 47 45 6 3 0 27 28 29 30 31 32 33 34 35 -> 20 23 26 51 47 45 6 3 0 42 39 36 33 30 27 34 31 28 35 32 29
    #l : 42 39 36 20 23 26 51 47 45 6 3 0 27 28 29 30 31 32 33 34 35 -> 6 3 0 42 39 36 20 23 26 51 47 45 29 32 35 28 31 34 27 30 33
    
    #U : 0 1 2 9 10 11 18 19 20 27 28 29 36 37 38 39 40 41 42 43 44 -> 9 10 11 18 19 20 27 28 29 0 1 2 42 39 36 43 40 37 44 41 38
    #u : 0 1 2 9 10 11 18 19 20 27 28 29 36 37 38 39 40 41 42 43 44 -> 27 28 29 0 1 2 9 10 11 18 19 20 38 41 44 37 40 43 36 39 42
    
    #D : 6 7 8 15 16 17 24 25 26 33 34 35 51 52 53 48 49 50 45 46 47 -> 15 16 17 24 25 26 33 34 35 6 7 8 45 48 51 46 49 52 47 50 53
    #d : 6 7 8 15 16 17 24 25 26 33 34 35 51 52 53 48 49 50 45 46 47 -> 33 34 35 6 7 8 15 16 17 24 25 26 53 50 47 52 49 46 51 48 45    
    #get input, read each rotate, rotate, repeat if there is more on rotate, return result
    
    # 51 52 53
    # 48 49 50
    # 45 46 47
    
    # result = {}
    # encodedCube = parms.get('cube',None)       #get "cube" parameter if present
    # result['solution'] = 'FfRrBbLlUuDd'        #example rotations
    # result['status'] = 'ok'                     
    # return result

    # 


# dev strategy
#        validdate parms
#        load parms['cube'] into cube model
#        rotate cube in desired direction
#        serialize cube model in string
#        return string + status of 'ok'