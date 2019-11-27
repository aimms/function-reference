.. aimms:function:: forecasting::ExponentialSmoothingTrend(dataValues, estimates, noObservations, alpha, beta, ErrorMeasures, Residuals)

.. _forecasting::ExponentialSmoothingTrend:

forecasting::ExponentialSmoothingTrend
======================================

The exponential smoothing with trend procedure is a time series
forecasting procedure. This procedure is an extension from the
exponential smoothing whereby the forecast also captures a trend. The
reader interested in the mathematical background is referred to

-  https://www.otexts.org/book/fpp
-  http://en.wikipedia.org/wiki/Exponential_smoothing

Function Prototype
------------------

    To provide the error measures and residuals only when you need them,
    there are three flavors of the ``ExponentialSmoothingTrend`` procedure
    provided:

    .. code-block:: aimms

            forecasting::ExponentialSmoothingTrend(    
            ! Provides the estimates, but not the error measures nor the residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha,           ! Scalar input, weight of observation
                  beta)            ! Scalar input, weight of change in observation

    .. code-block:: aimms

            forecasting::ExponentialSmoothingTrendEM(  
            ! Provides estimates and error measures, but not the residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha,           ! Scalar input, weight of observation
                  beta,            ! Scalar input, weight of change in observation
                  ErrorMeasures)   ! Output, indexed over forecasting::ems

    .. code-block:: aimms

            forecasting::ExponentialSmoothingTrendEMR( 
            ! Provides estimates, error measures, and residuals
                  dataValues,      ! Input, parameter indexed over time set
                  estimates,       ! Output, parameter indexed over time set
                  noObservations,  ! Scalar input, length history
                  alpha,           ! Scalar input, weight of observation
                  beta,            ! Scalar input, weight of change in observation
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

    *beta*
        Specifies the weighting factor for the change in observation.

    *ErrorMeasures*
        The error measures as presented in :ref:`chapter:time-series-forecasting`.

    *Residuals*
        The residuals as presented in :ref:`chapter:time-series-forecasting`.

Example
-------

    With declarations and data as specified in :numref:`table:sample-input-data` the call:

    .. code-block:: aimms

                forecasting::ExponentialSmoothingTrend(
                    dataValues         :  sampDat,
                    estimates          :  sampEst1,
                    noObservations     :  31,
                    alpha              :  0.3,
                    beta               :  0.3);

    Will result in the following output: 

    .. code-block:: aimms

                    sampEst1 := data 
                    { 01-01 : 46.90141235,  01-02 : 31.89711841,  01-03 : 19.91486469,
                      01-04 : 11.09278244,  01-05 :  9.12476621,  01-06 : 14.24770491,
                      01-07 : 21.18135461,  01-08 : 25.00880483,  01-09 : 30.04118231,
                      01-10 : 29.60799603,  01-11 : 32.39262113,  01-12 : 41.18187664,
                      01-13 : 51.09710805,  01-14 : 57.24030837,  01-15 : 54.80598480,
                      01-16 : 52.57369145,  01-17 : 56.19151171,  01-18 : 60.35524890,
                      01-19 : 64.83322220,  01-20 : 65.33462956,  01-21 : 59.52540116,
                      01-22 : 58.20531338,  01-23 : 59.89873706,  01-24 : 66.10199203,
                      01-25 : 68.96338627,  01-26 : 65.20775937,  01-27 : 60.35010811,
                      01-28 : 62.98534714,  01-29 : 66.24030430,  01-30 : 68.25439193,
                      01-31 : 71.77479879,  02-01 : 73.73138118,  02-02 : 75.68796357,
                      02-03 : 77.64454596,  02-04 : 79.60112835,  02-05 : 81.55771074,
                      02-06 : 83.51429313,  02-07 : 85.47087552,  02-08 : 87.42745791,
                      02-09 : 89.38404030,  02-10 : 91.34062269,  02-11 : 93.29720508,
                      02-12 : 95.25378747,  02-13 : 97.21036985,  02-14 : 99.16695224 } ;

    This can be
    graphically displayed as:

    |image|

    .. |image| image:: ExponentialSmoothingTrend.png
