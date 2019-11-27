.. aimms:procedure:: DatasetNew(data\_category)

.. _DatasetNew:

DatasetNew
==========

The procedure :aimms:func:`DatasetNew` starts a new unnamed dataset for a specific
data category. The procedure is similar to the command **Dataset New**
from the **Data** menu. The procedure does not change any of the current
data, it only sets the current dataset to unnamed. If you did have a
currently named dataset and the data of this dataset has been changed,
then AIMMS will ask whether or not this dataset should be saved first.

.. code-block:: aimms

    DatasetNew(
            data_category       ! (input) an element of AllDataCategories
            )

Arguments
---------

    *data\_category*
        An element in ``AllDataCategories``, specifying the data category for
        which you want to start a new unnamed dataset.

Return Value
------------

    The procedure returns 1 on success. If the user cancelled the operation,
    then the procedure returns 0. If any other error occurs then the
    procedure returns :math:`-`\ 1 and :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If you use CaseNew, then the name of this new case is not specified
       until you save the case. If you want to start a new named case, then
       you can use the following piece of code:

    .. code-block:: aimms

          if ( CaseGetChangedStatus ) then
              if ( CaseSave = 0 ) then
                  return ;
              endif ;
          endif ;
          if ( CaseSelectNew( a_case ) ) then
              CaseSetCurrent( a_case );
              CaseSetChangedStatus( a_case, 1 );
          endif ;

.. seealso::

    The procedures :aimms:func:`DatasetLoadCurrent`, :aimms:func:`DatasetSave`, :aimms:func:`DatasetSelectNew`, :aimms:func:`DatasetSetCurrent`.
