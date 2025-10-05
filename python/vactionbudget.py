
cities = []
transport = []

cities.append(input("Where are you starting your journey? "))
num_dest = int(input("How many destinations are there on your trip? "))

for i in range(num_dest):
    cities.append(input(f"What is destination #{i + 1}: "))

for i in range(len(cities)):
    transport.append(input(f"How are you getting from {cities[i]} to {cities[(i + 1) % len(cities)]}: "))

group_size = int(input(f"How big is your group: "))

transport_cost = []
for i in range(len(transport)):
    transport_cost.append(int(input(f"How much is the {transport[i]} ticket from {cities[i]} to {cities[(i + 1) % len(cities)]}: ")))

total_cost = sum(transport_cost) * group_size
print(f"Your total cost on transportation for this trip is ${total_cost}.")
