.. aimms:function:: DialogMessage(message, title)

.. _DialogMessage:

DialogMessage
=============

The procedure :aimms:func:`DialogMessage` displays a small dialog box containing a
specified informational message and an **OK** button. The execution will
be halted until the user presses the **OK** button.

.. code-block:: aimms

    DialogMessage(
            message,        ! (input) string expression
            [title]         ! (optional) string expression
            )

Arguments
---------

    *message*
        A scalar string expression containing the text you want to display in
        the dialog box.

    *title*
        A scalar string expression containing the text that you want to appear
        in the title of the dialog box.

.. note::

    The procedures :aimms:func:`DialogMessage` and ``DialogError`` only differ in the
    icon that is displayed at the left side of the dialog box

.. seealso::

    The procedures :aimms:func:`DialogError`, :aimms:func:`DialogAsk`.
