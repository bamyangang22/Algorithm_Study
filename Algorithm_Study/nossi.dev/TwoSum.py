'''
1. 문제 이해하기
nums 배열과 target을 파라ㅏ미터로 받아 nums 배열에서 두 수를 더해
target 값을 만들 수 있는지 물어보는 문제.
자기 자신을 더하는 것X && 배열에서 답은 한번만 등장한다고 가정

2. 접근 방법
우선 배열에서 인덱스 i, j를 이중 for문을 이용하여 두 수의 합을 구하고
확인하는 방식으로 구현 가능 -> O(n^2)
But! n이 10^4까지 나오므로 O(nlogn)인 알고리즘을 적용해야함.
따라서 정렬을 적용한 후, 이중 for문이 아닌 방식으로 target을 찾을 방법을
떠올려 보자.

3. 코드 설계

4. 코드 구현
'''
class solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)-1):
            for j in range(i + 1, len(nums)): 
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
        return None

## 테스트
if __name__ == "__main__":
    sol = solution()

    print(sol.twoSum([2,7,11,15], 9))

    print(sol.twoSum([3,2,4], 6))

    print(sol.twoSum([3,3], 6))