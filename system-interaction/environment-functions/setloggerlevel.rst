.. aimms:procedure:: SetLoggerLevel(logger,level)

.. _SetLoggerLevel:

SetLoggerLevel
======================

The procedure :aimms:func:`SetLoggerLevel` modifies the logging threshold for a specific logger during model execution.

.. code-block:: aimms

    SetLoggerLevel(
         logger,              ! (input) scalar string expression
         level                ! (input) scalar string expression
         )

Arguments
---------

    *logger* 
        The name of the logger as a string.

    *level*  
        The new level for the logger as a string.
        Valid strings (in increasing order of severity) are: 
        ``'trace'``, ``'debug'``, ``'info'``, ``'warn'``, or ``'error'``.

Return Value
------------

The procedure returns the old level as a string.

