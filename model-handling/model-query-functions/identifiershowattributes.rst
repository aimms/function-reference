.. aimms:function:: IdentifierShowAttributes(identifier)

.. _IdentifierShowAttributes:

IdentifierShowAttributes
========================

The function :aimms:func:`IdentifierShowAttributes` allows you to programmatically
open the attribute window of a specific identifier in your model. The
function only works in a developer system, in an end-user system the
function raises an error message.

.. code-block:: aimms

    IdentifierShowAttributes(
         identifier       ! (input) element in AllIdentifiers
         )

Arguments
---------

    *identifier*
        The identifier for which you want to open the attribute window.

.. seealso::

    - The function :aimms:func:`IdentifierShowTreeLocation`.
