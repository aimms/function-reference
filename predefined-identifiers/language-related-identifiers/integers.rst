.. aimms:set:: Integers

.. _Integers:

Integers
========

The predefined set :aimms:set:`Integers` defines the range of allowed integer set
elements in AIMMS.

.. code-block:: aimms

        Set Integers {
            Index      :  IndexIntegers;
            Definition :  {
                { (-2^30+5) .. (2^30+2) }
            }
        }

Definition
----------

    The set :aimms:set:`Integers` defines the range of integers that can possibly
    serve as integer set elements in AIMMS.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Subsets of the sets :aimms:set:`Integers` are frequently used to enumerate
    objects within a model. Datafiles (i.e. cases and datasets) in AIMMS are
    enumerated as subsets of the set :aimms:set:`Integers`.

.. seealso::

    The sets :aimms:set:`AllDataFiles`, :aimms:set:`AllCases`, :aimms:set:`AllDataSets`. Integer sets are discussed in
    Section 3.2.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
