'''
Created on Monday 02/07/2018

file: base_threads.py

@author: yaztown
'''

from loopie.logging import get_logger
logger = get_logger()

from loopie.net import flask_app
from loopie.net.wsgiserver import WSThread

from loopie.core.base_threads.base_threads import LoopingThread


class MainLoop(LoopingThread):
    def __init__(self, setup_object={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
#         _ = MyGPIO()
#         self.setup_object = setup_object.copy()
        self.httpd = None
        logger.debug('Initialized {}'.format(self.name))
    
#     def _setup_mainloop(self):
#         pass
#     
#     def start_sub_threads(self):
#         for sensor in self.sensors:
#             sensor.start()
#         sleep(3)
#         for controller in self.controllers:
#             controller.start()
#     
    def _start_wsgiserver(self):
        self.httpd = WSThread(flask_app, name='wsgiserver')
        self.httpd.start()
    
    def start_server(self):
        self._start_wsgiserver()
#     
    def loop_setup(self):
#         self._setup_mainloop()
#         self.start_sub_threads()
        self.start_wsgiserver()
#         raise NotImplementedError('must implement in subclasses')

    def loop_logic(self):
        pass
#         raise NotImplementedError('must implement in subclasses')
        
    def _stop_wsgiserver(self):
        self.httpd.stop()
    
    def stop_server(self):
        self._stop_wsgiserver()
     
    def stop_sub_threads(self):
        self.stop_server()
#         for controller in self.controllers:
#             controller.stop()
#             controller.join()
#         for sensor in self.sensors:
#             sensor.stop()
#             sensor.join()
#         raise NotImplementedError('must implement in subclasses')
    
    def clean_up(self):
        self.stop_sub_threads()
        
#     def get_status(self):
#         pass
