.. aimms:function:: SQLViewName(Datasource, ViewNo, Owner)

.. _SQLViewName:

SQLViewName
===========

With the function :aimms:func:`SQLViewName` you can determine the name of a
certain view in a datasource. This function is designed to be used in
conjunction with the ``SQLNumberOfViews`` function.

.. code-block:: aimms

    SQLViewName(
         Datasource,          ! (input) a string expression
         TableNo,             ! (input) an integer expression
         Owner                ! (input/optional) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *ViewNo*
        An integer containing the number of the view for which you want to
        retrieve the name. To determine the maximum value of this argument,
        please use the function ``SQLNumberOfViews`` prior to calling this
        function. The minimum value of this argument is 1.

    *Owner*
        A string containing the owner of the view for which the name must be
        determined. If the datasource doesn't support the owner concept, but the
        owner argument is specified, an error will be raised.

Return Value
------------

    The function returns the name of the view, with the number as specified
    through the ``ViewNo`` argument.

.. note::

    Typically, this function can best be used in a construction like the
    following: 

    .. code-block:: aimms

            NumberOfViews := SQLNumberOfViews("MyDataSource");

            while LoopCount <= NumberOfViews do
                ViewName := SQLViewName("MyDataSource", LoopCount);
                ! Do something with the retrieved view name here...
            endwhile;

.. seealso::

    The functions :aimms:func:`SQLNumberOfViews` and :aimms:func:`SQLTableName`.
