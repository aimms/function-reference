.. aimms:procedure:: GMP::Event::Set(Event)

.. _GMP::Event::Set:

GMP::Event::Set
===============

The procedure :aimms:func:`GMP::Event::Set` activates an event.

.. code-block:: aimms

    GMP::Event::Set(
         Event             ! (input) an event
         )

Arguments
---------

    *Event*
        An element in the set :aimms:set:`AllGMPEvents`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Event::Create`, :aimms:func:`GMP::Event::Delete` and :aimms:func:`GMP::Event::Reset`, and :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/synchronization-events` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

