//Nicholas Byrnes
//ECE2524 Process Object Assignment
//It has a few errors..

#include "Process.h"
using namespace std;

Process::Process(const string &args) {
	m_name = args[0];
	const char* cargs;
	
	cargs.push_back(NULL);

	if(pipe(readpipe))
		cerr << "Error with read pipe!" << endl;
	if(pipe(writepipe))
		cerr << "Error with write pipe!" << endl;
	
	m_pid = fork();
	if(m_pid == -1)
		cerr << "Error with child process!" << endl;

	else if(m_pid == 0) {
		dup2(readpipe[1], STDOUT_FILENO);
		close(readpipe[1]);

		dup2(writepipe[0], STDIN_FILENO);
		close(writepipe[1]);

		close(readpipe[0]);
		close(writepipe[0]);
		
		execve(m_name.c_str(), const_cast<char**>(&cargs[0]), NULL);
	}

	else {
		cout << "Parent[" getpid() << "] Process-object constructor" << endl;
		close(readpipe[1]);
		close(writepipe[0]);
		m_pread = fdopen(readpipe[0], "r");
	}

}

Process::~Process() {
	close(writepipe[1]);
	close(readpipe[0]);
	kill(m_pid, SIGTERM);
	waitpid(m_pid, NULL, 0);
}

void Process::write(const string& str) {
	::write(writepipe[1], str.c_str(), strlen(str.c_str()));
}

string Process::readline() {
	char* input;
	size_t length;
	length = getline(&input, &length, m_pread);
	if(length == -1)
		cerr << "Error with readline()!" << endl;
		
	return string(input);
}










