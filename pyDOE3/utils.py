"""
Utility functions for pyDOE3 package.

This module provides common utility functions used across different DOE methods,
including sample scaling, bounds checking, and other shared functionality.
"""

import numpy as np
from typing import List, Tuple

__all__ = ["scale_samples"]


def scale_samples(samples: np.ndarray, bounds: List[Tuple[float, float]]) -> np.ndarray:
    """
    Scale samples from [0, 1] to specified bounds.

    This utility function scales sample points from the unit hypercube [0, 1]^d
    to arbitrary bounds for each dimension. It can be used with any DOE method
    that generates samples in [0, 1].

    Parameters
    ----------
    samples : ndarray of shape (n_samples, n_vars)
        Sample matrix with values in [0, 1] range.
    bounds : list of tuple of float
        List of (min, max) bounds for each variable.
        Must be of length equal to samples.shape[1].

    Returns
    -------
    scaled_samples : ndarray of shape (n_samples, n_vars)
        Sample matrix scaled to the specified bounds.

    Examples
    --------
    >>> import numpy as np
    >>> from pyDOE3.utils import scale_samples
    >>> samples = np.array([[0.1, 0.2], [0.8, 0.9]])
    >>> bounds = [(-1, 1), (0, 10)]
    >>> scale_samples(samples, bounds)
    array([[-0.8,  2. ],
           [ 0.6,  9. ]])
    """
    samples = np.asarray(samples)
    bounds = np.asarray(bounds)

    if bounds.shape[0] != samples.shape[1]:
        raise ValueError(
            f"Number of bounds ({bounds.shape[0]}) must match number of variables "
            f"({samples.shape[1]})"
        )

    scaled_samples = np.empty_like(samples)
    for i, (low, high) in enumerate(bounds):
        if low >= high:
            raise ValueError(
                f"Invalid bounds for variable {i}: [{low}, {high}]. "
                "Lower bound must be less than upper bound."
            )
        scaled_samples[:, i] = samples[:, i] * (high - low) + low

    return scaled_samples
