.. aimms:set:: AllGeneratedMathematicalPrograms

.. _AllGeneratedMathematicalPrograms:

AllGeneratedMathematicalPrograms
================================

The predefined set :aimms:set:`AllGeneratedMathematicalPrograms` contains the
names of all generated mathematical programs associated with the
symbolic mathematical programs in an AIMMS model.

.. code-block:: aimms

        Set AllGeneratedMathematicalPrograms {
            Index       :  IndexGeneratedMathematicalPrograms;
            Parameter   :  CurrentGeneratedMathematicalProgram;
        }

Definition
----------

    -  The contents of the set :aimms:set:`AllGeneratedMathematicalPrograms` is the
       collection of all generated mathematical programs associated with
       symbolic mathematical programs in your model, and generated through
       the ``SOLVE`` statement, or the functions ``GMP::Instance::Generate``
       and ``GMP::Instance::CreateDual``.

    -  The element parameter ``CurrentGeneratedMathematicalProgram`` refers
       to the currently active generated mathematical program instance.

Updatability
------------

    The contents of the set can only be modified through the ``SOLVE``
    statement, and the functions ``GMP::Instance::Generate``,
    ``GMP::Instance::Copy``, ``GMP::Instance::Rename``,
    ``GMP::Instance::Delete`` and ``GMP::Instance::CreateDual``.

.. seealso::

    The function :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Copy`, :aimms:func:`GMP::Instance::Rename`, :aimms:func:`GMP::Instance::Delete` and :aimms:func:`GMP::Instance::CreateDual`.
