.. aimms:procedure:: CloneElement(updateSet, originalElement, cloneName, cloneElement, includeDefinedSubsets)

.. _CloneElement:

CloneElement
============

The procedure :aimms:func:`CloneElement` copies the data associated with a
particular element to another element.

.. code-block:: aimms

     CloneElement(
       updateSet,              ! (input, output) a set identifier
       originalElement,        ! (input) an element in the set 
       cloneName,              ! (input) a string that is the name of the clone
       cloneElement,           ! (output) an element parameter
       includeDefinedSubsets ) ! (optional) an integer, default 0.

The procedure :aimms:func:`CloneElement` performs the following actions:

#. It creates or finds an element with name ``cloneName``:
   ``cloneElement``. The element ``cloneElement`` is inserted into
   ``updateSet`` if it is not already there. This insertion is only
   permitted if ``updateSet`` does not have a definition.

#. For each domain set of ``updateSet``, say ``insertDomainSet``, the
   element ``cloneElement`` is inserted into ``insertDomainSet`` if it
   is not already there. Such an insertion is only permitted if
   ``insertDomainSet`` does not have a definition.

#. For each subset of ``updateSet``, say ``insertSubset`` in which
   ``originalElement`` is an element, ``cloneElement`` is also inserted
   into ``insertSubset``. If ``includeDefinedSubsets`` is 0, then
   ``insertSubset`` is skipped if it is a defined subset.

#. The domain sets of steps 1 and 2, and the sets modified in step 3
   form a set, say ``modifiedSets``.

#. Identifiers declared over a set in ``modifiedSets`` that meet one of
   the following criteria, are selected:

   -  It is a non-local multi-dimensional set without a definition.

   -  It is a non-local parameter without a definition.

   -  It is a variable.

   -  It is a constraint.

   These identifiers form the set ``modifiedIdentifiers``.

#. For each identifier in the set ``modifiedIdentifiers``, and all
   suffixes of this identifier, the data associated with element
   ``originalElement`` is copied to ``cloneElement``.

Arguments
---------

    *updateSet*
        A one-dimensional set.

    *originalElement*
        An element valued expression that should result in an element in
        ``updateSet``.

    *cloneName*
        A string expression that should result in a name that is in the set
        ``updateSet`` or can be added to that set.

    *cloneElement*
        An element parameter, in which the resulting element is stored.

    *includeDefinedSubsets*
        When non-zero, defined subsets are included in the ``modifiedSets`` as
        well. When these defined subsets are evaluated thereafter again, this
        may result in the creation of inactive data. Inactive data can be
        removed by a ``CLEANUP`` or ``CLEANDEPENDENTS`` statement, see :doc:`data-communication-components/data-initialization-verification-and-control/data-control`
        of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__. Defined subsets that are defined as an
        enumeration are never included.

Return Value
------------

    The procedure returns 1 if successful and 0 otherwise. Possible reasons
    for returning 0 are:

    -  ``originalElement`` is not in ``updateSet``.

    -  ``cloneName`` equals name of ``originalElement``.

    -  There are no identifiers modified.

.. note::

    If you want to make sure that the string ``cloneName`` is not yet an
    element in ``updateSet``, use a statement like: 

    .. code-block:: aimms

            if ( not ( cloneName in updateSet ) ) then
                CloneElement( ... );
            endif ;

Example
-------

    With the following declarations (and initial data): 

    .. code-block:: aimms

                Set S {
                    Index        :  i, j;
                    Parameter    :  ep;
                    InitialData  :  data { a };
                }
                Parameter P {
                    IndexDomain  :  i;
                    InitialData  :  data { a : 1 };
                }
                Parameter Q {
                    IndexDomain  :  (i,j);
                    InitialData  :  data { ( a, a ) : 1 };
                }

    the
    statement 

    .. code-block:: aimms

                CloneElement( S, 'a', "b", ep );

    results in ``S``, ``P``, ``Q`` and ``ep`` having
    the following data: 

    .. code-block:: aimms

                S := data { a, b } ;
                P := data { a : 1,  b : 1 } ;
                Q := data { ( a, a ) : 1,  ( a, b ) : 1,  ( b, a ) : 1,  ( b, b ) : 1 } ;
                ep := 'b' ;

.. seealso::

    - The function :aimms:func:`StringToElement`, the procedure :aimms:func:`FindUsedElements` and the procedure :aimms:func:`RestoreInactiveElements`.
