.. aimms:set:: AllViolationTypes

.. _AllViolationTypes:

AllViolationTypes
=================

The predefined set :aimms:set:`AllViolationTypes` contains the collection of all
violation types for which violation penalties can be specified in a
mathematical program declaration.

.. code-block:: aimms

        Set AllViolationTypes {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexViolationTypes;
            Definition :  data { Lower, Upper, Definition };
        }

Definition
----------

    The set :aimms:set:`AllViolationTypes` contains the violation types for which
    violation penalties can be specified in a mathematical program
    declaration.

Updatability
------------

    The contents of the set :aimms:set:`AllViolationTypes` is completely under the
    control of AIMMS, and cannot be modified.

.. note::

    The set :aimms:set:`AllViolationTypes` is typically used in the index domain of
    identifiers specified in the ``ViolationPenalties`` attribute of a
    ``MathematicalProgram``.

.. seealso::

    The sets :aimms:set:`AllMathematicalProgrammingTypes`, :aimms:set:`AllMatrixManipulationDirections`, :aimms:set:`ContinueAbort`, :aimms:set:`DiskWindowVoid`, :aimms:set:`MaximizingMinimizing`,
    :aimms:set:`MergeReplace`, :aimms:set:`OnOff`. The ``ViolationPenalties`` attribute of a
    mathematical programs is discussed in Section 15.4 of the Language
    Reference.
