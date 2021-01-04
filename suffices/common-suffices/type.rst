.. _.type:

.type
=====

Definition
----------

    The ``.type`` suffix returns the type of the identifier at hand.

Datatype
--------

    The value of the ``.type`` suffix is an element in the Set :aimms:set:`AllIdentifierTypes`.

Dimension
---------

    The ``.type`` suffix is scalar.

.. note::

    -  This suffix is typically used with an index into the set :aimms:set:`AllIdentifiers`,
       as illustrated in the common example in :numref:`CommonSuffixExample`.

    -  See also :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  This suffix is deprecated, see :aimms:func:`IdentifierType`.
