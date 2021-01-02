.. aimms:function:: EvaluateUnit(unit)

.. _EvaluateUnit:

EvaluateUnit
============

With the function :aimms:func:`EvaluateUnit` you can compute the numerical value
(with associated unit) of a given unit expression.

.. code-block:: aimms

    EvaluateUnit(
         unit                ! (input) scalar unit expression
         )

Arguments
---------

    *unit*
        A unit expression of which the numerical value (with associated unit)
        must be computed

Return Value
------------

    The function returns the numerical value (with associated unit),
    corresponding to one unit of *unit*.

.. note::

    The function :aimms:func:`EvaluateUnit` is an extension of AIMMS' local unit
    override capabilities which allows computed unit expressions.

.. seealso::

    Unit expressions are discussed in full detail in :doc:`advanced-language-components/units-of-measurement/index` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
