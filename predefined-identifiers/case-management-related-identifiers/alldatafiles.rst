.. aimms:set:: AllDataFiles

.. _AllDataFiles:

AllDataFiles
============

The predefined set :aimms:set:`AllDataFiles` contains the references to all data
files stored in the data manager file currently loaded within an AIMMS
project.

.. code-block:: aimms

        Set AllDataFiles {
            Index      :  IndexDataFiles;
            Definition :  AllCases + AllDataSets;
        }

Definition
----------

    The contents of the set :aimms:set:`AllDataFiles` is the collection of (integer)
    references to all data files (i.e. cases and datasets) stored within the
    data manager file currently loaded within an AIMMS project.

Updatability
------------

    The contents of the set can only be modified by adding or deleting cases
    and dataset in the **Data Manager** or through the **Data** menu, or
    using various case and dataset interface functions.

.. note::

    -  Elements of the set :aimms:set:`AllDataFiles` are more commonly referenced
       through its subsets :aimms:set:`AllCases` and :aimms:set:`AllDataSets`.

    -  Further information about the integer data file references can be
       obtained through the functions :aimms:func:`DataFileGetAcronym`, :aimms:func:`DataFileGetDescription`, :aimms:func:`DataFileGetGroup`,
       :aimms:func:`DataFileGetName`, :aimms:func:`DataFileGetOwner`, :aimms:func:`DataFileGetPath` and :aimms:func:`DataFileGetTime`.

    -  The integer data file references stored in the set :aimms:set:`AllDataFiles`
       are only guaranteed to be unique within a single AIMMS session, and,
       furthermore, only within the context of a single data manager file
       associated with a project. As a consequence, additional data file
       information retrieved through the functions listed above must be
       refreshed after opening another data manager file.

.. seealso::

    The sets :aimms:set:`AllCases`, :aimms:set:`AllDataSets`.
