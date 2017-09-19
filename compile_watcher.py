import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler

class CompileEventHandler(FileSystemEventHandler):

    def __init__(self, build_dir=None):
        super(CompileEventHandler, self).__init__()
        self.build_dir = build_dir[0:-1] if build_dir and build_dir[-1] == "/" else build_dir
    
    def __to_js(self, filename):
        """
        Assumes that you give it ".ts" files and changes the extension to ".js".
        """
        filename_parse = filename.split(".")
        sans_extension = ".".join(filename_parse[0:-1])
        if self.build_dir:
            sans_extension_parse = sans_extension.split("/")
            sans_extension_parse[-2] = self.build_dir
            sans_extension = "/".join(sans_extension_parse)
        return sans_extension + ".js"
    
    def __compile(self, src):
        outfile = self.__to_js(src)
        subprocess.call([
            "node_modules/typescript/bin/tsc", "--lib", "es2015,es2015.iterable,dom", "--outFile", outfile, src
            #"node_modules/typescript/bin/tsc", "--lib", "es6", "--outFile", outfile, src
        ])
        logging.info("compiled %s to %s" % (src, outfile))
    
    def __delete(self, fname):
        outfile = self.__to_js(fname)
        subprocess.call(["rm", outfile])
        logging.info("deleted %s" % outfile)

    def __is_ts_event(self, event):
        return not event.is_directory and event.src_path.endswith(".ts")

    def on_created(self, event):
        super(CompileEventHandler, self).on_created(event)
        if self.__is_ts_event(event):
            logging.debug("TS created event %s" % event)
            self.__compile(event.src_path)

    def on_deleted(self, event):
        super(CompileEventHandler, self).on_deleted(event)
        if self.__is_ts_event(event):
            logging.debug("TS delete event %s" % event)
            self.__delete(event.src_path)

    def on_modified(self, event):
        super(CompileEventHandler, self).on_modified(event)
        if self.__is_ts_event(event):
            logging.debug("TS modified event %s" % event)
            self.__compile(event.src_path)

    def on_moved(self, event):
        """
        This assumes that you did not move a ".js" file to something of another
        extension.
        """
        super(CompileEventHandler, self).on_moved(event)
        if self.__is_ts_event(event):
            logging.debug("TS moved event %s" % event)
            self.__delete(event.src_path)
            if event.dest_path.endswith(".ts"):
                self.__compile(event.dest_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    observer.schedule(CompileEventHandler("jsbuild"), path, recursive=True)
    observer.start()
    logging.info("Watching directory...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
