.. aimms:set:: AllDifferencingModes

.. _AllDifferencingModes:

AllDifferencingModes
====================

The predefined set :aimms:set:`AllDifferencingModes` contains the collection of
all possible differencing modes supported by the :aimms:func:`CaseCreateDifferenceFile` function.

.. code-block:: aimms

        Set AllDifferencingModes {
            Index      :  IndexDifferencingModes;
            Definition :  {
                 data { blockReplacement, elementReplacement,
                        elementAddition, elementMultiplication  }
            }
        }

Definition
----------

    The predefined set :aimms:set:`AllDifferencingModes` contains the collection of
    all possible differencing modes supported by the :aimms:func:`CaseCreateDifferenceFile` function:

    -  ``blockReplacement``: When there are differences between the
       reference case and the current case for an identifier the data of
       that identifier in the current case is entirely displayed.

    -  ``elementReplacement``: When there are differences between the
       reference case and the current case for an identifier the differing
       elements in the current case are displayed. This may include defaults
       for elements deleted.

    -  ``elementAddition``: When there are differences between the reference
       case and the current case for an identifier the differences between
       elements in the current case and reference case are displayed.

    -  ``elementMultiplication``: When there are differences between the
       reference case and the current case for an identifier the relative
       differences between elements in the current case and reference case
       are displayed.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Element parameters into :aimms:set:`AllDifferencingModes` can be used as the
    *diffTypes* argument of the :aimms:func:`CaseCreateDifferenceFile` function.

.. seealso::

    The function :aimms:func:`CaseCreateDifferenceFile`.
