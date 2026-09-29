import r2r_adc as ADC
import time
import adc_plot


if __name__ == "__main__":
    adc = ADC.R2R_ADC(3.291, compare_time=0.0001)

    voltage_values = []
    time_values = []
    duration = 3.0

    try:
        start = time.time()
        while time.time() - start < duration:
            voltage_values.append(adc.get_sc_voltage())
            time_values.append(time.time() - start)

        adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.5)
        adc_plot.plot_sampling_period_hist(time_values)
    finally:
        adc.deinit()