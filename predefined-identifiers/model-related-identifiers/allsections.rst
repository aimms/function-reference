.. aimms:set:: AllSections

.. _AllSections:

AllSections
===========

The predefined set :aimms:set:`AllSections` contains the names of all sections
within an AIMMS model.

.. code-block:: aimms

        Set AllSections {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexSections;
        }

Definition
----------

    The contents of the set :aimms:set:`AllSections` is the collection of all section
    names defined within a particular model tree.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    sections in the **Model Explorer**.

.. note::

    Section names contained in :aimms:set:`AllSections` are occassionally used in
    ``READ``, ``WRITE`` or ``DISPLAY`` statements to indicate the set of
    identifiers to be read or written, as well as in data control statements
    such as ``EMPTY`` and ``CLEANUP``.

.. seealso::

    The set :aimms:set:`AllIdentifiers`. Model sections are discussed in :doc:`creating-and-managing-a-model/index`. 
    Data control statements are discussed in Section :doc:`data-communication-components/data-initialization-verification-and-control/data-control`, the
    ``READ`` and ``WRITE`` statements in :ref:`sec:rw.read-write`, and the ``DISPLAY``
    statement in :ref:`sec:report.display` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
