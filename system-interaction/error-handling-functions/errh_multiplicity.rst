.. aimms:function:: errh::Multiplicity(err)

.. _errh::Multiplicity:

errh::Multiplicity
==================

The function :aimms:func:`errh::Multiplicity` returns the number of occurrences of
this error.

.. code-block:: aimms

    errh::Multiplicity(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns the number of occurrences of this error.

.. note::

    When ``err`` does not reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.


Example
-------

.. code-block:: aimms
    :linenos:

    block 
        pr_divideByZero();
    onerror _ep_err do
        _p_mult := errh::Multiplicity(_ep_err);
        errh::MarkAsHandled( _ep_err, 1 );
    endblock ;


Afterwards:

.. code-block:: aimms

    _p_mult = 1

.. seealso::

    The functions :aimms:func:`errh::Code`, :aimms:func:`errh::Category`, :aimms:func:`errh::Message` and :aimms:func:`errh::Severity`.
