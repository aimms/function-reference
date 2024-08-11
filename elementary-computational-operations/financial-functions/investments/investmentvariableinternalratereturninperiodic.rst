.. aimms:function:: InvestmentVariableInternalRateReturnInPeriodic(Value, Date, Basis, LowerBound, UpperBound, Error)

.. _InvestmentVariableInternalRateReturnInPeriodic:

InvestmentVariableInternalRateReturnInPeriodic
==============================================

The function :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic` returns
the internal rate of return for an investment based on a series of
in-periodic cash flows. The internal rate of return is the interest rate
received for an investment. This function uses the procedure
``InvestmentVariableInternalRateReturnInPeriodicAll`` to determine all
possible internal rates and returns the internal rate that is within the
specified bounds.

.. code-block:: aimms

    InvestmentVariableInternalRateReturnInPeriodic(
        Value,                   ! (input) one-dimensional numerical expression
        Date,                    ! (input) one-dimensional string expression
        [Basis,]                 ! (optional) numerical expression
        [LowerBound,]            ! (optional) numerical expression
        [UpperBound,]            ! (optional) numerical expression
        [Error]                  ! (optional) numerical expression
        )

Arguments
---------

    *Value*
        The periodic payments (positive or negative), which must be equally
        spaced in time. The order of the payments in *Value* must be the same as
        the order in which the cash flows occur. *Value* is an one dimensional
        parameter of real numbers. *Value* given by positive numbers represent
        incoming amounts and *Value* given by negative numbers represent
        outgoing amounts. em Value must contain at least one positive and at
        least one negative number.

    *Date*
        The dates on which the payments occur. *Date* and *Value* must have the
        same order. *Date* is an one-dimensional parameter of dates given in a
        date format. The first payment date indicates the beginning of the
        schedule of payments. All other dates must be later than this date, but
        they may occur in any order. *Date* should contain as many dates as the
        number of values given by *Value*.

    *Basis*
        The day-count basis method to be used. The default is 1.

    *LowerBound*
        Indicates a minimum for the internal rate to be accepted by this
        function. The default is :math:`-1`.

    *UpperBound*
        Indicates a maximum for the internal rate to be accepted by this
        function. The default is :math:`5`.

    *Error*
        Indicates whether AIMMS should give an error if multiple solutions are
        found that satisfy the bounds. :math:`Error = 0`: if multiple solutions
        are found, return the solution with the smallest absolute value.
        :math:`Error = 1`: if multiple solutions are found, return an error
        message. The default is :math:`0`.

Return Value
------------

    The function :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic` returns
    the internal rate of return for an investment based on a series of
    in-periodic cash flows. The internal rate of return is the interest rate
    received for an investment.

.. note::

    -  The function :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic` can
       be used in an objective function or constraint. The input parameter
       *Value* can be used as a variable.

    -  The function :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic` is
       similar to the Excel function `XIRR <https://learn.microsoft.com/en-us/office/troubleshoot/excel/algorithm-of-xirr-funcation>`_.


Example
-------

Often, internal rate of return is an investment first, (period 0, negative value),
and then return cashflows in following periods. 

.. code-block:: aimms

    _s_periods := ElementRange(0,4);
    _p_val('0') := -100 ;
    _p_val('1') := 25 ;
    _p_val(_i_per | _i_per > '1') := _p_val(_i_per-1) * 1.1 ;
    _sp_startQuarter(_i_per) := MomentToString(
        Format        :  "%c%y-%m-%d", 
        unit          :  [month], 
        ReferenceDate :  "2024-01-01", 
        Elapsed       :  ((ord(_i_per)-1)*3)[month]);

    _p_irr := InvestmentVariableInternalRateReturnInPeriodic(
        value      :  _p_val, 
        date       :  _sp_startQuarter,
        LowerBound :  -1, 
        UpperBound :  5, 
        Error      :  1);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display { _p_val, _sp_startQuarter }, _p_irr ;
    endblock ;

This results in the following IRR:

.. code-block:: aimms

    Composite table:
        _i_per         _p_val  _sp_startQuarter
    !   ------    -----------  ----------------
             0    -100.000000  "2024-01-01"    
             1      25.000000  "2024-04-01"    
             2      27.500000  "2024-07-01"    
             3      30.250000  "2024-10-01"    
             4      33.275000  "2025-01-01"    
        ;

        _p_irr := 0.258815 ;
      

References
-----------

    *  The functions :aimms:func:`InvestmentVariableInternalRateReturn`, 

    * :aimms:func:`InvestmentVariableInternalRateReturnInPeriodicAll`. 

    * Day count basis :ref:`methods<ff.dcb>`.
