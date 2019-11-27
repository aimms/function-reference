.. aimms:procedure:: DialogGetString(message, reference, title)

.. _DialogGetString:

DialogGetString
===============

The procedure :aimms:func:`DialogGetString` displays a small dialog in which the
user can enter a text string. The dialog remains on the screen (and thus
halts the execution) until the user presses either the **OK** or the
**Cancel** button.

.. code-block:: aimms

    DialogGetString(
            message,        ! (input) string expression
            reference,      ! (input/output) scalar string parameter
            [title]         ! (optional) string expression
            )

Arguments
---------

    *message*
        A scalar string expression containing the text you want to display in
        front of the edit field.

    *reference*
        A scalar string valued identifier. When creating the dialog, its value
        is used to fill the edit field. After the user presses the **OK**
        button, the edited string is returned through this argument.

    *title*
        A scalar string expression containing the text that you want to appear
        in the title of the dialog box.

Return Value
------------

    The procedure returns 1 if the user has pressed the **OK** button, and 0
    if he has pressed the **Cancel** button.

.. seealso::

    The procedures :aimms:func:`DialogGetNumber`, :aimms:func:`DialogGetPassword`, :aimms:func:`DialogGetElement`.
