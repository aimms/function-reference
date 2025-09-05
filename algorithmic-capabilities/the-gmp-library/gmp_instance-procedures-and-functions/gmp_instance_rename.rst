.. aimms:function:: GMP::Instance::Rename(GMP, Name)

.. _GMP::Instance::Rename:

GMP::Instance::Rename
=====================

The procedure :aimms:func:`GMP::Instance::Rename` can be used to rename a
generated mathematical program.

.. code-block:: aimms

    GMP::Instance::Rename(
         GMP,            ! (input) a generated mathematical program
         Name            ! (input) a string expression
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *Name*
        A string that holds the new name.

Return Value
------------

    :aimms:func:`GMP::Instance::Rename` has no return value.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::Copy`.
