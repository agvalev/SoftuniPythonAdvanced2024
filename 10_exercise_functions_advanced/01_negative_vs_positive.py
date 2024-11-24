def nums_sums(*args):
    n_sum = sum(n for n in args if n < 0)
    p_sum = sum(n for n in args if n > 0)
    return n_sum, p_sum


nums = map(int, input().split())

neg_sum, pos_sum = nums_sums(*nums)

print(neg_sum)
print(pos_sum)

if abs(neg_sum) > pos_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
