from plotting import plot_math_function, plot_bar
def choose_plot():
    print("***** Hello World *****")
    print("Press (1) for math equation chart")
    print("Press (2) for moons count bar chart")
    number = 0
    while number not in range(1, 3):
        number = int(input("Which one? "))
        if number == 1:
            print("Plotting math equation...")
            plot_math_function()
        elif number == 2:
            print("Plotting Moons...")
            plot_bar()
        else:
            print("Choose a valid option")
if __name__ == "__main__":
    choose_plot()
