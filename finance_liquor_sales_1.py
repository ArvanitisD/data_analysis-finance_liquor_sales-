import pandas as pd
import matplotlib.pyplot as plt

# Φόρτωση των δεδομένων από το URL
df = pd.read_csv("https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv")

# Μετατροπή της στήλης 'date' σε αντικείμενο datetime
df["date"] = pd.to_datetime(df["date"])

# Εφαρμογή του φίλτρου για τα έτη και επαναφορά του index
filtered_df = df[(df["date"].dt.year >= 2016) & (df["date"].dt.year <= 2019)].reset_index()

# Έλεγχος πληροφοριών και ελλιπών τιμών
filtered_df.info()

# Ομαδοποίηση και άθροιση των πωληθέντων φιαλών
bottles_sold = filtered_df.groupby(["zip_code", "item_number"])["bottles_sold"].sum().reset_index()

# Εύρεση του δείκτη (index) του μέγιστου για κάθε ομάδα
idx = bottles_sold.groupby("zip_code")["bottles_sold"].idxmax()

# Επιλογή των γραμμών με τις μέγιστες πωλήσεις
max_bottles = bottles_sold.loc[idx].reset_index()

# Ταξινόμηση τιμών και επιλογή των κορυφαίων 20
sorted_values = max_bottles.sort_values(by="bottles_sold", ascending=False).head(20)

# Δημιουργία του γραφήματος
plt.figure(figsize=(12, 7))
plt.bar(sorted_values["zip_code"].astype(str), sorted_values["bottles_sold"], color="skyblue")
plt.xlabel("Ταχυδρομικός Κώδικας")
plt.ylabel("Πωληθείσες Φιάλες")
plt.title("Μέγιστες Πωλήσεις Φιαλών ανά Ταχυδρομικό Κώδικα")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()