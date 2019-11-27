.. aimms:set:: CurrentMatrixRowCount

.. _CurrentMatrixRowCount:

CurrentMatrixRowCount
=====================

The predefined parameter :aimms:set:`CurrentMatrixRowCount` contains the number
of rows for the last mathematical program generated.

.. code-block:: aimms

        Parameter CurrentMatrixRowCount {
            IndexDomain  :  IndexConstraints;
        }

Definition
----------

    The parameter :aimms:set:`CurrentMatrixRowCount` contains the number of rows for
    the last mathematical program generated. The parameter counts the rows
    generated for each individual *symbolic* constraint.

.. note::

    -  You can use the parameter :aimms:set:`CurrentMatrixRowCount`, for example, to
       analyze which symbolic constraint accounts for a number of rows in a
       mathematical program that appears to be unnaturally high.

    -  The parameters :aimms:set:`CurrentMatrixRowCount`, :aimms:set:`CurrentMatrixColumnCount` and :aimms:set:`CurrentMatrixBlockSizes` are only set when
       the AIMMS option **Solvers General - Matrix Generation -
       Matrix_Block_Sizes** is set to ``on``.

.. seealso::

    The sets :aimms:set:`CurrentMatrixColumnCount`, :aimms:set:`CurrentMatrixBlockSizes`.
