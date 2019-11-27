.. aimms:function:: IdentifierElementRange(identifierName)

.. _IdentifierElementRange:

IdentifierElementRange
======================

The function :aimms:func:`IdentifierElementRange` returns the range as a set.

.. code-block:: aimms

    IdentifierElementRange(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllSymbols` specifying the
        identifier for which the range should be obtained.

Return Value
------------

    This function returns the set, as an element in :aimms:set:`AllSymbols`, that is the
    range of ``identifierName`` if it is element valued. If
    ``identifierName`` is not an identifier, an error message is issued. If
    ``identifierName`` is not element valued, the empty element is returned
    without further warning.

.. seealso::

    -  The functions :aimms:func:`DomainIndex`, :aimms:func:`IdentifierDimension`, and :aimms:func:`IndexRange`.

    -  Section 25.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The common example in :numref:`CommonModelQueryExample`.