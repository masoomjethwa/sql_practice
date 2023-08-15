import pandas as pd
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to execute")
        return result
    return wrapper

@timing_decorator
def wrangle_data(filename):
    """
    This function wrangles the data in the given file.

    Args:
      filename: The name of the file containing the data.

    Returns:
      A Pandas DataFrame containing the wrangled data.
    """
    # ... (your existing code)

if __name__ == "__main__":
    data_2021, data_2022, average_temperature_2021, average_temperature_2022 = wrangle_data("data.csv")
    print("The average temperature in 2021 was", average_temperature_2021)
    print("The average temperature in 2022 was", average_temperature_2022)
