.. aimms:function:: ShowMessageWindow([do\_show])

.. _ShowMessageWindow:

ShowMessageWindow
=================

With the procedure :aimms:func:`ShowMessageWindow` you programmatically open or
close the AIMMS message window.

.. code-block:: aimms

    ShowMessageWindow(
         [do_show]       ! (optional) scalar expression
         )

Arguments
---------

    *do\_show (optional)*
        A scalar 0-1 expression, indicating whether the message window should be
        opened (value is 1) or should be closed (value is 0). The default is 1.

.. seealso::

    The procedure :aimms:func:`ShowProgressWindow`.
