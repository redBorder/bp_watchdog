#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1

static void daemonize(void)
{
    pid_t pid, sid;

    if ( getppid() == 1 ) return;

    pid = fork();
    if (pid < 0) 
        exit(EXIT_FAILURE);
    
    if (pid > 0) 
        exit(EXIT_SUCCESS);

    umask(0);
    sid = setsid();
    if (sid < 0) 
        exit(EXIT_FAILURE);

    if ((chdir("/")) < 0) {
        exit(EXIT_FAILURE);
    }

    freopen( "/dev/null", "r", stdin);
    freopen( "/dev/null", "w", stdout);
    freopen( "/dev/null", "w", stderr);
}

int main( int argc, char *argv[] ) {
    daemonize();

    while (1){
        system("logger pabloooo");
        sleep(1);
    }
    return EXIT_SUCCESS;
}
