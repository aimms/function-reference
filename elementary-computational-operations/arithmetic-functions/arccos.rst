.. aimms:function:: ArcCos(x)

.. _ArcCos:

ArcCos
======

.. code-block:: aimms

    ArcCos(
          x             ! (input) numerical expression
          )

Arguments
---------

    *x*
        A scalar numerical expression in the range :math:`[-1,1]`.

Return Value
------------

    The :aimms:func:`ArcCos` function returns the arccosine of *x* in the range 0 to
    :math:`\pi` radians.

.. note::

    -  A run-time error results if *x* is outside the range :math:`[-1,1]`.

    -  The function :aimms:func:`ArcCos` can be used in constraints of nonlinear
       mathematical programs.

.. seealso::

    The functions :aimms:func:`ArcSin`, :aimms:func:`ArcTan`, :aimms:func:`Cos`. Arithmetic functions are
    discussed in full detail in Section 6.1.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
