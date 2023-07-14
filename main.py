from sys import exit


try:
    import matplotlib as plt
    print("matplotlib module loaded")
except:
    print("No such module like matplotlib")
    exit(0)

try:
    import pandas as pd
    print("pandas module loaded")
except:
    print("No such module like pandas")
    exit(0)

source_data = "https://raw.githubusercontent.com/abixadamj/helion-python/main/Rozdzial_5/data.csv"
print(f"Source data: {source_data}")

try:
    df = pd.read_csv(source_data)
    print("Source data loaded")
except:
    print("Error occur while try load source data.")
    exit(0)

print("----[ Info about source data ]----")
print(df)
print("------------------------")

new_df = df[['obce', 'polskie', 'month']]

plot = new_df.plot(
    kind="line",
    x="month",
    xlabel="Rok - miesiąc",
    ylabel="Liczba obsłużonych statów",
    title="Przeładunki w porcie w Gdyni",
)

plot.get_figure().savefig("chart.png")
