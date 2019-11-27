.. aimms:set:: CurrentMatrixColumnCount

.. _CurrentMatrixColumnCount:

CurrentMatrixColumnCount
========================

The predefined parameter :aimms:set:`CurrentMatrixColumnCount` contains the
number of columns for the last mathematical program generated.

.. code-block:: aimms

        Parameter CurrentMatrixColumnCount {
            IndexDomain  :  IndexVariables;
        }

Definition
----------

    The parameter :aimms:set:`CurrentMatrixColumnCount` contains the number of
    columns for the last mathematical program generated. The parameter
    counts the columns generated for each individual *symbolic* variable.

.. note::

    -  You can use the parameter :aimms:set:`CurrentMatrixColumnCount`, for example,
       to analyze which symbolic variable accounts for a number of columns
       in a mathematical program that appears to be unnaturally high.

    -  The parameters :aimms:set:`CurrentMatrixRowCount`, :aimms:set:`CurrentMatrixColumnCount` and :aimms:set:`CurrentMatrixBlockSizes` are only set when
       the AIMMS option **Solvers General - Matrix Generation -
       Matrix_Block_Sizes** is set to ``on``.

.. seealso::

    The sets :aimms:set:`CurrentMatrixRowCount`, :aimms:set:`CurrentMatrixBlockSizes`.
