.. aimms:set:: AllMatrixManipulationDirections

.. _AllMatrixManipulationDirections:

AllMatrixManipulationDirections
===============================

The predefined set :aimms:set:`AllMatrixManipulationDirections` contains the list
of optimization directions supported by the matrix manipulation library
of AIMMS.

.. code-block:: aimms

        Set AllMatrixManipulationDirections {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexMatrixManipulationDirections;
        }

Definition
----------

    The set :aimms:set:`AllMatrixManipulationDirections` contains the list of
    optimization directions supported by the matrix manipulation library of
    AIMMS.

Updatability
------------

    The contents of the set :aimms:set:`AllMatrixManipulationDirections` is
    completely under the control of AIMMS, and cannot be modified.

.. note::

    Element parameters into the set :aimms:set:`AllMatrixManipulationDirections` can
    be used as the *direction* argument of the :aimms:func:`GMP::Instance::SetDirection` function.

.. seealso::

    The set :aimms:set:`AllValueKeywords`, the function :aimms:func:`GMP::Instance::SetDirection`. Matrix manipulation is
    discussed in more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
