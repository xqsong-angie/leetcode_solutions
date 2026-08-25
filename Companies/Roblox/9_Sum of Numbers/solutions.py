#20260823
#不会
class Solution:
    def solution(self, matrix: list[list[int]], frameSize: int) -> int:
        R = len(matrix)
        C = len(matrix[0])
        k = frameSize
        
        max_sum = float('-inf')
        max_frames_elements = []  # 存放所有拥有最大和的边框的元素列表
        
        # 遍历所有可能的左上角起始点 (r, c)
        for r in range(R - k + 1):
            for c in range(C - k + 1):
                # 提取当前 frameSize x frameSize 的边框元素
                elements = []
                
                if k == 1:
                    elements.append(matrix[r][c])
                else:
                    # 1. 上边 (包含端点)
                    for col in range(c, c + k):#长度为k
                        elements.append(matrix[r][col])
                    # 2. 右边 (不含上端点，含下端点)
                    for row in range(r + 1, r + k):#len=k-1
                        elements.append(matrix[row][c + k - 1])
                    # 3. 下边 (不含右端点，含左端点)
                    for col in range(c + k - 2, c - 1, -1):
                        elements.append(matrix[r + k - 1][col])
                    # 4. 左边 (不含上下两端点)
                    for row in range(r + k - 2, r, -1):
                        elements.append(matrix[row][c])
                
                current_sum = sum(elements)
                
                # 更新最大和并收集对应的边框元素
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_frames_elements = [elements]
                elif current_sum == max_sum:
                    max_frames_elements.append(elements)
        
        # 将所有最大边框里的数字放入集合去重
        distinct_numbers = set()
        for frame_elems in max_frames_elements:
            for val in frame_elems:
                distinct_numbers.add(val)
                
        return sum(distinct_numbers)