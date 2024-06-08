.. aimms:function:: Min(x1,x2,...)

.. _Min:

Min
===

.. code-block:: aimms

    Min(
        x1,      ! (input) numerical, string or element expression
        x2,      ! (input) numerical, string or element expression
        ..
        )

* The **Function** ``Min``, returns the minimum of its arguments.
* Not to be confused with the **iterative operator**, ``Min``, which returns the minimum of all values iterated over. 


Arguments
---------

    *x1,x2,*:math:`\dots`
        Multiple numerical, string or element expressions.


Return Value
------------

    The function :aimms:func:`Min` returns the smallest number, the string lowest in
    the lexicographical ordering, or the element value with the lowest
    ordinal value, among :math:`x1,x2,\dots`


Example
-----------

.. code-block:: aimms


    _s_names := data { John, Jack } ;
    _p_values(_i_name) := data { John : 3, Jack : 4 } ;
    _ep_name1 := 'John' ;
    _ep_name2 := 'Jack' ;

    _sp_name1 := formatString("%e", _ep_name1);
    _sp_name2 := formatString("%e", _ep_name2);
    _sp_names(_i_name) := formatString("%e", _i_name);

    ! For elements, ordering is based on their positions in the set.
    _p_minFunc := min( _p_values( 'John' ), _p_values( 'Jack' ) ); ! returns 3
    _p_minIter := min( _i_name, _p_values( _i_name ) ); ! returns 3

    ! For strings, ordering is the lexicographic ordering.
    _ep_minFunc := min( _ep_name1, _ep_name2 ); ! returns 'John'.
    _ep_minIter := min( _i_name, _i_name ); ! returns 'John'.

    _sp_minFunc := min( _sp_name1, _sp_name2 ); ! returns "Jack"
    _sp_minIter := min( _i_name, _sp_names(_i_name) );  ! returns "Jack"



.. note::

    The function :aimms:func:`Min` can be used in constraints of nonlinear
    mathematical programs. However, nonlinear solvers may experience
    convergence problems if the first order derivatives of two arguments
    between which the :aimms:func:`Min` function switches are discontinous.

.. seealso::

    The function :aimms:func:`Max`. Arithmetic functions are discussed in full
    detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
