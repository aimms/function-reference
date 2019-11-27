.. aimms:procedure:: GMP::Instance::Delete(GMP)

.. _GMP::Instance::Delete:

GMP::Instance::Delete
=====================

The procedure :aimms:func:`GMP::Instance::Delete` deletes a generated mathematical
program from the set :aimms:set:`AllGeneratedMathematicalPrograms`.

.. code-block:: aimms

    GMP::Instance::Delete(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    All memory associated with the generated mathematical program is also
    freed.

.. seealso::

    The function :aimms:func:`GMP::Instance::Generate`.
