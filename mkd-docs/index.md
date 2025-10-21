# pyDOE3: An experimental design package for Python

**pyDOE3 is fork of pyDOE2 which is a fork of pyDOE.**

As for `pyDOE2` wrt to `pyDOE`, `pyDOE3` came to life to solve 
bugs and issues that remained unsolved in `pyDOE2`.

The `pyDOE3` package is designed to help the 
**scientist, engineer, statistician,** etc., to construct appropriate 
**experimental designs**.

!!! tip "Quick Start"
    All available designs can be accessed after a simple import statement:
    
    ```python
    >>> from pyDOE3 import *
    ```

## Capabilities

The package currently includes functions for creating designs for any 
number of factors:

### [Factorial Designs](factorial.md)

1. [General Full-Factorial](factorial.md#general-full-factorial) (`fullfact`)
2. [2-Level Full-Factorial](factorial.md#2-level-full-factorial) (`ff2n`)
3. [2-Level Fractional-Factorial](factorial.md#2-level-fractional-factorial) (`fracfact`)
4. [Plackett-Burman](factorial.md#plackett-burman) (`pbdesign`)
5. [Generalized Subset Design](factorial.md#generalized-subset-design) (`gsd`)

### [Response Surface Designs](rsm.md)

1. [Box-Behnken](rsm.md#box-behnken) (`bbdesign`)
2. [Central-Composite](rsm.md#central-composite) (`ccdesign`)
3. [Doehlert Design](rsm.md#doehlert-design) (`doehlert_shell_design`, `doehlert_simplex_design`)

### [Randomized Designs](randomized.md)

1. [Latin-Hypercube](randomized.md#latin-hypercube) (`lhs`)
2. [Random K-Means](randomized.md#random-k-means) (`random_k_means`)
3. [Random Uniform](randomized.md#random-uniform) (`random_uniform`)

### [Low-Discrepancy Sequences](low_discrepancy_sequences.md)

1. [Sukharev Grid](low_discrepancy_sequences.md#sukharev-grid) (`sukharev_grid`)
2. [Sobol' Sequence](low_discrepancy_sequences.md#sobol-sequence) (`sobol_sequence`)
3. [Halton Sequence](low_discrepancy_sequences.md#halton-sequence) (`halton_sequence`)
4. [Rank-1 Lattice Design](low_discrepancy_sequences.md#rank1-lattice) (`rank1_lattice`)
5. [Korobov Sequence](low_discrepancy_sequences.md#korobov-sequence) (`korobov_sequence`)
6. [Cranley-Patterson Randomization](low_discrepancy_sequences.md#cranley-patterson) (`cranley_patterson_shift`)

### [Sampling Designs](sampling_designs.md)

1. [Morris Method](sampling_designs.md#morris-method) (`morris_sampling`)
2. [Saltelli Sampling](sampling_designs.md#saltelli-sampling) (`saltelli_sampling`)

### [Taguchi Designs](taguchi.md)

1. Orthogonal arrays and robust design utilities (`taguchi_design`, `compute_snr`)

### [Optimal Designs](doe_optimal.md)

1. Advanced optimal design algorithms (`optimal_design`)
2. Optimality criteria (`A`, `C`, `D`, `E`, `G`, `I`, `S`, `T`, `V`)
3. Search algorithms (`Sequential (Dykstra)`, `Simple Exchange (Wynn-Mitchell)`, `Fedorov`, `Modified Fedorov`, `DETMAX`)

## Requirements

- NumPy
- SciPy

## Installation

```bash
pip install --upgrade pyDOE3
```

or with Anaconda distribution

```bash
conda install -c conda-forge pydoe3
```

## Credits

This code was originally published by the following individuals for use with
Scilab:

- Copyright (C) 2012 - 2013 - Michael Baudin
- Copyright (C) 2012 - Maria Christopoulou
- Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
- Copyright (C) 2009 - Yann Collette
- Copyright (C) 2009 - CEA - Jean-Marc Martinez

pyDOE

- Copyright (c) 2014, Abraham D. Lee & tisimst

pyDOE2

- Copyright (c) 2018, Rickard Sjögren & Daniel Svensson

Much thanks goes to these individuals.

## License

This package is provided under The *BSD License* (3-Clause)

## References

- [Factorial designs](http://en.wikipedia.org/wiki/Factorial_experiment)
- [Plackett-Burman designs](http://en.wikipedia.org/wiki/Plackett-Burman_design)
- [Box-Behnken designs](http://en.wikipedia.org/wiki/Box-Behnken_design)
- [Central composite designs](http://en.wikipedia.org/wiki/Central_composite_design)
- [Latin-Hypercube designs](http://en.wikipedia.org/wiki/Latin_hypercube_sampling)
- [Taguchi designs](https://www.itl.nist.gov/div898/handbook/pri/section5/pri56.htm)
- [Optimal experimental design](https://en.wikipedia.org/wiki/Optimal_experimental_design)
- [Halton sequence](https://en.wikipedia.org/wiki/Halton_sequence)
- [Sobol' sequence](https://en.wikipedia.org/wiki/Sobol_sequence)
- [Cranley-Patterson method](https://doi.org/10.1137/0713071)

There is also a wealth of information on the [NIST](http://www.itl.nist.gov/div898/handbook/pri/pri.htm) website about the
various design matrices that can be created as well as detailed information
about designing/setting-up/running experiments in general.