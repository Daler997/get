import mcp3021_driver as MCP
import time
import adc_plot


if __name__ == "__main__":
    mcp = MCP.MCP3021(5)

    voltage_values = []
    time_values = []
    duration = 3.0

    try:
        start = time.time()
        while time.time() - start < duration:
            voltage_values.append(mcp.get_voltage())
            time_values.append(time.time() - start)

        adc_plot.plot_voltage_vs_time(time_values, voltage_values, 5.2)
        adc_plot.plot_sampling_period_hist(time_values)
    finally:
        mcp.deinit()