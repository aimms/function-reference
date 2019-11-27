.. aimms:set:: errh::PendingErrors

.. _errh::PendingErrors:

errh::PendingErrors
===================

The predefined set :aimms:set:`errh::PendingErrors` contains the error numbers of
the errors that can be processed by the current error filter.

.. code-block:: aimms

        Set PendingErrors {
            SubsetOf   :  Integers;
            Index      :  IndexPendingErrors;
        }

Updatability
------------

    The contents of this set cannot be modified. It is initialized when an
    error filter becomes active.
