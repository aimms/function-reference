Forecasting Functions
*********************

AIMMS supports the following functions for making forecasts:

-  :aimms:func:`forecasting::MovingAverage`
-  :aimms:func:`forecasting::WeightedMovingAverage`
-  :aimms:func:`forecasting::ExponentialSmoothing`
-  :aimms:func:`forecasting::ExponentialSmoothingTrend`
-  :aimms:func:`forecasting::ExponentialSmoothingTrendSeasonality`
-  :aimms:func:`forecasting::ExponentialSmoothingTune`
-  :aimms:func:`forecasting::ExponentialSmoothingTrendTune`
-  :aimms:func:`forecasting::ExponentialSmoothingTrendSeasonalityTune`
-  :aimms:func:`forecasting::SimpleLinearRegression`

.. _section:Forecasting-Introduction:

Introduction
============

AIMMS is a development tool for decision support application. Important
to decision support are good forecasts. The ``AIMMSForecasting`` library
provides tools to compute forecasts from historical data. The usage of
this library is discussed in this chapter.

Installation
------------

Before the functions in this section can be used in your model, you will
need to add the library

Prefix
------

The prefix of the ``AIMMSForecasting`` library is ``forecasting``.

Restriction
-----------

This library does not support the special values ``NA``, ``ZERO``,
``-INF``, ``INF``, and ``UNDF``.

.. _chapter:time-series-forecasting:

Time Series Forecasting
=======================

.. _subsection:Time-series-forcasting:

Notational Conventions Time Series Forecasting
----------------------------------------------

For time series forecasting, such as **Moving Average** and
**Exponential Smoothing**, we follow the conventions below.

Observations and Estimates
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``AIMMSForecasting`` library uses as input observations made in the
history. It provides estimates over both the history and the horizon. A
single set and index is used to index both the history and the
estimates, this set is called the **time set**. In addition, you will
need to specify the number of elements that belong to the history. The
corresponding mathematical notation is:

.. _table:notation-observation-estimation:

.. table:: Time series forecasting notation

   ====================================== ======================
   :math:`T`                              number of observations
   :math:`H`                              length of horizon
   :math:`\{1\ldots T+H\}`                time set
   :math:`t`                              index in time set
   :math:`y_t, t \in \{1\ldots T\}`       observation
   :math:`e_t, t \in \textrm{ time set }` estimate
   ====================================== ======================

The forecasts are provided in :math:`e_t`,
:math:`t \in \{T+1 \ldots T+H\}`.

Residuals
^^^^^^^^^

The residual, :math:`r_t` where :math:`t \in \{1\ldots T\}`, is the
difference between the corresponding observation :math:`y_t` and
estimate :math:`e_t`. To obtain the residuals, you will need to provide
a parameter declared over the time set.

Error Measures
^^^^^^^^^^^^^^

From the residuals, error measures such as Mean Absolute Deviation
(MAD), Mean Absolute Percentage Error (MAPE), and Mean Squared Deviation
(MSD) can be computed.

Predeclared Index ``ems``
^^^^^^^^^^^^^^^^^^^^^^^^^

Whenever one of the time series forecasting functions communicates the
error measures, it uses identifiers declared over the index
``forecasting::ems``, declared as follows:

.. code-block:: aimms

            Set ErrorMeasureSet {
                Index: ems;
                Definition: {
                    data {
                        MAD,  ! Mean Absolute Deviation
                        MAPE, ! Mean Absolute Percentage Error (provided as fraction)
                        MSE   ! Mean Squared Error
                    }
                }
            }

To obtain the error measures, you will need to provide a parameter indexed over ``forecasting::ems`` to the time series forecasting functions.
Note that the MAPE is a fraction, in order to use it as a percentage, you can use the predeclared quantity ``SI_unitless``.
For instance, given the declarations:

.. code-block:: aimms

            Quantity SI_Unitless {
                BaseUnit: -;
                Conversions: % -> - : # -> # / 100;
                Comment: "Expresses a dimensionless value.";
            }
            Parameter myMAPE {
                Unit: %;
            }
            Parameter myErrorMeasures { 
                IndexDomain: forecasting::ems;
            }

The following statements:

.. code-block:: aimms

            myMAPE := myErrorMeasures('MAPE') ;
            display myErrorMeasures, myMAPE ;

The output may look as follows:

.. code-block:: aimms

            myErrorMeasures := data { MAPE : 0.417092,  MAD : 1.785714,  MSE : 3.982143 } ;
            myMAPE := 41.709184 [%] ;

AIMMS supports the following functions for making time series forecasts:

.. toctree::
   :maxdepth: 1

   forecasting_movingaverage
   forecasting_weightedmovingaverage
   forecasting_exponentialsmoothing
   forecasting_exponentialsmoothingtrend
   forecasting_exponentialsmoothingtrendseasonality
   forecasting_exponentialsmoothingtune
   forecasting_exponentialsmoothingtrendtune
   forecasting_exponentialsmoothingtrendseasonalitytune
   
Simple Linear Regression
========================

.. _section: Simple-Linear-Regression-Notation:

Notational Conventions for Simple Linear Regression
---------------------------------------------------

For simple linear regression we follow the conventions below.

Observations and Estimates
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``AimmsForecasting`` library uses as input data observations for the
independent variable and the dependent variable. It provides estimates
for the coefficients of the simple linear regression line.

.. _table:notation-observation-data-SLR:

.. table:: Simple Linear Regression notation 

    ======================================== ======================================================
    :math:`N`                                number of observations
    :math:`x_i, i \in \{1\ldots N\}`         observations of the independent variable
    :math:`y_i, i \in \{1\ldots N\}`         observations of the dependent variable
    :math:`\bar{x}=(1/N)\sum_{i=1}^{N}x_{i}` average of the independent observations
    :math:`\bar{y}=(1/N)\sum_{i=1}^{N}y_{i}` average of the dependent observations
    :math:`\hat{y}_i, i \in \{1\ldots N\}`   predictions of the dependent variable
    :math:`\beta_{0}, \beta_{1}`             coefficients of the linear relationship (random)
    :math:`\hat{\beta}_{0}, \hat{\beta}_{1}` coefficients of the linear regression line (estimates)
    :math:`e_i, i \in \{1\ldots N\}`         error (residual) for observation data points
    ======================================== ======================================================

Linear Relationship
^^^^^^^^^^^^^^^^^^^

The linear relationship between :math:`x_i` and :math:`y_i` is modeled
by the equation:

.. math:: y_i = \beta_{0} + \beta_{1}x_i + \epsilon_i

where :math:`\epsilon_i` is an error term which averages out to 0 for
every :math:`i`.

Linear Regression
^^^^^^^^^^^^^^^^^

The random :math:`\beta_{0}` and :math:`\beta_{1}` are estimated by
:math:`\hat{\beta}_{0}` and :math:`\hat{\beta}_{1}`, such that the
prediction for :math:`y_i` is given by the equation:

.. math:: \hat{y}_i = \hat{\beta}_{0} + \hat{\beta_{1}}x_i 
   :label: SLR-line

So, the predictions based on simple linear regression corresponding to
the observation data points :math:`(x_i,y_i)` are provided in
:math:`\hat{y}_i, i \in \{1\ldots N\}`.

Residuals
^^^^^^^^^

The error (residual) :math:`e_i` for the data point :math:`i` is the
difference between the observed :math:`y_i` and the predicted
:math:`\hat{y}_i`, so
:math:`e_i = y_i - \hat{\beta}_0 - \hat{\beta}_1x_i`. In order to obtain
the residuals, the user will need to provide a one-dimensional parameter
declared over the set of observations.

Variation Components
^^^^^^^^^^^^^^^^^^^^

Given the values of the observations, the estimates, and the
residuals, several components of variation can be computed, such as
**sum of squares total** = SST, **sum of squares error** = SSE, and
**sum of squares regression** = SSR, which are defined as follows:

.. math:: SST = \sum_{i=1}^{N}(y_i - \bar{y})^2

.. math:: SSE = \sum_{i=1}^{N}(y_i - \hat{y}_i)^2 = \sum_{i=1}^{N}e_i^2

.. math:: SSR = \sum_{i=1}^{N}(\hat{y}_i - \bar{y})^2

These components of variation satisfy the relation :math:`SST = SSE + SSR`.

Furthermore, it is also possible to compute the **coefficient of
determination** = :math:`R^2`, the **sample linear correlation** =
:math:`r_{xy}`, and the **standard error of the estimate** =
:math:`s_e`, which are defined as follows:

.. math:: R^2 = \frac{SSR}{SST}

.. math:: r_{xy} = \left\{ \begin{array}{ll} +\sqrt{R^2} & \textrm{ if } \hat{\beta}_1 \geq 0 \\ -\sqrt{R^2} & \textrm{ if } \hat{\beta}_1 \leq 0 \end{array} \right.

.. math:: s_e = \sqrt{\frac{SSE}{N-2}}

Predeclared Index ``vcs``
^^^^^^^^^^^^^^^^^^^^^^^^^

The linear regression functions return the values of the line
coefficients in a parameter declared over the index ``forecasting::co``
declared as follows: 

.. code-block:: aimms

               Set LRcoeffSet{
                   Index: co;
                   Definition: {
                     data {
                       0,      ! Intercept Coefficient of Regression Line
                       1       ! Slope Coefficient of Regression Line
                     }
                   }
                 }

Whenever one of the linear regression
functions communicates back components of variations, it uses
identifiers declared over the index ``forecasting::vcs`` declared as
follows: 

.. code-block:: aimms

               Set VariationCompSet {
                   Index: vcs;
                   Definition: {
                      data {
                          SST,       ! Sum of Squares Total
                          SSE,       ! Sum of Squares Error
                          SSR,       ! Sum of Squares Regression
                          Rsquare,   ! Coefficient of Determination
                          MultipleR, ! Sample Linear Correlation Rxy
                          Se         ! Standard Error
                         }
                     }
                   }

In order to obtain the variation components, the
user will need to provide a parameter indexed over ``forecasting::vcs``
to the linear regression functions.

AIMMS supports the following function for simple linear regression:

.. toctree::
   :maxdepth: 1

   forecasting_simplelinearregression