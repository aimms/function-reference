.. aimms:function:: CallerNumberOfLocations()

.. _CallerNumberOfLocations:

CallerNumberOfLocations
=======================

The function :aimms:func:`CallerNumberOfLocations` returns the number of nodes on
the current execution stack, not counting the current internal procedure
or function.

.. code-block:: aimms

    CallerNumberOfLocations( )

Example
-------

    The following code provides the skeleton of a simple stack dump.

    .. code-block:: aimms

            Parameter noLocs ;
            Parameter aDepth ;
            Parameter aLine ;
            ElementParameter aNode {
                range : AllIdentifiers ;
            }
            ElementParameter anAttr {
                range : AllAttributeNames ;
            }
            File outf {
                Name: "a41t001.put";
            }
            Procedure reportStack {
                Body: {
                    noLocs := callerNumberOfLocations();
                    aDepth := 1 ;
                    put outf, "Current execution stack: ", / ;
                    put "depth":5, " ", "node":20, " ", "attribute":12, " ", "line":4, / ;
                    put "-"*5,     " ", "-"*20,    " ", "-"*12,         " ", "-"*4,    / ;
                    while aDepth <= noLocs do
                        aLine := callerLine( aDepth );
                        aNode := callerNode( aDepth );
                        anAttr := callerAttribute( aDepth );
                        put aDepth:5:0, " ", aNode:20, " ", anAttr:12, " ", aLine:4:0, " ", / ;
                        aDepth += 1 ;
                    endwhile ;
                    putclose ;
                }
            }

    An instance of its output might be: 

    .. code-block:: aimms

        Current execution stack:
        depth node                 attribute    line
        ----- -------------------- ------------ ----
            1 work1                body            4
            2 MainExecution        body            1

.. seealso::

    The functions :aimms:func:`CallerAttribute`, :aimms:func:`CallerLine`, :aimms:func:`CallerNode`, and :aimms:func:`errh::NumberOfLocations`.
