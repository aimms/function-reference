.. aimms:function:: StatusMessage(message)

.. _StatusMessage:

StatusMessage
=============

With the procedure :aimms:func:`StatusMessage` you can display a short message in
the status bar at the bottom of the AIMMS window.

.. code-block:: aimms

    StatusMessage(
            message         ! (input) string expression
            )

Arguments
---------

    *message*
        A scalar string expression containing the text you want to display in
        the status bar.

.. note::

    If you have set the status bar to be hidden (via the project options),
    then the message will not be visible to the user.

.. seealso::

    The procedures :aimms:func:`DialogMessage`, :aimms:func:`DialogProgress`.
