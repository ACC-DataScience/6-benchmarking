# 6. Benchmarking Acquisition Functions

Perform benchmarking to compare the optimization performance of expected
improvement (EI) vs. upper confidence bound (UCB) acquisition functions.

## The Assignment

Practitioners are often interested in comparing the relative performance of different
acquisition functions in Bayesian optimization problems. The success of a particular
acquisition function can depend on the problem at hand, the model being used, and the
nature of the problem's constraints.

In this assignment, you will compare the performance of two acquisition functions,
Expected Improvement (EI) and Upper Confidence Bound (UCB), on the synthetic Ackley
optimization problem. To get a sense for random seed sensitivity, you will run 10 full
optimization campaigns with each acquisition function using different random seeds.
From these, you will be able to get a sense of average performance and variance of
each acquisition function.

The Ackley function is a common benchmark function used in optimization that takes in
two input variables and has a global minimum at (0, 0). A python implementation of the
function is provided in the utils file and is imported for convenience. The bounds
for both input variables are [-32.768, 32.768].

Your goal is to use Honegumi and your knowledge of the Ax API to perform benchmarking
on the Ackley function using the EI and UCB acquisition functions over 10 optimization
campaigns. For each campaign, you will run 5 Sobol iterations and 20 iterations with
the respective aquisition function.

### **TASK A:** Run 10 optimization campaigns with ExpectedImprovement.

Now you will construct a loop that runs 10 optimization campaigns with the Expected
Improvement acquisition function. You will want to specify a custom generation strategy
that specifies Sobol iterations and BOTORCH_MODULAR model iteratons. BOTORCH_MODULAR
takes in a `model_kwargs` varibale with an option for "botorch_acqf_class" for setting
the acquisition function.

Ax, by default, prints a lot of information. You can suppress this by passing
verbose_logging=False to AxClient.

An example of how to specify such models is provided in the snippet below:

```python
...
    GenerationStep(
        model=Generators.BOTORCH_MODULAR,
        num_trials=-1,
        max_parallelism=3,
        model_kwargs={"botorch_acqf_class": qKnowledgeGradient},
    ),
...
```

### **TASK B:** Run 10 optimization campaigns with UpperConfidenceBound.

As above you will run another 10 optimization campaigns, this time with the Upper
Confidence Bound acquisition function.

### **TASK C:** Compare the performance of the two acquisition functions.

Visualize the performance of the two acquisition functions by plotting the mean and
standard deviation of the objective function over the 10 optimization campaigns for
each acquisition function. You can use np.minimum.accumulate() to produce the "trace"
of each campaign prior to taking the average and standard deviation. After plotting
both traces on the same plot, observe the behavior of each. Create two variables named
`best_avg_performance` and `most_consistent` and assign either "EI" or "UCB" to each
based on what you observe.

### **TASK D:** Report average and maximum difference in the average performances.

Using the average performance traces, compute the the average difference in the
average performances of each acquisition function and assign it to a variable named
`avg_diff`. Next, compute the maximum difference in the average performances of each
acquisition function and assign it to a variable named `max_diff`.

### **TASK E:** Comparing LogExpectedImprovement 

A [paper](https://arxiv.org/abs/2310.20708) (Jan 2024) showed that taking the
logarithm of the Expected Improvement acquisition function yields better
performance on certain optimization problems. We are interested in seeing how it
compares on the Ackley function. Run 10 optimization campaigns with the
`LogExpectedImprovement` acquisition function.

### **TASK F:** Did LogExpectedImprovement perform better?

Visualize the performance of the LogExpectedImprovement acquisition function on the
same plot as the other two acquisition functions. Observe whether LogEI performed
better or worss and assign either True or False to a variable named `log_better`.

## Setup command

See `postCreateCommand` from [`devcontainer.json`](.devcontainer/devcontainer.json).

## Run command
`pytest`

## Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be inaccessible.
