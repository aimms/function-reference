.. aimms:function:: DirectoryOfLibraryProject(libraryname, directoryname)

.. _DirectoryOfLibraryProject:

DirectoryOfLibraryProject
==========================

Via the procedure :aimms:func:`DirectoryOfLibraryProject` the name of the folder (directory) where a library is located can be obtained. This is the folder where the corresponding `Project.xml` file exists.

.. code-block:: aimms

    DirectoryOfLibraryProject(
        libraryname,  ! (input) a scalar string
        directoryname ! (output) a scalar string
    )

Arguments
---------

    *libraryname* 
        The name of the library or the name of the library prefix.

    *directoryname* 
        The full path to the folder where the `Project.xml` file of the library is located.

Return value
-------------

    Returns 1 on success, 0 if the library cannot be found in the current AIMMS application.