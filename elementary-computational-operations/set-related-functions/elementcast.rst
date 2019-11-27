.. aimms:function:: ElementCast(set, element[, create])

.. _ElementCast:

ElementCast
===========

With the function :aimms:func:`ElementCast` you can cast an element of one set to
an (existing) element with the same name in a set with a different root
set.

.. code-block:: aimms

    ElementCast(
         set,             ! (input) a set expression
         element,         ! (input) a scalar element expression
         [create]         ! (optional) 0 or 1
         )

Arguments
---------

    *set*
        A set in which you want to find a specific element name.

    *element*
        A scalar element expression, representing the element that you want to
        convert to a different root set hierarchy.

    *create (optional)*
        An indicator whether or not a nonexisting element are added to the set
        during the call.

Return Value
------------

    The function returns the existing element or, if the element cannot be
    converted to an existing element and the argument *create* is not set to
    1, the function returns the empty element. If *create* is set to 1,
    nonexisting elements will be created on the fly.

.. seealso::

    The procedure :aimms:procedure:`SetElementAdd`.
