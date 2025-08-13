.. aimms:function:: Round(x[, decimals])

.. _Round:

Round
=====

.. code-block:: aimms

    Round(
         x,            ! (input) numerical expression
         decimals      ! (optional) integer expression
         )

Arguments
---------

    *x*
        A scalar numerical expression.

    *decimals (optional)*
        An integer expression.

Return Value
------------

    The function :aimms:func:`Round` returns the integer value nearest to *x*. In the
    presence of the optional argument *n* the function :aimms:func:`Round` returns the
    value of *x* rounded to *n* decimal places left (:math:`decimals < 0`)
    or right (:math:`decimals > 0`) of the decimal point.

.. note::

    -  The function :aimms:func:`Round` can be used in constraints of nonlinear
       mathematical programs. However, nonlinear solvers may experience
       convergence problems around the discontinuities of the :aimms:func:`Round`
       function.

    -  When the numerical expression contains a unit (has a magnitude), 
       the function :aimms:func:`Round` will first convert the expression to that unit, 
       before evaluating the function itself. 
       See also the option ``rounding compatibility`` in the option category ``backward compatibility``.

Example
-------

Basic
^^^^^

.. code-block:: aimms

    _p_val := 123.456789 ;
    _p_returnA := round( _p_val, -1 ); ! round( _p_val, -1 ) =  120
    _p_returnB := round( _p_val,  0 ); ! round( _p_val,  0 ) =  123
    _p_returnC := round( _p_val,  2 ); ! round( _p_val,  2 ) =  123.46
    _p_returnD := round( _p_val,  5 ); ! round( _p_val,  5 ) =  123.45679

The above illustrates how to round up to a number of decimals, either positive or negative.

Arguments with a Magnitude
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let the magnitudes of interest be specified in a quantity, 
for instance the unitless quantity:

.. code-block:: aimms

    Quantity SI_Unitless {
        BaseUnit: -;
        Conversions: {
            %   -> - : #-># / 100,
            k1  -> - : #-># * 1000,
            M1  -> - : #-># * 1000000
        }
        Comment: "Expresses a dimensionless value.";
    }

then these units can be used to specify the magnitudes of the following identifiers:

.. code-block:: aimms

    Parameter _p_inpSmall;
    Parameter _p_pct {
        Unit: %;
    }
    Parameter _p_rndSmall;
    Parameter _p_rndpct {
        Unit: %;
    }
    Parameter _p_inpLarge;
    Parameter _p_kilo {
        Unit: k1;
    }
    Parameter _p_mega {
        Unit: M1;
    }
    Parameter _p_rndLarge;
    Parameter _p_rndKilo {
        Unit: k1;
    }
    Parameter _p_rndMega {
        Unit: M1;
    }

And the following code will assign some values:

.. code-block:: aimms
    :linenos:

    _p_inpSmall := 0.12345 ;
    _p_pct := _p_inpSmall ;

    _p_rndSmall := round( _p_inpSmall );
    _p_rndPct := round( _p_pct );

    _p_inpLarge := 123456789 ;
    _p_kilo := _p_inpLarge ;
    _p_mega := _p_inpLarge ;

    _p_rndLarge := round( _p_inpLarge );
    _p_rndKilo := round( _p_kilo );
    _p_rndMega := round( _p_mega );

    block where listing_number_precision := 6 ;
        display { _p_inpSmall, _p_pct, _p_rndSmall, _p_rndPct },
            { _p_inpLarge, _p_kilo, _p_mega, 
            _p_rndLarge, _p_rndKilo, _p_rndMega } ;
    endblock ;

The code will produce the following overview in the listing file:

.. code-block:: aimms

    _p_inpSmall :=  0.123450      ;
    _p_pct      := 12.345000  [%] ;
    _p_rndSmall :=         0      ;
    _p_rndpct   :=        12  [%] ;

    _p_inpLarge :=     123456789       ;
    _p_kilo     := 123456.789000  [k1] ;
    _p_mega     :=    123.456789  [M1] ;
    _p_rndLarge :=     123456789       ;
    _p_rndKilo  :=        123457  [k1] ;
    _p_rndMega  :=           123  [M1] ;

As you can see, ``_p_rndpct`` is a rounded multiple of a percentage.
Note that in the computation of this value, round uses the unit of its argument, so the unit of ``_p_pct``.

Similarly, ``_p_rndKilo``, and ``_p_rndMega`` are rounded multiples of 1.000 and 1.000.000 respectively
by using the units of ``_p_kilo`` and ``_p_mega``.

.. seealso::

    *   :aimms:func:`Precision`, :aimms:func:`Ceil`, :aimms:func:`Floor`, :aimms:func:`Trunc`.
    *   Arithmetic functions are discussed in full detail in :ref:`sec:expr.num.functions` of the Language Reference.
