.. aimms:set:: CurrentGroup

.. _CurrentGroup:

CurrentGroup
============

The predefined string parameter :aimms:set:`CurrentGroup` contains the name of
the user group associated with the user currently logged on to an AIMMS
project.

.. code-block:: aimms

        StringParameter CurrentGroup;

Definition
----------

    The contents of the string parameter :aimms:set:`CurrentGroup` is the name of the
    user group associated with the user currently logged on to a project.
    User groups are defined by the User Administrator in the **User Setup**
    dialog box.

Updatability
------------

    The contents of :aimms:set:`CurrentGroup` can only be modified by logging on to
    the project as another user through the **File-Authorization-User**
    menu, or directly through the **File-Authorization-Group** menu.

.. note::

    The string parameter :aimms:set:`CurrentGroup` only contains data when the
    project has been linked to a user database. The use of User Groups in
    AIMMS directly is deprecated, as user authentication and authorization
    during deployment is now arranged via AIMMS PRO (cf. Section
    `Project Security <https://documentation.aimms.com/user-guide/miscellaneous/project-security/index.html>`_).

.. seealso::

    The function :aimms:func:`SecurityGetGroups`.
