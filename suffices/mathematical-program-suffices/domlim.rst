.. _.domlim:

.domlim
=======

Definition
----------

    When the number of domain violations during the optimization of a
    nonlinear program exceeds the value of the suffix ``.domlim`` the
    solution process is stopped. When specified this suffix overrides the
    option ``maximal_number_of_domain_errors``.

Datatype
--------

    The value of the ``.domlim`` suffix is numeric.

.. note::

    -  The suffix ``.domlim`` is initialized to ``NA``. AIMMS considers it
       specified when its value is not equal to ``NA``.
