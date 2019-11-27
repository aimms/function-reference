.. aimms:procedure:: UserColorGetRGB(color\_name, red, green, blue)

.. _UserColorGetRGB:

UserColorGetRGB
===============

With the procedure :aimms:func:`UserColorGetRGB` you can programmatically obtain
the RGB values of a color in the set of user colors.

.. code-block:: aimms

    UserColorGetRGB(
         color_name,          ! (input) scalar string expression
         red,                 ! (output) scalar numerical parameter
         green,               ! (output) scalar numerical parameter
         blue                 ! (output) scalar numerical parameter
         )

Arguments
---------

    *color\_name*
        A string expression holding the name of the user color to query.

    *red*
        An scalar parameter that, on return, holds the red component in the RGB
        value of the color.

    *green*
        An scalar parameter that, on return, holds the green component in the
        RGB value of the color.

    *blue*
        An scalar parameter that, on return, holds the blue component in the RGB
        value of the color.

Return Value
------------

    The procedure returns 1 if the color exists in the set of user colors,
    or 0 if the color does not exist.

.. seealso::

    :aimms:func:`UserColorAdd`, :aimms:func:`UserColorDelete`, :aimms:func:`UserColorModify`. User colors are discussed in full
    detail in Section 11.4 of the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.
