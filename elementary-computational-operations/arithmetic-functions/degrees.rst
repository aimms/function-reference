.. aimms:function:: Degrees(x)

.. _Degrees:

Degrees
=======

.. code-block:: aimms

    Degrees(
           x             ! (input) numerical expression
           )

Arguments
---------

    *x*
        A scalar numerical expression.

Example
-----------------

.. code-block:: aimms

	_p_returnA := degrees(p_pi  ); ! degrees(pi)   = 180
	_p_returnB := degrees(p_pi/2); ! degrees(pi/2) =  90
	_p_returnC := degrees(   0  ); ! degrees(0)    =   0 
	_p_returnD := degrees(p_pi/4); ! degrees(pi/4) =  45  1



Return Value
------------

    The function :aimms:func:`Degrees` returns the value of *x* converted from radians
    to degrees.

.. note::

    The function :aimms:func:`Degrees` can be used in constraints of linear and
    nonlinear mathematical programs.

.. seealso::

    The function :aimms:func:`Radians`. Arithmetic functions are discussed in full
    detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
