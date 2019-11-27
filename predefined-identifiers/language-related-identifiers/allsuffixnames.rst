.. aimms:set:: AllSuffixNames

.. _AllSuffixNames:

AllSuffixNames
==============

The predefined set :aimms:set:`AllSuffixNames` contains the names of all existing
suffixes of all identifier types.

.. code-block:: aimms

        Set AllSuffixNames {
            Index      :  IndexSuffixNames;
        }

Definition
----------

    The set :aimms:set:`AllSuffixNames` contains the names of all possible suffixes
    for the entire collection of identifier types.

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    -  The set :aimms:set:`AllIdentifiers`.

    -  The functions :aimms:func:`ScalarValue`, :aimms:func:`ActiveCard`, :aimms:func:`Card`, :aimms:func:`CaseCompareIdentifier`, and
       :aimms:func:`GMP::Solution::SendToModelSelection`.
