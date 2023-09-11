#User function Template for python3

class Solution:
    def isSquare(self, x1, y1, x2, y2, x3, y3, x4, y4):
        # code here 
        if(x1==x2==x3==x4):
            return "No"
        elif(abs(abs(x1)-abs(x2))==abs(abs(x3)-abs(x4)) and abs(abs(y1)-abs(y2))==abs(abs(y3)-abs(y4))):
            return "Yes"
        else:
            return "No"
