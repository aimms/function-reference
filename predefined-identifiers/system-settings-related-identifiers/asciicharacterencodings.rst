.. aimms:set:: ASCIICharacterEncodings

.. _ASCIICharacterEncodings:

ASCIICharacterEncodings
=======================

The predefined set :aimms:set:`ASCIICharacterEncodings` contains the names of
ASCII character encodings. Here an ASCII character encoding is an
encoding whereby code point 33 thru 126 are the same as the US-ASCII
encoding.

.. code-block:: aimms

        Set ASCIICharacterEncodings {
            SubsetOf   :  AllCharacterEncodings;
            Index      :  IndexAvailableCharacterEncodings;
        }

Definition
----------

    The contents of the set :aimms:set:`ASCIICharacterEncodings` is the collection of
    ASCII character encodings.

Updatability
------------

    The contents of the set can not be modified and is determined at AIMMS
    startup.

.. seealso::

    -  Paragraph Text files in the preliminaries of the language reference
       18.

    -  The encoding attribute of files, see 496.

    -  The set of all character encodings known to AIMMS: :aimms:set:`AllCharacterEncodings`.
