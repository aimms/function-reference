.. aimms:function:: forecasting::WeightedMovingAverage(dataValues, estimates, noObservations, weights, noAveragingPeriods, ErrorMeasures, Residuals)

.. _forecasting::WeightedMovingAverage:

forecasting::WeightedMovingAverage
==================================

The weighted moving average procedure is a time series forecasting
procedure. Essentially, this procedure forecasts by taking the weighted
average over the last :math:`N` observations.

Mathematical Formulation
------------------------

    Using the notation for observations and estimates given in
    :numref:`table:notation-observation-estimation`, the estimates are defined as:

    .. math:: e_t = \sum_{j=1,\tau=t-(N+1)+j}^N {w_j \tilde y}_\tau \mspace{4mu}\mspace{4mu}\mspace{4mu} \textrm{ where } {\tilde y}_\tau = \left\{ \begin{array}{ll} y_1 & \textrm{ if } \tau < 1 \\ y_\tau & \textrm{ if } \tau \in \{1 .. T \} \\ e_\tau & \textrm{ if } \tau > T \end{array} \right.

Function Prototype
------------------

    To provide the error measures and residuals only when you need them,
    there are three flavors of the ``WeightedMovingAverage`` procedure
    provided:

    .. code-block:: aimms

            forecasting::WeightedMovingAverage(
                  ! Provides the estimates, 
                  ! but not the error measures nor the residuals
                  dataValues,              ! Input, parameter indexed over time set
                  estimates,               ! Output, parameter indexed over time set
                  noObservations,          ! Scalar input, length history
                  weights,                 ! Input, parameter  
                  noAveragingPeriods)      ! Scalar input, averaging length

    .. code-block:: aimms

            forecasting::WeightedMovingAverageEM(  
                  ! Provides estimates and error measures, but not the residuals
                  dataValues,              ! Input, parameter indexed over time set
                  estimates,               ! Output, parameter indexed over time set
                  noObservations,          ! Scalar input, length history
                  weights,                 ! Input, parameter  
                  noAveragingPeriods,      ! Scalar input, averaging length
                  ErrorMeasures)           ! Output, indexed over forecasting::ems

    .. code-block:: aimms

            forecasting::WeightedMovingAverageEMR( 
                  ! Provides estimates, error measures, and residuals
                  dataValues,              ! Input, parameter indexed over time set
                  estimates,               ! Output, parameter indexed over time set
                  noObservations,          ! Scalar input, length history
                  weights,                 ! Input, parameter  
                  noAveragingPeriods,      ! Scalar input, averaging length
                  ErrorMeasures,           ! Output, indexed over forecasting::ems
                  Residuals)               ! Output, parameter indexed over time set

    Here, the time set is a set that encompasses both the history and the
    horizon.

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

    *weights*
        Specifies the weights. The weights should be indexed over a subset of
        :aimms:set:`Integers`: :math:`\{ 1 .. N\}`, in the range :math:`[0,1]` and sum to 1.

    *noAveragingPeriods*
        Specifies the number of values used to compute a single average. This
        parameter corresponds to :math:`N` in the mathematical notation above.

    *ErrorMeasures*
        The error measures as presented in :ref:`chapter:time-series-forecasting`.

    *Residuals*
        The residuals as presented in :ref:`chapter:time-series-forecasting`.

Example
-------

    With declarations and data as specified in :numref:`table:sample-input-data` the call:

    .. code-block:: aimms

                    weightSet := ElementRange(1,4);
                    locWeights := data { 1 : 0.1, 2 : 0.2, 3: 0.3, 4: 0.4 } ;
                    forecasting::WeightedMovingAverage(
                        dataValues         :  sampDat,
                        estimates          :  sampEst1,
                        noObservations     :  31,
                        weights            :  locWeights,
                        noAveragingPeriods :  4);

    Will result in the following output: 

    .. code-block:: aimms

                    sampEst1 := data 
                    { 01-01 : 46.901412,  01-02 : 46.901412,  01-03 : 45.400983,
                      01-04 : 41.907042,  01-05 : 36.063210,  01-06 : 28.902678,
                      01-07 : 29.356152,  01-08 : 33.990024,  01-09 : 41.435848,
                      01-10 : 45.518815,  01-11 : 41.568491,  01-12 : 35.958284,
                      01-13 : 37.144096,  01-14 : 39.077193,  01-15 : 51.025996,
                      01-16 : 58.200997,  01-17 : 54.913605,  01-18 : 48.165158,
                      01-19 : 44.846840,  01-20 : 53.967984,  01-21 : 63.412990,
                      01-22 : 62.343600,  01-23 : 58.683930,  01-24 : 53.088836,
                      01-25 : 53.599271,  01-26 : 64.608926,  01-27 : 69.237841,
                      01-28 : 68.325173,  01-29 : 60.482475,  01-30 : 56.579581,
                      01-31 : 62.544522,  02-01 : 72.698920,  02-02 : 73.408174,
                      02-03 : 73.248910,  02-04 : 74.611221,  02-05 : 73.212924,
                      02-06 : 73.581479,  02-07 : 73.683663,  02-08 : 73.893028,
                      02-09 : 73.485649,  02-10 : 73.664861,  02-11 : 73.704989,
                      02-12 : 73.706377,  02-13 : 73.605353,  02-14 : 73.679252 } ;

    This can be
    graphically displayed as:

    |image|

    Here the history is from ``01-01`` till ``01-31`` and the horizon is
    from ``02-01`` till ``02-14``.

    .. |image| image:: WeightedMovingAverage.png
