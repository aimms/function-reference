.. aimms:function:: Element(Set, n)

.. _Element:

Element
=======

With the function :aimms:func:`Element` you can retrieve the :math:`n`-th element
from a set.

.. code-block:: aimms

    Element(
           Set,           ! (input) set reference
           n              ! (input) integer expression
           )

Arguments
---------

    *Set*
        The set from which an element is to be returned.

    *n*
        An integer expression indicating the ordinal number of the element to be
        returned.

Return Value
------------

    The function Element returns the :math:`n`-th element of set *Set*.

.. note::

    If there is no :math:`n`-th element in *Set*, the function returns the
    empty element ``''`` instead.
