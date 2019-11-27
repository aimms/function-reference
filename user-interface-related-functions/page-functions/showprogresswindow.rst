.. aimms:function:: ShowProgressWindow([do\_show])

.. _ShowProgressWindow:

ShowProgressWindow
==================

With the procedure :aimms:func:`ShowProgressWindow` you programmatically open or
close the AIMMS progress window.

.. code-block:: aimms

    ShowProgressWindow(
         [do_show]       ! (optional) scalar expression
         )

Arguments
---------

    *do\_show (optional)*
        A scalar 0-1 expression, indicating whether the progress window should
        be opened (value is 1) or should be closed (value is 0). The default is
        1.

.. seealso::

    The procedure :aimms:func:`ShowMessageWindow`.
