from typing import Tuple
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import scripts.interpretation_methods as interpretation_methods
import scripts.calc_strategies_methods as calculate_strategies_methods


def remove_days(df: pd.DataFrame, days: int) -> pd.DataFrame:
    cutoff_date = datetime.now() - timedelta(days=days)
    return df[df["time"] < cutoff_date]


def calculate_history_data(data: pd.DataFrame, shape: int) -> np.ndarray:
    previous_day = None
    array = np.zeros((shape, 4, 3))

    for i in range(shape):
        data = remove_days(data, i)

        if not data.empty:
            if data.iloc[-1]["time"] == previous_day:
                continue
            else:
                previous_day = data.iloc[-1]["time"]

        strategies = calculate_strategies_methods.calculate_strategies(data=data)

        signals_buy, signals_sell, signals_hold = (
            calculate_strategies_methods.calculate_signals(
                data=data, strategies=strategies
            )
        )

        calculate_strategies_methods.interpret_strategies_result(
            signals_buy=signals_buy,
            signals_sell=signals_sell,
            signals_hold=signals_hold,
        )

        array[i][0] = interpretation_methods.percentage_method_values(
            signals_buy, signals_sell, signals_hold
        )
        array[i][1] = interpretation_methods.additive_method(
            signals_buy, signals_sell, signals_hold
        )
        array[i][2] = interpretation_methods.majority_vote_method(
            signals_buy, signals_sell, signals_hold
        )
        array[i][3] = interpretation_methods.median_method(
            signals_buy, signals_sell, signals_hold
        )

    # filer empty data
    mask = np.all(array == 0, axis=(1, 2))
    array = array[~mask]
    return array[::-1], array.shape[0]


def create_linear_chart(array: np.ndarray, shape: int, show: bool) -> None:
    y = np.linspace(1, shape, shape)

    # setup dark mode
    plt.style.use("dark_background")

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # buy chart
    axs[0].plot(
        y, array[:, 0, 0], color="green", linestyle="-", linewidth=2, label="BUY"
    )
    axs[0].scatter(y, array[:, 0, 0], color="green", marker="o")
    axs[0].set_ylim(-1, 101)
    axs[0].set_title("BUY HISTORY (%)", color="white")
    axs[0].set_xlabel("Index", color="white")
    axs[0].set_ylabel("Value", color="white")
    axs[0].axhline(
        y=50, color="grey", linestyle="--", linewidth=2, alpha=0.5, label="50%"
    )
    axs[0].legend(loc="best")

    # sell chart
    axs[1].plot(
        y, array[:, 0, 1], color="red", linestyle="-", linewidth=2, label="SELL"
    )
    axs[1].scatter(y, array[:, 0, 1], color="red", marker="o")
    axs[1].set_ylim(-1, 101)
    axs[1].set_title("SELL HISTORY (%)", color="white")
    axs[1].set_xlabel("Index", color="white")
    axs[1].set_ylabel("Value", color="white")
    axs[1].axhline(
        y=50, color="grey", linestyle="--", linewidth=2, alpha=0.5, label="50%"
    )
    axs[1].legend(loc="best")

    # hold chart
    axs[2].plot(
        y, array[:, 0, 2], color="grey", linestyle="-", linewidth=2, label="HOLD"
    )
    axs[2].scatter(y, array[:, 0, 2], color="grey", marker="o")
    axs[2].set_ylim(-1, 101)
    axs[2].set_title("HOLD HISTORY (%)", color="white")
    axs[2].set_xlabel("Index", color="white")
    axs[2].set_ylabel("Value", color="white")
    axs[2].axhline(
        y=50, color="grey", linestyle="--", linewidth=2, alpha=0.5, label="50%"
    )
    axs[2].legend(loc="best")

    # setup charts colors
    for ax in axs:
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")

    plt.tight_layout()
    if show:
        plt.show()

    fig.savefig("charts\\linear_chart.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def create_subplots_colors(
    array: np.ndarray, shape: int
) -> Tuple[np.array, np.array, np.array]:
    additive_data = array[:, 1]
    majority_vote = array[:, 2]
    median_data = array[:, 3]
    additive_colors = np.full(shape, " ", dtype="<U5")
    majority_vote_colors = np.full(shape, " ", dtype="<U5")
    median_colors = np.full(shape, " ", dtype="<U5")

    for i, (adi, maj, med) in enumerate(zip(additive_data, majority_vote, median_data)):
        if adi[0] == 1:
            additive_colors[i] = "green"
        elif adi[1] == 1:
            additive_colors[i] = "red"
        else:
            additive_colors[i] = "grey"

        if maj[0] == 1:
            majority_vote_colors[i] = "green"
        elif maj[1] == 1:
            majority_vote_colors[i] = "red"
        else:
            majority_vote_colors[i] = "grey"

        if med[0] == 1:
            median_colors[i] = "green"
        elif med[1] == 1:
            median_colors[i] = "red"
        else:
            median_colors[i] = "grey"

    return additive_colors, majority_vote_colors, median_colors


def create_all_linear_chart(array: np.ndarray, shape: int, show: bool) -> None:
    x = np.linspace(1, shape, shape)
    plt.style.use("dark_background")

    fig = plt.figure(figsize=(15, 8))
    gs = fig.add_gridspec(4, 1, height_ratios=[6, 1, 1, 1])

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[1, 0])
    ax2 = fig.add_subplot(gs[2, 0])
    ax3 = fig.add_subplot(gs[3, 0])

    additive_colors, majority_vote_colors, maximum_pessimism_colors = (
        create_subplots_colors(array, shape)
    )

    ax0.plot(
        x, array[:, 0, 0], color="green", linestyle="-", linewidth="2", label="BUY"
    )
    ax0.scatter(x, array[:, 0, 0], color="green", marker="o")
    ax0.plot(x, array[:, 0, 1], color="red", linestyle="-", linewidth="2", label="SELL")
    ax0.scatter(x, array[:, 0, 1], color="red", marker="o")
    ax0.plot(
        x, array[:, 0, 2], color="grey", linestyle="-", linewidth="2", label="HOLD"
    )
    ax0.scatter(x, array[:, 0, 2], color="grey", marker="o")
    ax0.axhline(y=50, color="grey", linestyle="--", linewidth=2, alpha=0.5, label="50%")
    ax0.set_title("BUY & SELL & HOLD HISTORY (%) WITH DECISION", color="white")
    ax0.legend(loc="best")
    ax0.set_xticks([])
    ax0.set_yticks([])
    ax0.set_xticklabels([])
    ax0.set_yticklabels([])

    for ax in [ax1, ax2, ax3]:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])

    y = np.linspace(0, 0, shape)
    ax1.set_ylim(-1, 1)
    ax1.scatter(x, y, color=additive_colors, marker="H", s=110)
    ax1.set_title("Additive decision method", color="white")

    ax2.set_ylim(-1, 1)
    ax2.scatter(x, y, color=majority_vote_colors, marker="H", s=110)
    ax2.set_title("Majority vote decision method", color="white")

    ax3.set_ylim(-1, 1)
    ax3.scatter(x, y, color=maximum_pessimism_colors, marker="H", s=110)
    ax3.set_title("Median decision method", color="white")

    plt.subplots_adjust(left=0.04, right=0.96, top=0.94, bottom=0.06)

    if show:
        plt.show()

    fig.savefig("charts\\all_linear_chart.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def create_histogram_chart(array: np.ndarray, show: bool) -> None:
    indices = np.arange(array.shape[0])
    plt.style.use("dark_background")
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # buy chart
    axs[0].bar(indices, array[:, 0, 0], color="green", edgecolor="black", label="BUY")
    axs[0].set_title("BUY HISTORY (%)", color="white")
    axs[0].set_xlabel("Index", color="white")
    axs[0].set_ylabel("Value", color="white")
    axs[0].set_ylim(0, 100)
    axs[0].axhline(
        y=50, color="grey", linestyle="--", linewidth=2, alpha=0.5, label="50%"
    )
    axs[0].legend(loc="best")

    # sell chart
    axs[1].bar(indices, array[:, 0, 1], color="red", edgecolor="black", label="SELL")
    axs[1].set_title("SELL HISTORY (%)", color="white")
    axs[1].set_xlabel("Index", color="white")
    axs[1].set_ylabel("Value", color="white")
    axs[1].set_ylim(0, 100)
    axs[1].axhline(
        y=50, color="grey", linestyle="--", linewidth=2, alpha=0.5, label="50%"
    )
    axs[1].legend(loc="best")

    # hold chart
    axs[2].bar(indices, array[:, 0, 2], color="grey", edgecolor="black", label="HOLD")
    axs[2].set_title("HOLD HISTORY (%)", color="white")
    axs[2].set_xlabel("Index", color="white")
    axs[2].set_ylabel("Value", color="white")
    axs[2].set_ylim(0, 100)
    axs[2].axhline(
        y=50, color="grey", linestyle="--", linewidth=2, alpha=0.5, label="50%"
    )
    axs[2].legend(loc="best")

    # setup charts colors
    for ax in axs:
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")

    plt.tight_layout()
    if show:
        plt.show()

    fig.savefig("charts\\histogram_chart.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
