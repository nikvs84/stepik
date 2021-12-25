n = int(input())

terms = []

remainder = n

for i in range(1, n + 1):
    current_remainder = remainder - i
    if current_remainder > i:
        terms.append(i)
        remainder = current_remainder
    else:
        terms.append(remainder)
        break

print(len(terms))
print(' '.join([str(a) for a in terms]))