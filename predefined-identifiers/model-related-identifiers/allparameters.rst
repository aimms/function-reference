.. aimms:set:: AllParameters

.. _AllParameters:

AllParameters
=============

The predefined set :aimms:set:`AllParameters` contains the names of all
parameters within an AIMMS model.

.. code-block:: aimms

        Set AllParameters {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexParameters;
        }

Definition
----------

    The contents of the set :aimms:set:`AllParameters` is the collection of all
    *symbolic* parameter names declared within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    parameters in the **Model Explorer**.

.. note::

    Subsets of :aimms:set:`AllParameters` are occassionally used in ``READ``,
    ``WRITE`` or ``DISPLAY`` statements to indicate the set of parameters to
    be read or written, as well as in data control statements such as
    ``EMPTY`` and ``CLEANUP``.

.. seealso::

    The sets :aimms:set:`AllDefinedParameters`, :aimms:set:`AllIdentifiers`. Data control statements are discussed in
    :doc:`data-communication-components/data-initialization-verification-and-control/data-control`, the ``READ`` and ``WRITE`` statements in :doc:`data-communication-components/the-read-and-write-statements/syntax-of-the-read-and-write-statements`, and
    the ``DISPLAY`` statement in :doc:`data-communication-components/text-reports-and-output-listing/the-display-statement` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
