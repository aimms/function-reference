.. aimms:function:: errh::IsMarkedAsHandled(err)

.. _errh::IsMarkedAsHandled:

errh::IsMarkedAsHandled
=======================

The function :aimms:func:`errh::IsMarkedAsHandled` returns 1 if the error is
marked as handled and 0 otherwise.

.. code-block:: aimms

    errh::IsMarkedAsHandled(
            err   ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns 1 if the error is marked as handled and 0 otherwise.

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
        _bp_isMarkedAsHandled := errh::IsMarkedAsHandled(_ep_err );
        errh::MarkAsHandled( _ep_err, 1 );
    endblock ;



Afterwards:

.. code-block:: aimms

    _bp_isMarkedAsHandled = 0
    
Because the error is marked as handled just after.

.. seealso::

    The function :aimms:func:`errh::MarkAsHandled`.
