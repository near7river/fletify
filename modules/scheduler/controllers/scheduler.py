from libs.controller import Controller
from modules.home.views.template import template
from modules.scheduler.models.entities import Scheduler
from modules.scheduler.views.scheduler_view import scheduler_view
from modules.scheduler.views.scheduler_view import *

class scheduler(Controller):

    def index(self):
        def add(s):
            s.save()
            
        def edit(e):
            pass

        def schedulers():
            return list(Scheduler)
            
        body = scheduler_view(self.page,schedulers,add,edit)
        return template(body, self.page)
