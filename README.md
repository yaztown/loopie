# loopie

This python framework is to provide a skeleton for managing a looping mainthread, with the ability of spawning childern threads that either loop of just do any other code and exit.

The project is designed to create a commandline application to loop through a custom python code while creating a skeleton for each project similar to the Arduino sketch code; meaning, for a loop to run there should be a loop_setup routine and a loop_logic routine that will be called on every loop.

One of the main uses of this project is to create a startup script (systemd) on a Raspberry Pi 2/3 that will run your custom python application, for example, to interact with the GPIO pins from the very start of the Pi.

To interact with the mainloop, the framework features a built-in WSGI application (which is based on [Flask](https://palletsprojects.com/p/flask/)) and a [wsgiserver](https://gitlab.com/fgallaire/wsgiserver) which act as a simple UI for the mainloop at [http://localhost:8000/](http://localhost:8000/).  In addition, a JSON RPC ([Flask-JSONRPC](https://pypi.org/project/Flask-JSONRPC/)) service is added to the WSGI app to enable creating JSON APIs for your service.  By default, the url for the api service is preappend with [http://localhost:8000/api/](http://localhost:8000/api/) and include a browsable api page found here [http://localhost:8000/api/browse/](http://localhost:8000/api/browse/).

This web server is enabled by default but can be disabled.  Additionally, you can use the included WSGI application to attach to any other server that supports WSGI.

This package is written in Python 3.

## Installation

The best option to install is through `pip` by running the command:

```
pip install loopie
```
or

```
sudo pip install loopie
```

## Example

```python
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

```