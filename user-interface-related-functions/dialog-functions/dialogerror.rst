.. aimms:function:: DialogError(message, title)

.. _DialogError:

DialogError
===========

The procedure :aimms:func:`DialogError` displays a small dialog box containing a
specified error message and an **OK** button. The execution will be
halted until the user presses the **OK** button.

.. code-block:: aimms

    DialogError(
            message,         ! (input) string expression
            [title]          ! (optional) title of dialog box
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

    The procedures ``DialogMessage`` and :aimms:func:`DialogError` only differ in the
    icon that is displayed at the left side of the dialog box.

.. seealso::

    The procedures :aimms:func:`DialogMessage`, :aimms:func:`DialogAsk`, :aimms:func:`DialogProgress`.
