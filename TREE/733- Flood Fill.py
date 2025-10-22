class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stcolor=image[sr][sc]
        if (stcolor==color):
            return image
        
        row, column= len(image), len (image[0])

        def dfs(r, c):
            if r<0 or c<0 or r>=row or c>=column:
                return 
            if image[r][c]!= stcolor:
                return 

            image[r][c]=color

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        dfs(sr,sc)
        return image