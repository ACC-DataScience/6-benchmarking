import os
import warnings
from utils import set_seeds, ackley
import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties
import matplotlib.pyplot as plt
import pytest


@pytest.fixture(scope="session")
def get_namespace():
    script_fname = "benchmark_assignment_ans.py"
    script_content = open(script_fname).read()

    namespace = {}
    exec(script_content, namespace)
    return namespace


def test_task_a(get_namespace):

    running_ax_client_EI = get_namespace["ax_client_EI"]

    user_EI_traces = get_namespace["EI_traces"]
    assert user_EI_traces.shape == (10, 20), "EI_traces has the wrong shape"

    # assert that they aren't any zero rows
    assert not np.any(user_EI_traces == 0), "There are zero rows in EI_traces"

    # there isn't a way to query custom botorch_acqf_functions so IDK
    # assert (
    #     str(running_ax_client_EI.generation_strategy._model.model.botorch_acqf_class)
    #     == "ExpectedImprovement"
    # ), "The acquisition function is not set to ExpectedImprovement"


def test_task_b(get_namespace):

    running_ax_client_UCB = get_namespace["ax_client_UCB"]

    user_UCB_traces = get_namespace["UCB_traces"]
    assert user_UCB_traces.shape == (10, 20), "EI_traces has the wrong shape"

    # assert that they aren't any zero rows
    assert not np.any(user_UCB_traces == 0), "There are zero rows in EI_traces"

    # there isn't a way to query custom botorch_acqf_functions so IDK
    # assert (
    #     str(running_ax_client_UCB.generation_strategy._model.model.botorch_acqf_class)
    #     == "ExpectedImprovement"
    # ), "The acquisition function is not set to ExpectedImprovement"


def test_task_c(get_namespace):

    best_avg_performance = "EI"
    most_consistent = "EI"

    user_best_avg_performance = get_namespace["best_avg_performance"]
    user_most_consistent = get_namespace["most_consistent"]

    assert (
        user_best_avg_performance == best_avg_performance
    ), "Best avg performance is incorrect"
    assert user_most_consistent == most_consistent, "Most consistent is incorrect"


def test_task_d(get_namespace):

    user_avg_diff = get_namespace["avg_diff"]
    user_max_diff = get_namespace["max_diff"]

    avg_diff = 2.44
    max_diff = 5.29

    # assert that they are within 0.2
    assert np.abs(user_avg_diff - avg_diff) < 0.2, "Average difference is incorrect"
    assert np.abs(user_max_diff - max_diff) < 0.2, "Max difference is incorrect"


def test_task_e(get_namespace):

    running_ax_client_LEI = get_namespace["ax_client_LEI"]

    user_LEI_traces = get_namespace["LEI_traces"]
    assert user_LEI_traces.shape == (10, 20), "LEI_traces has the wrong shape"

    # assert that they aren't any zero rows
    assert not np.any(user_LEI_traces == 0), "There are zero rows in EI_traces"

    # there isn't a way to query custom botorch_acqf_functions so IDK
    # assert (
    #     str(running_ax_client_EI.generation_strategy._model.model.botorch_acqf_class)
    #     == "ExpectedImprovement"
    # ), "The acquisition function is not set to ExpectedImprovement"


def test_task_f(get_namespace):

    log_better = False

    user_log_better = get_namespace["log_better"]

    assert user_log_better == log_better, "log_better is incorrect"
