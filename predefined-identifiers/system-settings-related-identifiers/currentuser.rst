.. aimms:set:: CurrentUser

.. _CurrentUser:

CurrentUser
===========

The predefined string parameter :aimms:set:`CurrentUser` contains the name of the
user currently logged on to an AIMMS project.

.. code-block:: aimms

        StringParameter CurrentUser;

Definition
----------

    The contents of the string parameter :aimms:set:`CurrentUser` is the name of the
    user currently logged on to a project. Project users are defined by the
    User Administrator in the **User Setup** dialog box.

Updatability
------------

    The contents of :aimms:set:`CurrentUser` can only be modified by logging on to
    the project as another user through the **File-Authorization-User**
    menu.

.. note::

    The string parameter :aimms:set:`CurrentUser` only contains data when the project
    has been linked to a user database. The use of User Groups in AIMMS
    directly is deprecated, as user authentication and authorization during
    deployment is now arranged via AIMMS PRO (cf. Section
    `Project Security <https://download.aimms.com/aimms/download/manuals/AIMMS3UG_ProjectSecurity.pdf>`_).

.. seealso::

    The function :aimms:func:`SecurityGetUsers`.
