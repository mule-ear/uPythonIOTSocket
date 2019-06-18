/* Adapted from https://www.geeksforgeeks.org/socket-programming-cc/
   C++ is not my strong suit
   There's a funky conversion from String to char that was necessary in order to
   get it to send. Must be a better way.
*/
// Client side C/C++ program to demonstrate Socket programming 
#include <stdio.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <unistd.h> 
#include <string.h> 
#include "iostream"
#include "cstring"
#define PORT 5020

using namespace std;
   
int main(int argc, char const *argv[]) 
{ 
    int sock = 0, valread; 
    struct sockaddr_in serv_addr; 
    string hello = ""; 
    char buffer[1024] = {0}; 
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
    { 
        printf("\n Socket creation error \n"); 
        return -1; 
    } 
   
    serv_addr.sin_family = AF_INET; 
    serv_addr.sin_port = htons(PORT); 
       
    // Convert IPv4 and IPv6 addresses from text to binary form 
    if(inet_pton(AF_INET, "192.168.22.106", &serv_addr.sin_addr)<=0)  
    { 
        printf("\nInvalid address/ Address not supported \n"); 
        return -1; 
    } 
   
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) 
    { 
        printf("\nConnection Failed \n"); 
        return -1; 
    } 
    while (hello != "QUIT") {
	cout << "Message: ";
	cin >> hello;
	// This conversion was necessary to work with cin and send
	const char *hello1 = hello.c_str();
    	send(sock , hello1 , hello.length() , 0 ); 
    	printf("Message sent: %s, length =  %d\n", hello1, hello.length()); 
    	valread = read( sock , buffer, 1024); 
    	printf("%s\n",buffer );
    }
    return 0; 
} 

