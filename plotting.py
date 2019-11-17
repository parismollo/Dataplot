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

from collections import Counter

def plot_grades():
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
    plt.bar([x + 5 for x in histogram.keys()],histogram.values(), 10, edgecolor=(0, 0, 0))
    plt.axis([-5, 105, 0, 5])
    plt.xticks([10 * i for i in range(11)])
    plt.xlabel("Decile")
    plt.ylabel("# of students")
    plt.title("Distribution of Exam grades")
    plt.show()

def plot_line_chart():
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    plt.plot(xs, variance, 'g-', label='variance')
    plt.plot(xs, bias_squared, 'r-', label='bias^2')
    plt.plot(xs, total_error, 'b:', label='total error')
    plt.legend(loc=9)
    plt.xlabel("Model complexity")
    plt.xticks([])
    plt.title("Bias Variance Tradeoff")
    plt.show()
    
def plot_scatter():
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]

    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    plt.scatter(friends, minutes)

    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label, xy=(friend_count, minute_count),
        xytext=(5, -5), textcoords='offset points')
    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()

if __name__ == "__main__":
    print("You should be using the main file...\nbut here is a taste of this one")
    plot_grades()
