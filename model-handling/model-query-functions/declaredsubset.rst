.. aimms:function:: DeclaredSubset(subsetName, supersetName)

.. _DeclaredSubset:

DeclaredSubset
==============

The function :aimms:func:`DeclaredSubset` returns 1 if both subsetName and
superName refer to a one-dimensional set and ``subsetName`` is directly
or indirectly declared to be a subset of ``supersetName``.

.. code-block:: aimms

    DeclaredSubset(
         subsetName,        ! (input) scalar element parameter
         supersetName       ! (input) scalar element parameter
         )

Arguments
---------

    *subsetName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers`.

    *supersetName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers`.

Return Value
------------

    This function returns 1 iff ``subsetName`` is directly or indirectly a
    subset of ``supersetName``. If ``subsetName`` or ``supersetName`` does
    not refer to a one-dimensional set, this function will return 0 without
    any warning or error message.

Example
-------

With the following declarations: 

.. code-block:: aimms

    Set MasterSet {
        Index        :  ms;
    }
    Set DomainSet {
        SubsetOf     :  MasterSet;
        Index        :  ds;
    }
    Set ActiveSet {
        SubsetOf     :  DomainSet;
        Index        :  as;
    }
    File outf {
        Name         :  "outf.put";
    }

The following statements:

.. code-block:: aimms

    put outf ;
    put "ActiveSet(=DomainSet =", DeclaredSubset('ActiveSet', 'DomainSet'):0:0,/;
    put "ActiveSet(=MasterSet =", DeclaredSubset('ActiveSet', 'MasterSet'):0:0,/;
    put "MasterSet(=ActiveSet =", DeclaredSubset('MasterSet', 'ActiveSet'):0:0,/;
    put "MasterSet(=outf      =", DeclaredSubset('MasterSet', 'outf'     ):0:0,/;
    putclose ;

Return the following output. 

.. code-block:: aimms

    ActiveSet(=DomainSet =1 ! ActiveSet is directly a subset of DomainSet
    ActiveSet(=MasterSet =1 ! ActiveSet is indirectly a subset of MasterSet
    MasterSet(=ActiveSet =0 ! But the reverse is not true.
    MasterSet(=outf      =0 ! outf isn't even a set.

.. seealso::

    - The function :aimms:func:`IndexRange`.
