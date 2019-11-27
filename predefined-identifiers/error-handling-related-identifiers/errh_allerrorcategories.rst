.. aimms:set:: errh::AllErrorCategories

.. _errh::AllErrorCategories:

errh::AllErrorCategories
========================

The predefined set :aimms:set:`errh::AllErrorCategories` contains the error
categories that can be assigned to an error.

.. code-block:: aimms

        Set AllErrorCategories {
            Index      :  IndexErrorCategories;
        }

The names below are the elements in the set. The elements are shown
indented in order to show the structure that is used by the function
``errh::InsideCategory``.

Engine
   Errors from the AIMMS engine.

   Internal
      This is about AIMMS internal logic that fails. These types of
      errors shouldn't occur, but if they do, they should be handled.
      Severe internal errors (after generating a dump file) and internal
      assertions that fail

   Authorization
      Protecting the intellectual property of the developer of the AIMMS
      application. % Your money

   Licensing
      Protecting the intellectual property of the developers of the
      AIMMS system. % Our money

   Memory
      Running out of memory.

   Limit
      Reaching an AIMMS limit.

   Compiler
      Errors detected by the AIMMS compiler.

      Syntax
         Errors related to the form of AIMMS model text.

      Semantics
         Errors related to the (allowed) interpretation of AIMMS model
         text.

      Legacy
         Errors related to GAMS, AIMMS 2 or the conversion from a GAMS
         or AIMMS 2 model to AIMMS 3.

   Execution
      Errors detected by the AIMMS execution engine.

      Math
         Errors such as division by zero, sqrt or log of a negative
         number.

      InvalidArgument
         Passing invalid arguments to the intrinsic functions of AIMMS.

      Unit
         Runtime unit consistency checks that fail.

      IO
         Database, File and Case IO errors.

      External
         Passing argument data to / from external functions and
         procedures and errors generated during the execution of
         external functions.

      Generation
         Runtime errors that occur during the generation of a
         mathematical program

      MathematicalProgramming
         Violating the requirements of a particular mathematical
         programming class, or the selection of a mathematical
         programming class that is too difficult or too easy for the
         problem at hand.

      NonlinearEvaluation
         Errors that happen during the evaluation of the (derivatives)
         of a constraint.

Solver
   Errors from the solution algorithms as part of the entire AIMMS
   package.

GUI
   Errors on pages

User
   Errors from ``RAISE`` statements or ``ASSERT`` statements.

Updatability
------------

    The contents of this set cannot be modified.
