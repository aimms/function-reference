.. aimms:procedure:: SolverReleaseControl(None)

.. _SolverReleaseControl:

SolverReleaseControl
====================

A single use local license allows you to run two concurrent AIMMS
sessions. At any time, however, only one of these sessions can make use
of a solver. Prior to executing a ``SOLVE`` statement, AIMMS will
determine whether the solver is already locked by another session. If
this is the case, AIMMS will abort the ``SOLVE`` statement with a
runtime error. If the solver is not locked, AIMMS locks the solver for
the duration of ``SOLVE`` statement by default. With the procedure
:aimms:func:`SolverReleaseControl` you can unlock a solver previously locked by a
call to the procedure ``SolverGetControl``.

.. code-block:: aimms

    SolverReleaseControl

Arguments
---------

    *None*

Return Value
------------

    The procedure returns 1 if successful, or 0 if the solver was not
    currently locked by this session.

.. note::

    -  AIMMS also supports multi-session local licenses that allow you to
       run multiple concurrent solves, and twice that number of concurrent
       AIMMS sessions.

    -  This procedure has no effect if you are connecting to an AIMMS
       network license server. In that case every session requires a
       separate floating network license.

.. seealso::

    The procedure :aimms:func:`SolverGetControl`.
