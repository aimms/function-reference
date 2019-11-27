.. aimms:procedure:: UserColorModify(color\_name, red, green, blue)

.. _UserColorModify:

UserColorModify
===============

With the procedure :aimms:func:`UserColorModify` you can programmatically modify
an existing color in the set of user colors.

.. code-block:: aimms

    UserColorModify(
         color_name,           ! (input) scalar string expression
         red,                 ! (input) scalar numerical expression
         green,               ! (input) scalar numerical expression
         blue                 ! (input) scalar numerical expression
         )

Arguments
---------

    *color\_name*
        A string expression holding the name of the user color to modify.

    *red*
        An integer value in the range :math:`0\dots 255` indicating the red
        component in the RGB value of the color.

    *green*
        An integer value in the range :math:`0\dots 255` indicating the green
        component in the RGB value of the color.

    *blue*
        An integer value in the range :math:`0\dots 255` indicating the blue
        component in the RGB value of the color.

Return Value
------------

    The procedure returns 1 if the color could be modified successfully, and
    0 if the color does not exist, or is contained in the fixed set of
    project colors.

.. note::

    You can only modify user colors that have been added using the procedure
    ``UserColorAdd``. Colors added through the **Tools-User Colors** dialog
    box are fixed and cannot be deleted or modified.

.. seealso::

    :aimms:func:`UserColorAdd`, :aimms:func:`UserColorDelete`, :aimms:func:`UserColorGetRGB`. User colors are discussed in full
    detail in Section 11.4 of the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.
