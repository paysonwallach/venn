#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

import cleo

class RemoveCommand(cleo.Command):
    """
    Remove environments from the active virtual environment

    remove
        {environments* : Virtual environments to remove from the currently-active environment}
    """

    def __init__(self, pf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pf = pf

    def handle(self):
        environments = self.argument("environments")

        for environment in environments:
            self.pf.remove_env(environment)

        self.pf.save()
