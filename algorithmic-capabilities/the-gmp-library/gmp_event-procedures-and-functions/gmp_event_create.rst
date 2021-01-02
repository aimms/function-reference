.. aimms:function:: GMP::Event::Create(Name)

.. _GMP::Event::Create:

GMP::Event::Create
==================

The function :aimms:func:`GMP::Event::Create` creates a new event.

.. code-block:: aimms

    GMP::Event::Create(
         Name              ! (input) a string expression
         )

Arguments
---------

    *Name*
        A string expression holding the name of the event.

Return Value
------------

    The function returns an element in the set :aimms:set:`AllGMPEvents`.

.. seealso::

    The routines :aimms:func:`GMP::Event::Delete`, :aimms:func:`GMP::Event::Reset` and :aimms:func:`GMP::Event::Set`, and :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/synchronization-events` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
