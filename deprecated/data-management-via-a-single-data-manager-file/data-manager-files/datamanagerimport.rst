.. aimms:procedure:: DataManagerImport(filename[, overwrite])

.. _DataManagerImport:

DataManagerImport
=================

With the procedure :aimms:func:`DataManagerImport` you can import the entire data
management tree that is stored in another data file into your current
data management tree. If the imported tree contains cases (or datasets)
that already exist in the current tree, then you can choose whether
these cases (or datasets) should overwrite the current nodes or should
be imported as new nodes.

.. code-block:: aimms

    DataManagerImport(
            filename,       ! (input) a scalar string expression
            [overwrite]     ! (optional) 0, 1 or 2
            )

Arguments
---------

    *filename*
        A string containing the name of the data file that must be imported.

    *overwrite (optional)*
        This integer indicates whether or not existing cases (or datasets) are
        overwritten by cases (or datasets) from the imported file. If 0 (the
        default), then a dialog box is displayed in which the user can decide to
        overwrite the existing node or to create a new node. If 1, then existing
        nodes are always overwritten. If 2, then all imported cases and datasets
        will result in new nodes in the tree.

Return Value
------------

    The procedure returns 1 on success. If the user canceled the operation,
    then the procedure returns 0. If any other error occurs then the
    procedure returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedure :aimms:func:`DataManagerExport`.
