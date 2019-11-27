.. aimms:procedure:: UserColorAdd(color\_name, red, green, blue)

.. _UserColorAdd:

UserColorAdd
============

With the procedure :aimms:func:`UserColorAdd` you can programmatically add a new
color to the set of user colors.

.. code-block:: aimms

    UserColorAdd(
         color_name,          ! (input) scalar string expression
         red,                 ! (input) scalar numerical expression
         green,               ! (input) scalar numerical expression
         blue                 ! (input) scalar numerical expression
         )

Arguments
---------

    *color\_name*
        A string expression holding the name of the user color to add.

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

    The procedure returns 1 if the color could be added successfully, or 0
    if the color already exists.

.. note::

    Only project colors, i.e. colors added through the **Tools-User Colors**
    dialog box, are persistent. User colors that are added to a project
    using the procedure :aimms:func:`UserColorAdd` do not persist, and, therefore,
    have to be added during the initialization of every project session.

.. seealso::

    :aimms:func:`UserColorDelete`, :aimms:func:`UserColorGetRGB`, :aimms:func:`UserColorModify`. User colors are discussed in full
    detail in Section 11.4 of the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.
