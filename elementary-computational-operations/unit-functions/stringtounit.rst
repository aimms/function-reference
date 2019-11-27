.. aimms:function:: StringToUnit(str)

.. _StringToUnit:

StringToUnit
============

With the function :aimms:func:`StringToUnit` you can compute a unit value
corresponding to a given string expression.

.. code-block:: aimms

    StringToUnit(
         str          ! (input) scalar string expression
         )

Arguments
---------

    *str*
        A string expression of which the associated unit value must be computed

Return Value
------------

    The function returns the associated unit value of *str*, or fails if the
    given string does not correspond to a string constant.

.. seealso::

    Unit expressions discussed in full detail in Chapter 32 of the Language
    Reference.
