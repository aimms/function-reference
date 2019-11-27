.. aimms:function:: GarbageCollectStrings()

.. _GarbageCollectStrings:

GarbageCollectStrings
=====================

The procedure :aimms:func:`GarbageCollectStrings` removes any unused strings in
the internal data structures of AIMMS. If you do not call this procedure
explicitly, AIMMS performs an automatic garbage collect at certain
places during execution. For example as part of the Empty statement when
recently a lot of string valued expressions have been executed.

.. code-block:: aimms

    GarbageCollectStrings()

.. note::

    Use this procedure only when you notice that AIMMS uses a lot of memory
    that might be related to having many strings in the model. It is a
    rather expensive procedure in terms of execution time, because it needs
    to enumerate all the individual entries of all string parameters in the
    model. After runnig it you might see a drop in the memory that is in use
    by AIMMS, but be aware that because of the internal memory model of
    AIMMS, some memory is not given back to the operating system directly,
    but has only been marked for re-use in subsequent memory requests.
