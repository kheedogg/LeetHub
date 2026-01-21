class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 초기값 세팅
        M, N = len(mat), len(mat[0])
        ans = []
        i, j, direction = 0, 0, [-1,1]

        while len(ans)<M*N:
            # 현재 위치 점 추가
            ans.append(mat[i][j])

            if direction == [-1,1]:
                if j==N-1:
                    i+=1
                    direction=[1,-1]
                elif i==0:
                    j+=1
                    direction=[1,-1]
                else:
                    i+=direction[0]
                    j+=direction[1]

            elif direction == [1,-1]:
                if i==M-1:
                    j+=1
                    direction=[-1,1]
                elif j==0:
                    i+=1
                    direction=[-1,1]
                else:
                    i+=direction[0]
                    j+=direction[1]            

        return ans






