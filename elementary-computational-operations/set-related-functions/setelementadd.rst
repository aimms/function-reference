.. aimms:procedure:: SetElementAdd(Setname, Elempar, Newname)

.. _SetElementAdd:

SetElementAdd
=============

With the procedure :aimms:procedure:`SetElementAdd` you can add new elements to a set.
When you apply :aimms:procedure:`SetElementAdd` to a root set, the element will be
added to that root set. When you apply it to a subset, the element will
be added to the subset as well as to all its supersets, up to and
including its associated root set.

.. code-block:: aimms

    SetElementAdd(
         Setname,   ! (input/output) a reference to a simple set
         Elempar,   ! (output) an element parameter
         Newname    ! (input) a scalar string expression
         )

Arguments
---------

    *Setname*
        The root set or subset to which you want to add the element.

    *Elempar*
        An element parameter into *Setname*, that on return will point to the
        newly added element.

    *Newname*
        A string holding the name of the element to be added.

.. note::

    If the element already exists in the set, the procedure does not make
    any changes to the set, and on return the element parameter *Elempar*
    will point to the existing element.

.. seealso::

    -  The function :aimms:func:`ElementCast` and the procedures :aimms:procedure:`SetElementRename` and :aimms:func:`StringToElement`.

    -  The lexical conventions for set elements in :doc:`preliminaries/language-preliminaries/lexical-conventions`.
