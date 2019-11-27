.. aimms:set:: ContinueAbort

.. _ContinueAbort:

ContinueAbort
=============

The predefined set :aimms:set:`ContinueAbort` defines the set of possible return
statuses of solver callback procedures.

.. code-block:: aimms

        Set ContinueAbort {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexContinueAbort;
            Definition :  data { continue, abort };
        }

Definition
----------

    The set :aimms:set:`ContinueAbort` defines the set of possible return statuses of
    solver callback procedures.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    The elements of the set :aimms:set:`ContinueAbort` can be assigned to the
    ``CallbackReturnStatus`` suffix of a mathematical program upon return of
    a solver callback procedure.

.. seealso::

    The set :aimms:set:`AllValueKeywords`. Solver callback procedures are discussed in Section
    15.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
