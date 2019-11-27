.. aimms:procedure:: DialogGetPassword(message, password, title)

.. _DialogGetPassword:

DialogGetPassword
=================

The procedure :aimms:func:`DialogGetPassword` displays a small dialog box in which
the user can enter a password string. In the dialog box the string is
presented by a sequence of asterisks. The dialog box remains on the
screen (and thus halts the execution) until the user presses either the
**OK** or the **Cancel** button.

.. code-block:: aimms

    DialogGetPassword(
            message,        ! (input) string expression
            password,       ! (input/output) scalar string parameter
            [title]         ! (optional) string expression
            )

Arguments
---------

    *message*
        A scalar string expression containing the text you want to display in
        front of the edit field.

    *password*
        A scalar string valued identifier containing the password. When creating
        the dialog box, its value is used to fill the edit field. After the user
        presses the **OK** button, the edited password string is returned
        through this argument.

    *title*
        A scalar string expression containing the text that you want to appear
        in the title of the dialog box.

Return Value
------------

    The procedure returns 1 if the user has pressed the **OK** button, and 0
    if he has pressed the **Cancel** button.

.. seealso::

    The procedure :aimms:func:`DialogGetString`.
