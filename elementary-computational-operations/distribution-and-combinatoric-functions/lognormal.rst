.. aimms:function:: LogNormal(Shape, Lowerbound, Scale)

.. _LogNormal:

LogNormal
=========

The function :aimms:func:`LogNormal` draws a random value from a lognormal
distribution.

.. code-block:: aimms

    LogNormal(
        Shape,        ! (input) numerical expression
        Lowerbound,   ! (optional) numerical expression
        Scale         ! (optional) numerical expression
        )

Arguments
---------

    *Shape*
        A scalar numerical expression :math:`> 0`.

    *Lowerbound*
        A scalar numerical expression.

    *Scale*
        A scalar numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`LogNormal` returns a random value drawn from a lognormal
    distribution with shape *Shape*, lower bound *Lowerbound* and scale
    *Scale*.

.. note::

    The prototype of this function has changed with the introduction of
    AIMMS 3.4. In order to run models that still use the original prototype,
    the option ``Distribution_compatibility`` should be set to
    ``Aimms_3_0``. The original function :aimms:func:`LogNormal`\ (*m*, *sd*) returns
    a random value drawn from a lognormal distribution with mean :math:`m>0`
    and standard deviation :math:`sd>0`. The same result should now be
    obtained by setting :math:`Shape = sd/m`, :math:`Lowerbound=0` and
    :math:`Scale = m`.

.. seealso::

    The :aimms:func:`LogNormal` distribution is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
