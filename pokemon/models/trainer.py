from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Trainer(models.Model):
    _name = 'pokemon.trainer'
    _description = "Entrenador de pokemones"

    trainer_name = fields.Char(string="Nombre del entrenador", required=True)
    team = fields.One2many(comodel_name="pokemon.pokemon", inverse_name="trainer", required=True)

    # Realizame una constraint de que el equipo sea de 6 pokemones
    @api.constrains('team')
    def _check_team(self):
        for record in self:
            if len(record.team) > 6:
                raise ValidationError("El equipo no puede tener mas de 6 pokemones")
            elif len(record.team) < 6:
                raise ValidationError("El equipo no puede tener menos de 6 pokemones")
