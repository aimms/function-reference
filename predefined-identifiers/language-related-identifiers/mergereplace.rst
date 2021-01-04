.. aimms:set:: MergeReplace

.. _MergeReplace:

MergeReplace
============

The predefined set :aimms:set:`MergeReplace` defines the set of modes for the
``READ``, ``WRITE`` and ``SOLVE`` statements.

.. code-block:: aimms

        Set MergeReplace {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexMergeReplace;
            Definition :  data { merge, replace };
        }

Definition
----------

    The predefined set :aimms:set:`MergeReplace` defines the set of modes for the
    ``READ``, ``WRITE`` and ``SOLVE`` statements as specified through the
    ``IN MERGE/REPLACE MODE`` clause.

Updatability
------------

    The contents of the set :aimms:set:`MergeReplace` cannot be modified.

.. note::

    Element parameters into the set :aimms:set:`MergeReplace` can be used to
    dynamically indicate the mode of a ``READ``, ``WRITE`` or ``SOLVE``
    statement.

.. seealso::

    The set :aimms:set:`AllValueKeywords`. The ``SOLVE`` statement is discussed in :doc:`optimization-modeling-components/solving-mathematical-programs/the-solve-statement`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__, the ``READ`` and ``WRITE`` statements in
    :doc:`data-communication-components/the-read-and-write-statements/syntax-of-the-read-and-write-statements`
