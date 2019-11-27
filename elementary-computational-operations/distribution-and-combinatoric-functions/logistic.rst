.. aimms:function:: Logistic(Location, Scale)

.. _Logistic:

Logistic
========

The function :aimms:func:`Logistic` draws a random value from a logistic
distribution.

.. code-block:: aimms

    Logistic(
             Location,    ! (optional) numerical expression
             Scale        ! (optional) numerical expression
             )

Arguments
---------

    *Location*
        A scalar numerical expression.

    *Scale*
        A scalar numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`Logistic` returns a random value drawn from a logistic
    distribution with mean *Location* and scale *Scale*.

.. seealso::

    The :aimms:func:`Logistic` distribution is discussed in full detail in Appendix A
    of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
