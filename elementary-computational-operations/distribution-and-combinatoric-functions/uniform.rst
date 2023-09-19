.. aimms:function:: Uniform(Minimum, Maximum)

.. _Uniform:

Uniform
=======

The function :aimms:func:`Uniform` draws a random value from a uniform
distribution.

.. code-block:: aimms

    Uniform(
        Minimum,         ! (optional) numerical expression
        Maximum          ! (optional) numerical expression
        )

Arguments
---------

    *Minimum*
        A scalar numerical expression.

    *Maximum*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`Uniform` returns a random value drawn from a uniform
    distribution with lower bound *Minimum* and upper bound *Maximum*.

.. note::

    The arguments must satisfy the relation :math:`Minimum < Maximum`.

.. seealso::

    The :aimms:func:`Uniform` distribution is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/continuous-distributions`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
