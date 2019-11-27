.. aimms:procedure:: SecurityGetGroups(group\_set)

.. _SecurityGetGroups:

SecurityGetGroups
=================

With the procedure :aimms:func:`SecurityGetGroups` you can fill a set with group
names from the user database that is linked to the project.

.. code-block:: aimms

    SecurityGetGroups(
         group_set          ! (output) an (empty) root set
         )

Arguments
---------

    *group\_set*
        A root set, that on return will contain elements that represent all
        group names from the user database.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. seealso::

    The procedure :aimms:func:`SecurityGetUsers`.
