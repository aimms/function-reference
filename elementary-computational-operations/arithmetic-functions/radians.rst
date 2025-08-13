.. aimms:function:: Radians(x)

.. _Radians:

Radians
=======

.. code-block:: aimms

    Radians(
           x             ! (input) numerical expression
           )

Arguments
---------

    *x*
        A scalar numerical expression.

Example
-----------------

.. code-block:: aimms

	_p_returnA := radians(180); ! radians(180) = pi
	_p_returnB := radians( 90); ! radians( 90) = pi/2
	_p_returnC := radians(  0); ! radians(  0) = 0
	_p_returnD := radians( 45); ! radians( 45) = pi/4

Return Value
------------

    The function :aimms:func:`Radians` returns the value of *x* converted from degrees
    to radians.

.. note::

    The function :aimms:func:`Radians` can be used in constraints of linear and
    nonlinear mathematical programs.

.. seealso::

    - The function :aimms:func:`Degrees`. 
    - Arithmetic functions are discussed in full detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
