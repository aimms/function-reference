.. aimms:function:: DialogProgress(message[, percentage])

.. _DialogProgress:

DialogProgress
==============

The procedure :aimms:func:`DialogProgress` displays a small dialog box containing
a specified message and a progress bar that can indicate how much of a
specific task has already been processed. This dialog box will not halt
the execution, and you can call the procedure sequentially during a
timely task to change either the displayed message or the length of the
progress bar.

.. code-block:: aimms

    DialogProgress(
            message,         ! (input) string expression
            [percentage]     ! (optional) integer expression
            )

Arguments
---------

    *message*
        A scalar string expression containing the text you want to display in
        the dialog box.

    *percentage (optional)*
        A scalar value between 0 and 100. It is used to set the length of the
        progress bar at the bottom of the dialog box. If this argument is
        omitted then the progress bar is not displayed.

.. note::

    The progress dialog box does not adjust the length of the progress bar
    itself, so you must do it yourself by sequentially calling the procedure
    with an increasing percentage. The progress dialog box is automatically
    removed from the screen if the execution terminates. If you want to
    remove the dialog box yourself, then you should call :aimms:func:`DialogProgress`
    with an empty message string: ``DialogProgress("")``.

.. seealso::

    The procedures :aimms:func:`DialogMessage`, :aimms:func:`DialogError`, :aimms:func:`DialogAsk`.
