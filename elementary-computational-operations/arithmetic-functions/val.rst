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


Example
-----------

.. code-block:: aimms

    _s_nums := data { 1, '3.14' } ;
    _p_returnA := Val( first( _s_nums ) ); ! returns 1
    _p_returnB := Val( last( _s_nums ) ); ! returns  3.14
    _p_returnC := Val( "33"   ); ! returns  33
    _p_returnD := Val( "1.0e3"); ! returns  1000

.. note::

    If *str* cannot be interpreted as a numerical value, a runtime error may
    occur, see option ``suppress error messages of val function``.

.. seealso::

    - The :aimms:func:`Val` function is discussed in full detail in :ref:`sec:set-expr.elem.functions` of the Language Reference.
