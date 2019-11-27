.. aimms:procedure:: SetElementRename(Setname, Element, Newname)

.. _SetElementRename:

SetElementRename
================

With the procedure :aimms:procedure:`SetElementRename` you can rename an element in a
set.

.. code-block:: aimms

    SetElementRename(
         Setname,        ! (input) a set
         Element,        ! (input) an element parameter
         Newname         ! (input) a scalar string expression
         )

Arguments
---------

    *Setname*
        The root set or subset in which you want to rename an element.

    *Element*
        The element that you want to rename.

    *Newname*
        A string holding the new name of the element.

.. note::

    -  If the new name for the element already exists in the set, the
       procedure will generate an execution error.

    -  AIMMS will refuse to rename a set element, if an explicit reference
       to such an element exists in the model source.

.. seealso::

    -  The procedure :aimms:procedure:`SetElementAdd`, and the function :aimms:func:`StringToElement`.

    -  The lexical conventions for set elements in Section 2.3 of the
       `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
