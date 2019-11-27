.. aimms:function:: errh::Filename(err)

.. _errh::Filename:

errh::Filename
==============

The function :aimms:func:`errh::Filename` returns the file in which the error
occurred during reading from file

.. code-block:: aimms

    errh::Filename(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns a string containing the filename in which the error occurred, if
    that error occurred during reading from file and the empty string
    otherwise.

.. note::

    When ``err`` does not reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The functions :aimms:func:`errh::Line` and :aimms:func:`errh::Column`.
