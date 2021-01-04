.. aimms:function:: Pareto(Shape, Location, Scale)

.. _Pareto:

Pareto
======

The function :aimms:func:`Pareto` draws a random value from a Pareto distribution.

.. code-block:: aimms

    Pareto(
          Shape,           ! (input) numerical expression
          Location,        ! (optional) numerical expression
          Scale            ! (optional) numerical expression
          )

Arguments
---------

    *Shape*
        A scalar numerical expression :math:`> 0`.

    *Location*
        A scalar numerical expression.

    *Scale*
        A scalar numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`Pareto` returns a random value drawn from a Pareto
    distribution with shape *Shape*, location *Location* and scale *Scale*.

.. note::

    The prototype of this function has changed with the introduction of
    AIMMS 3.4. In order to run models that still use the original prototype,
    the option ``Distribution_compatibility`` should be set to
    ``Aimms_3_0``. The original function :aimms:func:`Pareto`\ (*s*, *beta*) returns a
    random value drawn from a Pareto distribution with shape *beta*,
    location :math:`0` and scale *s*.

.. seealso::

    The :aimms:func:`Pareto` distribution is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions` of
    the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
