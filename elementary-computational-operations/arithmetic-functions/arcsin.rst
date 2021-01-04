.. aimms:function:: ArcSin(x)

.. _ArcSin:

ArcSin
======

.. code-block:: aimms

    ArcSin(
          x             ! (input) numerical expression
          )

Arguments
---------

    *x*
        A scalar numerical expression in the range :math:`[-1,1]`.

Return Value
------------

    The :aimms:func:`ArcSin` function returns the arcsine of *x* in the range
    :math:`-\pi/2` to :math:`\pi/2` radians.

.. note::

    -  A run-time error results if *x* is outside the range :math:`[-1,1]`.

    -  The function :aimms:func:`ArcSin` can be used in constraints of nonlinear
       mathematical programs.

.. seealso::

    The functions :aimms:func:`ArcCos`, :aimms:func:`ArcTan`, :aimms:func:`Sin`. Arithmetic functions are
    discussed in full detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
