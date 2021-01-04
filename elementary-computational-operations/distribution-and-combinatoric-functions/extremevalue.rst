.. aimms:function:: ExtremeValue(location, scale)

.. _ExtremeValue:

ExtremeValue
============

The function :aimms:func:`ExtremeValue` draws a random value from an extreme value
distribution.

.. code-block:: aimms

    ExtremeValue(
           location,    ! (optional) numerical expression
           scale        ! (optional) numerical expression
           )

Arguments
---------

    *location*
        A scalar numerical expression.

    *scale*
        A scalar numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`ExtremeValue` returns a random value drawn from an
    extreme value distribution with location *location* and scale *scale*.

.. seealso::

    The :aimms:func:`ExtremeValue` distribution is discussed in full detail in
    :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
