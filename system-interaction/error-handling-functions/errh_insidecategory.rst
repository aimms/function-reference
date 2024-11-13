.. aimms:function:: errh::InsideCategory(err, cat)

.. _errh::InsideCategory:

errh::InsideCategory
====================

The function :aimms:func:`errh::InsideCategory` returns 1 if the error is inside
the given category.

.. code-block:: aimms

    errh::InsideCategory(
            err,  ! (input) an element
            cat   ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

    *cat*
        An element in the set :aimms:set:`errh::AllErrorCategories` referencing an error.

Return Value
------------

    Returns 1 if ``err`` in inside the category ``cat`` and 0 otherwise.

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
        _bp_insideCat := errh::InsideCategory(_ep_err, 'Solver' );
        errh::MarkAsHandled( _ep_err, 1 );
    endblock ;


Afterwards:

.. code-block:: aimms

    _bp_insideCat = 0

Because the error is unrelated to a solver.

.. seealso::

    The functions :aimms:func:`errh::Code` and :aimms:func:`errh::Category`.
