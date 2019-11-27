.. aimms:set:: AllCharacterEncodings

.. _AllCharacterEncodings:

AllCharacterEncodings
=====================

The predefined set :aimms:set:`AllCharacterEncodings` contains the names of all
character encodings known to AIMMS.

.. code-block:: aimms

        Set AllCharacterEncodings {
            Index      :  IndexCharacterEncodings;
        }

Definition
----------

    The contents of the set :aimms:set:`AllCharacterEncodings` is the collection of
    all character encodings known to AIMMS.

Updatability
------------

    The contents of the set can not be modified; it has the following fixed
    contents: 

    .. code-block:: aimms

            AllCharacterEncodings := data 
            { ASMO-708     , ! Arabic

              BIG5         , ! Chinese used in Taiwan, Hong Kong, and 
                             ! Macau for Traditional Chinese characters.

              CP737        , ! Greek
              CP875        , ! EBCDIC Greek Modern
              CP932        , ! Windows SHift JIS, Japan
              CP949        , ! Windows Korean

              EUC-CN       , ! Extended Unix Code, simplified Chinese
              EUC-JP       , ! Extended Unix Code, Japanese

              GB2312       , ! Chinese national standard
              GB18030      , ! Chinese national standard

              IBM037       , ! EBCDIC with Latin-1
              IBM273       , ! EBCDIC German
              IBM277       , ! EBCDIC Danish
              IBM278       , ! EBCDIC Finnish
              IBM280       , ! EBCDIC Italian
              IBM284       , ! EBCDIC Spanish
              IBM285       , ! EBCDIC British
              IBM290       , ! EBCDIC Japanese
              IBM297       , ! EBCDIC French
              IBM420       , ! EBCDIC Arabic
              IBM423       , ! EBCDIC Greek
              IBM424       , ! EBCDIC Hebrew
              IBM437       , ! EBCDIC Latin-1 (PC)
              IBM500       , ! EBCDIC Latin-1 International
              IBM775       , ! EBCDIC Polish
              IBM850       , ! IBM ASCII Latin 1
              IBM852       , ! IBM ASCII Latin 2
              IBM855       , ! IBM ASCII Cyrillic
              IBM857       , ! IBM ASCII Turkish
              IBM860       , ! IBM DOS Portuguese
              IBM861       , ! IBM DOS Icelandic
              IBM862       , ! IBM DOS Hebrew
              IBM863       , ! IBM DOS French Canadian
              IBM864       , ! IBM DOS Arabic
              IBM865       , ! IBM DOS Nordic
              IBM866       , ! IBM DOS Cyrillic
              IBM869       , ! IBM DOS Greek
              IBM870       , ! IBM EBCDIC Latin 2
              IBM871       , ! IBM EBCDIC Iceland
              IBM880       , ! IBM EBCDIC Cyrillic Russian
              IBM905       , ! IBM EBCDIC Turkish
              IBM1026      , ! IBM EBCDIC Turkish Latin 5

              ISO-2022-KR  , ! ISO 2022 Korean
              ISO-8859-1   , ! ASCII based Latin-1 (West  European)
              ISO-8859-2   , ! ASCII based Latin-2 (East  European)
              ISO-8859-3   , ! ASCII based Latin-3 (South European)
              ISO-8859-4   , ! ASCII based Latin-4 (North European)
              ISO-8859-5   , ! ASCII based Latin/Cyrillic
              ISO-8859-6   , ! ASCII based Latin/Arabic
              ISO-8859-7   , ! ASCII based Latin/Greek
              ISO-8859-9   , ! ASCII based Latin-5 Turkish
              ISO-8859-13  , ! ASCII based Latin-7 Baltic Rim
              ISO-8859-15  , ! ASCII based Latin-9 Western European

              JOHAB        , ! Korean

              KOI8-R       , ! Cyrillic 8 bit Russian
              KOI8-U       , ! Cyrillic 8 bit Ukrainian

              US-ASCII     , ! 7 bit ASCII

              UTF-16BE     , ! Unicode 2 byte, Big endian
              UTF-16LE     , ! Unicode 2 byte, Little endian
              UTF-32BE     , ! Unicode 4 byte, Big endian
              UTF-32LE     , ! Unicode 4 byte, Little endian

              UTF8         , ! Unicode multi-byte and preferred!

              WINDOWS-874  , ! ASCII Windows Thai
              WINDOWS-1250 , ! ASCII Windows Latin Central European
              WINDOWS-1251 , ! ASCII Windows Cyrillic
              WINDOWS-1252 , ! ASCII Windows Latin Wetern European
              WINDOWS-1253 , ! ASCII Windows Greek
              WINDOWS-1254 , ! ASCII Windows Turkish
              WINDOWS-1255 , ! ASCII Windows Hebrew
              WINDOWS-1256 , ! ASCII Windows Arabic
              WINDOWS-1257 , ! ASCII Windows Latin Baltic
              WINDOWS-1258 } ! ASCII Windows Vietnamese

.. note::

    Not all character encodings enumerated above may be available on your
    system. The subset of available character encodings is :aimms:set:`AllAvailableCharacterEncodings`. The
    set :aimms:set:`AllCharacterEncodings` is the range for the options:

    -  ``aim_input_character_encoding`` used for reading and writing of
       model text files,

    -  ``ascii_case_character_encoding`` used for reading cases created by
       the ASCII flavor of AIMMS 3.13 and older,

    -  ``default_input_character_encoding`` used during a ``read from file``
       statement,

    -  ``default_output_character_encoding`` used during a ``write to file``
       and ``put`` statements, and

    -  ``external_string_character_encoding`` used for communicating strings
       to external DLLs.

.. seealso::

    -  Paragraph Text files in the preliminaries of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__
       18.

    -  The encoding attribute of files, see page 496 of the Language
       Reference.

    -  The set of character encodings available to the current AIMMS
       session: :aimms:set:`AllAvailableCharacterEncodings`.
