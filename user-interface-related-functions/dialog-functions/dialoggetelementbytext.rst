.. aimms:procedure:: DialogGetElementByText(message, reference, element\_text)

.. _DialogGetElementByText:

DialogGetElementByText
======================

The procedure :aimms:func:`DialogGetElementByText` displays a dialog box in which
the user can select an element from a set. However, other than
``DialogGetElement``, this procedure does not show a list of element
names but a list of strings, which are given as a separate argument to
the procedure.

.. code-block:: aimms

    DialogGetElementText(
            message,        ! (input) string expression
            reference,      ! (input/output) scalar element parameter
            element_text    ! (input) 1-dimensional string parameter
            )

Arguments
---------

    *message*
        A scalar string expression containing the text you want to display as
        title of the dialog box.

    *reference*
        A scalar element parameter. When creating the dialog box, the range set
        of this parameter is used to fill the list with elements, and the
        current value of the element parameter will be initially selected. On
        return, this parameter will refer to the selected element.

    *element\_text*
        A 1-dimensional string parameter, with a domain that matches the range
        set of the element parameter *reference*. Instead of the element names,
        the dialog box will display the corresponding strings of this parameter.

Return Value
------------

    The procedure returns 1 if the user has pressed the **OK** button, and 0
    if he has pressed the **Cancel** button.

.. seealso::

    The procedures :aimms:func:`DialogGetElement`, :aimms:func:`DialogGetElementByData`.
