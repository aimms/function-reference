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

.. seealso::

    The procedure :aimms:func:`errh::Adapt`.
