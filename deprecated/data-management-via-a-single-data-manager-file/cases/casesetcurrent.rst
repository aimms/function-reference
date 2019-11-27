.. aimms:procedure:: CaseSetCurrent(case)

.. _CaseSetCurrent:

CaseSetCurrent
==============

The procedure :aimms:func:`CaseSetCurrent` sets the case that is regarded as the
current case. It does not load or save any data or checks whether data
needs to be saved. You can, for example, use it to make a newly created
case the current case, so that during a ``CaseSave`` the data is written
to this case.

.. code-block:: aimms

    CaseSetCurrent(
            case               ! (input) element of the set AllCases
            )

Arguments
---------

    *case*
        An element of the set ``AllCases``, refering to the case that should
        become the current case.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseFileSetCurrent`
       instead.

.. seealso::

    The procedures :aimms:func:`CaseNew`, :aimms:func:`CaseCreate`, :aimms:func:`CaseSelectNew`, :aimms:func:`CaseSave`.
