.. aimms:function:: First(Set)

.. _First:

First
=====

With the function :aimms:func:`First` you can retrieve the first element from a
set.

.. code-block:: aimms

    First(
           Set,             ! (input) set reference
         )

Arguments
---------

    *Set*
        The set from which the first element is to be returned.

Return Value
------------

    The function First returns the first element of set *Set*.

.. note::

    If there is no element in *Set*, the function returns the empty element
    ``''`` instead.
