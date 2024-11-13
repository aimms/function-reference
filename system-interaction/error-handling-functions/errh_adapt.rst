.. aimms:function:: errh::Adapt(err, severity, message, category, code)

.. _errh::Adapt:

errh::Adapt
===========

The procedure :aimms:func:`errh::Adapt` adapts an error with the specified
information.

.. code-block:: aimms

    errh::Adapt(
       err,       ! (input) an element
       severity,  ! (optional input) an element
       message,   ! (optional input) a string
       category,  ! (optional input) an element
       code       ! (optional input) an element 
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

    *severity*
        An element in the set :aimms:set:`errh::AllErrorSeverities`.

    *message*
        A string describing the problem and possibly suggestions for repairing
        the problem.

    *category*
        An element in the set :aimms:set:`errh::AllErrorCategories`, indicating the problem category to
        which the error belongs.

    *code*
        An element with root set :aimms:set:`errh::ErrorCodes`. The element will be added to the set
        :aimms:set:`errh::ErrorCodes` if needed.

Return Value
------------

    Returns 1 if adapting the error is successful, 0 otherwise. In the
    latter case additional error(s) have been raised.

.. note::

    When ``err`` does not reference an error in the set :aimms:set:`errh::PendingErrors` an
    additional error will be raised. If the current filter is the filter
    ``To Global Collector`` an additional error will be raised.


Example
-------

.. code-block:: aimms
    :linenos:

    block 
        pr_divideByZero();
    onerror _ep_err do
        errh::Adapt(
            err      :  _ep_err, 
            message  :  "Don't worry, be happy" );
    endblock ;

Lines 4-6 adapt the message of the error thrown by ``pr_divideByZero`` to ``"Don't worry, be happy"``

References
-----------

    *   :aimms:func:`errh::Severity` 
   
    *   :aimms:func:`errh::Message`

    *   :aimms:func:`errh::Category`

    *   :aimms:func:`errh::Code`



 