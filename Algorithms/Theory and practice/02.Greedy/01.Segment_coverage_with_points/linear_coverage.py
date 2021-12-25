n = int(input())
sorted_segments = sorted([list(map(int, input().split())) for x in range(0, n)], key=lambda x: x[1])

current_point = -1
points = set()

for i in range(0, n):
    current_segment = sorted_segments[i]
    if current_segment[0] > current_point:
        current_point = current_segment[1]
        points.add(current_point)

print(len(points))
print(" ".join(str(b) for b in points))

