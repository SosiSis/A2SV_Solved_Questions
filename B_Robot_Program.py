import sys

def solve():
    t = int(input())
    results = []

    for _ in range(t):
        n, x, k = map(int, input().split())
        s = input().strip()

        time_to_first_zero = -1
        current_x = x

        for i in range(min(n, k)):
            if s[i] == 'L':
                current_x -= 1
            else:
                current_x += 1

            if current_x == 0:
                time_to_first_zero = i + 1
                break

        if time_to_first_zero == -1:
            results.append("0")
            continue

        ans = 1
        remaining_k = k - time_to_first_zero

        time_to_return_zero = -1
        current_x = 0

        for i in range(n):
            if s[i] == 'L':
                current_x -= 1
            else:
                current_x += 1

            if current_x == 0:
                time_to_return_zero = i + 1
                break

        if time_to_return_zero != -1:
            ans += (remaining_k // time_to_return_zero)

        results.append(str(ans))

    print("\n".join(results))

if __name__ == "__main__":
    solve()
