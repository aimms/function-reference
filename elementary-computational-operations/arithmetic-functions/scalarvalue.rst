.. aimms:function:: ScalarValue(identifier, suffix)

.. _ScalarValue:

ScalarValue
===========

.. code-block:: aimms

    ScalarValue(
        identifier,   ! (input) element expression into AllIdentifiers
        suffix        ! (optional) element expression into AllSuffixNames
       )

Arguments
---------

    *identifier*
        A scalar element expression into :aimms:set:`AllIdentifiers`

    *suffix*
        A scalar element expression into :aimms:set:`AllSuffixNames`

Return Value
------------

    The function :aimms:func:`ScalarValue` returns the value contained in the scalar
    identifier *identifier* or scalar reference *identifier.suffix*.

.. note::

    When *identifier* or *identifier.suffix* is not a scalar numerical
    valued reference, the function :aimms:func:`ScalarValue` returns 0.0.

.. seealso::

    The function :aimms:func:`Val`. The :aimms:func:`ScalarValue` function is a function that
    operates on subsets of :aimms:set:`AllIdentifiers`. Other functions that operate on
    subsets of :aimms:set:`AllIdentifiers` are referenced in :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the Language
    Reference.
