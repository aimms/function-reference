.. aimms:procedure:: DialogGetNumber(message, reference, decimals, title)

.. _DialogGetNumber:

DialogGetNumber
===============

The procedure :aimms:func:`DialogGetNumber` displays a small dialog box in which
the user can enter a single numerical value. The dialog box remains on
the screen (and thus halts the execution) until the user presses either
the **OK** or the **Cancel** button.

.. code-block:: aimms

    DialogGetNumber(
            message,        ! (input) string expression
            reference,      ! (input/output) scalar numerical identifier
            [decimals,]     ! (optional) integer
            [title]         ! (optional) string expression
            )

Arguments
---------

    *message*
        A scalar string expression containing the text you want to display in
        front of the edit field.

    *reference*
        A scalar identifier. When creating the dialog box, its value is used to
        fill the edit field. After the user presses the **OK** button, the
        edited value is returned through this argument.

    *decimals*
        A integer expression to indicate the number of decimals that is
        displayed initially.

    *title*
        A scalar string expression containing the text that you want to appear
        in the title of the dialog box.

Return Value
------------

    The procedure returns 1 if the user has pressed the **OK** button, and 0
    if he has pressed the **Cancel** button.

.. seealso::

    The procedures :aimms:func:`DialogGetString`, :aimms:func:`DialogGetElement`.
