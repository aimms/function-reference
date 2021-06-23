.. aimms:procedure:: GMP::Event::Reset(Event)

.. _GMP::Event::Reset:

GMP::Event::Reset
=================

The procedure :aimms:func:`GMP::Event::Reset` resets an event.

.. code-block:: aimms

    GMP::Event::Reset(
         Event             ! (input) an event
         )

Arguments
---------

    *Event*
        An element in the set :aimms:set:`AllGMPEvents`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    The state of the event will be reset to the state just after creating
    the event.

.. seealso::

    The routines :aimms:func:`GMP::Event::Create`, :aimms:func:`GMP::Event::Delete` and :aimms:func:`GMP::Event::Reset`, and :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/synchronization-events` of the
     Language Reference.
