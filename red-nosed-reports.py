"""
Input:
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

Output: 2
"""


def red_nosed_reports(reports):
    num_safe = 0
    for i in range(len(reports)):
        is_increasing = True
        is_decreasing = True
        has_valid_difference = True
        for j in range(1, len(reports[i])):
            diff = abs(reports[i][j - 1] - reports[i][j])
            # safe if all levels i, j are increasing or decreasing
            if reports[i][j - 1] < reports[i][j]:
                is_decreasing = False
            if reports[i][j - 1] > reports[i][j]:
                is_increasing = False
            # safe if any two adjacent levels differ by at least 1 and most 3
            if diff < 1 or diff > 3:
                has_valid_difference = False
        if (is_increasing or is_decreasing) and has_valid_difference:
            num_safe += 1

    return num_safe


def main():
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    print(red_nosed_reports(reports))


if __name__ == "__main__":
    main()
