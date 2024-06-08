.. aimms:function:: Max(x1,x2,...)

.. _Max:

Max
===

.. code-block:: aimms

    Max(
        x1,      ! (input) numerical, string or element expression
        x2,      ! (input) numerical, string or element expression
        ...
        )

* The **Function** ``Max``, returns the maximum of its arguments.
* Not to be confused with the **iterative operator**, ``Max``, which returns the maximum of all values iterated over. 


Arguments
---------

    *x1,x2,...*
        Multiple numerical, string or element expressions.

Return Value
------------

    The function :aimms:func:`Max` returns the largest number, the string highest in
    the lexicographical ordering, or the element value with the highest
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

    _p_maxFunc := max( _p_values( 'John' ), _p_values( 'Jack' ) ); ! returns 4
    _p_maxIter := max( _i_name, _p_values( _i_name ) ); ! returns 4

    ! For elements, ordering is based on their positions in the set.
    _ep_maxFunc := max( _ep_name1, _ep_name2 ); ! returns 'Jack'.
    _ep_maxIter := max( _i_name, _i_name ); ! returns 'Jack'.

    ! For string, ordering is the lexicographic ordering.
    _sp_maxFunc := max( _sp_name1, _sp_name2 ); ! returns "John"
    _sp_maxIter := max( _i_name, _sp_names(_i_name) );  ! returns "John"



.. note::

    The function :aimms:func:`Max` can be used in constraints of nonlinear
    mathematical programs. However, nonlinear solvers may experience
    convergence problems if the first order derivatives of two arguments
    between which the :aimms:func:`Max` function switches are discontinous.

.. seealso::

    The function :aimms:func:`Min`. Arithmetic functions are discussed in full
    detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
