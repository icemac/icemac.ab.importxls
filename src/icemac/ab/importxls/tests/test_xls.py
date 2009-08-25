# -*- coding: utf-8 -*-
# Copyright (c) 2009 Michael Howitz
# See also LICENSE.txt

import icemac.ab.importer.reader.testing
import icemac.ab.importxls.xls


class TestXLS(icemac.ab.importer.reader.testing.BaseReaderTest):

    reader_class = icemac.ab.importxls.xls.XLSReader
    import_file = 'long.xls'
    import_file_short = 'short.xls'
