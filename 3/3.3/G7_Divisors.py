print({n: [j for j in range(1, n + 1) if n % j == 0] for n in sorted(numbers)})
