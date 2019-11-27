.. aimms:function:: StringToElement(Set, Name[, create])

.. _StringToElement:

StringToElement
===============

With the function :aimms:func:`StringToElement` you can convert a string into an
(existing) element of a set.

.. code-block:: aimms

    StringToElement(
         Set,             ! (input/output) a reference to a simple set
         Name,            ! (input) a scalar string
         [create]         ! (optional) 0 or 1, default 0
         )

Arguments
---------

    *Set*
        A set in which you want to find (or create) a specific element.

    *Name*
        A scalar string expression, representing the string that you want to
        convert.

    *create (optional)*
        An indicator whether or not a nonexisting element are added to the set
        during the call.

Return Value
------------

    The function returns the existing element or, if the string cannot be
    converted to an existing element and the argument *create* is not set to
    1, the function return the empty element. If *create* is set to 1,
    nonexisting elements will be created on the fly.

.. seealso::

    -  The function :aimms:func:`ElementCast` and the procedure :aimms:procedure:`SetElementAdd`.

    -  The lexical conventions for set elements in Section 2.3 of the
       `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
