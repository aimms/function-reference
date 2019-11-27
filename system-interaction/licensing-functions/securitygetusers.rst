.. aimms:procedure:: SecurityGetUsers(user\_set[, group][, level])

.. _SecurityGetUsers:

SecurityGetUsers
================

With the procedure :aimms:func:`SecurityGetUsers` you can fill a set with user
names from the user database that is linked to the project. You can
filter which users are included in the set based upon their group or
authorization level.

.. code-block:: aimms

    SecurityGetUsers(
         user_set,       ! (output) an (empty) root set
         [group,]        ! (optional) scalar string
         [level]         ! (optional) element of the set AllAuthorizationLevels
         )

Arguments
---------

    *user\_set*
        A root set, that on return will contain elements that represent the user
        names from the user database.

    *group (optional)*
        A string representing a group name from the user database. If specified,
        then only the users that belong to this group are returned.

    *level (optional)*
        An element of the set :aimms:set:`AllAuthorizationLevels`. If specified, then only the users that
        have the specified authorization level are returned.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. seealso::

    The procedure :aimms:func:`SecurityGetGroups`.
