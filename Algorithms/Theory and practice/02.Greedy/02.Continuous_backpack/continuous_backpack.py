n, w = map(int, input().split())
def compute_thing_props(price, volume):
    return [price, volume, price / volume]
things_sorted = sorted([compute_thing_props(*map(int, input().split())) for i in range(0, n)], key=lambda x: x[2], reverse=True)
# print(things_sorted)

free_space_remaining = w
index_of_thing = 0
amount = 0
while free_space_remaining > 0 and index_of_thing < n:
    thing = things_sorted[index_of_thing]
    thing_part_weight = min(free_space_remaining, thing[1])
    free_space_remaining -= thing_part_weight
    current_price = thing[2]
    current_cost = thing_part_weight * current_price
    amount += current_cost
    # print("Add " + str(thing_part_weight) + " of thing #" + str(index_of_thing) + " for " + str(current_price) + " (+ " + str(current_cost) + ")")
    if thing_part_weight >= thing[1]:
        index_of_thing += 1

print(f"{amount:.3f}")