import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler

class CompileEventHandler(FileSystemEventHandler):
    
    def __to_js(self, filename):
        """
        Assumes that you give it ".ts" files and changes the extension to ".js".
        """
        filename = src.split(".")
    
    def __compile(self, src):
        outfile = self.__to_js(src)
        subprocess.call([
            "node_modules/typescript/bin/tsc", "--outFile", outfile, src
        ])
        logging.info("compiled %s to %s" % (src, outfile))
    
    def __delete(self, fname):
        outfile = self.__to_js(fname)
        subprocess.call(["rm", outfile])
        logging.info("deleted %s" % outfile)

    def __is_js_event(self, event):
        return not event.is_directory and event.src_path.endswith(".js")

    def on_created(self, event):
        super(CompileEventHandler, self).on_created(event)
        if self.__is_js_event(event):
            self.__compile(event.src_path)

    def on_deleted(self, event):
        super(CompileEventHandler, self).on_deleted(event)
        if self.__is_js_event(event):
            self.__delete(event.src_path)

    def on_modified(self, event):
        super(CompileEventHandler, self).on_modified(event)
        if self.__is_js_event(event):
            self.__compile(event.src_path)

    def on_moved(self, event):
        """
        This assumes that you did not move a ".js" file to something of another
        extension.
        """
        super(CompileEventHandler, self).on_moved(event)
        if self.__is_js_event(event):
            self.__delete(event.src_path)
            self.__compile(event.dest_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    observer.schedule(CompileEventHandler(), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
