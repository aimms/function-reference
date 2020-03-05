.. aimms:function:: IdentifierShowTreeLocation(identifier)

.. _IdentifierShowTreeLocation:

IdentifierShowTreeLocation
==========================

The function :aimms:func:`IdentifierShowTreeLocation` allows you to
programmatically show the position of a specific identifier in the Model
Explorer tree. If the Model Explorer is not currently opened, it will
open automatically. The function only works in a developer system, in an
end-user system the function raises an error message.

.. code-block:: aimms

    IdentifierShowTreeLocation(
         identifier       ! (input) element in AllIdentifiers
         )

Arguments
---------

    *identifier*
        The identifier for which you want to show the location in the Model
        Explorer.

.. seealso::

    The function :aimms:func:`IdentifierShowAttributes`.
