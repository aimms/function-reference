.. aimms:set:: AllDataCategories

.. _AllDataCategories:

AllDataCategories
=================

The predefined set :aimms:set:`AllDataCategories` contains the names of all data
categories declared within an AIMMS project.

.. code-block:: aimms

        Set AllDataCategories {
            Index      :  IndexDataCategories;
        }

Definition
----------

    The contents of the set :aimms:set:`AllDataCategories` is the collection of all
    data categories defined within the **Data Management Setup** tool of a
    project.

Updatability
------------

    The contents of the set can only be modified by adding or deleting data
    categories in the **Data Management Setup** tool.

.. note::

    -  The function :aimms:func:`DatasetGetCategory` returns the data category of a dataset as an
       element of the set :aimms:set:`AllDataCategories`. The identifiers associated
       with a data category can be obtained through the function :aimms:func:`DataCategoryContents`.

    -  This identifier is only relevant when the chosen
       ``Data_Management_style`` is ``single_data_manager_file``.
