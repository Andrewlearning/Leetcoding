"""
给定两个升序排序的有序数组A和B，以及一个目标值x。数组下标从0开始。
请你求出满足A[i] + B[j] = x的数对(i, j)。

数据保证有唯一解。

输入格式
第一行包含三个整数n，m，x，分别表示A的长度，B的长度以及目标值x。

第二行包含n个整数，表示数组A。

第三行包含m个整数，表示数组B。

输出格式
共一行，包含两个整数 i 和 j。

数据范围
数组长度不超过100000。
同一数组内元素各不相同。
1≤数组元素≤109
输入样例：
4 5 6
1 2 4 7
3 4 6 8 9
输出样例：
1 1
"""
def main():
    for i in range(n):
        j = m - 1
        # 在这里移动双指针
        # 我们的目标是找到，i在当前位置，满足i + j = x的最左j
        while j > 0 and a[i] + b[j] > x:
            j -= 1
        if a[i] + b[j] == x:
            return i, j


if __name__ == "__main__":
    n, m, x = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(main())

