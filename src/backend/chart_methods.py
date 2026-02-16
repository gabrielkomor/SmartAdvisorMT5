"""
This file is responsible for creating an interactive candlestick chart that is used in the main application window
when analyzing historical data.
"""

from typing import Dict

import plotly.graph_objs as go
import pandas as pd


def add_sma_10_indicator_to_chart(
    fig: go.Figure, ohlc_data: pd.DataFrame, strategies: Dict
) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :param strategies: data.
    :return: nothing, only creates new indicator on chart.
    """
    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["sma_10_data"],
            mode="lines",
            name="SMA 10",
            line=dict(color="yellow", width=2),
            hoverinfo="x+y+text",
            visible="legendonly",
        )
    )


def add_sma_20_indicator_to_chart(
    fig: go.Figure, ohlc_data: pd.DataFrame, strategies: Dict
) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :param strategies: data.
    :return: nothing, only creates new indicator on chart.
    """
    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["sma_20_data"],
            mode="lines",
            name="SMA 20",
            line=dict(color="blue", width=2),
            hoverinfo="x+y+text",
            visible="legendonly",
        )
    )


def add_sma_30_indicator_to_chart(
    fig: go.Figure, ohlc_data: pd.DataFrame, strategies: Dict
) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :param strategies: data.
    :return: nothing, only creates new indicator on chart.
    """
    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["sma_30_data"],
            mode="lines",
            name="SMA 30",
            line=dict(color="brown", width=2),
            hoverinfo="x+y+text",
            visible="legendonly",
        )
    )


def add_bb_indicator_to_chart(
    fig: go.Figure, ohlc_data: pd.DataFrame, strategies: Dict
) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :param strategies: data.
    :return: nothing, only creates new indicator on chart.
    """
    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["bb_upper"],
            mode="lines",
            name="Upper BB",
            line=dict(color="red", width=1, dash="dash"),
            visible="legendonly",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["bb_lower"],
            mode="lines",
            name="Lower BB",
            line=dict(color="red", width=1, dash="dash"),
            visible="legendonly",
        )
    )


def add_rsi_indicator_to_chart(
    fig: go.Figure, ohlc_data: pd.DataFrame, strategies: Dict
) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :param strategies: data.
    :return: nothing, only creates new indicator on chart.
    """
    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["rsi"],
            mode="lines",
            name="RSI",
            line=dict(color="purple", width=2),
            visible="legendonly",
        )
    )


def add_macd_indicator_to_chart(
    fig: go.Figure, ohlc_data: pd.DataFrame, strategies: Dict
) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :param strategies: data.
    :return: nothing, only creates new indicator on chart.
    """
    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["macd_line"],
            mode="lines",
            name="MACD",
            line=dict(color="orange", width=2),
            visible="legendonly",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["macd_signal_line"],
            mode="lines",
            name="MACD SL",
            line=dict(color="grey", width=2),
            visible="legendonly",
        )
    )

    fig.add_trace(
        go.Bar(
            x=ohlc_data["time"],
            y=strategies["macd_line"] - strategies["macd_signal_line"],
            name="MACD Hist",
            marker=dict(
                color=(strategies["macd_line"] - strategies["macd_signal_line"]).apply(
                    lambda x: "green" if x > 0 else "red"
                )
            ),
            visible="legendonly",
        )
    )


def add_adx_indicator_to_chart(
    fig: go.Figure, ohlc_data: pd.DataFrame, strategies: Dict
) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :param strategies: data.
    :return: nothing, only creates new indicator on chart.
    """
    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["adx"],
            mode="lines",
            name="ADX",
            line=dict(color="blue", width=2),
            visible="legendonly",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["adx_pdi"],
            mode="lines",
            name="DI+",
            line=dict(color="green", width=2),
            visible="legendonly",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=ohlc_data["time"],
            y=strategies["adx_ndi"],
            mode="lines",
            name="DI-",
            line=dict(color="red", width=2),
            visible="legendonly",
        )
    )


def add_volume_indicator_to_chart(fig: go.Figure, ohlc_data: pd.DataFrame) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :return: nothing, only creates new indicator on chart.
    """
    fig.add_trace(
        go.Bar(
            y=ohlc_data["tick_volume"],
            name="Volume",
            x=ohlc_data["time"],
            marker_color="rgba(1, 1, 1, 1.0)",
            opacity=1,
            yaxis="y2",
            visible="legendonly",
        )
    )


def add_fibonacci_levels_indicator_to_chart(
    fig: go.Figure, ohlc_data: pd.DataFrame, strategies: Dict
) -> None:
    """
    This function is responsible for add indicator into interactive chart.
    :param fig: current chart.
    :param ohlc_data: data.
    :param strategies: data.
    :return: nothing, only creates new indicator on chart.
    """
    time_range = ohlc_data["time"]
    legend_group_name = "Fib Lvls"

    for i, (price, fibo) in enumerate(
        zip(strategies["fibo_lvl"], strategies["levels"])
    ):
        fig.add_trace(
            go.Scatter(
                x=time_range,
                y=[price] * len(time_range),
                mode="lines",
                name=legend_group_name if i == 0 else None,
                legendgroup=legend_group_name,
                showlegend=True if i == 0 else False,
                line=dict(dash="dash", width=1.5, color="lightgrey"),
                visible="legendonly",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[ohlc_data["time"].iloc[1]],
                y=[price],
                mode="text",
                text=[f"{fibo}%"],
                textposition="middle left",
                legendgroup=legend_group_name,
                showlegend=False,
                visible="legendonly",
            )
        )


def create_html_chart(
    ohlc_data: pd.DataFrame,
    file_path: str,
    name: str,
    strategies: Dict,
    time_breaks: int,
) -> None:
    """
    This function is responsible for creating interactive chart in html format.
    :param ohlc_data: data
    :param file_path: path
    :param name: chart name.
    :param strategies: data.
    :param time_breaks: data.
    :return: nothing, only creates chart.
    """
    # Creating a candlestick chart
    fig = go.Figure(
        data=[
            go.Candlestick(
                name="Chart",
                x=ohlc_data["time"],
                open=ohlc_data["Open"],
                high=ohlc_data["High"],
                low=ohlc_data["Low"],
                close=ohlc_data["Close"],
            )
        ]
    )

    # Adding indicators
    add_sma_10_indicator_to_chart(fig=fig, ohlc_data=ohlc_data, strategies=strategies)
    add_sma_20_indicator_to_chart(fig=fig, ohlc_data=ohlc_data, strategies=strategies)
    add_sma_30_indicator_to_chart(fig=fig, ohlc_data=ohlc_data, strategies=strategies)
    add_bb_indicator_to_chart(fig=fig, ohlc_data=ohlc_data, strategies=strategies)
    add_rsi_indicator_to_chart(fig=fig, ohlc_data=ohlc_data, strategies=strategies)
    add_macd_indicator_to_chart(fig=fig, ohlc_data=ohlc_data, strategies=strategies)
    add_adx_indicator_to_chart(fig=fig, ohlc_data=ohlc_data, strategies=strategies)
    add_volume_indicator_to_chart(fig=fig, ohlc_data=ohlc_data)
    add_fibonacci_levels_indicator_to_chart(
        fig=fig, ohlc_data=ohlc_data, strategies=strategies
    )

    # calculating the maximum volume value to the correct scale
    max_tick_volume = round(ohlc_data["tick_volume"].max() * 6.5)

    # styles
    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="rgba(30, 30, 30, 1)",
        font=dict(color="white"),
        xaxis=dict(
            gridcolor="gray", zerolinecolor="white", showline=True, linecolor="white"
        ),
        yaxis=dict(
            gridcolor="gray", zerolinecolor="white", showline=True, linecolor="white"
        ),
    )

    # Added hiding of non-trading hours and days
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Price",
        yaxis2=dict(
            title="Volume",
            overlaying="y",
            side="right",
            showgrid=False,
            range=[0, max_tick_volume],
        ),
        xaxis=dict(
            rangeslider_visible=True,
            rangebreaks=[dict(bounds=["sat", "mon"])]
            + (
                [dict(bounds=[23.01, 16.5], pattern="hour")]
                if time_breaks == 1  # M1
                else (
                    [dict(bounds=[23.08, 16.5], pattern="hour")]
                    if time_breaks == 2  # M5
                    else (
                        [dict(bounds=[23.2, 16.5], pattern="hour")]
                        if time_breaks == 3  # M15
                        else (
                            [dict(bounds=[23.5, 16.5], pattern="hour")]
                            if time_breaks == 4  # M30
                            else (
                                [dict(bounds=[24, 16], pattern="hour")]
                                if time_breaks == 5  # H1
                                else (
                                    [dict(bounds=[22, 14], pattern="hour")]
                                    if time_breaks == 6  # H3
                                    else (
                                        [dict(bounds=[21, 9], pattern="hour")]
                                        if time_breaks == 7  # H6
                                        else []
                                    )
                                )
                            )
                        )
                    )
                )
            ),
        ),
        yaxis=dict(
            tickformat=".2f",
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        dragmode="drawline",
        modebar_add=["drawline", "drawrect", "eraseshape"],
    )

    fig.write_html(file_path)
