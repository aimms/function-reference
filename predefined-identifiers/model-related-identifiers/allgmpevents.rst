.. aimms:set:: AllGMPEvents

.. _AllGMPEvents:

AllGMPEvents
============

The predefined set :aimms:set:`AllGMPEvents` contains all GMP Events.

.. code-block:: aimms

        Set AllGMPEvents {
            SubsetOf     :  AllSolverSessionCompletionObjects;
            Index        :  IndexGMPEvents;
        }

Definition
----------

    The set :aimms:set:`AllGMPEvents` contains all GMP events used by the functions
    ``GMP::Event::Create``, ``GMP::Event::Delete``, ``GMP::Event::Reset``,
    and ``GMP::Event::Set``.

.. seealso::

    The functions :aimms:func:`GMP::Event::Create`, :aimms:func:`GMP::Event::Delete`, :aimms:func:`GMP::Event::Reset`, and :aimms:func:`GMP::Event::Set`, and the
    predeclared identifier :aimms:set:`AllSolverSessionCompletionObjects`.
