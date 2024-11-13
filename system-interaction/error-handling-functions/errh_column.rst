.. aimms:function:: errh::Column(err)

.. _errh::Column:

errh::Column
============

The function :aimms:func:`errh::Column` returns the column number within the line
in the file in which the error occured during reading from file.

.. code-block:: aimms

    errh::Column(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns a column number if the information is available and 0 otherwise.

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
        _p_col := errh::Column(_ep_err);
        errh::MarkAsHandled( _ep_err, 1 );
    endblock ;


Afterwards:

.. code-block:: aimms

    _p_col = 11

.. seealso::

    The functions :aimms:func:`errh::Line` and :aimms:func:`errh::Filename`.
