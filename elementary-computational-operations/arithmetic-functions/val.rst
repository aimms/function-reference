.. aimms:function:: Val(str)

.. _Val:

Val
===

.. code-block:: aimms

    Val(
        str    ! (input) string or element expression
       )

Arguments
---------

    *str*
        A scalar string or element expression.

Return Value
------------

    The function :aimms:func:`Val` returns the numerical value represented by the
    string or element *str*.

.. note::

    If *str* cannot be interpreted as a numerical value, a runtime error may
    occur, see option ``suppress error messages of val function``.

.. seealso::

    The :aimms:func:`Val` function is discussed in full detail in :ref:`sec:set-expr.elem.functions` of the
     Language Reference.
