from typing import Callable, Tuple
import matplotlib.pyplot as plt


def secante(function: str, x0: float, x1: float, error: float) -> Tuple[float, float, plt.Figure]:

    # Convert the function string to a callable function
    func = eval(f"lambda x: {function}")

    # Initialize variables
    x2 = x1 - ((func(x1) * (x1 - x0)) / (func(x1) - func(x0)))
    error_percent = abs((x2 - x1) / x2) * 100
    iterations = 1
    x_values = [x0, x1, x2]
    y_values = [func(x0), func(x1), func(x2)]

    # Keep iterating until the error is within the allowed range
    while error_percent > error:
        x0 = x1
        x1 = x2
        x2 = x1 - ((func(x1) * (x1 - x0)) / (func(x1) - func(x0)))
        error_percent = abs((x2 - x1) / x2) * 100
        iterations += 1
        x_values.append(x2)
        y_values.append(func(x2))

    # Plot the graph
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_title("Secant Method")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Return the root, error percentage, and graph
    return x2, error_percent, fig