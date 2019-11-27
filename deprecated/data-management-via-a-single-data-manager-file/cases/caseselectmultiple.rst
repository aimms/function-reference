.. aimms:procedure:: CaseSelectMultiple([cases\_only])

.. _CaseSelectMultiple:

CaseSelectMultiple
==================

The procedure :aimms:func:`CaseSelectMultiple` shows a dialog box in which the
user can select a number of cases (and datasets). The selected subset of
cases and datasets is stored in the pre-defined set
``CurrentCaseSelection``, which is used in the page objects for which
the property **Multiple Cases** is set.

.. code-block:: aimms

    CaseSelectMultiple(
            [cases_only]    ! (optional) 0 or 1
            )

Arguments
---------

    *cases\_only (optional)*
        This argument controls whether the user can only select cases or can
        select both datasets and cases. If this argument is omitted, then the
        default value is 0, which means that both cases and datasets can be
        selected.

Return Value
------------

    The procedure returns 1 if the user pressed the **OK** button, and 0 if
    the user pressed **Cancel**.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseDialogSelectMultiple`
       instead.
