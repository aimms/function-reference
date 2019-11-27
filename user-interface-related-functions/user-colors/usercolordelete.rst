.. aimms:procedure:: UserColorDelete(color\_name)

.. _UserColorDelete:

UserColorDelete
===============

With the procedure :aimms:func:`UserColorDelete` you can programmatically delete a
color from the set of user colors.

.. code-block:: aimms

    UserColorDelete(
         color_name            ! (input) scalar string expression
         )

Arguments
---------

    *color\_name*
        A string expression holding the name of the user color to delete.

Return Value
------------

    The procedure returns 1 if the color could be deleted successfully, or 0
    if the color does not exist, or is contained in the fixed set of project
    colors.

.. note::

    You can only delete user colors that have been added using the procedure
    ``UserColorAdd``. Colors added through the **Tools-User Colors** dialog
    box are fixed and cannot be deleted or modified.

.. seealso::

    :aimms:func:`UserColorAdd`, :aimms:func:`UserColorGetRGB`, :aimms:func:`UserColorModify`. User colors are discussed in full
    detail in Section 11.4 of the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.
