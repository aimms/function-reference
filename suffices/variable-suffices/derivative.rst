.. _.Derivative:

.Derivative
===========

Definition
----------

    The variable suffix ``.Derivative`` contains the derivative values of a
    variable used in an external function which is again used inside a
    constraint. The ``.Derivative`` suffix is only applicable inside the
    ``derivative call`` attribute of external functions.

Datatype
--------

    The value of the ``.Derivative`` suffix is numeric.

Dimension
---------

    The dimension of the suffix ``.Derivative`` is the dimension of the
    external function plus the dimension of the variable. The domain of the
    suffix ``.Derivative`` is the domain of the external function followed
    by the domain of the variable.

.. note::

    -  See also :ref:`sec:intern.func.derivative` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
