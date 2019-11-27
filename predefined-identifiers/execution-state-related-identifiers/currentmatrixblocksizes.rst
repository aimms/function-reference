.. aimms:set:: CurrentMatrixBlockSizes

.. _CurrentMatrixBlockSizes:

CurrentMatrixBlockSizes
=======================

The predefined parameter :aimms:set:`CurrentMatrixBlockSizes` contains the number
of non-zeros for the last mathematical program generated.

.. code-block:: aimms

        Parameter CurrentMatrixBlockSizes {
            IndexDomain  :  (IndexConstraints, IndexVariables);
        }

Definition
----------

    The parameter :aimms:set:`CurrentMatrixBlockSizes` contains the number of
    non-zeros for the last mathematical program generated. The parameter
    counts the non-zeros in all generated rows of a particular *symbolic*
    constraint with respect to all generated columns of a particular
    *symbolic* variable.

.. note::

    -  You can use the parameter :aimms:set:`CurrentMatrixBlockSizes`, for example,
       to analyze which constraint-variable sub-block of the generated
       matrix accounts for a number of non-zeros in a mathematical program
       that appears to be unnaturally high.

    -  The parameters :aimms:set:`CurrentMatrixRowCount`, :aimms:set:`CurrentMatrixColumnCount` and :aimms:set:`CurrentMatrixBlockSizes` are only set when
       the AIMMS option **Solvers General - Matrix Generation -
       Matrix_Block_Sizes** is set to ``on``.

.. seealso::

    The sets :aimms:set:`CurrentMatrixColumnCount`, :aimms:set:`CurrentMatrixRowCount`.
