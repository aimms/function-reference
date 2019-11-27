.. _.Level:

.Level
======

Definition
----------

    The ``.Level`` suffix contains the current value of a variable. When the
    property ``Level`` of a constraint is set, the ``.Level`` suffix
    contains the current value of the left hand side of the constraint after
    the last solve.

Datatype
--------

    The value of the ``.Level`` suffix is numeric.

Dimension
---------

    The ``.Level`` suffix has the same dimension and domain as that of the
    constraint or variable at hand.

.. note::

    -  When a variable without a suffix is used inside an assignment
       statement or a parameter definition the ``.Level`` suffix is
       automatically used.

    -  See also Section 14.2.5 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The GAMS and AIMMS 2 equivalent suffix name is ``.l``.
