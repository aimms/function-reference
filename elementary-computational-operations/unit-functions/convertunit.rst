.. aimms:function:: ConvertUnit(unit, convention)

.. _ConvertUnit:

ConvertUnit
===========

With the function :aimms:func:`ConvertUnit` you can compute the associated unit
value of a unit expression with respect to a given convention.

.. code-block:: aimms

    ConvertUnit(
         unit,                ! (input) scalar unit expression
         convention           ! (input) element expression
         )

Arguments
---------

    *unit*
        A unit expression of which the associated unit value in the given
        convention must be computed

    *convention*
        An element expression in to :aimms:set:`AllConventions`, representing the convention with
        respect to which a unit value must be computed.

Return Value
------------

    The function returns the associated unit value of *unit* with respect to
    *convention*.

.. seealso::

    Unit expressions and conventions are discussed in full detail in :doc:`advanced-language-components/units-of-measurement/index`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
