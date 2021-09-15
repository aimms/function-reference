.. aimms:set:: CurrentAuthorizationLevel

.. _CurrentAuthorizationLevel:

CurrentAuthorizationLevel
=========================

The predefined element parameter :aimms:set:`CurrentAuthorizationLevel` refers to
the authorization level assigned to the user currently logged on to an
AIMMS project.

.. code-block:: aimms

        ElementParameter CurrentAuthorizationLevel {
            Range      :  AllAuthorizationLevels;
        }

Definition
----------

    The contents of the element parameter :aimms:set:`CurrentAuthorizationLevel` is
    the authorization level assigned to the user currently logged on to a
    project, as assigned by the User Administrator in the **User Setup**
    dialog box.

Updatability
------------

    The contents of :aimms:set:`CurrentAuthorizationLevel` can only be modified by
    logging on to the project as another user through the
    **File-Authorization-User** menu, or by directly modifying the
    authorization level through the **File-Authorization-Level** menu.

.. note::

    The element parameter :aimms:set:`CurrentAuthorizationLevel` is typically used
    refer to the slice of model-defined data that defines access rights to
    various parts of the model or end-user interface of a model. By
    referring to the data slice determined by the value of element parameter
    :aimms:set:`CurrentAuthorizationLevel`, AIMMS will use the accessibility rights
    associated with the authorization level of the current logged on user.
    The use of authorization levels in AIMMS directly is deprecated, as user
    authentication and authorization during deployment is now arranged via
    AIMMS PRO (cf. Section
    `Project Security <https://documentation.aimms.com/user-guide/miscellaneous/project-security/index.html>`_).

.. seealso::

    The set :aimms:set:`AllAuthorizationLevels`.
