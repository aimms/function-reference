.. aimms:function:: SQLNumberOfViews(Datasource, Owner)

.. _SQLNumberOfViews:

SQLNumberOfViews
================

With the function :aimms:func:`SQLNumberOfViews` you can determine the number of
views in a datasource.

.. code-block:: aimms

    SQLNumberOfViews(
         Datasource,          ! (input) a string expression
         Owner                ! (input/optional) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *Owner*
        A string containing the owner for which the number of views must be
        determined. If the datasource doesn't support the owner concept, but the
        owner argument is specified, an error will be raised.

Return Value
------------

    The function returns the number of views in the specified datasource. If
    there are no views for the specified datasource and owner, 0 is
    returned. If an error occurs when determining the number of views, -1 is
    returned and an error message is displayed in the error window.

.. seealso::

    The functions :aimms:func:`SQLNumberOfTables`, :aimms:func:`SQLNumberOfColumns` and :aimms:func:`SQLViewName`.
