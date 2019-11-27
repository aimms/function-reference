.. aimms:procedure:: DialogGetElement(title, reference)

.. _DialogGetElement:

DialogGetElement
================

The procedure :aimms:func:`DialogGetElement` displays a dialog box in which the
user can select an element from a list of set elements.

.. code-block:: aimms

    DialogGetElement(
            title,          ! (input) string expression
            reference       ! (input/output) scalar element parameter
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

Return Value
------------

    The procedure returns 1 if the user has pressed the **OK** button, and 0
    if he has pressed the **Cancel** button.

.. seealso::

    The procedures :aimms:func:`DialogGetElementByText`, :aimms:func:`DialogGetElementByData`, :aimms:func:`DialogGetNumber`.
