# Session 9

import pandas as pd
import numpy as np

def build_report():
    df = pd.DataFrame({
        "Date": pd.date_range("2024-01-01", periods=10, freq="D"),
        "Revenue": np.random.randint(200, 800, 10),
        "Expenses": np.random.randint(100, 400, 10)
    })

    print("\nInitial Data:")
    print(df)

    df["Profit"] = df["Revenue"] - df["Expenses"]
    df["Cumulative"] = df["Profit"].cumsum()

    print("\nWith Profit and Cumulative:")
    print(df)

    good_days = df[df["Profit"] > 250]
    print("\nHigh Profit Days:")
    print(good_days)

    df.set_index("Date", inplace=True)
    summary = df.resample("W").mean(numeric_only=True)

    print("\nWeekly Averages:")
    print(summary)

if __name__ == '__main__':
    build_report()