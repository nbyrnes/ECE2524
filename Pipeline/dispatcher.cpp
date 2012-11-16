//Nicholas Byrnes
//Dispatcher.cpp for Heard it on the Pipeline HW

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){
	int fdPipe[2];
	if(pipe(fdPipe)) {
		return EXIT_FAILURE;
	}
	int PID1;
	int PID2;
	
	char** buf = {NULL};
	
	//forks generator.cpp
	PID1 = fork();
	if(!PID1) {
		dup2(fdPipe[1], STDOUT_FILENO);
		close(fdPipe[0]);
		execve("./generator", buf, NULL);
		exit(0);
	}
	
	//wait one second!
	sleep(1);

	//stop the generator
	if(!kill(PID1, SIGTERM))
		waitpid(PID1, NULL, 0);

	//forks consumer.cpp
	PID2 = fork();
	if(!PID2) {
		dup2(fdPipe[0], STDIN_FILENO);
		close(fdPipe[1]);
		execve("./consumer", buf, NULL);
		exit(0);
	}

	return 0;
}
