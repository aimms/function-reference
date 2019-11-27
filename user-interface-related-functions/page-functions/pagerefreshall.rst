.. aimms:function:: PageRefreshAll(None)

.. _PageRefreshAll:

PageRefreshAll
==============

Normally, the data on all open pages is refreshed automatically each
time AIMMS has finished executing a procedure. Via a call to
:aimms:func:`PageRefreshAll` you can refresh the data on all pages at any time
during a procedure run (for example to show intermediate results).

.. code-block:: aimms

    PageRefreshAll

Arguments
---------

    *None*

.. note::

    -  Pages that you open from within a procedure will always show the data
       that is available at that moment, so it is not necessary to call
       :aimms:func:`PageRefreshAll` for a newly opened page.

    -  At the end of an button action, AIMMS will automatically refresh all
       pages.

.. seealso::

    The procedure :aimms:func:`PageOpen`.
