#include <stdlib.h>
#include <stdio.h>
#include <time.h>

long long multi(int x,int y){
	
	return (long long)x*y;
	}

int main(){
	srand(time(NULL));
	volatile long long a;
	for (int i =0; i<10000000; i++){ 	
		int x = rand() %10000000 +100000 ;
		int y = rand() %10000000 +100000 ;
		a = multi(x,y);
	}
	
	
	return 0; 	
	}


