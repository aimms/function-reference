.. aimms:function:: Last(Set)

.. _Last:

Last
====

With the function :aimms:func:`Last` you can retrieve the last element from a set.

.. code-block:: aimms

    Last(
           Set,             ! (input) set reference
        )

Arguments
---------

    *Set*
        The set from which the last element is to be returned.

Return Value
------------

    The function Last returns the last element of set *Set*.

.. note::

    If there is no element in *Set*, the function returns the empty element
    ``''`` instead.
