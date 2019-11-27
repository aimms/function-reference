.. aimms:procedure:: GMP::Event::Delete(Event)

.. _GMP::Event::Delete:

GMP::Event::Delete
==================

The procedure :aimms:func:`GMP::Event::Delete` deletes an event.

.. code-block:: aimms

    GMP::Event::Delete(
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

    The routines :aimms:func:`GMP::Event::Create`, :aimms:func:`GMP::Event::Reset` and :aimms:func:`GMP::Event::Set`, and Section 16.6 of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
