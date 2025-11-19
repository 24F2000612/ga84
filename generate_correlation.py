# generate_correlation.py
# Author: Udghosh Rao
# Email: 24f2000612@ds.study.iitm.ac.in

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# ------------ Configuration ------------
INPUT_CSV = "supply_chain.csv"
OUT_CSV = "correlation.csv"
OUT_PNG = "heatmap.png"
OUT_PX = 500
DPI = 100.0
FIGSIZE = (OUT_PX / DPI, OUT_PX / DPI)
# ---------------------------------------

def load_data(path):
    return pd.read_csv(path)

def compute_correlation(df):
    numeric = df.select_dtypes(include=[np.number])
    corr = numeric.corr()
    corr.to_csv(OUT_CSV, index=True)
    return corr

def make_cmap():
    return LinearSegmentedColormap.from_list(
        "rgw",
        ["#b30000", "#ffffff", "#006600"]
    )

def save_heatmap(corr):
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    cmap = make_cmap()
    im = ax.imshow(corr.values, cmap=cmap, vmin=-1, vmax=1)

    labels = corr.columns.tolist()
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)

    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            ax.text(j, i, f"{corr.iat[i,j]:.2f}",
                    ha="center", va="center", color="black")

    plt.colorbar(im)
    plt.title("Correlation Matrix Heatmap")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=DPI)
    plt.close()

def main():
    df = load_data(INPUT_CSV)
    corr = compute_correlation(df)
    save_heatmap(corr)
    print("Files generated:")
    print(" - correlation.csv")
    print(" - heatmap.png")

if __name__ == "__main__":
    main()
