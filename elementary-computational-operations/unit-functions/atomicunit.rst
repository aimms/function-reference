.. aimms:function:: AtomicUnit(unit)

.. _AtomicUnit:

AtomicUnit
==========

With the function :aimms:func:`AtomicUnit` you can retrieve the atomic unit
expression corresponding to the unit expression passed as the argument
to the function.

.. code-block:: aimms

    AtomicUnit(
         unit                ! (input) scalar unit expression
         )

Arguments
---------

    *unit*
        A unit expression of which the associated atomic unit expression must be
        computed

Return Value
------------

    The function returns the atomic unit expression corresponding to *unit*.

.. note::

    The atomic unit expression associated with a given unit is the unit
    expression solely in terms of atomic unit symbols by which the given
    unit differs a constant scale factor only.

.. seealso::

    Unit expressions are discussed in full detail in :doc:`advanced-language-components/units-of-measurement/index` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
