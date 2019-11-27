.. aimms:set:: errh::ErrorCodes

.. _errh::ErrorCodes:

errh::ErrorCodes
================

The predefined set :aimms:set:`errh::ErrorCodes` contains the error codes of the
errors encountered during this AIMMS session.

.. code-block:: aimms

        Set ErrorCodes {
            Index      :  IndexErrorCodes;
        } 

Updatability
------------

    This set is grown during AIMMS error handling by storing the codes of
    all errors encountered.
