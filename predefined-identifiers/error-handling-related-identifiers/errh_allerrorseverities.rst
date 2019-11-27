.. aimms:set:: errh::AllErrorSeverities

.. _errh::AllErrorSeverities:

errh::AllErrorSeverities
========================

The predefined set :aimms:set:`errh::AllErrorSeverities` contains the error
categories that can be assigned to an error.

.. code-block:: aimms

        Set AllErrorSeverities {
            Index      :  IndexErrorSeverities;
        }

The names below are the elements in the set.

severe
   A severe internal error is an error that has occurred in the AIMMS
   logic itself.

error
   A normal error which indicates a situation from which normally
   execution shouldn't continue.

warning
   Something that should be looked at, but doesn't necessarily indicate
   a problem. %

informational
   Summarizing information that might be of interest. %

detail
   Detailed information.

Updatability
------------

    The contents of this set cannot be modified.
