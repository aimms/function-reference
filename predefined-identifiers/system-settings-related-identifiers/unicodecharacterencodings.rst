.. aimms:set:: UnicodeCharacterEncodings

.. _UnicodeCharacterEncodings:

UnicodeCharacterEncodings
=========================

The predefined set :aimms:set:`UnicodeCharacterEncodings` contains the names of
Unicode character encodings.

.. code-block:: aimms

        Set UnicodeCharacterEncodings {
            SubsetOf   :  AllCharacterEncodings;
            Index      :  IndexAvailableCharacterEncodings;
        }

Definition
----------

    The contents of the set :aimms:set:`UnicodeCharacterEncodings` is the collection
    of Unicode character encodings.

Updatability
------------

    The contents of the set can not be modified and is determined at AIMMS
    startup.

.. seealso::

    -  Paragraph Text files in the preliminaries of the language reference
       18.

    -  The encoding attribute of files, see 496.

    -  The set of all character encodings known to AIMMS: :aimms:set:`AllCharacterEncodings`.
