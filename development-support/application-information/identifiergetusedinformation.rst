.. aimms:procedure:: IdentifierGetUsedInformation(identifier, isUsedInPages, isUsedInMenus, isUsedInDataCategories)

.. _IdentifierGetUsedInformation:

IdentifierGetUsedInformation
============================

With the procedure :aimms:func:`IdentifierGetUsedInformation` you can obtain
information on whether an identifier in the model is still referenced in
either a page, a user menu or a case type/data category.

.. code-block:: aimms

    IdentifierGetUsedInformation(
         identifier             ! (input) element parameter
         isUsedInPages,         ! (output) scalar numerical identifier 
         isUsedInMenus,         ! (output) scalar numerical identifier
         isUsedInDataCategories ! (output) scalar numerical identifier
         )

Arguments
---------

    *identifier*
        The identifier, given as element in the set ``AllIdentifiers``, whose
        usage info you want to retrieve. Please note that local identifiers
        (declared inside procedures or functions) are not taken into account by
        this function.

    *isUsedInPages*
        On return this value is set to 1 if the identifier is referenced in
        either a page, template or print page. It is set to 0 otherwise.

    *isUsedInMenus*
        On return this value is set to 1 if the identifier is referenced in a
        menu item or submenu of a user menu. It is set to 0 otherwise.

    *isUsedInDataCategories*
        On return this value is set to 1 if the identifier is referenced in
        either a data category or case type. It is set to 0 otherwise.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    The function only indicates whether the identifier is used in either of
    the three GUI areas. To figure out in which specific page, menu or data
    category the identifier is used you can use the drag-and-find feature of
    the IDE: if you drag an identifier from the Model Explorer, holding down
    both the Control and Shift key, and drop it on either the Page Manager,
    Template Manager, Menu Builder or Data Management Setup tree, all items
    that reference the identifier will be highlighted.

.. seealso::

    The procedure :aimms:func:`PageGetUsedIdentifiers`.
