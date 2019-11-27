.. aimms:function:: GMP::Instance::CreateMasterMIP(GMP, name)

.. _GMP::Instance::CreateMasterMIP:

GMP::Instance::CreateMasterMIP
==============================

The function :aimms:func:`GMP::Instance::CreateMasterMIP` creates a Master MIP
copy of the specified generated mathematical program. The copy will
remove all nonlinear rows from the GMP.

.. code-block:: aimms

    GMP::Instance::CreateMasterMIP(
         GMP,            ! (input) a generated mathematical program
         name            ! (input) a string expression
    )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *name*
        A string that holds the name for the Master MIP.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  The *name* argument should be different from the name of the original
       generated mathematical program.

    -  If an element with name specified by the *name* argument is already
       present in the set :aimms:set:`AllGeneratedMathematicalPrograms` the corresponding generated mathematical
       program will be replaced (or updated in case the same symbolic
       mathematical program is involved).

    -  The generated mathematical program should have type MINLP (or MIQP or
       MIQCP). It can also have type NLP in which case the created GMP will
       have type LP.

    -  If the objective constraint is nonlinear,
       :aimms:func:`GMP::Instance::CreateMasterMIP` adds an extra row and column to
       the Master MIP. If ``mp`` denotes the symbolic mathematical program
       then the extra row will be associated with
       ``mp.ExtendedConstraint(MasterMIPObjective)`` and the extra column
       with ``mp.ExtendedVariable(MasterMIPObjective)``. The extra row will
       be

       .. math:: \verb|objvar| - \verb|mp.ExtendedVariable(MasterMIPObjective)| = 0

       \ where ``objvar`` denotes the objective variable of the GMP. Column
       ``mp.ExtendedVariable(MasterMIPObjective)`` will become the objective
       column of the Master MIP.

.. seealso::

    The function :aimms:func:`GMP::Instance::Generate`. See Section 16.3.6 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__ for
    more details on extended suffixes.
