# test_control.py
# Simple test for Python control library

import control as ctrl
import matplotlib.pyplot as plt

def main():
    # Define a second-order transfer function: G(s) = 1 / (s^2 + 3s + 2)
    num = [1, 2]
    den = [1, 3, 2]
    system = ctrl.tf(num, den)
    sysMinreal = ctrl.minreal(system)


    # Print the transfer function
    print("Transfer function:")
    print(system)

    print("Transfer function after minreal:")
    print(sysMinreal)

    # Step response
    time, response = ctrl.step_response(system)
    time2 , response2 = ctrl.step_response(sysMinreal)

    # Trim the last 50 points for better visualization
    time2, response2 = time2[0:len(response2)-50], response2[0:len(response2)-50]

    # plole zero plot of system
    ctrl.pzmap(system, title='Pole-Zero Map of G(s)', grid=True)

    # Plot the step response
    plt.plot(time, response)
    plt.plot(time2, response2)
    plt.title("Step Response of G(s) = 1 / (s^2 + 3s + 2)")
    plt.xlabel("Time (s)")
    plt.ylabel("Output")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
