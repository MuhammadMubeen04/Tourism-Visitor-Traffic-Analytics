"""Tourism & Visitor Traffic Analytics - EDA and charts"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE = Path(__file__).parent.parent
DATA = BASE / "data"
CHARTS = Path(__file__).parent / "charts"
CHARTS.mkdir(exist_ok=True)
SUM = DATA / "summaries"
SUM.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (11, 6)

city = pd.read_csv(DATA / "monthly_city_traffic.csv")
visits = pd.read_csv(DATA / "visits.csv")

print("=" * 60)
print("TOURISM & VISITOR TRAFFIC ANALYTICS")
print("=" * 60)
print(f"Total visitors (monthly): {city['Visitors'].sum():,}")
print(f"Est. spend (SAR): {city['EstSpendSAR'].sum():,.0f}")
print(f"Avg occupancy: {city['HotelOccupancyPct'].mean():.1f}%")
print(f"Visit sample: {len(visits):,}")

# Charts
fig, ax = plt.subplots()
city.groupby("City")["Visitors"].sum().sort_values().plot(kind="barh", color="#2b6cb0", ax=ax)
ax.set_title("Total Visitors by City")
ax.set_xlabel("Visitors")
plt.tight_layout()
plt.savefig(CHARTS / "01_visitors_by_city.png", dpi=150)
plt.close()

monthly = city.groupby("YearMonth")["Visitors"].sum()
fig, ax = plt.subplots(figsize=(14, 5))
monthly.plot(ax=ax, marker="o", color="#2b6cb0")
ax.set_title("Monthly Visitor Traffic")
ax.tick_params(axis="x", rotation=60)
plt.tight_layout()
plt.savefig(CHARTS / "02_monthly_trend.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
city.groupby("Year")["Visitors"].sum().plot(kind="bar", color="#38a169", ax=ax)
ax.set_title("Yearly Visitors")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig(CHARTS / "03_yearly_visitors.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
visits["Purpose"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax, startangle=90)
ax.set_ylabel("")
ax.set_title("Visits by Purpose")
plt.tight_layout()
plt.savefig(CHARTS / "04_purpose_share.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
visits.groupby("Origin")["SpendSAR"].sum().sort_values().plot(kind="barh", color="#d69e2e", ax=ax)
ax.set_title("Total Spend by Origin (SAR)")
plt.tight_layout()
plt.savefig(CHARTS / "05_spend_by_origin.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
city.groupby("City")["HotelOccupancyPct"].mean().sort_values().plot(kind="barh", color="#805ad5", ax=ax)
ax.set_title("Average Hotel Occupancy by City (%)")
plt.tight_layout()
plt.savefig(CHARTS / "06_occupancy_by_city.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
visits.groupby("Purpose")["StayNights"].mean().sort_values().plot(kind="barh", color="#319795", ax=ax)
ax.set_title("Average Stay Nights by Purpose")
plt.tight_layout()
plt.savefig(CHARTS / "07_stay_by_purpose.png", dpi=150)
plt.close()

top_m = city.groupby("YearMonth")["Visitors"].sum().nlargest(10).sort_values()
fig, ax = plt.subplots()
top_m.plot(kind="barh", color="#e53e3e", ax=ax)
ax.set_title("Top 10 Months by Visitor Traffic")
plt.tight_layout()
plt.savefig(CHARTS / "08_top_months.png", dpi=150)
plt.close()

print(f"Charts → {CHARTS}")
pd.DataFrame([{
    "total_visitors": int(city["Visitors"].sum()),
    "est_spend_sar": round(city["EstSpendSAR"].sum(), 2),
    "avg_occupancy": round(city["HotelOccupancyPct"].mean(), 1),
    "cities": city["City"].nunique()
}]).to_csv(SUM / "overall_kpis.csv", index=False)
city.groupby("City")["Visitors"].sum().to_csv(SUM / "visitors_by_city.csv")
visits["Purpose"].value_counts().to_csv(SUM / "purpose_counts.csv")
print("Done.")
