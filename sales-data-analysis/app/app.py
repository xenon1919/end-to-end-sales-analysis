from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def index():
    # -------- Path Handling (Bulletproof) --------
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(
        BASE_DIR, "..", "data", "cleaned", "sales_data_final.csv"
    )
    STATIC_DIR = os.path.join(BASE_DIR, "static")

    df = pd.read_csv(DATA_PATH)

    # -------- Core Metrics --------
    total_revenue = round(df["Revenue"].sum(), 2)
    total_orders = df["OrderID"].nunique()
    avg_order_value = round(df["Revenue"].mean(), 2)

    # -------- Key Insights --------
    top_category = (
        df.groupby("ProductCategory")["Revenue"]
        .sum()
        .idxmax()
    )

    best_region = (
        df.groupby("Region")["Revenue"]
        .sum()
        .idxmax()
    )

    discount_corr = df[["Discount", "Revenue"]].corr().iloc[0, 1]
    discount_insight = (
        "Discounts have a strong impact on revenue"
        if abs(discount_corr) > 0.3
        else "Discounts have a weak impact on revenue"
    )

    above_market_pct = round(df["AboveMarketPrice"].mean() * 100, 1)
    market_insight = f"{above_market_pct}% of products are priced above market"

    # -------- Chart 1: Revenue by Category --------
    category_revenue = df.groupby("ProductCategory")["Revenue"].sum()

    plt.figure()
    category_revenue.plot(kind="bar")
    plt.title("Revenue by Product Category")
    plt.ylabel("Revenue")
    plt.tight_layout()

    category_chart = os.path.join(STATIC_DIR, "revenue_by_category.png")
    plt.savefig(category_chart)
    plt.close()

    # -------- Chart 2: Revenue by Region --------
    region_revenue = df.groupby("Region")["Revenue"].sum()

    plt.figure()
    region_revenue.plot(kind="bar")
    plt.title("Revenue by Region")
    plt.ylabel("Revenue")
    plt.tight_layout()

    region_chart = os.path.join(STATIC_DIR, "revenue_by_region.png")
    plt.savefig(region_chart)
    plt.close()

    return render_template(
    "index.html",
    total_revenue=total_revenue,
    total_orders=total_orders,
    avg_order_value=avg_order_value,


    top_category=top_category,
    best_region=best_region,
    discount_insight=discount_insight,
    market_insight=market_insight
)


if __name__ == "__main__":
    app.run(debug=True)
