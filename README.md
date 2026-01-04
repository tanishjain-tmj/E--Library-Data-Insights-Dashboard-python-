# E--Library-Data-Insights-Dashboard-python-
# E-Library Data Insights Dashboard

## 📌 Project Objective
The objective of this project is to develop a **Python-based E-Library Data Insights Dashboard** that analyzes library borrowing data and provides meaningful insights into book popularity, user activity, and borrowing trends over time.

The project demonstrates the practical use of:
- Control Structures & Arrays
- Object-Oriented Programming (OOP)
- NumPy for numerical computations
- Pandas for data handling
- Matplotlib & Seaborn for data visualization

---

## ✨ Features and Functionalities

### 1. Data Input and Validation
- Accepts a CSV file (`library_transactions.csv`) as input.
- Validates file format and required columns.
- Handles missing or invalid data entries.

### 2. Object-Oriented Design
- Uses a `LibraryDashboard` class.
- Encapsulates all functionalities into reusable methods:
  - `load_data()`
  - `calculate_statistics()`
  - `filter_transactions()`
  - `generate_report()`
  - `visualize()`

### 3. Data Analysis and Computation
- Identifies:
  - Most borrowed book
  - Average borrowing duration
  - Busiest borrowing day
- Uses NumPy for calculating averages and statistics.
- Uses Pandas for grouping and aggregating data.

### 4. Data Filtering
- Allows filtering of transactions based on:
  - Genre
  - Date range

### 5. Data Visualization
Generates insightful visualizations:
- **Bar Chart** – Top 5 most borrowed books
- **Line Graph** – Borrowing trends over months
- **Pie Chart** – Distribution of books by genre
- **Heatmap** – Borrowing activity by day

---

## 🖥️ User Interface

This project uses a **Command Line Interface (CLI)** along with **graphical visualizations**.

### CLI Output:
- Displays loading status
- Shows a summarized analysis report:
  - Most borrowed book
  - Average borrowing duration
  - Busiest day

### Graphical Interface:
- Visualizations are displayed in separate windows using:
  - Matplotlib
  - Seaborn

The interface is simple, user-friendly, and suitable for academic demonstrations and viva examinations.

---

## 📂 Dataset Details

**File Name:** `library_transactions.csv`

**Columns Used:**
- Transaction ID
- Date (YYYY-MM-DD)
- User ID
- Book Title
- Genre
- Borrowing Duration (Days)

The dataset contains multiple users, books, and genres spread across several months to enable meaningful analysis.

---

## ⚙️ Project Requirements

### Software Requirements
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
