.. aimms:function:: SetAsString(set)

.. _SetAsString:

SetAsString
===========

With the function :aimms:func:`SetAsString` you can cast a set expression to a string.

.. code-block:: aimms

    SetAsString(
         set             ! (input) a set expression
         )

Arguments
---------

    *set*
        A set for which you want to get a string representation.

Return Value
------------

    The function returns the string representation of the given set, 
    being elements of the set separated by commas and enclosed in curly brackets.
    If the set is empty then the strings is just curly brackets, like so : aimms:token:`{}`.


.. note::

    This function is available since AIMMS version 4.89.
    
    Implicit cast from a set expression to a string is decommissioned since AIMMS version 4.89 and will result in a compile error in a future AIMMS version.
    SetAsString function is intended to be used instead.
