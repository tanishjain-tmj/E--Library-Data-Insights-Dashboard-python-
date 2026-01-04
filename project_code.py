import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class LibraryDashboard:

    def __init__(self):
        self.df = None

    def load_data(self, file_path):
        print("Loading dataset...")

        if not os.path.exists(file_path):
            raise FileNotFoundError("CSV file not found!")

        if not file_path.endswith(".csv"):
            raise ValueError("Invalid file format. Please provide a CSV file.")

        self.df = pd.read_csv(file_path)

        required_columns = [
            "Transaction ID",
            "Date",
            "User ID",
            "Book Title",
            "Genre",
            "Borrowing Duration (Days)"
        ]
        for col in required_columns:
            if col not in self.df.columns:
                raise ValueError(f"Missing column: {col}")

        self.df.dropna(inplace=True)

        self.df["Date"] = pd.to_datetime(self.df["Date"])

        print(" Data loaded and validated successfully.")

    def calculate_statistics(self):
        most_borrowed_book = self.df["Book Title"].value_counts().idxmax()
        avg_borrow_duration = np.mean(self.df["Borrowing Duration (Days)"])
        busiest_day = self.df["Date"].dt.day_name().value_counts().idxmax()

        stats = {
            "Most Borrowed Book": most_borrowed_book,
            "Average Borrowing Duration (Days)": round(avg_borrow_duration, 2),
            "Busiest Day": busiest_day
        }

        return stats

    def filter_transactions(self, genre=None, start_date=None, end_date=None):
        filtered_df = self.df.copy()

        if genre:
            filtered_df = filtered_df[filtered_df["Genre"] == genre]

        if start_date and end_date:
            filtered_df = filtered_df[
                (filtered_df["Date"] >= start_date) &
                (filtered_df["Date"] <= end_date)
            ]

        return filtered_df

    def generate_report(self):
        stats = self.calculate_statistics()

        print("\n E-LIBRARY DATA INSIGHTS REPORT")
        print("--------------------------------")
        for key, value in stats.items():
            print(f"{key}: {value}")

    def visualize(self):

        # Bar Chart – Top 5 Books
        plt.figure(figsize=(10, 5))
        self.df["Book Title"].value_counts().head(5).plot(kind="bar")
        plt.title("Top 5 Most Borrowed Books")
        plt.xlabel("Book Title")
        plt.ylabel("Borrow Count")
        plt.tight_layout()
        plt.show()

        # Line Graph – Monthly Trends
        plt.figure(figsize=(10, 5))
        monthly_data = self.df.groupby(self.df["Date"].dt.month)["Transaction ID"].count()
        monthly_data.plot(marker='o')
        plt.title("Borrowing Trends Over Months")
        plt.xlabel("Month")
        plt.ylabel("Number of Borrows")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Pie Chart – Genre Distribution
        plt.figure(figsize=(7, 7))
        self.df["Genre"].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90
        )
        plt.title("Distribution of Books by Genre")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

        # Heatmap – Borrowing Activity by Day
        heatmap_df = self.df.copy()
        heatmap_df["Day"] = heatmap_df["Date"].dt.day_name()

        pivot_table = pd.pivot_table(
            heatmap_df,
            index="Day",
            values="Transaction ID",
            aggfunc="count"
        )

        plt.figure(figsize=(8, 5))
        sns.heatmap(pivot_table, annot=True, cmap="coolwarm")
        plt.title("Borrowing Activity Heatmap")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    dashboard = LibraryDashboard()

    try:
        dashboard.load_data("library_transaction.csv")
        dashboard.generate_report()
        dashboard.visualize()
    except Exception as error:
        print("Error:", error)
