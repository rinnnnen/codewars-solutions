def evaluate_polynomial(coefficients: list[int], x: int) -> int:
    result = 0 #first it
    for coef in coefficients:
        result = result * x + coef #here is cycle, 0 * 2 + 2 -> 2 * 2 + 3 -> 7 * 2 + 4
    return result
