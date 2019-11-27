.. _.Basic:

.Basic
======

Definition
----------

    When the property ``Basic`` of a constraint or variable is set or when
    the option ``Always store basics`` is set to ``on``, the ``.Basic``
    suffix contains basis status of the constraint or variable at the end of
    a solve.

Datatype
--------

    The value of the ``.Basic`` suffix is an element in the predeclared set
    :aimms:set:`AllBasicValues`.

Dimension
---------

    The ``.Basic`` suffix has the same dimension and domain as that of the
    constraint or variable at hand.

.. note::

    -  The default of the option ``Always store basics`` is ``on``.

    -  In order to access the basic status of the definition of a variable
       ``X`` use the notation ``X_definition.Basic``.

    -  See also Section 14.1 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__
