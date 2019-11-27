.. aimms:set:: AllCaseComparisonModes

.. _AllCaseComparisonModes:

AllCaseComparisonModes
======================

The predefined set :aimms:set:`AllCaseComparisonModes` contains the collection of
all possible modes supported by the :aimms:func:`CaseCompareIdentifier` function.

.. code-block:: aimms

        Set AllCaseComparisonModes {
            Index      :  IndexCaseComparisonModes;
            Definition :  {
                data { min, max, sum
                       average, count }
              }
        }

Definition
----------

    The predefined set :aimms:set:`AllCaseComparisonModes` contains the collection of
    all possible modes supported by the :aimms:func:`CaseCompareIdentifier` function.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Element parameters into :aimms:set:`AllCaseComparisonModes` can be used as the
    *mode* argument of the :aimms:func:`CaseCompareIdentifier` function.

.. seealso::

    The function :aimms:func:`CaseCompareIdentifier`.
