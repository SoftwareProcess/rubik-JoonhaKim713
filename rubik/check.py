import rubik.cube as rubik
from pickle import TRUE

def _check(parms):
    result={}
    
    
    
    '''
    is present (V)
    is a string (V)
    has 54 elements (V)
    has 9 occurrences of 6 colors (V)
    has each middle face being a different color (V)
    '''
    encodedCube = parms.get('cube', None)   
   
    count={}
    

           
        
    if (encodedCube == None):
        result['status'] = 'error: cube is none'
        return result
    
    elif (encodedCube == ''):
        result['status'] = 'error: there is empty cube input'
        return result
    
    elif ((str(type(encodedCube)) != "<class 'str'>")):
        result['status'] = 'error: Invalid cube input type'
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
        
    elif(len(count) != 6):
        result['status'] = 'error: Cube does not have 6 colors.'
          
    elif(numCnt):
        result['status'] = 'error: Some cube color may not have 9 occurrences'  
        
    elif(faceCheck):
        result['status'] = 'error: Invalid cube middle face color'  

    else:
        result['status'] = 'ok'
   
    return result