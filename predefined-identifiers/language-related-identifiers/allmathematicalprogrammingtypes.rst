.. aimms:set:: AllMathematicalProgrammingTypes

.. _AllMathematicalProgrammingTypes:

AllMathematicalProgrammingTypes
===============================

The predefined set :aimms:set:`AllMathematicalProgrammingTypes` contains the list
of mathematical programming types supported by AIMMS.

.. code-block:: aimms

        Set AllMathematicalProgrammingTypes {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexMathematicalProgrammingTypes;
        }

Definition
----------

    The set :aimms:set:`AllMathematicalProgrammingTypes` contains the list of
    mathematical programming types supported by AIMMS.

Updatability
------------

    The contents of the set :aimms:set:`AllMathematicalProgrammingTypes` is
    completely under the control of AIMMS, and cannot be modified.

.. note::

    Element parameters into the set :aimms:set:`AllMathematicalProgrammingTypes` can
    be used in the declaration of mathematical programs or as part of the
    ``SOLVE`` statement to dynamically modify the type of a mathematical
    program. The predefined identifier :aimms:set:`CurrentSolver` defines the active solver
    for each mathematical programming type.

.. seealso::

    The set :aimms:set:`AllValueKeywords`, :aimms:set:`CurrentSolver`. Mathematical programs are discussed in
    full detail in Section 15.1 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, the ``SOLVE``
    statement in Section 15.3.
