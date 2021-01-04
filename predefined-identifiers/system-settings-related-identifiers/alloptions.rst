.. aimms:set:: AllOptions

.. _AllOptions:

AllOptions
==========

The predefined set :aimms:set:`AllOptions` contains the names of all options
available in AIMMS.

.. code-block:: aimms

        Set AllOptions {
            Index      :  IndexOptions;
        }

Definition
----------

    The contents of the set :aimms:set:`AllOptions` is the collection of all options
    available in AIMMS from the language and through the **Options** dialog
    box.

Updatability
------------

    The contents of the set can only be modified through the **Solver
    Configuration** dialog box. By adding or removing solvers the
    corresponding solver options will be added or removed in the set
    :aimms:set:`AllOptions`.

.. note::

    In the set :aimms:set:`AllOptions`, the solver specific options are prefixed by
    the solver name and version.

.. seealso::

    Options in AIMMS is described in detail in :doc:`optimization-modeling-components/robust-optimization/basic-concepts` of the '`User\'s Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__'.
