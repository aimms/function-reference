.. aimms:set:: AllValueKeywords

.. _AllValueKeywords:

AllValueKeywords
================

The predefined set :aimms:set:`AllValueKeywords` serves as the root set of
various other predefined sets containing AIMMS keywords.

.. code-block:: aimms

        Set AllValueKeywords {
            Index      :  IndexValueKeywords;
            Definition :  {
                AllMathematicalProgrammingTypes +
                AllMatrixManipulationDirections +
                AllViolationTypes + YesNo +
                ContinueAbort + MergeReplace + OnOff +
                DiskWindowVoid + MaximizingMinimizing
            }
        }

Definition
----------

    The set :aimms:set:`AllValueKeywords` contains keywords used in various other
    predefined sets containing AIMMS keywords.

Updatability
------------

    The contents of the set :aimms:set:`AllValueKeywords` is completely under the
    control of AIMMS, and cannot be modified.

.. note::

    The set :aimms:set:`AllValueKeywords` is, in general, of little direct use in an
    AIMMS application.

.. seealso::

    The sets :aimms:set:`AllMathematicalProgrammingTypes`, :aimms:set:`AllMatrixManipulationDirections`, :aimms:set:`AllViolationTypes`, :aimms:set:`YesNo`, :aimms:set:`ContinueAbort`,
    :aimms:set:`DiskWindowVoid`, :aimms:set:`MaximizingMinimizing`, :aimms:set:`MergeReplace`, :aimms:set:`OnOff`.
