.. aimms:function:: Execute(executable[, commandline, workdir, wait, minimized])

.. _Execute:

Execute
=======

With the :aimms:func:`Execute` procedure you can start another application.

.. code-block:: aimms

    Execute(
         executable,          ! (input) scalar string expression
         [commandline,]       ! (optional) scalar string expression
         [workdir,]           ! (optional) scalar string expression
         [wait,]              ! (optional) 0 or 1
         [minimized]          ! (optional) 0 or 1
         )

Arguments
---------

    *executable*
        A string representing the name of the program that you want to execute.

    *commandline (optional)*
        A string representing the arguments that you want to pass to the
        program.

    *workdir (optional)*
        A string representing the directory where the program should start in.
        If omitted, then the current project directory is used. Please note that
        this argument does not specify the folder where the executable is
        located. Rather, it specifies the folder that the executable should use
        as its working folder.

    *wait (optional)*
        This argument indicates whether or not AIMMS will wait for the program
        to finish. The default value is 0 (not wait).

    *minimized (optional)*
        This argument indicates whether or not the program should run in a
        minimized state. The default is 0 (not minimized).

.. note::

    *   When running on Linux and the program is located in the AIMMS project
        folder, the program name must be prefixed with ``./``.

    *   On Linux, ensure the program has the permission to execute.
        To ensure ``myprog`` is executable, whereby ``myprog`` is in the current directory:
        
        .. code-block:: aimms 
            :linenos:

            Execute(
                Executable  :  "chmod", 
                CommandLine :  " a+rx ./myprog ");
                
    *   On Linux, avoid using redirects in the command line (using chacters ``>``, ``<``, and ``|``.

    *   As a general rule, you should not wait for interactive windowed
        applications. Waiting for the termination of a program is necessary when
        the program does some form of external data processing which is required
        for the execution of your model.


.. seealso::

    The procedure :aimms:func:`OpenDocument`.
