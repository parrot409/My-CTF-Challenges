// gcc -fstack-protector -pie -fPIE -z now ./source.c -o heap_heap
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <signal.h>

#define TIMEOUT 60

typedef struct settings_s {
	char *input_buf;
	uint64_t freed_chunk;
} settings_s;

typedef struct story {
	char title[16];
	char content[];
} story; 

settings_s *s;
story *stories[10]; 
int story_sizes[10]; 

/* Utils */
int read_str(char *buf,int n){
	if(n == 0 || buf == NULL) _exit(1);
	n = read(0,buf,n);
	if(buf[n-1] == '\n') buf[n-1] = '\x00'; 
	return n;
}

int read_int(){
	read_str(s->input_buf,0x100);
	return atoi(s->input_buf);
}

int get_idx(){
	int idx;
	printf("What's your story's idx?\n> ");
	idx = read_int();

	if(idx<0 || idx>9){
		puts("Invalid idx!");
		return -1;
	}

	if(stories[idx] == NULL){
		puts("Story doesn't exist");
		return -1;
	}

	return idx;
}

/* mem stuff */
void alloc_story(){
	story *to_add;
	int idx;
	int story_size;

	for(idx=0;idx<10;idx++){
		if(stories[idx] == NULL) break; 
	}

	if(idx == 10){
		puts("Oh you have too many stories");
		_exit(1);
	}

	printf("How long is your story?\n> ");
	story_size = read_int();
	if(story_size<0){
		puts("Invalid size!");
		return;
	}

	to_add = malloc(16+story_size);
	printf("What's your story's title?\n> ");
	read_str(to_add->title,16);

	printf("What's your story?\n> ");
	read_str(to_add->content,story_size);

	stories[idx] = to_add;
	story_sizes[idx] = story_size;
	printf("Added!\nYour story's id is %d!\n",idx);
}

void remove_story(){
	int idx;

	idx = get_idx();
	if(idx == -1){
		return;
	}

	if(s->freed_chunk){
		puts("You can only remove one story :(");
		return;
	}

	s->freed_chunk = -1;
	free(stories[idx]);
	puts("Removed!");
}

void rewrite_story(){
	int idx;

	idx = get_idx();
	if(idx == -1){
		return;
	}

	printf("What's your story?\n> ");
	read_str(stories[idx]->content,story_sizes[idx]);
	puts("Done!");
}

void read_story(){
	int idx;

	idx = get_idx();
	if(idx == -1){
		return;
	}

	printf("Your story: %s\n",stories[idx]->content);
}

/* Printing stuff*/
void print_main_menu(){
	puts("HEAPHEAPHEAPHEAPHEAPHEAPHEAPHEAPHEAPHEAP");
	puts("HEAP 1. Write a story               HEAP");
	puts("HEAP 2. Remove a story              HEAP");
	puts("HEAP 3. rewrite a story             HEAP");
	puts("HEAP 4. read a story                HEAP");
	puts("HEAP 5. Exit                        HEAP");
	puts("HEAPHEAPHEAPHEAPHEAPHEAPHEAPHEAPHEAPHEAP");
}

void timeout(){
	puts("Ohhhh too slow");
	_exit(1);
}

void init_proc(){
	char *input_buf;
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	signal(SIGALRM,timeout);
	alarm(TIMEOUT);
	input_buf = malloc(0x100);
	s = malloc(sizeof(struct settings_s));
	s->input_buf = input_buf;  
	s->freed_chunk = 0; 
}

int main(){
	init_proc();

	while(1){
		print_main_menu();
		printf("> ");
		switch(read_int()){
			case 1:
				alloc_story();
				break;
			case 2:
				remove_story();
				break;
			case 3:
				rewrite_story();
				break;
			case 4:
				read_story();
				break;
			case 5:
				puts("Goodbye!");
				return 0;
			default:
				puts("?");
				break;
		}
	}
}