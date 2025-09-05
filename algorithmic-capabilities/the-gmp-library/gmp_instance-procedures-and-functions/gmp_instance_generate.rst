.. aimms:function:: GMP::Instance::Generate(MP, name)

.. _GMP::Instance::Generate:

GMP::Instance::Generate
=======================

The function :aimms:func:`GMP::Instance::Generate` generates a mathematical
program instance from a symbolic mathematical program.

.. code-block:: aimms

    GMP::Instance::Generate(
         MP,             ! (input) a symbolic mathematical program
         [name]          ! (optional) a string expression
         )

Arguments
---------

    *MP*
        A symbolic mathematical program in the set :aimms:set:`AllMathematicalPrograms`. The mathematical
        program should have model type LP, MIP, QP, MIQP, QCP, MIQCP, NLP,
        MINLP, RMIP or RMINLP.

    *name*
        A string that holds the name for the mathematical program to be
        generated.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  If the second argument is not specified, or if it is the empty
       string, the name of the symbolic mathematical program is used to
       create a new element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    -  If an element with name specified by the *name* argument is already
       present in the set :aimms:set:`AllGeneratedMathematicalPrograms` the corresponding generated mathematical
       program will be replaced (or updated in case the same symbolic
       mathematical program is involved or the second argument is not specified). In that
       case all existing solver sessions created for the generated mathematical program will be deleted.

    -  It is possible to generate indexed mathematical program instances.
       See the example in :ref:`sec:gmp.examples.indexed` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  A callback procedure should be installed using the appropriate GMP
       procedure, (e.g., :aimms:func:`GMP::Instance::SetCallbackIterations`) instead
       of using a suffix of the mathematical program (e.g., suffix
       ``CallbackIterations``).

    -  If an error occurs during the execution of
       :aimms:func:`GMP::Instance::Generate`, e.g., if one of the constraints appears
       to be empty and infeasible, then the program status of the
       mathematical program will be set to ``Infeasible`` and the solver
       status to ``PreprocessorError``.


Example
-------

Assume that ``MP`` is a symbolic mathematical program which we want to solve twice thereby changing the constraint set: 

.. code-block:: aimms

    ConstraintSet := { 'C1', 'C2' };
    myGMP1 := GMP::Instance::Generate( MP );
    GMP::Instance::Solve( myGMP1 );
    
    ConstraintSet := { 'C3', 'C4' };
    myGMP2 := GMP::Instance::Generate( MP );

After executing these statements, ``myGMP1`` and ``myGMP2`` will point to the same generated math program,
namely the one using the constraints ``C3`` and ``C4``. The set
:aimms:set:`AllGeneratedMathematicalPrograms` will contain only one element, namely ``MP``. At this point it
makes no difference to use

.. code-block:: aimms

    GMP::Instance::Solve( myGMP1 );

or

.. code-block:: aimms

    GMP::Instance::Solve( myGMP2 );

By using the *name* argument we can create two different GMP's from the same symbolic mathematical program:

.. code-block:: aimms

    ConstraintSet := { 'C1', 'C2' };
    myGMP1 := GMP::Instance::Generate( MP, "FirstGMP" );
    GMP::Instance::Solve( myGMP1 );
    
    ConstraintSet := { 'C3', 'C4' };
    myGMP2 := GMP::Instance::Generate( MP, "SecondGMP" );
    GMP::Instance::Solve( myGMP2 );

This time the set :aimms:set:`AllGeneratedMathematicalPrograms` will contain two elements, namely
``FirstGMP`` and ``SecondGMP``.
               
.. seealso::

    - The routines :aimms:func:`GMP::Instance::Delete` and :aimms:func:`GMP::Instance::SetCallbackIterations`.
