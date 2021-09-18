#Time Complexity: O(N)
#Space Complexity: O(1)

def solution(A):
    
    N = len(A) + 1
    
    missingElement = ((N + 1) * N) / 2
    
    for x in A:
        missingElement -= x
    
    return missingElement
