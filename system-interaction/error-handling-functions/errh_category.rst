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


Example
-------

.. code-block:: aimms
    :linenos:

	block 
		pr_divideByZero();
	onerror _ep_err do
		_ep_cat := errh::Category(_ep_err);
		errh::MarkAsHandled( _ep_err, 1 );
	endblock ;

Afterwards:

.. code-block:: aimms

	_ep_cat = 'Math'
	
.. seealso::

    The function :aimms:func:`errh::Code`, :aimms:func:`errh::InsideCategory`.
