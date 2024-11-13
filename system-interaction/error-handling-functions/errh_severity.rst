.. aimms:function:: errh::Severity(err)

.. _errh::Severity:

errh::Severity
==============

The function :aimms:func:`errh::Severity` returns the severity of the error.

.. code-block:: aimms

    errh::Severity(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns an element in :aimms:set:`errh::AllErrorSeverities` if the information is available and the
    empty element otherwise.

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
        _ep_sev := errh::severity(_ep_err);
        errh::MarkAsHandled( _ep_err, 1 );
    endblock ;



Afterwards:

.. code-block:: aimms

    _ep_sev = 'error'
 
.. seealso::

    The procedures :aimms:func:`errh::Adapt` and :aimms:func:`errh::MarkAsHandled`.
