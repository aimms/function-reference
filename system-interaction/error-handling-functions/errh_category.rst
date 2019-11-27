.. aimms:function:: errh::Category(err)

.. _errh::Category:

errh::Category
==============

The function :aimms:func:`errh::Category` returns the error category to which the
error belongs.

.. code-block:: aimms

    errh::Category(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns an element in :aimms:set:`errh::AllErrorCategories` if the information is available and the
    empty element otherwise.

.. note::

    When ``err`` does not reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The function :aimms:func:`errh::Code`, :aimms:func:`errh::InsideCategory`.
