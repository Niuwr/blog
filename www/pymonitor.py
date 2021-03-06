# -*- coding: utf-8 -*-


import os, sys, time,subprocess

from watchdog.observers import Observer

from watchdog.events import FileSystemEventHandler


def log(s):
    print('[Monitor] {}'.format(s))


class MyFileSystemEventHandler(FileSystemEventHandler):

    def __init__(self, fn):
        super().__init__()
        self.restart = fn

    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed: {}'.format(event.src_path))
            self.restart()


command = ['echo', 'ok']
process = None


def kill_process():
    global process
    if process:
        process.kill()
        process.wait()
        log('Process ended with code: {}'.format(process.returncode))
        process = None


def start_process():
    global process, command
    log('Start process {} ...'.format(' '.join(command)))
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)


def restart_process():
    kill_process()
    start_process()


def start_watch(path, callback):
    observer = Observer()
    observer.schedule(MyFileSystemEventHandler(restart_process), path, recursive=True)
    observer.start()
    log('Watching directory {}.'.format(path))
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    argv = sys.argv
    argv.append("")
    if not argv[1]:
        print("Usage: python pymonitor your-script.py")
        exit(0)
    if argv[0] != 'python':
        argv[0] = 'python'
    argv.pop()
    command = argv
    path = os.path.abspath('.')
    start_watch(path, None)
