.. aimms:procedure:: GMP::Instance::GetInfeasibleData(GMP, parSet, message, method, effort, textFormat)

.. _GMP::Instance::GetInfeasibleData:

GMP::Instance::GetInfeasibleData
================================

| Usually, methods for detecting the cause of an infeasibiliy in a mathematical model
  return information about constraints and variables. The procedure
  :aimms:func:`GMP::Instance::GetInfeasibleData` uses a different approach, namely, it
  can be used to retrieve information about parameters that cause a (linear)
  mathematical program to become infeasible.
| 
| This procedure only considers parameters without a definition, i.e.,
  parameters that can be changed by, e.g., an end user.
| 
| This procedure returns information in two ways. First, it will fill the output
  *message* argument with a text describing the cause of the infeasibility.
  Second, it will fill the suffix ``.SuspicionLevel`` for each parameter that contributes
  to the infeasibility. This suffix may be used to assign identifier
  `annotations <https://documentation.aimms.com/webui/css-styling.html#data-dependent-styling>`_
  to the parameters of interest. Such annotations may be subsequently used in order to highlight
  the suspicious values of those parameters in the graphical user interface and visually
  notify the user about potentially incorrect data values.

.. code-block:: aimms

    GMP::Instance::GetInfeasibleData(
         GMP,            ! (input) a generated mathematical program
         parSet,         ! (input) a set of parameters
         message,        ! (output) a string parameter
         [method],       ! (optional) a scalar integer value
         [effort],       ! (optional) a scalar integer value
         [textFormat]    ! (optional) a scalar binary value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *parSet*
        A subset of :aimms:set:`AllParameters`.

    *message*
        A string that describes the cause of the infeasibility.

    *method*
        An integer scalar value between 0 and 4 that specifies the method used to find
        the cause of the infeasibility. Default is 0. The methods are described below.

    *effort*
        An integer scalar value between 0 and 2 that specifies the effort level used
        by this procedure to find the cause of the infeasibility. Default is 2. A higher
        value means more effort.

    *textFormat*
        A scalar binary value to indicate whether the message should use plain text
        (value 0; the default) or HTML formatting (value 1).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *GMP* must be linear.

    -  Typically, :aimms:set:`AllParameters` is passed to the *parSet* argument.

    -  The procedure :aimms:func:`GMP::Instance::GetInfeasibleData` will use one of the
       following methods, as specified by the *method* argument:

       - 0: IIS (default)

       - 1: Solve feasibility problem: minimize sum of infeasibilities

       - 2: Solve feasibility problem: minimize largest infeasibility

       - 3: Solve feasibility problem: minimize sum of infeasibilities after scaling model

       - 4: Solve feasibility problem: minimize largest infeasibility after scaling model

    -  The calculation of the IIS or solving the feasibility problem can be time consuming
       if the model is large or complex, and as a consequence, the procedure
       :aimms:func:`GMP::Instance::GetInfeasibleData` will then be time consuming.
    
    -  The *effort* level influences how much effort is used to find outliers in the (infeasible)
       data. It does not influence the running time of the *method* used.

    -  If the text attribute of a parameter is specified then it will be used in the *message*,
       otherwise the identifier name.
       
    -  If the `webui::ElementTextIdentifier <https://documentation.aimms.com/webui/multi-language.html#element-text>`_
       attribute of a set is specified then it will be used to print the set elements in the *message*.
    
    -  The option ``Element format`` determines the format used for printing elements in the *message*.

    -  The suffix ``.SuspicionLevel`` gets a value from the set `AllSuspicionLevels`, or remains empty
       if the parameter is not part of the infeasible data.

    -  The procedure :aimms:func:`GMP::Instance::GetInfeasibleData` is not supported for generated
       mathematical programs created by one of the following functions:

       -  GMP::Instance::GenerateRobustCounterpart,
       
       -  GMP::Instance::GenerateStochasticProgram,
       
       -  GMP::Instance::CreatePresolved,
       
       -  GMP::Instance::CreateDual, or
       
       -  GMP::Instance::CreateMasterMIP.

Example
-------

Assume that ``MP`` is a symbolic mathematical program and ``pMessage`` a string parameter.

.. code-block:: aimms

    solve MP;
    
    if ( MP.ProgramStatus = 'Infeasible'            or
        MP.ProgramStatus = 'InfeasibleOrUnbounded' ) then
        GMP::Instance::GetInfeasibleData( 'MP', AllParameters, pMessage,
                                            method: 4, textFormat: 1 );
        
        ! Change the font size for the HTML formatted text.
        pMessage := "<span style=\"font-size: 20px\">" + pMessage + "</span>";
    endif;

.. seealso::

    -  Section `Explainability <https://documentation.aimms.com/language-reference/optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/managing-generated-mathematical-program-instances.html#explainability>`_ in the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
    -  Example `Infeasible Data <https://how-to.aimms.com/Articles/662/662-infeasible_data.html>`__.
