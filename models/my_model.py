from odoo import models, fields, api
from datetime import date


class MyModule(models.Model):
    _name = "my.module"
    _description = "Task"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")

    priority = fields.Selection(
        [
            ("0", "Low"),
            ("1", "Normal"),
            ("2", "High"),
        ],
        string="Priority",
        default="1",
    )

    due_date = fields.Date(string="Due Date")

    assigned_to = fields.Many2one(
        "res.users",
        string="Assigned To",
    )

    state = fields.Selection(
        [
            ("todo", "To Do"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
        ],
        string="Status",
        default="todo",
        tracking=True,
    )

    # NEW: computed flag
    is_overdue = fields.Boolean(
        string="Overdue",
        compute="_compute_is_overdue",
        store=True,
    )

    @api.depends("due_date", "state")
    def _compute_is_overdue(self):
        today = date.today()
        for task in self:
            task.is_overdue = bool(
                task.due_date
                and task.due_date < today
                and task.state != "done"
            )
