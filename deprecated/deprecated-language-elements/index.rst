.. _chap:Deprecated:

Deprecated Language Elements
============================

The current implementation of AIMMS supports the following deprecated
features, but it may cease to do so in a future implementation. The
current implementation does so to support converted ``GAMS`` and AIMMS 2
applications.

.. _sec:deprecated.keywords:

Deprecated Keywords
-------------------

The keywords for which direct replacements are available are documented
in :numref:`table:old.new.keywords`.

.. _table:old.new.keywords:

.. table:: AIMMS deprecated keywords and their modern equivalents 

    ================================= =================================
    **Deprecated**                    **Modern equivalent**
    ================================= =================================
    ``clean``                         ``CleanDependents``
    ``CumulativeDistribution``        ``DistributionCumulative``
    ``eps``                           ``zero``
    ``evaluate``                      ``update``
    ``FailureCount``                  ``FailCount``
    ``InverseCumulativeDistribution`` ``DistributionInverseCumulative``
    ``maximise``                      ``maximize``
    ``maximising``                    ``maximize``
    ``maximizing``                    ``maximize``
    ``minimise``                      ``minimize``
    ``minimising``                    ``minimize``
    ``minimizing``                    ``minimize``
    ``net_inflow``                    ``netinflow``
    ``net_outflow``                   ``netoutflow``
    ``puttl``                         ``puthd``
    ================================= =================================

The Deprecated Keyword ``abort``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The keyword ``abort`` is a GAMS keyword that can be followed by a
condition and a list of identifiers to be displayed. The execution run
is interrupted after executing this statement. Suggested rewrite: use a
``display`` statement followed by a ``halt`` statement or a
``raise error`` statement. See also

-  ``display`` (see :doc:`data-communication-components/text-reports-and-output-listing/the-display-statement` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__),

-  ``halt`` (see :ref:`sec:exec.flow.halt` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__) and

-  ``raise error`` (see :ref:`sec:exec.error.raising` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__).

The Deprecated Keywords ``yes`` and ``no``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The keywords ``yes`` and ``no`` are GAMS keywords that can be used in
assignments to sets in order to add or remove elements. Suggested
rewrite: use the AIMMS set syntax. For instance, replace 

.. code-block:: aimms

        s1(i) $ cond1(i) := yes ;
        s2(i) $ cond2(i) := no  ;

by the following code: 

.. code-block:: aimms

        s1 += { i | cond1(i) } ;
        s2 -= { i | cond2(i) } ;

The Deprecated Keyword ``system``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GAMS keyword ``system`` is followed by a suffix. The AIMMS language
supports the following equivalent code for selected ``system`` suffixes
as documented in Table :numref:`table:deprecated.gams.system.suffices`.

.. _table:deprecated.gams.system.suffices:

.. table:: The keyword ``system`` and selected suffixes with their modern counterparts 

    ============== ==================================================
    **Deprecated** **Modern equivalent**
    ============== ==================================================
    ``.date``      ``CurrentToString("%Am|AllAbbrMonths| %d, %c%y")``
    ``.time``      ``CurrentToString("%H:%M:%S")``
    ``.version``   ``AimmsRevisionString(string parameter, 4);``
    ``.page``      ``currentOutputFile.PageNumber``
    ============== ==================================================

The system suffixes ``.ifile``, ``.ofile``, ``.rdate``, ``.rfile``,
``.rtime``, ``.sfile``, and ``.title`` are pointless within the AIMMS
environment.

.. _sec:deprecated.intrinsics:

Deprecated Intrinsic Procedures and Functions
---------------------------------------------

The mapping of the removed matrix manipulation procedures to GMP procedures and
functions is documented in :ref:`sec:depr_mm_proc`. The following GMP procedures
are deprecated:

-  The procedure ``GMP::Instance::DeleteSolverSession`` has been replaced by
   :any:`SolverSession::Delete`.

The following intrinsic functions are deprecated, but can be replaced by an
equivalent call to an existing intrinsic procedure or function:

-  ``FindRString( SearchString, Key, CaseSensitive, WordOnly, IgnoreWhite)``
   can be replaced by a call to
   ``FindNthString( SearchString, Key, -1, CaseSensitive, WordOnly, IgnoreWhite)``
   where ``-1`` indicates that searching should be done right to left,
   see also :aimms:func:`FindNthString`.

-  One may replace ``SQLDirect`` with ``DirectSQL``

-  One may replace ``StringToLabel`` with ``StringToElement``

The deprecated iterative operators are documented in :numref:`table:deprecated.iterative.operators`.

.. _table:deprecated.iterative.operators:

.. table:: AIMMS deprecated iterative operators and their modern equivalents 

    ============== =====================
    **Deprecated** **Modern equivalent**
    ============== =====================
    ``smax``       ``max``
    ``smin``       ``min``
    ``arg``        ``nth``
    ============== =====================

.. _sec:deprecated.suffices:

Deprecated Suffixes
-------------------

.. _table:old.new.suffices:

.. table:: AIMMS deprecated suffixes and their modern equivalents 

    ========================= ==================================
    **Deprecated**            **Modern equivalent**
    ========================= ==================================
    **Variables**            
    ``.l``                    ``.level``
    ``.lo``                   ``.lower``
    ``.up``                   ``.upper``
    ``.freeze``               ``.nonvar``
    ``.prior``                ``.priority``
    **Files**                
    ``.bm``                   ``.BottomMargin``
    ``.cc``                   ``.BodyCurrrentColumn``
    ``.cr``                   ``.BodyCurrrentRow``
    ``.ftcc``                 ``.FooterCurrrentColumn``
    ``.ftcr``                 ``.FooterCurrrentRow``
    ``.ftll``                 ``.HeaderSize``
    ``.hdcc``                 ``.HeaderCurrrentColumn``
    ``.hdcr``                 ``.HeaderCurrrentRow``
    ``.hdll``                 ``.FooterSize``
    ``.lm``                   ``.LeftMargin``
    ``.lp .pn``               ``.PageNumber``
    ``.pc``                   ``.PageMode``
    ``.ps``                   ``.PageSize``
    ``.pw``                   ``.PageWidth``
    ``.tm``                   ``.TopMargin``
    **Mathematical programs**
    ``.bestest`` ``.objest``  ``.BestBound``
    ``.CallbackNewIncumbent`` ``.CallbackIncumbent``
    ``.iterusd``              ``.iterations``
    ``.nodusd``               ``.nodes``
    ``.number``               ``.SolverCalls``
    ``.numequ``               ``.NumberOfConstraints``
    ``.numinfes``             ``.NumberOfInfeasibilities``
    ``.numintvar``            ``.NumberOfIntegerVariables``
    ``.numnlequ``             ``.NumberOfNonlinearConstraints``
    ``.numnlins``             ``.NumberOfNonlinearInstructions``
    ``.numnlnz`` ``.numnlz``  ``.NumberOfNonlinearNonzeros``
    ``.numnlvar``             ``.NumberOfNonlinearVariables``
    ``.numnz``                ``.NumberOfNonzeros``
    ``.numSOS1``              ``.NumberOfSOS1Constraints``
    ``.numSOS2``              ``.NumberOfSOS2Constraints``
    ``.numvar``               ``.NumberOfVariables``
    ``.objval``               ``.Objective``
    ``.resgen``               ``.GenTime``
    ``.resusd``               ``.SolutionTime``
    ``.suminfes``             ``.SumOfInfeasibilities``
    ========================= ==================================

Most deprecated suffixes can be directly translated into their modern
equivalents, as documented in :numref:`table:old.new.suffices`. The following suffixes
deserve some more consideration:

-  ``.ap`` The append mode of a file, 0: replace contents when opening
   the file, 1: append to file. This functionality is now covered by the
   ``mode`` attribute of that file, see :doc:`data-communication-components/text-reports-and-output-listing/the-file-declaration` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

-  ``.m`` The marginal value of a variable or constraint. For a
   constraint the suffix ``.m`` should be replaced by the suffix
   ``.ShadowPrice``. For a variable the suffix ``.m`` should be replaced
   by the suffix ``.ReducedCost``.

-  ``.modelstat`` This suffix of a mathematical program is numeric, it
   should be replaced by the element valued suffix ``.ProgramStatus``.
   Note that
   ``Element( AllSolutionStates, mp.solvestat+1 ) = mp.ProgramStatus``.
   See also :ref:`table:mp.status` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__ and
   :aimms:set:`AllSolutionStates`.

-  ``.solvestat`` or ``.solverstat`` These suffixes of a mathematical
   program are numeric, they should be replaced by the element valued
   suffix ``.SolverStatus``. Note that
   ``Element( AllSolutionStates, mp.solvestat+15 ) = mp.SolverStatus``.
   See also :ref:`table:mp.status` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__ and
   :aimms:set:`AllSolutionStates`.

-  ``.dim`` This should be replaced by a call to :aimms:func:`IdentifierDimension`.

-  ``.txt`` This should be replaced by a call to :aimms:func:`IdentifierText`.

-  ``.type`` This should be replaced by a call to :aimms:func:`IdentifierType`.
