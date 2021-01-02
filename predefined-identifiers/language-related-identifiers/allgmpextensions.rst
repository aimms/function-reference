.. aimms:set:: AllGMPExtensions

.. _AllGMPExtensions:

AllGMPExtensions
================

The predefined set :aimms:set:`AllGMPExtensions` contains the collection of all
possible extensions in the matrix manipulation library of AIMMS.

.. code-block:: aimms

        Set AllGMPExtensions {
            Index      :  IndexGMPExtensions;
            Definition :  {
                 data { DualObjective, DualDefinition,
                        DualLowerBound, DualUpperBound }
            }
        }

Definition
----------

    The predefined set :aimms:set:`AllGMPExtensions` contains the collection of all
    possible extensions in the matrix manipulation library of AIMMS.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Together with the suffixes ``.ExtendedConstraint`` and
    ``.ExtendedVariable``, element parameters into :aimms:set:`AllGMPExtensions` can
    be used as the ``extension`` argument of a constraint, a variable, and a
    mathematical program.

.. seealso::

    The set :aimms:set:`AllSuffixNames`. Matrix manipulation is discussed in more detail in
    :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
