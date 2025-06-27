# ======================================================================================
# ASSIGNMENT 6: Benchmarking Acquisition Functions

# Your goal is to use Honegumi and your knowledge of the Ax API to perform
# benchmarking on the Ackley function using the EI and UCB acquisition functions
# over 10 optimization campaigns. For each campaign, you will run 5 Sobol
# iterations and 20 iterations with the respective aquisition function. Refer to
# the README for specifics regarding each task.
# ======================================================================================

from utils import set_seeds, ackley

set_seeds()  # setting the random seed for reproducibility

# --------------------------------------------------------------------------------------
# TASK A: Run 10 optimization campaigns with ExpectedImprovement.
# --------------------------------------------------------------------------------------

import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties
from ax.modelbridge.factory import Generators
from ax.generation_strategy.generation_strategy import GenerationStep, GenerationStrategy
from botorch.acquisition import ExpectedImprovement

seed_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

EI_traces = np.zeros((len(seed_list), 20))

for seed in seed_list:

    gs = GenerationStrategy(
        # TODO: Your Code Goes Here
    )

    ax_client_EI = AxClient(verbose_logging=False, random_seed=seed)

    # TODO: Your Code Goes Here


# --------------------------------------------------------------------------------------
# TASK B: Run 10 optimization campaigns with UpperConfidenceBound.
# --------------------------------------------------------------------------------------
import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties
from ax.modelbridge.factory import Generators
from ax.generation_strategy.generation_strategy import GenerationStep, GenerationStrategy
from botorch.acquisition import UpperConfidenceBound

seed_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

UCB_traces = np.zeros((len(seed_list), 20))

for seed in seed_list:

    gs = GenerationStrategy(
        # TODO: Your Code Goes Here
    )

    ax_client_UCB = AxClient(verbose_logging=False, random_seed=seed)

    # TODO: Your Code Goes Here


# --------------------------------------------------------------------------------------
# TASK C: Compare the performance of the two acquisition functions.
# --------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK D: Report average and maximum difference in the average performances.
# --------------------------------------------------------------------------------------

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK E: Comparing LogExpectedImprovement
# --------------------------------------------------------------------------------------

import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties
from ax.modelbridge.factory import Generators
from ax.generation_strategy.generation_strategy import GenerationStep, GenerationStrategy
from botorch.acquisition import LogExpectedImprovement

seed_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

LEI_traces = np.zeros((len(seed_list), 20))

for seed in seed_list:

    gs = GenerationStrategy(
        # TODO: Your Code Goes Here
    )

    ax_client_LEI = AxClient(verbose_logging=False, random_seed=seed)

    # TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK F: Did LogExpectedImprovement perform better?
# --------------------------------------------------------------------------------------

# TODO: Your Code Goes Here
