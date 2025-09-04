.. aimms:procedure:: RetrieveCurrentVariableValues(Variables)

.. _RetrieveCurrentVariableValues:

RetrieveCurrentVariableValues
=============================

With the procedure :aimms:procedure:`RetrieveCurrentVariableValues` you can obtain the
variable values for a given collection of variables during a running
solution process. This procedure can only be called from within the
context of a solver callback procedure.

.. code-block:: aimms

    RetrieveCurrentVariableValues(
         Variables    ! (input) a subset of AllVariables
         )

Arguments
---------

    *Variables*
        A subset of :aimms:set:`AllVariables`, holding all the variables for which you want to
        retrieve the current values.

.. seealso::

    -   Solver callback procedures are discussed in full detail in :doc:`optimization-modeling-components/solving-mathematical-programs/suffices-and-callbacks` 
        of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__
