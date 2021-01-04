.. _.RelaxationOnly:

.RelaxationOnly
===============

Definition
----------

    The constraint suffix ``.RelaxationOnly`` is an indicator to the solver
    ``Baron`` that this constraint should be included as a relaxation to the
    branch-and-bound algorithm, while it should be excluded from the local
    search.

Datatype
--------

    The value of the ``.RelaxationOnly`` suffix is an integer in the range
    {0,1} and the default is 0.

Dimension
---------

    The ``.RelaxationOnly`` suffix has the same dimension and domain as that
    of the constraint at hand.

.. note::

    -  See also :ref:`sec:var.constr.glob-suff` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
