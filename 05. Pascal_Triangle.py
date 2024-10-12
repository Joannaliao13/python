"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it 

Example 1:
Input: numRows = 1
Output: [[1]]

Example 2:
Input: numRows = 2
Output: [[1],[1,1]]

Example 3:
Input: numRows = 3
Output: [[1],[1,1],[1,2,1]]

Example 4:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


"""

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ret = []
    if numRows == 0:
        return []
       
    first_row=[1]
    ret.append(first_row)

    for i in range(1,numRows):
        previous_row=ret[i-1]
        current_row=[1]

        for j in range(1, i):
            current_row.append(previous_row[j-1]+previous_row[j])

        current_row.append(1)
        ret.append(current_row)
        
    return ret

n=generate(5)
print("Ans:",n)     # Ans: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


