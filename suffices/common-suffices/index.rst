Common Suffices
===============

The following collection of suffices are common to all identifier types.

.. toctree::
   :maxdepth: 1

   dim
   txt
   type
   unit

Example
-------

These suffixes are typically appended to an index into the set :aimms:set:`AllIdentifiers`
or a subset thereof. Consider the following declaration: 

.. code-block:: aimms

        Set SelectedIdentifiers {
            SubsetOf   :  AllIdentifiers;
            Index      :  si;
            OrderBy    :  si;
        }

Then the following loop will make a simple overview of those
identifiers:

.. code-block:: aimms
   :caption: Common suffix example
   :name: CommonSuffixExample

        SelectedIdentifiers := AllParameters ; ! Or some other selection.

        put outf ;

        outf.pagewidth := 255 ; ! Wide
        put "type":20, "  ", "name":32, "  ", "dim  ", "unit":20, "  ", "Text", / ;
        put "-"*20,    "  ", "-"*32,    "  ", "---  ", "-"*20,    "  ", "-"*40, / ;

        for ( si ) do                  ! For each selected identifier
            put si.type:20, "  "       ! Type
                si:32, "  ",           ! name
                "(",si.dim:1:0, ")  ", ! dimension
                si.unit:20, "  ",      ! unit
                si.txt, /              ! Documenting text.
        endfor ;

        putclose ;

.. note::

    Note that the suffixes :ref:`.dim`, :ref:`.txt` and :ref:`.type` are
    deprecated. See also :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
