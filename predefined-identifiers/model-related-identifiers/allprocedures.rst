.. aimms:set:: AllProcedures

.. _AllProcedures:

AllProcedures
=============

The predefined set :aimms:set:`AllProcedures` contains the names of all
procedures defined within an AIMMS model.

.. code-block:: aimms

        Set AllProcedures {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexProcedures;
        }

Definition
----------

    The contents of the set :aimms:set:`AllProcedures` is the collection of all
    procedure names defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    procedures in the **Model Explorer**.

.. note::

    Elements of the set :aimms:set:`AllProcedures` are typically used in conjunction
    with the ``APPLY`` statement, to allow data-driven procedural execution.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`. Procedures are discussed in :doc:`procedural-language-components/procedures-and-functions/internal-procedures` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, the ``APPLY`` statement in :ref:`sec:intern.ref.apply`.
