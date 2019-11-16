from matplotlib import pyplot as plt

def plot_math_function():
    xs = [x for x in range(10)]
    ys = [x**2 for x in xs]

    plt.plot(xs, ys, color='red', marker='o', linestyle='solid')
    plt.title("Squared X")
    plt.ylabel("X**2")
    plt.xlabel("Xs")
    plt.show()

def plot_bar():
    planets = ["Earth", "Jupiter", "Saturn", "Neptune", "Mars", "Uranus", "Mercury", "Venus"]

    number_of_moons = [1, 67, 62, 14, 2, 27, 0, 0]

    plt.bar(range(len(planets)), number_of_moons)
    plt.title("Number of Moons per planet")
    plt.ylabel("# of moons")
    plt.xticks(range(len(planets)), planets)
    plt.show()
if __name__ == "__main__":
    plot_bar()
