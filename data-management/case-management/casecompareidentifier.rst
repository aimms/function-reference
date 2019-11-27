.. aimms:function:: CaseCompareIdentifier(FirstCase, SecondCase, Identifier, Suffix, Mode)

.. _CaseCompareIdentifier:

CaseCompareIdentifier
=====================

With the function :aimms:func:`CaseCompareIdentifier` you can determine whether or
not two cases differ with respect to a certain identifier.

.. code-block:: aimms

    CaseCompareIdentifier(
            FirstCase,    ! (input) element in the set AllCases
            SecondCase,   ! (input) element in the set AllCases
            Identifier,   ! (input) element in the set AllIdentifiers
            Suffix        ! (optional) element in the set AllSuffixNames
            Mode          ! (optional) element in the set AllCaseComparisonModes
            )

Arguments
---------

    *FirstCase*
        An element in the set :aimms:set:`AllCases`

    *SecondCase*
        An element in the set :aimms:set:`AllCases`

    *Identifier*
        An element in the set :aimms:set:`AllIdentifiers`, refering to the specific identifier
        that you want to compare.

    *Suffix*
        An element in the set :aimms:set:`AllSuffixNames` with respect to which you want to
        compare the data.

    *Mode*
        An element in the :aimms:set:`AllCaseComparisonModes` with respect to how you want to compare the
        data.

Return Value
------------

    -  For numerical identifiers the function returns the differences
       between the values of the identifier in both cases, based on the
       mode. It can be the minimum, maximum, average, sum or count of all
       differences.

    -  For non-numerical identifiers the function counts the number of
       differences between the identifier in both cases.
