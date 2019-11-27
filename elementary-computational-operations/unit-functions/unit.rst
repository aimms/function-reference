.. aimms:function:: Unit(unit)

.. _Unit:

Unit
====

The function :aimms:func:`Unit` returns the unit value of a given unit constant.

.. code-block:: aimms

    Unit(
         unit          ! (input) scalar unit constant
         )

Arguments
---------

    *unit*
        A unit constant of which the associated unit value must be computed

Return Value
------------

    The function returns the unit value of a unit constant *unit*.

.. note::

    The function :aimms:func:`Unit` simply returns its argument. It exists to allow
    the use of numeric constants in computed unit expressions.

.. seealso::

    Unit expressions discussed in full detail in Chapter 32 of the Language
    Reference.
