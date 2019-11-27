.. aimms:set:: AllSolverSessionCompletionObjects

.. _AllSolverSessionCompletionObjects:

AllSolverSessionCompletionObjects
=================================

The predefined set :aimms:set:`AllSolverSessionCompletionObjects` is the root set
containing both ``AllGMPEvents`` and ``AllSolverSessions``.

.. code-block:: aimms

        Set AllSolverSessionCompletionObjects {
            Index        :  IndexSolverSessionCompletionObjects;
            Definition   :  AllGMPEvents + AllSolverSessions;
        }

Definition
----------

    The set ``AllExecutionStatuses`` is the root set containing both
    ``AllGMPEvents`` and ``AllSolverSessions``.

.. seealso::

    The predeclared identifiers :aimms:set:`AllGMPEvents` and :aimms:set:`AllSolverSessions`.
