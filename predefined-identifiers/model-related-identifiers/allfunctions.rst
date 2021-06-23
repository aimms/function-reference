.. aimms:set:: AllFunctions

.. _AllFunctions:

AllFunctions
============

The predefined set :aimms:set:`AllFunctions` contains the names of all functions
defined within an AIMMS model.

.. code-block:: aimms

        Set AllFunctions {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexFunctions;
        }

Definition
----------

    The contents of the set :aimms:set:`AllFunctions` is the collection of all
    function names defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    functions in the **Model Explorer**.

.. note::

    Elements of the set :aimms:set:`AllFunctions` are typically used in conjunction
    with the ``APPLY`` statement, to allow data-driven evaluation of
    functional expressions.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`. Functions are discussed in :doc:`procedural-language-components/procedures-and-functions/internal-functions` of the
     Language Reference, the ``APPLY`` statement in :ref:`sec:intern.ref.apply`.
