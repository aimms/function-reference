.. aimms:function:: Normal(Mean, Deviation)

.. _Normal:

Normal
======

The function :aimms:func:`Normal` draws a random value from a normal distribution.

.. code-block:: aimms

    Normal(
        Mean,       ! (optional) numerical expression
        Deviation   ! (optional) numerical expression
        )

Arguments
---------

    *Mean*
        A scalar numerical expression.

    *Deviation*
        A scalar numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`Normal` returns a random value drawn from a normal
    distribution with mean *Mean* and standard deviation *Deviation*.

.. seealso::

    The :aimms:func:`Normal` distribution is discussed in full detail in Appendix A of
    the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
