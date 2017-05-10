#!/usr/bin/env python

from Daemon import daemon
import time
import sys

class Test(daemon):
    counter = 0
    log_file = '/tmp/testing_daemon.log'

    def run(self):
        while True:
            with open(self.log_file, 'a') as f:
                f.write("Current count is: {0}.\n".format(self.counter))
            time.sleep(1)
            self.counter += 1

if __name__ == "__main__":
    daemon = Test('/tmp/testing_pid.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            print('Starting service...')
            daemon.start()
        elif 'stop' == sys.argv[1]:
            print('Stopping service...')
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            print('Restarting service...')
            daemon.restart()
        else:
            print('Unknown service function: {0}.'.format(sys.argv[1]))
            sys.exit(2)

    else:
        print('Usage: start|stop|restart'.format(sys.argv[0]))
        sys.exit(2)