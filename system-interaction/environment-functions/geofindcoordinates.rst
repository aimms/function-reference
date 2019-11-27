.. aimms:procedure:: GeoFindCoordinates(address, latitude, longitude, email, url)

.. _GeoFindCoordinates:

GeoFindCoordinates
==================

The procedure :aimms:func:`GeoFindCoordinates` can be used to find the
latitude/longitude coordinates for a given address. The procedure uses
the free `OpenStreetMap <http://www.openstreetmap.org>`__ (OSM)
geocoding service. You are advised to carefully read the OSM geocoder
`usage
policy <http://wiki.openstreetmap.org/wiki/Nominatim#Usage_Policy>`__
before using this procedure in your application.

.. code-block:: aimms

    GeoFindCoordinates(
         address,             ! (input) scalar string expression
         latitude,            ! (output) scalar numerical parameter
         longitude,           ! (output) scalar numerical parameter
         email,               ! (optional) scalar string parameter
         url                  ! (optional) scalar string parameter
         )

Arguments
---------

    *address*
        A string representing the address for which the latitude and longitude
        coordinates have to be found.

    *latitude*
        A scalar numerical parameter that will contain the latitude coordinate
        of the specified address upon success.

    *longitude*
        A scalar numerical parameter that will contain the longitude coordinate
        of the specified address upon success.

    *email*
        An optional string representing the email address that the OSM
        organization will use to contact you in the event of problems (as
        mentioned in their `usage
        policy <http://wiki.openstreetmap.org/wiki/Nominatim#Usage_Policy>`__).

    *url*
        An optional string representing the url of an alternative (e.g. your
        own) OSM geocoder server. If not specified, the public OSM geocoder
        server is being used.

Return Value
------------

    The procedure returns 1 on success, and 0 if the specified address could
    not be found. On failure, the pre-defined identifier :aimms:set:`CurrentErrorMessage` will
    contain a proper error message.

Example
-------

    The following calls to the procedure :aimms:func:`GeoFindCoordinates` return valid
    latitude and longitude coordinates 

    .. code-block:: aimms

            GeoFindCoordinates("Netherlands", Latitude, Longitude, "me@mycompany.com");
            GeoFindCoordinates("Haarlem, Netherlands", Latitude, Longitude);
            GeoFindCoordinates("2034 Haarlem, Netherlands", Latitude, Longitude);
            GeoFindCoordinates("Schipholweg, Haarlem, Netherlands", Latitude, Longitude);    

            GeoFindCoordinates("US", Latitude, Longitude);
            GeoFindCoordinates("Kirkland, WA, US", Latitude, Longitude);
            GeoFindCoordinates("Lake Washington Boulevard NE, Kirkland, US", Latitude, Longitude);
            GeoFindCoordinates("5400 Carillon Point, Kirkland, US", Latitude, Longitude);

            GeoFindCoordinates("Singapore", Latitude, Longitude);
            GeoFindCoordinates("Chulia Street, Singapore", Latitude, Longitude);

            GeoFindCoordinates("Shanghai, China", Latitude, Longitude);
            GeoFindCoordinates("Middle Huaihai Road, Shanghai, China", Latitude, Longitude);

    assumed that *Latitude*
    and *Longitude* are declared as numerical parameters in your model.

.. note::

    -  With the introduction of AIMMS 3.9.5 and AIMMS 3.10 PR, this
       procedure has been disabled because Microsoft discontinued support to
       the Virtual Earth geocoder service that was used to locate the
       address. In AIMMS 3.11 FR2, the :aimms:func:`GeoFindCoordinates` procedure was
       enabled again by using the OSM `geocoding
       service <http://wiki.openstreetmap.org/wiki/Nominatim>`__ instead.

    -  *'One of the hard things about geocoding is parsing addresses into
       something intelligible'* (see the OpenStreetMap
       `wiki <http://wiki.openstreetmap.org/wiki/Geocoding>`__ for details
       on address formats). As a result, you may need to slightly play
       around with the address format in order for the geocoder to correctly
       parse your address.

    -  To discourage *'bulk geocoding'* (see the OSM `usage
       policy <http://wiki.openstreetmap.org/wiki/Nominatim#Usage_Policy>`__
       for more details), AIMMS inserts a small delay in case the time
       between two consecutive geocoding requests is smaller than a second.
