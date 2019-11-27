.. aimms:function:: forecasting::MovingAverage(dataValues, estimates, noObservations, noAveragingPeriods, ErrorMeasures, Residuals)

.. _forecasting::MovingAverage:

forecasting::MovingAverage
==========================

The moving average procedure is a time series forecasting procedure.
Essentially, this procedure forecasts by taking the average over the
last :math:`N` observations.

Mathematical Formulation
------------------------

    Using the notation for observations and estimates given in
    :numref:`table:notation-observation-estimation`, the estimates are defined as:

    .. math:: e_t = \sum_{\tau=t-1-N}^{t-1} {\tilde y}_\tau / N \mspace{4mu}\mspace{4mu}\mspace{4mu} \textrm{ where } {\tilde y}_\tau = \left\{ \begin{array}{ll} y_1 & \textrm{ if } \tau < 1 \\ y_\tau & \textrm{ if } \tau \in \{1 .. T \} \\ e_\tau & \textrm{ if } \tau > T \end{array} \right.

Function Prototype
------------------

    To provide the error measures and residuals only when you need them,
    there are three flavors of the ``MovingAverage`` procedure provided:

    .. code-block:: aimms

            forecasting::MovingAverage(    ! Provides the estimates, but not the
                                           ! error measures nor the residuals
                  dataValues,              ! Input, parameter indexed over time set
                  estimates,               ! Output, parameter indexed over time set
                  noObservations,          ! Scalar input, length history
                  noAveragingPeriods)      ! Scalar input, averaging length

    .. code-block:: aimms

            forecasting::MovingAverageEM(  ! Provides estimates and error measures, 
                                           ! but not the residuals
                  dataValues,              ! Input, parameter indexed over time set
                  estimates,               ! Output, parameter indexed over time set
                  noObservations,          ! Scalar input, length history
                  noAveragingPeriods,      ! Scalar input, averaging length
                  ErrorMeasures)           ! Output, indexed over forecasting::ems

    .. code-block:: aimms

            forecasting::MovingAverageEMR( ! Provides estimates, error measures,
                                           ! and residuals
                  dataValues,              ! Input, parameter indexed over time set
                  estimates,               ! Output, parameter indexed over time set
                  noObservations,          ! Scalar input, length history
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

    *noAveragingPeriods*
        Specifies the number of values used to compute a single average. This
        parameter corresponds to :math:`N` in the mathematical notation above.

    *ErrorMeasures*
        The error measures as presented in :ref:`chapter:time-series-forecasting`.

    *Residuals*
        The residuals as presented in :ref:`chapter:time-series-forecasting`.

Example
-------

    .. code-block:: aimms
       :caption: Sample declarations and input data for the time series calculation 
       :name: table:sample-input-data

			Parameter sampDat {
				IndexDomain: d;
			}
			Parameter sampEst1 {
				IndexDomain: d;
			}
			Calendar dayCalendar {
				Index: d;
				Parameter: e_d;
				Unit: day;
				BeginDate: "2014-01-01";
				EndDate: "2014-02-14";
				TimeslotFormat: "\%m-\%d";
			}

			sampDat := data 
			{ 01-01 : 46.90141235,  01-02 : 31.89711841,  01-03 : 26.96629187,
			  01-04 : 23.40251489,  01-05 : 33.73439963,  01-06 : 48.02000981,
			  01-07 : 49.04696039,  01-08 : 37.26693007,  01-09 : 41.43336694,
			  01-10 : 24.82954314,  01-11 : 36.55593066,  01-12 : 58.10699762,
			  01-13 : 65.57196981,  01-14 : 58.57130575,  01-15 : 35.72346055,
			  01-16 : 39.68732832,  01-17 : 60.82132259,  01-18 : 64.86992271,
			  01-19 : 68.72671146,  01-20 : 58.78141816,  01-21 : 40.21333644,
			  01-22 : 55.16152950,  01-23 : 64.79961509,  01-24 : 80.05554631,
			  01-25 : 70.93319924,  01-26 : 51.14691246,  01-27 : 47.93612512,
			  01-28 : 71.77896968,  01-29 : 73.84184908,  01-30 : 70.68011104,
			  01-31 : 76.98754704 } ;

    With declarations and data as specified in :numref:`table:sample-input-data` the call:

    .. code-block:: aimms

                    forecasting::MovingAverage(
                        dataValues         :  sampDat, 
                        estimates          :  sampEst1, 
                        noObservations     :  31, 
                        noAveragingPeriods :  5);

    Will result in the following output: 

    .. code-block:: aimms

                    sampEst1 := data 
                    { 01-01 : 46.90141235,  01-02 : 46.90141235,  01-03 : 43.90055356,
                      01-04 : 39.91352947,  01-05 : 35.21374997,  01-06 : 32.58034743,
                      01-07 : 32.80406692,  01-08 : 36.23403532,  01-09 : 38.29416296,
                      01-10 : 41.90033337,  01-11 : 40.11936207,  01-12 : 37.82654624,
                      01-13 : 39.63855369,  01-14 : 45.29956164,  01-15 : 48.72714940,
                      01-16 : 50.90593288,  01-17 : 51.53221241,  01-18 : 52.07507740,
                      01-19 : 51.93466798,  01-20 : 53.96574913,  01-21 : 58.57734065,
                      01-22 : 58.68254227,  01-23 : 57.55058365,  01-24 : 57.53652213,
                      01-25 : 59.80228910,  01-26 : 62.23264531,  01-27 : 64.41936052,
                      01-28 : 62.97427964,  01-29 : 64.37015056,  01-30 : 63.12741111,
                      01-31 : 63.07679348,  02-01 : 68.24492039,  02-02 : 72.30667944,
                      02-03 : 72.41222140,  02-04 : 72.12629586,  02-05 : 72.41553283,
                      02-06 : 71.50112998,  02-07 : 72.15237190,  02-08 : 72.12151039,
                      02-09 : 72.06336819,  02-10 : 72.05078266,  02-11 : 71.97783263,
                      02-12 : 72.07317316,  02-13 : 72.05733341,  02-14 : 72.04449801 } ;

    This can be
    graphically displayed as:

    |image|

    Here the history is from ``01-01`` till ``01-31`` and the horizon is
    from ``02-01`` till ``02-14``.

    .. |image| image:: MovingAverage.png
