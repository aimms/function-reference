.. aimms:function:: ErrorF(x)

.. _ErrorF:

ErrorF
======

.. code-block:: aimms

    ErrorF(
           x             ! (input) numerical expression
           )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`ErrorF` returns the error function value
    :math:`{\frac{1}{\sqrt{2\pi}}} \int_{-\infty}^x e^{-{\frac{t^2}{2}}}\, dt`.

.. note::

    The function :aimms:func:`ErrorF` can be used in constraints of nonlinear
    mathematical programs.

.. seealso::

    Arithmetic functions are discussed in full detail in Section 6.1.4 of
    the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
