.. aimms:function:: forecasting::ExponentialSmoothingTrendSeasonality(dataValues, estimates, noObservations, noAveragingPeriods, alpha, beta, gamma, periodLength, ErrorMeasures, Residuals)

.. _forecasting::ExponentialSmoothingTrendSeasonality:

forecasting::ExponentialSmoothingTrendSeasonality
=================================================

The exponential smoothing with trend and seasonality procedure is a time
series forecasting procedure. This procedure is an extension from the
exponential smoothing whereby the forecast also captures both a trend
and a seasonality. The reader interested in the mathematical background
is referred to

-  https://www.otexts.org/book/fpp
-  http://en.wikipedia.org/wiki/Exponential_smoothing

Function Prototype
------------------

    To provide the error measures and residuals only when you need them,
    there are three flavors of the ``ExponentialSmoothingTrendSeasonality``
    procedure provided:

    .. code-block:: aimms

            forecasting::ExponentialSmoothingTrendSeasonality(    
            ! Provides the estimates, but not the error measures nor the residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha,           ! Scalar input, weight of observation
                  beta,            ! Scalar input, weight of change in observation
                  gamma,           ! Scalar input, weight of seasonality
                  periodLength)    ! Scalar input, length of season

    .. code-block:: aimms

            forecasting::ExponentialSmoothingTrendSeasonalityEM(  
            ! Provides estimates and error measures, but not the residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha,           ! Scalar input, weight of observation
                  beta,            ! Scalar input, weight of change in observation
                  gamma,           ! Scalar input, weight of seasonality
                  periodLength,    ! Scalar input, length of season
                  ErrorMeasures)   ! Output, indexed over forecasting::ems

    .. code-block:: aimms

            forecasting::ExponentialSmoothingTrendSeasonalityEMR( 
            ! Provides estimates, error measures, and residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha,           ! Scalar input, weight of observation
                  beta,            ! Scalar input, weight of change in observation
                  gamma,           ! Scalar input, weight of seasonality
                  periodLength,    ! Scalar input, length of season
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

    *noAveragingPeriods*
        Specifies the number of values used to compute a single average. This
        parameter corresponds to :math:`N` in the mathematical notation above.

    *alpha*
        Specifies the weighting factor for the observation. This parameter
        corresponds to :math:`\alpha` in the mathematical notation above.

    *beta*
        Specifies the weighting factor for the change in observation.

    *gamma*
        Specifies the weighting factor for the seasonality.

    *periodLength*
        Specifies the period length.

    *ErrorMeasures*
        The error measures as presented in :ref:`chapter:time-series-forecasting`.

    *Residuals*
        The residuals as presented in :ref:`chapter:time-series-forecasting`.

Example
-------

    With declarations and data as specified in :numref:`table:sample-input-data` the call:

    .. code-block:: aimms

                    forecasting::ExponentialSmoothingTrendSeasonality(
                        dataValues         :  sampDat,
                        estimates          :  sampEst1,
                        noObservations     :  31,
                        alpha              :  0.5,
                        beta               :  0.3,
                        gamma              :  0.3, 
                        periodLength       :  7);

    Will result in the following output: 

    .. code-block:: aimms

                    sampEst1 := data 
                    { 01-01 : 48.17421514,  01-02 : 33.42448176,  01-03 : 28.16272649,
                      01-04 : 24.07455476,  01-05 : 33.94263017,  01-06 : 47.93386652,
                      01-07 : 48.83947317,  01-08 : 46.31365850,  01-09 : 23.89344424,
                      01-10 : 30.27764654,  01-11 : 24.95849413,  01-12 : 45.51882876,
                      01-13 : 74.25387499,  01-14 : 76.43874408,  01-15 : 62.30360776,
                      01-16 : 34.03705964,  01-17 : 18.95751109,  01-18 : 47.97903657,
                      01-19 : 78.64240904,  01-20 : 90.15243324,  01-21 : 71.83828787,
                      01-22 : 37.68452884,  01-23 : 43.80677029,  01-24 : 54.55643634,
                      01-25 : 70.28818669,  01-26 : 82.29733841,  01-27 : 67.89367583,
                      01-28 : 49.77439370,  01-29 : 67.81915419,  01-30 : 76.48587445,
                      01-31 : 74.36541195,  02-01 : 63.51664916,  02-02 : 76.26956592,
                      02-03 : 77.83862565,  02-04 : 65.67879532,  02-05 : 59.94750898,
                      02-06 : 65.94274949,  02-07 : 77.84397349,  02-08 : 79.13679316,
                      02-09 : 83.83707749,  02-10 : 85.40613721,  02-11 : 73.24630688,
                      02-12 : 67.51502054,  02-13 : 73.51026105,  02-14 : 85.41148505 } ;

    This can be
    graphically displayed as:

    |image|

    .. |image| image:: ExponentialSmoothingTrendSeasonality.png
