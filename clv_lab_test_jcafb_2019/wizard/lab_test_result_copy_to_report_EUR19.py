# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class LabTestResultCopyToReport(models.TransientModel):
    _inherit = 'clv.lab_test.result.copy_to_report'

    #
    # EUR19
    #

    def _default_is_EUR19(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EUR19':
            is_EUR19 = True
        else:
            is_EUR19 = False
        return is_EUR19
    is_EUR19 = fields.Boolean('Is EUR19', readonly=True, default=_default_is_EUR19)

    def _default_EUR19_volume(self):
        return self._get_default('EUR19', 'EUR19-02-01')
    EUR19_volume = fields.Char(
        'Volume', readonly=False, default=_default_EUR19_volume
    )

    def _write_EUR19_volume(self):
        self._set_result('EUR19', 'EUR19-02-01', self.EUR19_volume)
        self._copy_result('EUR19', 'EUR19-02-01', self.EUR19_volume)

    def _default_EUR19_densidade(self):
        return self._get_default('EUR19', 'EUR19-02-02')
    EUR19_densidade = fields.Char(
        'Densidade', readonly=False, default=_default_EUR19_densidade
    )

    def _write_EUR19_densidade(self):
        self._set_result('EUR19', 'EUR19-02-02', self.EUR19_densidade)
        self._copy_result('EUR19', 'EUR19-02-02', self.EUR19_densidade)

    def _default_EUR19_aspecto(self):
        return self._get_default('EUR19', 'EUR19-02-03')
    EUR19_aspecto = fields.Selection([
        (u'Límpido', u'Límpido'),
        (u'Ligeiramente Turvo', u'Ligeiramente Turvo'),
        (u'Turvo', u'Turvo'),
    ], 'Aspecto', readonly=False, default=_default_EUR19_aspecto)

    def _write_EUR19_aspecto(self):
        self._set_result('EUR19', 'EUR19-02-03', self.EUR19_aspecto)
        self._copy_result('EUR19', 'EUR19-02-03', self.EUR19_aspecto)

    def _default_EUR19_cor(self):
        return self._get_default('EUR19', 'EUR19-02-04')
    EUR19_cor = fields.Selection([
        (u'Amarela Palha', u'Amarela Palha'),
        (u'Amarela Claro', u'Amarela Claro'),
        (u'Amarela Citrino', u'Amarela Citrino'),
        (u'Amarela Ouro', u'Amarela Ouro'),
        (u'Eritrocrômica', u'Eritrocrômica'),
        (u'Âmbar', u'Âmbar'),
    ], 'Cor', readonly=False, default=_default_EUR19_cor)

    def _write_EUR19_cor(self):
        self._set_result('EUR19', 'EUR19-02-04', self.EUR19_cor)
        self._copy_result('EUR19', 'EUR19-02-04', self.EUR19_cor)

    def _default_EUR19_odor(self):
        return self._get_default('EUR19', 'EUR19-02-05')
    EUR19_odor = fields.Selection([
        (u'Sui Generis', u'Sui Generis'),
        (u'Pútrido', u'Pútrido'),
    ], 'Odor', readonly=False, default=_default_EUR19_odor)

    def _write_EUR19_odor(self):
        self._set_result('EUR19', 'EUR19-02-05', self.EUR19_odor)
        self._copy_result('EUR19', 'EUR19-02-05', self.EUR19_odor)

    def _default_EUR19_ph(self):
        return self._get_default('EUR19', 'EUR19-03-01')
    EUR19_ph = fields.Char(
        'pH', readonly=False, default=_default_EUR19_ph
    )

    def _write_EUR19_ph(self):
        self._set_result('EUR19', 'EUR19-03-01', self.EUR19_ph)
        self._copy_result('EUR19', 'EUR19-03-01', self.EUR19_ph)

    def _default_EUR19_proteinas(self):
        return self._get_default('EUR19', 'EUR19-03-02')
    EUR19_proteinas = fields.Selection([
        (u'Negativo', u'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Proteina', readonly=False, default=_default_EUR19_proteinas)

    def _write_EUR19_proteinas(self):
        self._set_result('EUR19', 'EUR19-03-02', self.EUR19_proteinas)
        self._copy_result('EUR19', 'EUR19-03-02', self.EUR19_proteinas)

    def _default_EUR19_glicose(self):
        return self._get_default('EUR19', 'EUR19-03-03')
    EUR19_glicose = fields.Selection([
        (u'Negativo', u'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Glicose', readonly=False, default=_default_EUR19_glicose)

    def _write_EUR19_glicose(self):
        self._set_result('EUR19', 'EUR19-03-03', self.EUR19_glicose)
        self._copy_result('EUR19', 'EUR19-03-03', self.EUR19_glicose)

    def _default_EUR19_cetona(self):
        return self._get_default('EUR19', 'EUR19-03-04')
    EUR19_cetona = fields.Selection([
        (u'Negativo', u'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Cetona', readonly=False, default=_default_EUR19_cetona)

    def _write_EUR19_cetona(self):
        self._set_result('EUR19', 'EUR19-03-04', self.EUR19_cetona)
        self._copy_result('EUR19', 'EUR19-03-04', self.EUR19_cetona)

    def _default_EUR19_pigmentos_biliares(self):
        return self._get_default('EUR19', 'EUR19-03-05')
    EUR19_pigmentos_biliares = fields.Selection([
        (u'Negativo', u'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Pigmentos biliares', readonly=False, default=_default_EUR19_pigmentos_biliares)

    def _write_EUR19_pigmentos_biliares(self):
        self._set_result('EUR19', 'EUR19-03-05', self.EUR19_pigmentos_biliares)
        self._copy_result('EUR19', 'EUR19-03-05', self.EUR19_pigmentos_biliares)

    def _default_EUR19_sangue(self):
        return self._get_default('EUR19', 'EUR19-03-06')
    EUR19_sangue = fields.Selection([
        (u'Negativo', u'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Sangue', readonly=False, default=_default_EUR19_sangue)

    def _write_EUR19_sangue(self):
        self._set_result('EUR19', 'EUR19-03-06', self.EUR19_sangue)
        self._copy_result('EUR19', 'EUR19-03-06', self.EUR19_sangue)

    def _default_EUR19_urobilinogenio(self):
        return self._get_default('EUR19', 'EUR19-03-07')
    EUR19_urobilinogenio = fields.Selection([
        (u'Normal', u'Normal'),
        (u'Positivo até Diluição de 1/20', u'Positivo até Diluição de 1/20'),
        (u'Positivo até Diluição de 1/40', u'Positivo até Diluição de 1/40'),
        (u'Positivo até Diluição de 1/80', u'Positivo até Diluição de 1/80'),
        (u'Positivo até Diluição de 1/160', u'Positivo até Diluição de 1/160'),
        (u'Positivo até Diluição de 1/320', u'Positivo até Diluição de 1/320'),
        (u'Positivo até Diluição de 1/640', u'Positivo até Diluição de 1/640'),
        (u'Positivo até Diluição de 1/1280', u'Positivo até Diluição de 1/1280'),
        (u'Positivo até Diluição de 1/2560', u'Positivo até Diluição de 1/2560'),
    ], 'Urobilinogênio', readonly=False, default=_default_EUR19_urobilinogenio)

    def _write_EUR19_urobilinogenio(self):
        self._set_result('EUR19', 'EUR19-03-07', self.EUR19_urobilinogenio)
        self._copy_result('EUR19', 'EUR19-03-07', self.EUR19_urobilinogenio)

    def _default_EUR19_nitrito(self):
        return self._get_default('EUR19', 'EUR19-03-08')
    EUR19_nitrito = fields.Selection([
        (u'Negativo', u'Negativo'),
        (u'Positivo', u'Positivo'),
    ], 'Nitrito', readonly=False, default=_default_EUR19_nitrito)

    def _write_EUR19_nitrito(self):
        self._set_result('EUR19', 'EUR19-03-08', self.EUR19_nitrito)
        self._copy_result('EUR19', 'EUR19-03-08', self.EUR19_nitrito)

    def _default_EUR19_celulas_epiteliais(self):
        return self._get_default('EUR19', 'EUR19-04-01')
    EUR19_celulas_epiteliais = fields.Selection([
        (u'Ausentes', u'Ausentes'),
        (u'Raras', u'Raras'),
        (u'Frequentes', u'Frequentes'),
        (u'Numerosas', u'Numerosas'),
    ], 'Células Epiteliais', readonly=False, default=_default_EUR19_celulas_epiteliais)

    def _write_EUR19_celulas_epiteliais(self):
        self._set_result('EUR19', 'EUR19-04-01', self.EUR19_celulas_epiteliais)
        self._copy_result('EUR19', 'EUR19-04-01', self.EUR19_celulas_epiteliais)

    def _default_EUR19_muco(self):
        return self._get_default('EUR19', 'EUR19-04-02')
    EUR19_muco = fields.Selection([
        (u'Ausente', u'Ausente'),
        (u'Raros Filamentos', u'Raros Filamentos'),
        (u'Frequentes Filamentos', u'Frequentes Filamentos'),
        (u'Numerosos Filamentos', u'Numerosos Filamentos'),
    ], 'Muco', readonly=False, default=_default_EUR19_muco)

    def _write_EUR19_muco(self):
        self._set_result('EUR19', 'EUR19-04-02', self.EUR19_muco)
        self._copy_result('EUR19', 'EUR19-04-02', self.EUR19_muco)

    def _default_EUR19_leucocitos(self):
        return self._get_default('EUR19', 'EUR19-04-04')
    EUR19_leucocitos = fields.Char(
        'Leucócitos', readonly=False, default=_default_EUR19_leucocitos
    )

    def _write_EUR19_leucocitos(self):
        self._set_result('EUR19', 'EUR19-04-04', self.EUR19_leucocitos)
        self._copy_result('EUR19', 'EUR19-04-04', self.EUR19_leucocitos)

    def _default_EUR19_hemacias(self):
        return self._get_default('EUR19', 'EUR19-04-05')
    EUR19_hemacias = fields.Char(
        'Hemácias', readonly=False, default=_default_EUR19_hemacias
    )

    def _write_EUR19_hemacias(self):
        self._set_result('EUR19', 'EUR19-04-05', self.EUR19_hemacias)
        self._copy_result('EUR19', 'EUR19-04-05', self.EUR19_hemacias)

    def _default_EUR19_cilindros(self):
        return self._get_default('EUR19', 'EUR19-04-06')
    EUR19_cilindros = fields.Selection([
        (u'Ausentes', u'Ausentes'),
        (u'Presentes', u'Presentes'),
    ], 'Cilindros', readonly=False, default=_default_EUR19_cilindros)

    def _write_EUR19_cilindros(self):
        self._set_result('EUR19', 'EUR19-04-06', self.EUR19_cilindros)
        self._copy_result('EUR19', 'EUR19-04-06', self.EUR19_cilindros)

    def _default_EUR19_cilindros_hialinos(self):
        return self._get_default('EUR19', 'EUR19-04-07')
    EUR19_cilindros_hialinos = fields.Char(
        'Cilindros Hialinos', readonly=False, default=_default_EUR19_cilindros_hialinos
    )

    def _write_EUR19_cilindros_hialinos(self):
        self._set_result('EUR19', 'EUR19-04-07', self.EUR19_cilindros_hialinos)
        self._copy_result('EUR19', 'EUR19-04-07', self.EUR19_cilindros_hialinos)

    def _default_EUR19_cilindros_granulosos(self):
        return self._get_default('EUR19', 'EUR19-04-08')
    EUR19_cilindros_granulosos = fields.Char(
        'Cilindros Granulosos', readonly=False, default=_default_EUR19_cilindros_granulosos
    )

    def _write_EUR19_cilindros_granulosos(self):
        self._set_result('EUR19', 'EUR19-04-08', self.EUR19_cilindros_granulosos)
        self._copy_result('EUR19', 'EUR19-04-08', self.EUR19_cilindros_granulosos)

    def _default_EUR19_cilindros_leucocitarios(self):
        return self._get_default('EUR19', 'EUR19-04-09')
    EUR19_cilindros_leucocitarios = fields.Char(
        'Cilindros Leucocitários', readonly=False, default=_default_EUR19_cilindros_leucocitarios
    )

    def _write_EUR19_cilindros_leucocitarios(self):
        self._set_result('EUR19', 'EUR19-04-09', self.EUR19_cilindros_leucocitarios)
        self._copy_result('EUR19', 'EUR19-04-09', self.EUR19_cilindros_leucocitarios)

    def _default_EUR19_cilindros_hematicos(self):
        return self._get_default('EUR19', 'EUR19-04-10')
    EUR19_cilindros_hematicos = fields.Char(
        'Cilindros Hemáticos', readonly=False, default=_default_EUR19_cilindros_hematicos
    )

    def _write_EUR19_cilindros_hematicos(self):
        self._set_result('EUR19', 'EUR19-04-10', self.EUR19_cilindros_hematicos)
        self._copy_result('EUR19', 'EUR19-04-10', self.EUR19_cilindros_hematicos)

    def _default_EUR19_cilindros_cereos(self):
        return self._get_default('EUR19', 'EUR19-04-11')
    EUR19_cilindros_cereos = fields.Char(
        'Cilindros Céreos', readonly=False, default=_default_EUR19_cilindros_cereos
    )

    def _write_EUR19_cilindros_cereos(self):
        self._set_result('EUR19', 'EUR19-04-11', self.EUR19_cilindros_cereos)
        self._copy_result('EUR19', 'EUR19-04-11', self.EUR19_cilindros_cereos)

    def _default_EUR19_outros_tipos_de_cilindros(self):
        return self._get_default('EUR19', 'EUR19-04-12')
    EUR19_outros_tipos_de_cilindros = fields.Char(
        'Outros tipos de Cilindros', readonly=False, default=_default_EUR19_outros_tipos_de_cilindros
    )

    def _write_EUR19_outros_tipos_de_cilindros(self):
        self._set_result('EUR19', 'EUR19-04-12', self.EUR19_outros_tipos_de_cilindros)
        self._copy_result('EUR19', 'EUR19-04-12', self.EUR19_outros_tipos_de_cilindros)

    def _default_EUR19_obs(self):
        return self._get_default('EUR19', 'EUR19-05-01')
    EUR19_obs = fields.Char(
        'Observações', readonly=False, default=_default_EUR19_obs
    )

    def _write_EUR19_obs(self):
        self._set_result('EUR19', 'EUR19-05-01', self.EUR19_obs)
        self._copy_result('EUR19', 'EUR19-05-01', self.EUR19_obs)

    def _default_EUR19_cristais(self):
        return self._get_default('EUR19', 'EUR19-04-03')
    EUR19_cristais = fields.Char(
        'Cristais', readonly=False, default=_default_EUR19_cristais
    )

    def _write_EUR19_cristais(self):
        self._set_result('EUR19', 'EUR19-04-03', self.EUR19_lab_test_crystal_names)
        self._copy_result('EUR19', 'EUR19-04-03', self.EUR19_lab_test_crystal_names)

    def _default_EUR19_lab_test_crystal_ids(self):
        LabTestCrystal = self.env['clv.lab_test.crystal']
        crystal_ids = []
        if self._get_default('EUR19', 'EUR19-04-03') is not False:
            cristais = self._get_default('EUR19', 'EUR19-04-03').split(', ')
            for cristal in cristais:
                crystal = LabTestCrystal.search([
                    ('name', '=', cristal),
                ])
                if crystal.id is not False:
                    crystal_ids.append((4, crystal.id))
        return crystal_ids
    EUR19_lab_test_crystal_ids = fields.Many2many(
        comodel_name='clv.lab_test.crystal',
        relation='clv_lab_test_crystal_lab_test_result_copy_to_report_rel',
        string='Lab Test Crystals',
        default=_default_EUR19_lab_test_crystal_ids
    )

    EUR19_lab_test_crystal_names = fields.Char(
        string='Cristais',
        compute='_compute_EUR19_lab_test_crystal_names',
        store=True
    )
    EUR19_lab_test_crystal_names_suport = fields.Char(
        string='Crystal Names Suport',
        compute='_compute_EUR19_lab_test_crystal_names_suport',
        store=False
    )

    @api.depends('EUR19_lab_test_crystal_ids')
    def _compute_EUR19_lab_test_crystal_names(self):
        for r in self:
            r.EUR19_lab_test_crystal_names = r.EUR19_lab_test_crystal_names_suport

    @api.multi
    def _compute_EUR19_lab_test_crystal_names_suport(self):
        for r in self:
            EUR19_lab_test_crystal_names = False
            for crystal in r.EUR19_lab_test_crystal_ids:
                if EUR19_lab_test_crystal_names is False:
                    EUR19_lab_test_crystal_names = crystal.name
                else:
                    EUR19_lab_test_crystal_names = EUR19_lab_test_crystal_names + ', ' + crystal.name
            r.EUR19_lab_test_crystal_names_suport = EUR19_lab_test_crystal_names
            # if r.EUR19_lab_test_crystal_names != EUR19_lab_test_crystal_names:
            #     record = self.env['clv.lab_test.report.edit'].search([('id', '=', r.id)])
            #     record.write({'EUR19_lab_test_crystal_ids': r.EUR19_lab_test_crystal_ids})

    def _do_result_copy_to_report_EUR19(self):

        self._write_EUR19_volume()
        self._write_EUR19_densidade()
        self._write_EUR19_aspecto()
        self._write_EUR19_cor()
        self._write_EUR19_odor()
        self._write_EUR19_ph()
        self._write_EUR19_proteinas()
        self._write_EUR19_glicose()
        self._write_EUR19_cetona()
        self._write_EUR19_pigmentos_biliares()
        self._write_EUR19_sangue()
        self._write_EUR19_urobilinogenio()
        self._write_EUR19_nitrito()
        self._write_EUR19_celulas_epiteliais()
        self._write_EUR19_muco()
        self._write_EUR19_cristais()
        self._write_EUR19_leucocitos()
        self._write_EUR19_hemacias()
        self._write_EUR19_cilindros()
        self._write_EUR19_cilindros_hialinos()
        self._write_EUR19_cilindros_granulosos()
        self._write_EUR19_cilindros_leucocitarios()
        self._write_EUR19_cilindros_hematicos()
        self._write_EUR19_cilindros_cereos()
        self._write_EUR19_outros_tipos_de_cilindros()
        self._write_EUR19_obs()

        return True
