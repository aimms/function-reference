.. aimms:procedure:: DialogAsk(message, button1, button2[, button3], title)

.. _DialogAsk:

DialogAsk
=========

The procedure :aimms:func:`DialogAsk` displays a small dialog box containing a
message and two or three buttons. Usually these buttons are an **OK**
and **Cancel**, or **Yes**, **No** and **Cancel**, but they can contain
any text you want. The procedure returns the number of the button that
is pressed by the user.

.. code-block:: aimms

    DialogAsk(
            message,        ! (input) string expression
            button1,        ! (input) string expression
            button2,        ! (input) string expression
            [button3]       ! (optional) string expression
            [title]         ! (optional) title of dialog box
            )

Arguments
---------

    *message*
        A scalar string expression containing the text you want to display in
        the dialog box.

    *button1*
        A scalar string expression containing the text of the first button.

    *button2*
        A scalar string expression containing the text of the second button.

    *button3 (optional)*
        A scalar string expression containing the text of the third button. If
        this argument is omitted then the dialog box will only show two buttons.

    *title*
        A scalar string expression containing the text that you want to appear
        in the title of the dialog box.

Return Value
------------

    The procedure returns the number of the button that is pressed: 1 for
    the first button, 2 for the second button or 3 for the third button.

.. note::

    If the user presses the **Esc** key, or closes the dialog box via the
    [x] in the top right corner, then this is interpreted as pressing the
    last button in the dialog box (which is usually the **Cancel** button).

.. seealso::

    The procedures :aimms:func:`DialogMessage`, :aimms:func:`DialogError`.
