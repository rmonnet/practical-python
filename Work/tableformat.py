# Provides classes to format tables in different ways

class TableFormatter:

    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')


def create_formatter(fmt):

    if fmt == 'txt':
        return TextTableFormatter()

    if fmt == 'csv':
        return CSVTableFormatter()

    if fmt == 'html':
        return HTMLTableFormatter()

    raise FormatError(f'Unknown format {fmt}')


class FormatError(Exception):
    pass


def print_table(data, colnames, formatter):
    cap_colnames = [colname.capitalize() for colname in colnames]
    formatter.headings(cap_colnames)
    for row in data:
        rowdata = []
        for colname in colnames:
            value = getattr(row, colname)
            if isinstance(value, str):
                pass
            elif isinstance(value, float):
                value = f'{value:0.2f}'
            else:
                value = str(value)
            rowdata.append(value)
        formatter.row(rowdata)
