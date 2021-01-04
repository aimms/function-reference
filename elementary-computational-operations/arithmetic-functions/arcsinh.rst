.. aimms:function:: ArcSinh(x)

.. _ArcSinh:

ArcSinh
=======

.. code-block:: aimms

    ArcSinh(
           x             ! (input) numerical expression
           )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The :aimms:func:`ArcSinh` function returns the inverse hyperbolic sine of *x* in
    the range from :math:`-\infty` to :math:`\infty`.

.. note::

    The function :aimms:func:`ArcSinh` can be used in constraints of nonlinear
    mathematical programs.

.. seealso::

    The functions :aimms:func:`ArcCosh`, :aimms:func:`ArcTanh`, :aimms:func:`Sinh`. Arithmetic functions are
    discussed in full detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
