
class Linear_search():
    @staticmethod
    def count_occ(array, n):
        count = 0
        for i in array:
            if n == i:
                count += 1

        return count


array = list(map(int, input().split()))
n = int(input())
result = Linear_search()
print(result.count_occ(array, n))



