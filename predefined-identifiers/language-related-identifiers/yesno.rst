.. aimms:set:: YesNo

.. _YesNo:

YesNo
=====

The predefined set :aimms:set:`YesNo` defines the set of elements ``Yes`` and
``No``.

.. code-block:: aimms

        Set YesNo {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexYesNo;
            Definition :  data { yes, no };
        }

Definition
----------

    The predefined set :aimms:set:`YesNo` defines the set of elements ``Yes`` and
    ``No``.

Updatability
------------

    The contents of the set :aimms:set:`YesNo` cannot be modified.

.. note::

    The set :aimms:set:`YesNo` is not used by AIMMS anymore.

.. seealso::

    The set :aimms:set:`AllValueKeywords`.
