.. aimms:function:: MemoryInUse()

.. _MemoryInUse:

MemoryInUse
===========

With the function :aimms:func:`MemoryInUse` you can obtain the current amount of
memory in use as it is reported by the operating system.

.. code-block:: aimms

    MemoryInUse()

Return Value
------------

    This function returns the amount of memory in use in [Mb].

.. note::

    See also the functions :aimms:func:`MemoryStatistics`, :aimms:func:`IdentifierMemory`, :aimms:func:`GMP::Instance::GetMemoryUsed`
