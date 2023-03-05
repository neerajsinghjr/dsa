'''
-------------------------------------------------------------------------------------
-> Title: 733. Flood Fill
-> Attempted: 04/03/2022
-> Description: 
-------------------------------------------------------------------------------------

An image is represented by an m x n integer grid image where image[i]
[j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color), and so on. Replace the color of all of the
aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1)
(i.e., the red pixel), all pixels connected by a path of the same color as
the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made
to the image.
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n

-------------------------------------------------------------------------------------
'''

from time import time

class Solution:

    def floodFill(self, image, sr, sc, color):
        if not image:
            return image
        if image[sr][sc] != color:
            old_color = image[sr][sc]
            self.dfs(image, sr, sc, color, old_color)

        return image

    def dfs(self, image, sr, sc, color, old_color):
        """
        _run: accepted
        _code: time: o(n*m) | space: (1) | stack: o(n*m)
        _choke: na
        _study: simply making dfs calls from image[sr][sc] to 
        up,down,left,right.
        NOTE: Always make sure you are calling dfs for your objective.        
        """
        dirs = ([1,0], [-1,0], [0,1], [0,-1])
        for (nr, nc) in dirs:
            # trace next row and col;;
            nex_r, nex_c = sr+nr, sc+nc
            # change the new color;;
            image[sr][sc] = color
            # recursive dfs call;;
            if(nex_r in range(len(image)) and \
            nex_c in range(len(image[0])) and \
            image[nex_r][nex_c] == old_color):
                self.dfs(image, nex_r, nex_c, color, old_color)

##---Main Execution;;
def main():
    pass    

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")