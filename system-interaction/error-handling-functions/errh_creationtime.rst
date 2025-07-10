.. aimms:function:: errh::CreationTime(err, fmt)

.. _errh::CreationTime:

errh::CreationTime
==================

The function :aimms:func:`errh::CreationTime` returns the creation time of the
error.

.. code-block:: aimms

    errh::CreationTime(
            err,  ! (input) an element
            fmt   ! (optional) a format string.
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

    *fmt*
        A string that holds the date and time format used in the returned
        string. Valid format strings are described in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods` When this
        argument is not given, or if ``fmt`` is not a valid string format, the
        full reference date format "``%c%y-%m-%d %H:%M:%S``" will be
        used.

Return Value
------------

    Returns the creation time of the error as a string.

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
        _sp_crea := errh::CreationTime(_ep_err, "%c%y-%m-%d %H:%M:%S");
        errh::MarkAsHandled( _ep_err, 1 );
    endblock ;



.. seealso::

    The function :aimms:func:`CurrentToString`.
