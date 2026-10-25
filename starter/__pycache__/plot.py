import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# 1. Gather all summary CSV files from the results directories
csv_files = glob.glob("results/**/summary.csv", recursive=True) + glob.glob("results/**/*.csv", recursive=True)

if not csv_files:
    # If file paths differ, fallback to reading individual files directly from current directory
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

dataframes = []
for file in csv_files:
    try:
        df = pd.read_csv(file)
        if "mean_steps_success" in df.columns:
            dataframes.append(df)
    except Exception:
        continue

if not dataframes:
    print("No matching CSV files found. Please ensure CSVs are in results/ or current directory.")
    exit()

# Combine all loaded evaluation data
full_df = pd.concat(dataframes, ignore_index=True).drop_duplicates()

# Create human-readable Task label (e.g., 'S -> W')
full_df["task_label"] = full_df["start"] + " → " + full_df["goal"]

# Aggregate metrics per delivery task across seeds
summary = full_df.groupby("task_label").agg(
    mean_steps=("mean_steps_success", "mean"),
    std_steps=("mean_steps_success", "std"),
    mean_return=("mean_return", "mean"),
    std_return=("mean_return", "std"),
    success_rate=("success_rate", "mean")
).reset_index()

# Set plot style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# --- Plot 1: Evaluation Steps to Goal by Task ---
plt.figure(figsize=(7, 4.5), dpi=300)
bars = plt.bar(summary["task_label"], summary["mean_steps"], color="#2b5c8f", width=0.5, edgecolor="black")

plt.ylabel("Mean Delivery Steps (Evaluation)", fontsize=11)
plt.xlabel("Delivery Task", fontsize=11)
plt.title("Q-Learning Policy Performance: Evaluation Path Length", fontsize=12, fontweight="bold")
plt.ylim(0, max(summary["mean_steps"]) + 5)

# Add exact value labels above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f"{int(yval)} steps", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig("eval_steps_by_task.png")
plt.close()

# --- Plot 2: Evaluation Mean Return by Task ---
plt.figure(figsize=(7, 4.5), dpi=300)
bars_ret = plt.bar(summary["task_label"], summary["mean_return"], color="#2e7d32", width=0.5, edgecolor="black")

plt.ylabel("Mean Episodic Return", fontsize=11)
plt.xlabel("Delivery Task", fontsize=11)
plt.title("Q-Learning Policy Performance: Mean Return", fontsize=12, fontweight="bold")
plt.ylim(0, max(summary["mean_return"]) + 6)

for bar in bars_ret:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f"{int(yval)}", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig("eval_return_by_task.png")
plt.close()

print("Successfully generated 'eval_steps_by_task.png' and 'eval_return_by_task.png'.")