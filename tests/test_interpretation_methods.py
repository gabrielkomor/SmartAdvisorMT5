import pytest
import numpy as np

from scripts.interpretation_methods import (
    additive_method,
    majority_vote_method,
    median_method,
    percentage_method_values,
)


@pytest.mark.parametrize(
    "sig_buy, sig_sell, sig_hold, result",
    [
        (np.array([0]), np.array([0.1]), np.array([0.9]), np.array([0, 0, 1])),
        (
            np.array([0.3, 0.1]),
            np.array([0.5, 0.4]),
            np.array([0.2, 0.5]),
            np.array([0, 1, 0]),
        ),
        (
            np.array([0.7, 0.4, 0.6]),
            np.array([0.3, 0.1, 0]),
            np.array([0, 0.5, 0.4]),
            np.array([1, 0, 0]),
        ),
        (
            np.array([0.1, 0.1, 0.5, 0]),
            np.array(
                [
                    0.5,
                    0.5,
                    0,
                    1,
                ]
            ),
            np.array([0.4, 0.4, 0.5, 0]),
            np.array([0, 1, 0]),
        ),
    ],
)
def test_additive_method(
    sig_buy: np.ndarray, sig_sell: np.ndarray, sig_hold: np.ndarray, result: np.ndarray
):
    """
    This function is used to test the correctness of the additive method function.
    :param sig_buy: buy signals.
    :param sig_sell: sell signals.
    :param sig_hold: hold signals.
    :param result: expected function result.
    :return: Nothing, only provides tests.
    """
    assert np.allclose(additive_method(sig_buy, sig_sell, sig_hold), result)


@pytest.mark.parametrize(
    "signals_buy, signals_sell, signals_hold, result",
    [
        (
            np.array([0.1, 0.4, 0.6, 1]),
            np.array([0.3, 0.1, 0, 0]),
            np.array([0.6, 0.5, 0.4, 0]),
            np.array([1, 0, 0]),
        ),
        (
            np.array([0.3, 0.1, 0, 0]),
            np.array([0.5, 0.4, 0.6, 1]),
            np.array([0.2, 0.5, 0.4, 0]),
            np.array([0, 1, 0]),
        ),
        (
            np.array([0, 0.4, 0.7, 0.3]),
            np.array([0, 0, 0, 0]),
            np.array([1, 0.6, 0.3, 0.7]),
            np.array([0, 0, 1]),
        ),
    ],
)
def test_majority_vote_method(
    signals_buy: np.ndarray,
    signals_sell: np.ndarray,
    signals_hold: np.ndarray,
    result: np.ndarray,
):
    assert np.allclose(
        majority_vote_method(signals_buy, signals_sell, signals_hold), result
    )


@pytest.mark.parametrize(
    "signals_buy, signals_sell, signals_hold, result",
    [
        (
            np.array([0, 0.4, 0.6, 1]),
            np.array([0.3, 0.1, 0, 0]),
            np.array([0.7, 0.5, 0.4, 0]),
            np.array([1, 0, 0]),
        ),
        (
            np.array([0.3, 0.1, 0, 0]),
            np.array([0.5, 0.4, 0.6, 1]),
            np.array([0.2, 0.5, 0.4, 0]),
            np.array([0, 1, 0]),
        ),
        (
            np.array([0, 0.4, 0.7, 0.3]),
            np.array([0, 0, 0, 0]),
            np.array([1, 0.6, 0.3, 0.7]),
            np.array([0, 0, 1]),
        ),
    ],
)
def test_median_method(
    signals_buy: np.ndarray,
    signals_sell: np.ndarray,
    signals_hold: np.ndarray,
    result: np.ndarray,
):
    assert np.allclose(median_method(signals_buy, signals_sell, signals_hold), result)


@pytest.mark.parametrize(
    "signals_buy, signals_sell, signals_hold, result",
    [
        (
            np.array([0, 0.4, 0.6, 1]),
            np.array([0.3, 0.1, 0, 0]),
            np.array([0.7, 0.5, 0.4, 0]),
            np.array([50, 10, 40]),
        ),
        (
            np.array([0.3, 0.1, 0, 0]),
            np.array([0.5, 0.4, 0.6, 1]),
            np.array([0.2, 0.5, 0.4, 0]),
            np.array([10, 62.5, 27.5]),
        ),
        (
            np.array([0, 0.4, 0.7, 0.3]),
            np.array([0, 0, 0, 0]),
            np.array([1, 0.6, 0.3, 0.7]),
            np.array([35, 0, 65]),
        ),
    ],
)
def test_percentage_method_values(
    signals_buy: np.ndarray,
    signals_sell: np.ndarray,
    signals_hold: np.ndarray,
    result: np.ndarray,
):
    assert np.allclose(
        percentage_method_values(signals_buy, signals_sell, signals_hold), result
    )
