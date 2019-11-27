.. aimms:set:: AllKeywords

.. _AllKeywords:

AllKeywords
===========

The predefined set :aimms:set:`AllKeywords` contains the names of all keywords in
AIMMS.

.. code-block:: aimms

        Set AllKeywords {
            SubsetOf   :  AllSymbols;
            Index      :  IndexKeywords;
        }

Definition
----------

    The contents of the set :aimms:set:`AllKeywords` is the collection of all
    keywords.

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    The set :aimms:set:`AllSymbols`.
