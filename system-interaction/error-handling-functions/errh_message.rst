.. aimms:function:: errh::Message(err)

.. _errh::Message:

errh::Message
=============

The function :aimms:func:`errh::Message` returns a description of the error.

.. code-block:: aimms

    errh::Message(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns a string if the information is available and the empty string
    otherwise.

.. note::

    When ``err`` does not reference an element in CrossRef2or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.


Example
-------

.. code-block:: aimms
    :linenos:

    block 
        pr_divideByZero();
    onerror _ep_err do
        _sp_msg := errh::Message(_ep_err);
        errh::MarkAsHandled( _ep_err, 1 );
    endblock ;

Afterwards:

.. code-block:: aimms

    _sp_msg =  "Division by zero error with 1 / 0."

.. seealso::

    The procedure :aimms:func:`errh::Adapt`.
