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
    discussed in full detail in Section 6.1.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
