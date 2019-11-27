.. aimms:procedure:: SolverGetControl(None)

.. _SolverGetControl:

SolverGetControl
================

A single use local license allows you to run two concurrent AIMMS
sessions. At any time, however, only one of these sessions can make use
of a solver. Prior to executing a ``SOLVE`` statement, AIMMS will
determine whether the solver is already locked by another session. If
this is the case, AIMMS will abort the ``SOLVE`` statement with a
runtime error. If the solver is not locked, AIMMS locks the solver for
the duration of ``SOLVE`` statement by default. With the procedure
:aimms:func:`SolverGetControl` you can programmatically lock the solver for a
prolonged period of time, for instance, during an algorithm requiring
multiple solves.

.. code-block:: aimms

    SolverGetControl

Arguments
---------

    *None*

Return Value
------------

    The procedure returns 1 if the solver was successfully locked, or 0
    otherwise.

.. note::

    -  AIMMS also supports multi-session local licenses that allow you to
       run multiple concurrent solves, and twice that number of concurrent
       AIMMS sessions.

    -  This procedure has no effect if you are connecting to an AIMMS
       network license server. In that case every session requires a
       separate floating network license.

.. seealso::

    The procedure :aimms:func:`SolverReleaseControl`.
