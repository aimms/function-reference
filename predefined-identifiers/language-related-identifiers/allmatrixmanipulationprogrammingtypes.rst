.. aimms:set:: AllMatrixManipulationProgrammingTypes

.. _AllMatrixManipulationProgrammingTypes:

AllMatrixManipulationProgrammingTypes
=====================================

The predefined set :aimms:set:`AllMatrixManipulationProgrammingTypes` contains
the collection of mathematical programming types that can be used in
conjunction with the GMP library of AIMMS.

.. code-block:: aimms

        Set AllMatrixManipulationProgrammingTypes {
            SubsetOf   :  AllMathematicalProgrammingTypes;
            Index      :  IndexMatrixManipulationProgrammingTypes;
        }

Definition
----------

    The predefined set :aimms:set:`AllMatrixManipulationProgrammingTypes` contains
    the collection of mathematical programming types that can be used in
    conjunction with the GMP library of AIMMS.

Updatability
------------

    The contents of the set :aimms:set:`AllMatrixManipulationProgrammingTypes` is
    completely under the control of AIMMS, and cannot be modified.

.. note::

    Element parameters into the set :aimms:set:`AllMatrixManipulationDirections` can
    be used as the *type* argument of the :aimms:func:`GMP::Instance::SetMathematicalProgrammingType` function.

.. seealso::

    The set :aimms:set:`AllMathematicalProgrammingTypes`, the function :aimms:func:`GMP::Instance::SetMathematicalProgrammingType`. The GMP library is
    discussed in more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
