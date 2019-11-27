.. aimms:set:: CurrentInputs

.. _CurrentInputs:

CurrentInputs
=============

The predefined set :aimms:set:`CurrentInputs` contains the names of the
identifiers which can actually be modified from within the graphical
end-user interface.

.. code-block:: aimms

        Set CurrentInputs {
            SubsetOf     :  AllUpdatableIdentifiers;
            Index        :  IndexCurrentInputs;
            InitialData  :  AllUpdatableIdentifiers;
        }

Definition
----------

    The set :aimms:set:`CurrentInputs` contains the names of the model identifiers
    that can actually modified from within the graphical end-user interface
    of AIMMS.

Updatability
------------

    The contents of :aimms:set:`CurrentInputs` can be modified programmatically from
    within an AIMMS model. The set cannot be updated from within the
    end-user interface.

.. note::

    -  The set :aimms:set:`AllUpdatableIdentifiers` determines which identifiers are updatable *in
       principle*. Therefore, you can only add identifiers to
       :aimms:set:`CurrentInputs` which are already contained in the set :aimms:set:`AllUpdatableIdentifiers`

    -  By default, variables are considered not updatable by AIMMS, and
       cannot be modified from within the end-user interface. If you want to
       allow your end-users to update some or all variables from within the
       end-user interface, you can accomplish this by adding these variables
       to both the sets :aimms:set:`AllUpdatableIdentifiers` and :aimms:set:`CurrentInputs`.

    -  Please be careful when changing the content of this set, because it
       has a side-effect which may be overlooked easily. For example, when
       executing the following statement: 

       .. code-block:: aimms

               CurrentInputs := 'MyIdentifier';

       you are not only
       assigning your identifier to the set, **but also totally replacing
       the previous content of the set!** In order to prevent this, you
       should use the following statement instead of the one above:

       .. code-block:: aimms

               CurrentInputs := CurrentInputs - 'Main_My_Model' + 'MyIdentifier'

       (if your model is called 'My Model')

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`CurrentInputs`.
