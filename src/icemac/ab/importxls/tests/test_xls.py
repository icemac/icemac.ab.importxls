# -*- coding: utf-8 -*-
# Copyright (c) 2009-2010 Michael Howitz
# See also LICENSE.txt

import icemac.ab.importer.reader.testing
import icemac.ab.importxls.xls


class TestXLS(icemac.ab.importer.reader.testing.ReaderTest):

    reader_class = icemac.ab.importxls.xls.XLSReader
    import_file = 'long.xls'
    import_file_short = 'short.xls'

    def test_getFieldSamples_float_values_are_returned_as_unicode(self):
        self.assertEqual(
            [u'3.1415', u'2.7'],
            list(self.getReader('edge.xls').getFieldSamples(u'float-col')))
