
bp_watchdog: bp_watchdog.o
	gcc -o bp_watchdog bp_watchdog.o

bp_watchdog.o: bp_watchdog.c
	gcc -c bp_watchdog.c 

install: bp_watchdog
	mkdir -p /opt/rb/bin
	cp bp_watchdog /opt/rb/bin

clean:
	rm -f *.o
	rm -f bp_watchdog

rpm: clean
	        $(MAKE) -C packaging/rpm

rpmtest:
	        $(MAKE) LATEST=`git stash create` -C packaging/rpm
