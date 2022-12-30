.. _.GenTime:

.GenTime
========

Definition
----------

    The mathematical program suffix ``.GenTime`` contains the time required
    to generate the mathematical program.

Datatype
--------

    The value of the ``.GenTime`` suffix is numeric and in wallclock
    seconds.

.. note::

    -  The suffix ``.GenTime`` has unit [second] iff (1) this unit has been
       declared, and (2) the option ``solution_time_has_unit_seconds`` is
       set to on. In all other cases the suffix has no unit.

    -  The equivalent GAMS and AIMMS 2 name is ``.resgen``.

    -  The ``.GenTime`` suffix is also mentioned in Table :ref:`table:mp.suffix-mp.Solver`
       of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
