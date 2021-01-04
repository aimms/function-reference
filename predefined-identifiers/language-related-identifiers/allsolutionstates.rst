.. aimms:set:: AllSolutionStates

.. _AllSolutionStates:

AllSolutionStates
=================

The predefined set :aimms:set:`AllSolutionStates` contains the names of possible
values of the program and solver status of a mathematical program.

.. code-block:: aimms

        Set AllSolutionStates {
            Index      :  IndexSolutionStates;
        }

Definition
----------

    The set :aimms:set:`AllSolutionStates` contains the names of all possible values
    of the ``ProgramStatus`` and ``SolverStatus`` suffixes of a mathematical
    program.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    The suffixes ``ProgramStatus`` and ``SolverStatus`` of a mathematical
    program take their values in the set :aimms:set:`AllSolutionStates`.

.. seealso::

    The program status and solver status are discussed in more detail in
    :doc:`optimization-modeling-components/solving-mathematical-programs/suffices-and-callbacks` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
