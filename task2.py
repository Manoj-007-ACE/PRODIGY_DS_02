import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(r"C:\prodigy_task2\Titanic-Dataset.csv")

# DATA CLEANING
df["Age"].fillna(df["Age"].median(), inplace=True)
df.drop(columns=["Cabin"], inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df.drop(columns=["PassengerId", "Name", "Ticket"], inplace=True)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

print("Cleaning Done! Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

sns.set_style("whitegrid")

# Plot 1: Survival Count
plt.figure(figsize=(7, 5))
ax = sns.countplot(x="Survived", data=df, palette=["#E24B4A", "#1D9E75"])
ax.bar_label(ax.containers[0], fontsize=12, fontweight="bold")
plt.title("Survival Count", fontsize=15, fontweight="bold")
plt.xticks([0, 1], ["Did Not Survive", "Survived"], fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task2\plot1_survival_count.png", dpi=150)
plt.show()
print("Plot 1 saved!")

# Plot 2: Survival by Gender
plt.figure(figsize=(7, 5))
ax = sns.countplot(x="Sex", hue="Survived", data=df, palette=["#E24B4A", "#1D9E75"])
ax.bar_label(ax.containers[0], fontsize=11)
ax.bar_label(ax.containers[1], fontsize=11)
plt.title("Survival by Gender", fontsize=15, fontweight="bold")
plt.xticks([0, 1], ["Male", "Female"], fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)
plt.legend(["Did Not Survive", "Survived"], fontsize=11)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task2\plot2_survival_gender.png", dpi=150)
plt.show()
print("Plot 2 saved!")

# Plot 3: Survival by Class
plt.figure(figsize=(7, 5))
ax = sns.countplot(x="Pclass", hue="Survived", data=df, palette=["#E24B4A", "#1D9E75"])
ax.bar_label(ax.containers[0], fontsize=11)
ax.bar_label(ax.containers[1], fontsize=11)
plt.title("Survival by Passenger Class", fontsize=15, fontweight="bold")
plt.xticks([0, 1, 2], ["1st Class", "2nd Class", "3rd Class"], fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)
plt.legend(["Did Not Survive", "Survived"], fontsize=11)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task2\plot3_survival_class.png", dpi=150)
plt.show()
print("Plot 3 saved!")

# Plot 4: Age Distribution
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x="Age", hue="Survived", bins=30, palette=["#E24B4A", "#1D9E75"], alpha=0.7)
plt.title("Age Distribution by Survival", fontsize=15, fontweight="bold")
plt.xlabel("Age", fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)
plt.legend(["Did Not Survive", "Survived"], fontsize=11)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task2\plot4_age_distribution.png", dpi=150)
plt.show()
print("Plot 4 saved!")

# Plot 5: Fare by Class
plt.figure(figsize=(10, 5))
sns.boxplot(x="Pclass", y="Fare", data=df, palette="Blues")
plt.title("Fare Distribution by Passenger Class", fontsize=15, fontweight="bold")
plt.xticks([0, 1, 2], ["1st Class", "2nd Class", "3rd Class"], fontsize=12)
plt.xlabel("Passenger Class", fontsize=12)
plt.ylabel("Fare", fontsize=12)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task2\plot5_fare_class.png", dpi=150)
plt.show()
print("Plot 5 saved!")

# Plot 6: Correlation Heatmap
plt.figure(figsize=(9, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, square=True)
plt.title("Correlation Heatmap", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig(r"C:\prodigy_task2\plot6_heatmap.png", dpi=150)
plt.show()
print("Plot 6 saved!")

print("\nAll 6 plots saved!")
print("\nKey Insights:")
print(f"Overall Survival Rate: {df['Survived'].mean()*100:.1f}%")
print(f"Female Survival Rate: {df[df['Sex']==1]['Survived'].mean()*100:.1f}%")
print(f"Male Survival Rate: {df[df['Sex']==0]['Survived'].mean()*100:.1f}%")
print(f"1st Class Survival Rate: {df[df['Pclass']==1]['Survived'].mean()*100:.1f}%")
print(f"3rd Class Survival Rate: {df[df['Pclass']==3]['Survived'].mean()*100:.1f}%")