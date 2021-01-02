.. _.Stochastic:

.Stochastic
===========

Definition
----------

    When the property ``Stochastic`` of a parameter or variable is set, the
    ``.Stochastic`` suffix contains the stochastic data of that parameter or
    variable. When the definition of a constraint contains a parameter or
    variable with the ``Stochastic`` property set the ``.Stochastic`` suffix
    of that constraint contains the stochastic rows.

Datatype
--------

    The value of the ``.Stochastic`` suffix is numeric.

Dimension
---------

    The dimension of ``.Stochastic`` suffix is one higher than that of the
    identifier at hand. The domain of the ``.Stochastic`` suffix is prefixed
    with the set :aimms:set:`AllStochasticScenarios` to the domain of the identifier at hand. The
    index domain of the ``.Stochastic`` suffix is prefixed with the index
    ``IndexStochasticScenarios`` to the index domain of the identifier at
    hand.

.. note::

    -  See also :doc:`optimization-modeling-components/stochastic-programming/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
