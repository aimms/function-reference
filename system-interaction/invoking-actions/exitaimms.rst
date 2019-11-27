.. aimms:function:: ExitAimms([interactive])

.. _ExitAimms:

ExitAimms
=========

With the procedure :aimms:func:`ExitAimms` you can exit the current AIMMS session
from within a procedure.

.. code-block:: aimms

    ExitAimms(
             [interactive]       ! (optional) 0 or 1
             )

Arguments
---------

    *interactive (optional)*
        This optional argument is still present for compatibility, but does no
        longer have any effect. You should use MainTermination to specify
        whether or not AIMMS should display a confirmation dialog box before
        closing the current project.

.. note::

    | The procedure does not immediately exit AIMMS, but it will try to exit
      as soon as the execution of the current procedure has finished. If
      existing, the logoff procedure and the procedure ``MainTermination``
      will be executed as normal.
    | Please note that calling the pre-definded function ``ExitAimms()``
      from within WebUI (for example, as part of an action behind a button
      widget) is currently not supported and will result in an error. In
      fact, calling ``ExitAimms()`` only works for the main AIMMS thread
      itself and not for any of the other AIMMS contexts (of which WebUI is
      just one example). Exiting only from the underlying AIMMS session
      itself is not deemed as a proper behavior for an application with
      Web-based User Interface.
