'''
Created on Friday 12/07/2019

@author: yaztown
'''

import loopie

class MyMain(loopie.MainLoop):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.i = 0
    
    def loop_logic(self):
        self.i += 1
        print(self.i)
    
    def importRoutes(self):
        # You can override this method to import the route file or create your on url routes
        super().importRoutes()
        @self.web_app.route('/hello')
        def hello(**kwargs):
            return 'Hello from overridden importRoutes()'

if __name__ == '__main__':
    main = MyMain(name='main', enable_web_browsable_api=True)
    app = loopie.Application(main)
    main.importRoutes()
    
    @main.json_rpc.method('core.MyLoop(uuid=String) -> Object')
    def MyLoop(**kwargs):
        uuid = kwargs.pop('uuid', 'no uuid')
        return dict(app='loopie_test', status='running', i=main.i, uuid=uuid)
    
    app.start()
    print('application ended')
