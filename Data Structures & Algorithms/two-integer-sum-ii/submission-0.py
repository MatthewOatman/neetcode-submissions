class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, back = 1, len(numbers)


        while (numbers[front - 1] + numbers[back - 1] != target):
            if (numbers[front - 1] + numbers[back - 1] > target): 
                back -= 1
            if (numbers[front - 1] + numbers[back - 1] < target):
                front += 1

        return [front, back]