.. aimms:set:: AllAuthorizationLevels

.. _AllAuthorizationLevels:

AllAuthorizationLevels
======================

The predefined set :aimms:set:`AllAuthorizationLevels` contains the names of all
authorization levels associated with an AIMMS project.

.. code-block:: aimms

        Set AllAuthorizationLevels {
            Index      :  IndexAuthorizationLevels;
        }

Definition
----------

    The contents of the set :aimms:set:`AllAuthorizationLevels` is the collection of
    all authorization levels defined for a particular project through the
    **Authorization Level Setup** dialog box.

Updatability
------------

    The contents of the set can only be modified through the **Authorization
    Level Setup** dialog box.

.. note::

    The set :aimms:set:`AllAuthorizationLevels` is typically used in the index
    domains of parameters used in the model and graphical end-user interface
    to define accessibility rights for groups of users with the same
    authorization level. By referring to the data slice determined by the
    value of element parameter :aimms:set:`CurrentAuthorizationLevel`, AIMMS will use the accessibility
    rights associated with the authorization level of the current user. The
    use of authorization levels in AIMMS directly is deprecated, as user
    authentication and authorization during deployment is now arranged via
    AIMMS PRO (cf. Section
    `[UGsec:security.auth] <#UGsec:security.auth>`__).
