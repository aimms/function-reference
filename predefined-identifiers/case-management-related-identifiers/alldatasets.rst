.. aimms:set:: AllDataSets

.. _AllDataSets:

AllDataSets
===========

The predefined set :aimms:set:`AllDataSets` contains the references to all
datasets stored in the data manager file currently loaded within an
AIMMS project.

.. code-block:: aimms

        Set AllDataSets {
            SubsetOf   :  AllDataFiles;
            Index      :  IndexDataSets;
        }

Definition
----------

    The contents of the set :aimms:set:`AllDataSets` is the collection of (integer)
    references to all datasets stored within the data manager file currently
    loaded within an AIMMS project.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    datasets in the **Data Manager**, by saving cases in the **Data** menu,
    or through the functions :aimms:func:`DatasetCreate`, :aimms:func:`DatasetDelete` and :aimms:func:`DatasetSaveAs`.

.. note::

    -  Further information about the integer dataset references can be
       obtained through the functions :aimms:func:`DataFileGetAcronym`, :aimms:func:`DataFileGetDescription`, :aimms:func:`DataFileGetGroup`,
       :aimms:func:`DataFileGetName`, :aimms:func:`DataFileGetOwner`, :aimms:func:`DataFileGetPath` and :aimms:func:`DataFileGetTime`.

    -  The integer dataset references stored in the set :aimms:set:`AllDataSets` are
       only guaranteed to be unique within a single AIMMS session, and,
       furthermore, only within the context of a single data manager file
       associated with a project. As a consequence, additional case
       information retrieved through the functions listed above must be
       refreshed after opening another data manager file.

    -  This identifier is only relevant when the chosen
       ``Data_Management_style`` is ``single_data_manager_file``.
