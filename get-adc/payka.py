import mcp3021_driver as MCP
import time
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    mcp = MCP.MCP3021(5)

    voltage_values = []
    time_values = []
    duration = 10

    plt.ion()
    fig, ax = plt.subplots()

    ax.set_ylim(-10, 1)


    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    plt.grid(True, which="major", linestyle="-")
    plt.minorticks_on()
    
    plt.grid(True, which="minor", linestyle=":")
    (scat, ) = ax.plot([], [])
    try:
        f = open("1.csv", "w")
        start = time.time()
        while time.time() - start < duration:
            voltage_values.append(np.log(mcp.get_voltage() / 5))
            time_values.append(time.time() - start)

            f.write(f"V = {mcp.get_voltage()},\tt = {time.time() - start}\n")

            scat.set_data(time_values, voltage_values)

            ax.set_xlim(0, (time.time() - start) * 1.05)

            fig.canvas.draw()
            fig.canvas.flush_events()
        plt.ioff()
        plt.show()
    finally:
        mcp.deinit()