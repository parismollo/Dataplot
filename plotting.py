from matplotlib import pyplot as plt

xs = [x for x in range(10)]
ys = [x**2 for x in xs]

plt.plot(xs, ys, color='red', marker='o', linestyle='solid')
plt.title("Squared X")
plt.ylabel("X**2")
plt.xlabel("Xs")
plt.show()
