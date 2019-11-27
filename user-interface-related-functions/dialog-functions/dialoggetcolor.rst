.. aimms:procedure:: DialogGetColor(r, g, b)

.. _DialogGetColor:

DialogGetColor
==============

The procedure :aimms:func:`DialogGetColor` displays a standard Windows color
selection dialog box. The procedure returns the color (RGB values)
selected by the user.

.. code-block:: aimms

    DialogGetColor(
            r,           ! (input/output) scalar numerical parameter
            g,           ! (input/output) scalar numerical parameter
            b            ! (input/output) scalar numerical parameter
            )

Arguments
---------

    *r*
        A scalar numerical paramter containing the red value of the selected
        color.

    *g*
        A scalar numerical paramter containing the green value of the selected
        color.

    *b*
        A scalar numerical paramter containing the blue value of the selected
        color.

Return Value
------------

    The procedure returns 1 if the user completed the color selection dialog
    box successfully, or 0 otherwise.
