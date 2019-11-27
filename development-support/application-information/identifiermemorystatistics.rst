.. aimms:procedure:: IdentifierMemoryStatistics(IdentSet, OutputFileName, AppendMode, MarkerText, ShowLeaksOnly, ShowTotals, ShowSinceLastDump, ShowMemPeak, ShowSmallBlockUsage, doAggregate)

.. _IdentifierMemoryStatistics:

IdentifierMemoryStatistics
==========================

With the procedure :aimms:func:`IdentifierMemoryStatistics` you can obtain a
report containing the statistics collected by AIMMS' memory manager for
a single or multiple high dimensional identifiers.

.. code-block:: aimms

    IdentifierMemoryStatistics(
         IdentSet,           ! (input) a set of identifiers
         OutputFileName,     ! (input) scalar string expression
         AppendMode,         ! (optional, default 0) scalar numerical expression
         MarkerText          ! (optional) scalar string expression
         ShowLeaksOnly       ! (optional) scalar expression
         ShowTotals          ! (optional) scalar expression
         ShowSinceLastDump   ! (optional) scalar expression
         ShowMemPeak         ! (optional) scalar expression
         ShowSmallBlockUsage ! (optional) scalar expression
         doAggregate         ! (optional, default 0) scalar expression
         )

Arguments
---------

    *IdentSet*
        A subset of :aimms:set:`AllIdentifiers` whose memory statistics are to be reported.

    *OutputFileName*
        A string expression holding the name of the file to which the statistics
        must be written.

    *AppendMode*
        An 0-1 value indicating whether the file must be overwritten or whether
        the statistics must be appended to an existing file.

    *MarkerText*
        A string printed at the top of the memory statistics report.

    *ShowLeaksOnly*
        A 0-1 value that is only used internally by AIMMS. The value specified
        doesn't influence the memory statistics report.

    *ShowTotals*
        A 0-1 value indicating whether the report should include detailed
        information about the total memory use in AIMMS' own memory management
        system until the moment of calling :aimms:func:`IdentifierMemoryStatistics`.

    *ShowSinceLastDump*
        A 0-1 value indicating whether the report should include basic and
        detailed information about the memory use in AIMMS' own memory
        management system since the previous call to
        :aimms:func:`IdentifierMemoryStatistics`.

    *ShowMemPeak*
        A 0-1 value indicating whether the report should include detailed
        information about the memory use in AIMMS' own memory management system,
        when the memory consumption was at its peak level prior to calling
        :aimms:func:`IdentifierMemoryStatistics`.

    *ShowSmallBlockUsage*
        A 0-1 value indicating whether the detailed information about the
        ``MemoryStatistics`` memory use in AIMMS' own memory management system
        is included at all in the memory statistics report. Setting this value
        to 0 results in a report with only the most basic statistical
        information about the memory use.

    *doAggregate*
        A 0-1 value (default 0) indicating whether a single aggregated report is
        to be presented or multiple individual reports.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The procedure prints a report of the statistics collected by AIMMS'
       memory manager since the last call to :aimms:func:`IdentifierMemoryStatistics`.

    -  AIMMS will only collect memory statistics if the option
       ``memory_statistics`` is ``on``.
