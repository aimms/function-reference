.. aimms:set:: AllColors

.. _AllColors:

AllColors
=========

The predefined set :aimms:set:`AllColors` contains the names of all users colors
associated with an AIMMS project.

.. code-block:: aimms

        Set AllColors {
            Index      :  IndexColors;
        }

Definition
----------

    The contents of the set :aimms:set:`AllColors` is the collection of all user
    colors defined for a particular project through the **User Colors**
    dialog box.

Updatability
------------

    The contents of the set can only be modified through the **User Colors**
    dialog box, or programmatically through the functions :aimms:func:`UserColorAdd` and
    :aimms:func:`UserColorDelete`.

.. note::

    The set :aimms:set:`AllColors` is typically used to allow programmatic assignment
    of colors to data displayed in the graphical end-user interface in a
    data-driven manner.

.. seealso::

    The use of user colors is explained in full detail in :doc:`miscellaneous/user-interface-language-components/setting-colors-within-the-model`.
