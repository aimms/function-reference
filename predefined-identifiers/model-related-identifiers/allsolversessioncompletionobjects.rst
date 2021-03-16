.. aimms:set:: AllSolverSessionCompletionObjects

.. _AllSolverSessionCompletionObjects:

AllSolverSessionCompletionObjects
=================================

The predefined set :aimms:set:`AllSolverSessionCompletionObjects` is the root set
containing both :aimms:set:`AllGMPEvents` and :aimms:set:`AllSolverSessions`.

.. code-block:: aimms

        Set AllSolverSessionCompletionObjects {
            Index        :  IndexSolverSessionCompletionObjects;
            Definition   :  AllGMPEvents + AllSolverSessions;
        }

Definition
----------

    The set :aimms:set:`AllExecutionStatuses` is the root set containing both
    :aimms:set:`AllGMPEvents` and :aimms:set:`AllSolverSessions`.

.. seealso::

    The predeclared identifiers :aimms:set:`AllGMPEvents` and :aimms:set:`AllSolverSessions`.
