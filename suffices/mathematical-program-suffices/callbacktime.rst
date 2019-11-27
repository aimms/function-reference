.. _.CallbackTime:

.CallbackTime
=============

Definition
----------

    The mathematical program suffix ``.CallbackTime`` contains the name of
    the AIMMS procedure to be called after a certain number of seconds have
    elapsed.

Datatype
--------

    The value of the ``.CallbackTime`` suffix is an element in the set of
    ``AllProcedures`` and the default is the empty element ``''``.

.. note::

    -  See also Section 15.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The ``CallbackTime`` callback procedure is supported by CPLEX,
       GUROBI, CBC, XA, CP OPTIMIZER, CONOPT, KNITRO, SNOPT and IPOPT.

    -  The number of (elapsed) seconds is determined by the general solvers
       option ``Progress Time Interval``. This option also specifies the
       interval for updating the Progress Window during a solve. As a
       consequence, the information passed to this callback procedure will
       be the same as the information displayed in the Progress Window
       (except for small differences for the solving time).

    -  The time callback will be called less often if CPLEX uses dynamic
       search as the MIP Search Strategy instead of branch-and-cut. In that
       case the interval between two successive calls might sometimes be
       larger than the interval as specified by the option
       ``Progress Time Interval``.
