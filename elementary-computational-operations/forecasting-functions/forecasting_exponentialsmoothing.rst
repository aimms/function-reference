.. aimms:function:: forecasting::ExponentialSmoothing(dataValues, estimates, noObservations, alpha, ErrorMeasures, Residuals)

.. _forecasting::ExponentialSmoothing:

forecasting::ExponentialSmoothing
=================================

The exponential smoothing procedure is a time series forecasting
procedure. This procedure forecasts by weighted average of an
observation and a previous forecast.

Mathematical Formulation
------------------------

    Using the notation in :numref:`table:notation-observation-estimation`, the estimates are defined as:

    .. math:: e_t = \alpha y_{t-1} + ( 1 - \alpha ) e_{t-1}

    \ To initialize this sequence, we take

    .. math:: \begin{array}{l} e_0 = y_1 \\ y_0 = y_1 \end{array}

    To calculate the forecasts for :math:`t\geq T+2`, we take :math:`y_t`
    for all :math:`t \in \{T+1 \ldots T+H \}` to be equal to :math:`e_t`.
    This results in :math:`y_t = y_{t-1}` for all
    :math:`t \in \{T+2 \ldots T+H \}`; which is graphically depicted as a
    horizontal line. The weighting factor :math:`\alpha` is a parameter in
    the range :math:`(0,1)`; high values of :math:`\alpha` give more weight
    to recent observations.

Function Prototype
------------------

    To provide the error measures and residuals only when you need them,
    there are three flavors of the ``ExponentialSmoothing`` procedure
    provided:

    .. code-block:: aimms

            forecasting::ExponentialSmoothing(    
            ! Provides the estimates, but not the error measures nor the residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha)           ! Scalar input, weight of observation

    .. code-block:: aimms

            forecasting::ExponentialSmoothingEM(  
            ! Provides estimates and error measures, but not the residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha,           ! Scalar input, weight of observation
                  ErrorMeasures)   ! Output, indexed over forecasting::ems

    .. code-block:: aimms

            forecasting::ExponentialSmoothingEMR( 
            ! Provides estimates, error measures, and residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha,           ! Scalar input, weight of observation
                  ErrorMeasures,   ! Output, indexed over forecasting::ems
                  Residuals)       ! Output, parameter indexed over time set

Arguments
---------

    *dataValues*
        A one dimensional parameter containing the observations for the first
        :math:`T` elements of the time set.

    *estimates*
        A one dimensional parameter containing the estimates for all elements in
        the time set.

    *noObservations*
        Specifies the number of elements that belong to the history of the time
        set. This parameter corresponds to :math:`T` in the notation presented
        in :numref:`table:notation-observation-estimation`.

    *alpha*
        Specifies the weighting factor for the observation. This parameter
        corresponds to :math:`\alpha` in the mathematical notation above.

    *ErrorMeasures*
        The error measures as presented in :ref:`chapter:time-series-forecasting`.

    *Residuals*
        The residuals as presented in :ref:`chapter:time-series-forecasting`.

.. note::

    In order to use this function, the AIMMSForecasting system library needs
    to be added to the application.

Example
-------

    With declarations and data as specified in :numref:`table:sample-input-data` the call:

    .. code-block:: aimms

                forecasting::ExponentialSmoothing(
                    dataValues         :  sampDat,
                    estimates          :  sampEst1,
                    noObservations     :  31,
                    alpha              :  0.3);

    Will result in the following output: 

    .. code-block:: aimms

                    sampEst1 := data 
                    { 01-01 : 46.90141235,  01-02 : 46.90141235,  01-03 : 42.40012417,
                      01-04 : 37.76997448,  01-05 : 33.45973660,  01-06 : 33.54213551,
                      01-07 : 37.88549780,  01-08 : 41.23393658,  01-09 : 40.04383462,
                      01-10 : 40.46069432,  01-11 : 35.77134897,  01-12 : 36.00672348,
                      01-13 : 42.63680572,  01-14 : 49.51735495,  01-15 : 52.23354019,
                      01-16 : 47.28051629,  01-17 : 45.00255990,  01-18 : 49.74818871,
                      01-19 : 54.28470891,  01-20 : 58.61730967,  01-21 : 58.66654222,
                      01-22 : 53.13058049,  01-23 : 53.73986519,  01-24 : 57.05779016,
                      01-25 : 63.95711700,  01-26 : 66.04994167,  01-27 : 61.57903291,
                      01-28 : 57.48616057,  01-29 : 61.77400331,  01-30 : 65.39435704,
                      01-31 : 66.98008324,  02-01 : 69.98232238,  02-02 : 69.98232238,
                      02-03 : 69.98232238,  02-04 : 69.98232238,  02-05 : 69.98232238,
                      02-06 : 69.98232238,  02-07 : 69.98232238,  02-08 : 69.98232238,
                      02-09 : 69.98232238,  02-10 : 69.98232238,  02-11 : 69.98232238,
                      02-12 : 69.98232238,  02-13 : 69.98232238,  02-14 : 69.98232238 } ;

    This can be
    graphically displayed as:

    |image|

    .. |image| image:: ExponentialSmoothing.png
