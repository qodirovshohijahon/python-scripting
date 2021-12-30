#!/usr/bin/env python

'''
    usage:   splitv.py my.pdf

    Creates splitv.my.pdf

    This is similar to unspread.py, in that it creates
    a new file that has twice the pages of the old file.

    It is different in two ways:

    1) It splits pages top and bottom rather than left and right
    2) The destination pages are the same size as the source pages,
    and the output is placed at the top.
'''

import sys
import os

from pdfrw import PdfReader, PdfWriter, PageMerge


def splitpage(src):
    ''' Split a page into two (top and bottom)
    '''
    # Yield a result for each half of the page
    for y_pos in (0, 0.5):

        # Create a blank, unsized destination page.
        page = PageMerge()

        # add a portion of the source page to it as
        # a Form XObject.
        page.add(src, viewrect=(0, y_pos, 1, 0.5))

        # By default, the object we created will be
        # at coordinates (0, 0), which is the lower
        # left corner.  To move it up on the page
        # to the top, we simply use its height
        # (which is half the source page height) as
        # its y value.
        page[0].y = page[0].h

        # When we render the page, the media box will
        # encompass (0, 0) and all the objects we have
        # placed on the page, which means the output
        # page will be the same size as the input page.
        yield page.render()


inpfn = sys.argv[1:]
outfn = 'splitv.' + os.path.basename(inpfn)
writer = PdfWriter()
for page in PdfReader(inpfn).pages:
    writer.addpages(splitpage(page))
writer.write(outfn)

splitpage("/home/mustofa/Downloads/chapter1.pdf")