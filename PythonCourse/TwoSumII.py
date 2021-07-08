class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if (numbers[i] + numbers[j] == target and i != j):
                    if (i < j):
                        return [i + 1, j + 1]
                    return [j + 1, i + 1]
                    break


