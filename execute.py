import json
import pandas as pd

def main():
    # Read the data
    df = pd.read_excel("data.xlsx")

    # Compute revenue
    df["revenue"] = df["units"] * df["price"]

    # row_count
    row_count = len(df)

    # regions: count of distinct regions
    regions_count = df["region"].nunique()

    # top_n_products_by_revenue (n=3)
    n = 3
    top_products = (
        df.groupby("product")['revenue']
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    top_products_list = [
        {"product": row["product"], "revenue": float(row["revenue"])}
        for _, row in top_products.iterrows()
    ]

    # rolling_7d_revenue_by_region: for each region, last value of 7-day moving average of daily revenue
    df["date"] = pd.to_datetime(df["date"])  # ensure datetime
    daily_rev = (
        df.groupby(["region", "date"])['revenue']  # daily revenue per region
        .sum()
        .reset_index()
    )
    rolling_avg = daily_rev.groupby("region")['revenue'].rolling(window=7).mean().reset_index()
    last_7d_avg = rolling_avg.groupby("region").last().reset_index()

    # Combine results
    result = {
        "row_count": row_count,
        "regions_count": regions_count,
        "top_products": top_products_list,
        "last_7d_avg": last_7d_avg.to_dict(orient='records')
    }

    # Print result in JSON format
    print(json.dumps(result))

if __name__ == '__main__':
    main()