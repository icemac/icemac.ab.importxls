from icemac.addressbook.i18n import MessageFactory as _
import datetime
import icemac.ab.importer.reader.base
import mmap
import xlrd


class XLSReader(icemac.ab.importer.reader.base.BaseReader):

    """Import reader for XLS files."""

    title = _(u'Microsoft Excel file')
    contents = None

    @classmethod
    def open(cls, file_handle):
        reader = super(XLSReader, cls).open(file_handle)
        reader.contents = mmap.mmap(
            reader.file.fileno(), 0, access=mmap.ACCESS_READ)
        reader.wb = xlrd.open_workbook(file_contents=reader.contents)
        reader.sheet = reader.wb.sheet_by_index(0)
        reader.field_names = reader.sheet.row_values(0)
        return reader

    def __del__(self):
        if self.contents is not None:
            self.contents.close()
        super(XLSReader, self).__del__()

    def _convert_value(self, value):
        res = value.value
        if value.ctype == xlrd.XL_CELL_DATE:
            date_tuple = xlrd.xldate_as_tuple(res, self.wb.datemode)
            res = datetime.date(*date_tuple[:3])
        elif res == '':
            res = None
        elif isinstance(res, float):
            res = unicode(res)
        return res

    def getFieldNames(self):
        """Get the names of the fields in the file."""
        return self.field_names

    def getFieldSamples(self, field_name):
        """Get sample values for a field."""
        for val in self.sheet.col_slice(self.field_names.index(field_name),
                                        1, 4):
            val = self._convert_value(val)
            if val is None:
                val = u''
            elif isinstance(val, datetime.date):
                val = unicode(val.strftime('%Y-%m-%d'))
            yield val

    def __iter__(self):
        """Iterate over the file."""
        for index in xrange(1, self.sheet.nrows):
            yield [self._convert_value(val) for val in self.sheet.row(index)]
