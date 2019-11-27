.. aimms:procedure:: MemoryStatistics(OutputFileName, AppendMode, MarkerText, ShowLeaksOnly, ShowTotals, ShowSinceLastDump, ShowMemPeak, ShowSmallBlockUsage, GlobalOnly)

.. _MemoryStatistics:

MemoryStatistics
================

With the procedure :aimms:func:`MemoryStatistics` you can obtain a report
containing the statistics collected by AIMMS' memory manager.

.. code-block:: aimms

    MemoryStatistics(
       OutputFileName,      ! (input) scalar string expression
       AppendMode,          ! (optional, default 0) scalar numerical expression
       MarkerText,          ! (optional, default empty) scalar string expression
       ShowLeaksOnly,       ! (optional, default 0) scalar numerical expression
       ShowTotals,          ! (optional, default 1) scalar numerical expression
       ShowSinceLastDump,   ! (optional, default 1) scalar numerical expression
       ShowMemPeak,         ! (optional, default 0) scalar numerical expression
       ShowSmallBlockUsage, ! (optional, default 0) scalar numerical expression
       GlobalOnly           ! (optional, default 0) scalar numerical expression
     )

Arguments
---------

    *OutputFileName*
        A string expression holding the name of the file to which the statistics
        must be written color to modify.

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
        system until the moment of calling MemoryStatistics.

    *ShowSinceLastDump*
        A 0-1 value indicating whether the report should include basic and
        detailed information about the memory use in AIMMS' own memory
        management system since the previous call to MemoryStatistics.

    *ShowMemPeak*
        0-1 value indicating whether the report should include detailed
        information about the memory use in AIMMS' own memory management system,
        when the memory consumption was at its peak level prior to calling
        MemoryStatistics.

    *ShowSmallBlockUsage*
        0-1 value indicating whether the detailed information about the memory
        use in AIMMS' own memory management system is included at all in the
        memory statistics report. Setting this value to 0 results in a report
        with only the most basic statistical information about the memory use.

    *GlobalOnly*
        A 0-1 value indicating whether only memory used by the global memory
        manager (i.e. the 'main' memory manager of AIMMS, as opposed to seperate
        memory manager for individual higher-dimensional identifiers) is
        reported in the memory statistics file.

Return Value
------------

    The procedure prints a report of the statistics collected by AIMMS'
    memory manager since the last call to :aimms:func:`MemoryStatistics`.

.. note::

    AIMMS will only collect memory statistics if the option
    ``memory_statistics`` is ``on``.
