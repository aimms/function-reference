.. aimms:procedure:: DialogGetElementByData(title, reference, element\_data)

.. _DialogGetElementByData:

DialogGetElementByData
======================

The procedure :aimms:func:`DialogGetElementByData` is an extension of the
procedure ``DialogGetElementByText``. Instead of only showing a list box
with only a single string per element, this procedure allows you to show
a list box with multiple columns of text per element. The text that is
displayed in each column is specified via a 2-dimensional string
parameter. The first dimension of this parameter corresponds to the rows
of the list box, the second dimension corresponds to the column in the
listbox.

.. code-block:: aimms

    DialogGetElementByData(
            title,          ! (input) string expression
            reference,      ! (input/output) scalar element parameter
            element_data    ! (input) 2-dimensional string parameter
            )

Arguments
---------

    *title*
        A scalar string expression containing the text you want to display as
        title of the dialog box.

    *reference*
        A scalar element parameter. When creating the dialog box, the range set
        of this parameter is used to fill the list with elements, and the
        current value of the element parameter will be initially selected. On
        return, this parameter will refer to the selected element.

    *element\_data*
        A 2-dimensional string parameter. The first index in its domain should
        matches the range set of the element parameter *reference*, the second
        index defines the number of columns that are shown. Instead of the
        element names, the dialog box will display multiple columns of text
        derived from this parameter.

Return Value
------------

    The procedure returns 1 if the user has pressed the **OK** button, and 0
    if he has pressed the **Cancel** button.

.. seealso::

    The procedures :aimms:func:`DialogGetElement`, :aimms:func:`DialogGetElementByText`.
