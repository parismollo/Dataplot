from plotting import plot_math_function, plot_bar, plot_grades, plot_line_chart, plot_scatter
def choose_plot():
    print("***** Hello World *****")
    print("Press (1) to plot a equation chart")
    print("Press (2) to plot bar chart")
    print("Press (3) to plot dispersion bar chart")
    print("Press (4) to plot a line chart")
    print("Press (5) to a scatter chart")
    number = 0
    while number not in range(1, 3):
        number = int(input("Which one? "))
        if number == 1:
            print("Plotting math equation...")
            plot_math_function()
        elif number == 2:
            print("Plotting Moons...")
            plot_bar()
        elif number == 3:
            print("Plotting grades...")
            plot_grades()
        elif number == 4:
            print("Plotting line charts...")
            plot_line_chart()
        elif number == 5:
            print("Plotting scatter...")
            plot_scatter()
        else:
            print("Choose a valid option")

if __name__ == "__main__":
    choose_plot()
