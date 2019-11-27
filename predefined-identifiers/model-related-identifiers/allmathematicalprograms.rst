.. aimms:set:: AllMathematicalPrograms

.. _AllMathematicalPrograms:

AllMathematicalPrograms
=======================

The predefined set ``AllMathematicalprograms`` contains the names of all
mathematical programs within an AIMMS model.

.. code-block:: aimms

        Set AllMathematicalPrograms {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexMathematicalPrograms;
        }

Definition
----------

    The contents of the set :aimms:set:`AllMathematicalPrograms` is the collection of
    all *symbolic* mathematical programs defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    mathematical in the **Model Explorer**.

.. seealso::

    -  Mathematical programs in Section 15.1 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GenerateStochasticProgram`, and :aimms:func:`GMP::Instance::GetSymbolicMathematicalProgram`.
