.. aimms:set:: AllExecutionStatuses

.. _AllExecutionStatuses:

AllExecutionStatuses
====================

The predefined set :aimms:set:`AllExecutionStatuses` contains the names of all
execution statuses associated with asynchronous solves.

.. code-block:: aimms

        Set AllExecutionStatuses {
            Index        :  IndexExecutionStatus;
        }

Definition
----------

    The set :aimms:set:`AllExecutionStatuses` contains the names of all execution
    statuses associated with asynchronous solves. The execution status of an
    asynchronous solve can be queried using the function
    ``GMP::SolverSession::ExecutionStatus``.

.. seealso::

    The function :aimms:func:`GMP::SolverSession::ExecutionStatus`.
