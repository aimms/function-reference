.. aimms:function:: me::SetAttribute(runtimeId, attr, txt)

.. _me::SetAttribute:

me::SetAttribute
================

The procedure :aimms:func:`me::SetAttribute` changes the type of a runtime
identifier.

.. code-block:: aimms

    me::SetAttribute(
            runtimeId,  ! (input) an element
            attr,       ! (input) an element
            txt         ! (input) a string expression
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *attr*
        An element in the set :aimms:set:`AllAttributeNames`

    *txt*
        The text to be assigned. Using the empty string will effectively delete
        the attribute from the runtime identifier.

Return Value
------------

    Returns 1 if the text assignment to the attribute is successful, 0
    otherwise. In the latter case error(s) have been raised. When
    ``runtimeId`` doesn't reference a runtime identifier an error will be
    raised.

.. seealso::

    -  The procedures :aimms:func:`me::Create` and :aimms:func:`me::ChangeType`.

    -  :any:`Articles/146/146-value-dynamic-identifier`
       illustrates the use of model edit functions. The purpose of
       :aimms:func:`me::SetAttribute` in that post is to specify the body of the
       procedure that does the actual work.
