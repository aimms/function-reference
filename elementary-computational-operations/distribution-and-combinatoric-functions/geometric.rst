.. aimms:function:: Geometric(ProbabilityOfSuccess)

.. _Geometric:

Geometric
=========

The function :aimms:func:`Geometric` draws a random value from a geometric
distribution.

.. code-block:: aimms

    Geometric(
       ProbabilityOfSuccess    ! (input) numerical expression
             )

Arguments
---------

    *ProbabilityOfSuccess*
        A scalar numerical expression in the range :math:`(0,1)`.

Return Value
------------

    The function :aimms:func:`Geometric` returns a random value drawn from a geometric
    distribution with a probability of success *ProbabilityOfSuccess*.

.. seealso::

    The :aimms:func:`Geometric` distribution is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
