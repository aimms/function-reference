.. aimms:function:: Sqrt(x)

.. _Sqrt:

Sqrt
====

.. code-block:: aimms

    Sqrt(
        x             ! (input) numerical expression
        )

Arguments
---------

    *x*
        A scalar numerical expression in the range :math:`[0,\infty)`.

Return Value
------------

    The function :aimms:func:`Sqrt` returns the :math:`\sqrt{x}`.

.. note::

    -  A run-time error results if *x* is outside the range
       :math:`[0,\infty)`.

    -  The function :aimms:func:`Sqrt` can be used in the constraints of nonlinear
       mathematical programs.

.. seealso::

    The functions :aimms:func:`Power`, :aimms:func:`Cube`, and :aimms:func:`Sqr`. Arithmetic functions
    are discussed in full detail in Section 6.1.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
