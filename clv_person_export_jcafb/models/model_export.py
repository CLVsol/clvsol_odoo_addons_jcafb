# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import *
from time import time
import xlwt
import csv
import sqlite3
from functools import reduce

from odoo import api, models

_logger = logging.getLogger(__name__)


def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


class ModelExport_xls(models.Model):
    _inherit = 'clv.model_export'

    @api.multi
    def do_model_export_execute_xls_person(self):

        start = time()

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', self.export_dir_path),
        ])

        IRModelFields = self.env['ir.model.fields']
        all_model_fields = IRModelFields.search([
            ('model_id', '=', self.model_id.id),
        ])

        self.date_export = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        model_name = self.model_id.model.replace('.', '_')
        label = ''
        if self.label is not False:
            label = '_' + self.label
        code = self.code
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')[2:]
        file_name = self.export_file_name\
            .replace('<model>', model_name)\
            .replace('_<label>', label)\
            .replace('<code>', code)\
            .replace('<timestamp>', timestamp)
        file_path = self.export_dir_path + '/' + file_name
        _logger.info(u'%s %s', '>>>>>>>>>>', file_path)

        book = xlwt.Workbook()

        sheet = book.add_sheet(file_name)
        row_nr = 0

        row = sheet.row(row_nr)
        col_nr = 0
        if self.export_all_fields is False:
            for field in self.model_export_field_ids:
                col_name = field.field_id.field_description
                if field.name is not False:
                    col_name = field.name
                row.write(col_nr, col_name)
                col_nr += 1
        else:
            for field in all_model_fields:
                col_name = field.name
                row.write(col_nr, col_name)
                col_nr += 1

        item_count = 0
        items = False
        if (self.export_all_items is False) and \
           (self.model_items is not False):
            items = eval('self.' + self.model_items)
        elif self.export_all_items is True:
            Model = self.env[self.model_model]
            items = Model.search(eval(self.export_domain_filter))

        if items is not False:
            for item in items:
                item_count += 1
                row_nr += 1
                row = sheet.row(row_nr)
                col_nr = 0
                if self.export_all_fields is False:
                    for field in self.model_export_field_ids:
                        row.write(col_nr, self._get_value(
                            item, field.field_id,
                            self.export_date_format, self.export_datetime_format)
                        )
                        col_nr += 1

                else:
                    for field in all_model_fields:
                        row.write(col_nr, self._get_value(
                            item, field,
                            self.export_date_format, self.export_datetime_format)
                        )
                        col_nr += 1

                _logger.info(u'>>>>>>>>>>>>>>> %s %s', item_count, item)

        book.save(file_path)

        self.directory_id = file_system_directory.id
        self.file_name = file_name
        self.stored_file_name = file_name

        _logger.info(u'%s %s', '>>>>>>>>>> file_path: ', file_path)
        _logger.info(u'%s %s', '>>>>>>>>>> item_count: ', item_count)
        _logger.info(u'%s %s', '>>>>>>>>>> Execution time: ', secondsToStr(time() - start))


class ModelExport_csv(models.Model):
    _inherit = 'clv.model_export'

    @api.multi
    def do_model_export_execute_csv_person(self):

        start = time()

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', self.export_dir_path),
        ])

        IRModelFields = self.env['ir.model.fields']
        all_model_fields = IRModelFields.search([
            ('model_id', '=', self.model_id.id),
        ])

        self.date_export = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        model_name = self.model_id.model.replace('.', '_')
        label = ''
        if self.label is not False:
            label = '_' + self.label
        code = self.code
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')[2:]
        file_name = self.export_file_name\
            .replace('<model>', model_name)\
            .replace('_<label>', label)\
            .replace('<code>', code)\
            .replace('<timestamp>', timestamp)
        file_path = self.export_dir_path + '/' + file_name
        _logger.info(u'%s %s', '>>>>>>>>>>', file_path)

        file = open(file_path, 'w', newline='')
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

        headings = []

        col_nr = 0
        if self.export_all_fields is False:
            for field in self.model_export_field_ids:
                col_name = field.field_id.field_description
                if field.name is not False:
                    col_name = field.name
                headings.insert(col_nr, col_name)
                col_nr += 1
        else:
            for field in all_model_fields:
                col_name = field.name
                headings.insert(col_nr, col_name)
                col_nr += 1

        writer.writerow(headings)

        item_count = 0
        items = False
        if (self.export_all_items is False) and \
           (self.model_items is not False):
            items = eval('self.' + self.model_items)
        elif self.export_all_items is True:
            Model = self.env[self.model_model]
            items = Model.search(eval(self.export_domain_filter))

        if items is not False:
            for item in items:
                item_count += 1
                row = []
                col_nr = 0
                if self.export_all_fields is False:
                    for field in self.model_export_field_ids:
                        # row.insert(col_nr, self._get_value_csv(
                        row.insert(col_nr, self._get_value(
                            item, field.field_id,
                            self.export_date_format, self.export_datetime_format)
                        )
                        col_nr += 1

                else:
                    for field in all_model_fields:
                        # row.insert(col_nr, self._get_value_csv(
                        row.insert(col_nr, self._get_value(
                            item, field,
                            self.export_date_format, self.export_datetime_format)
                        )
                        col_nr += 1

                _logger.info(u'>>>>>>>>>>>>>>> %s %s', item_count, item)

                writer.writerow(row)

        file.close()

        self.directory_id = file_system_directory.id
        self.file_name = file_name
        self.stored_file_name = file_name

        _logger.info(u'%s %s', '>>>>>>>>>> file_path: ', file_path)
        _logger.info(u'%s %s', '>>>>>>>>>> item_count: ', item_count)
        _logger.info(u'%s %s', '>>>>>>>>>> Execution time: ', secondsToStr(time() - start))


class ModelExport_sqlite(models.Model):
    _inherit = 'clv.model_export'

    @api.multi
    def do_model_export_execute_sqlite_person(self):

        start = time()

        db_name = self._cr.dbname
        table_name = self.model_model.replace('.', '_')
        label = ''
        if self.label is not False:
            label = '_' + self.label
        file_name = self.export_file_name\
            .replace('<dbname>', db_name)\
            .replace('_<label>', label)
        db_path = self.export_dir_path + '/' + file_name
        _logger.info(u'%s %s', '>>>>>>>>>>', db_path)

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', self.export_dir_path),
        ])

        IRModelFields = self.env['ir.model.fields']
        all_model_fields = IRModelFields.search([
            ('model_id', '=', self.model_id.id),
        ])

        conn = sqlite3.connect(db_path)
        conn.text_factory = str

        cursor = conn.cursor()
        try:
            cursor.execute('''DROP TABLE ''' + table_name + ''';''')
        except Exception as e:
            print('------->', e)

        create_table = 'CREATE TABLE ' + table_name + ' ('

        insert_into = 'INSERT INTO ' + table_name
        insert_into_fields = ''
        insert_into_values_1 = ''

        col_nr = 0
        if self.export_all_fields is False:
            for field in self.model_export_field_ids:

                col_name = field.field_id.name
                if col_name == 'values':
                    col_name = "'" + col_name + "'"

                if col_name == 'id':
                    create_table += 'id INTEGER NOT NULL PRIMARY KEY, '
                else:
                    if field.name is not False:
                        col_name = field.name
                    create_table += col_name + ', '
                if col_nr == 0:
                    insert_into_fields += col_name
                    insert_into_values_1 += '?'
                else:
                    insert_into_fields += ', ' + col_name
                    insert_into_values_1 += ',?'
                col_nr += 1
        else:
            for field in all_model_fields:

                col_name = field.name
                if col_name == 'values':
                    col_name = "'" + col_name + "'"

                if col_name == 'id':
                    create_table += 'id INTEGER NOT NULL PRIMARY KEY, '
                else:
                    create_table += col_name + ', '
                if col_nr == 0:
                    insert_into_fields += col_name
                    insert_into_values_1 += '?'
                else:
                    insert_into_fields += ', ' + col_name
                    insert_into_values_1 += ',?'
                col_nr += 1

        create_table += 'new_id INTEGER'
        create_table += ');'

        _logger.info(u'%s %s', '>>>>>>>>>> create_table:', create_table)

        insert_into += ' (' + insert_into_fields + \
                       ') VALUES(' + insert_into_values_1 + ')'

        _logger.info(u'%s %s', '>>>>>>>>>> insert_into:', insert_into)

        cursor.execute(create_table)

        self.date_export = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        item_count = 0
        items = False
        if (self.export_all_items is False) and \
           (self.model_items is not False):
            items = eval('self.' + self.model_items)
        elif self.export_all_items is True:
            Model = self.env[self.model_model]
            items = Model.search(eval(self.export_domain_filter))

        row_nr = 0
        if items is not False:
            for item in items:
                item_count += 1
                row_nr += 1
                col_nr = 0
                values = ()
                if self.export_all_fields is False:
                    for field in self.model_export_field_ids:
                        # values += (self._get_value_sqlite(
                        values += (self._get_value(
                            item, field.field_id,
                            self.export_date_format, self.export_datetime_format),
                        )
                        col_nr += 1

                else:
                    for field in all_model_fields:
                        # values += (self._get_value_sqlite(
                        values += (self._get_value(
                            item, field,
                            self.export_date_format, self.export_datetime_format),
                        )
                        col_nr += 1

                _logger.info(u'>>>>>>>>>>>>>>> %s %s', item_count, item)

                cursor.execute(insert_into, values)

        conn.commit()
        conn.close()

        self.directory_id = file_system_directory.id
        self.file_name = file_name
        # self.stored_file_name = file_name
        self.stored_file_name = False

        _logger.info(u'%s %s', '>>>>>>>>>> db_path: ', db_path)
        _logger.info(u'%s %s', '>>>>>>>>>> item_count: ', item_count)
        _logger.info(u'%s %s', '>>>>>>>>>> Execution time: ', secondsToStr(time() - start))
