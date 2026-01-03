# test_control.py
# Simple test for Python control library

import control as ctrl
import matplotlib.pyplot as plt

def main():
    # Define a second-order transfer function: G(s) = 1 / (s^2 + 3s + 2)
    num = [1]
    den = [1, 3, 2]
    system = ctrl.tf(num, den)

    # Print the transfer function
    print("Transfer function:")
    print(system)

    # Step response
    time, response = ctrl.step_response(system)

    # Plot the step response
    plt.plot(time, response)
    plt.title("Step Response of G(s) = 1 / (s^2 + 3s + 2)")
    plt.xlabel("Time (s)")
    plt.ylabel("Output")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
