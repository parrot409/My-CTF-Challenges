//cc -pie -fPIE -z now -fstack-protector ./source.c -o manga_store
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

#define RE_ZERO_PRICE 20
#define TIMEOUT 180

typedef struct manga {
	unsigned long long number_of_volumes;
	unsigned long long price;
	char *name;
} manga;

typedef struct cart_item {
	char reason[24];
	manga *item;
	unsigned long long id;
	unsigned long long volume;
	struct cart_item *next;
	char freed;
} cart_item;

static manga *mangas[4];
cart_item* cart_list;
unsigned long long last_inserted_id;
/* Utils */
size_t read_str(char *buf,size_t n){
	if(n == 0 || buf == NULL) _exit(1);
	long int readed = read(0,buf,n-1);
	if(readed <= 0){
		puts("Read??");
		_exit(1);
	}
	if(buf[readed-1] == '\n') buf[readed-1] = '\x00';
	buf[readed] = '\x00';
	return readed;
}

unsigned long long read_num(){
	char buf[16];
	size_t r = read_str((char *)&buf,16);
	return strtoull((char *)&buf,NULL,10);
}

/* Printing stuff */
void print_main_menu(){
	puts("-----------------------------");
	puts("| 1. Add manga              |");
	puts("| 2. Cart                   |");
	puts("| 3. Add feedback           |");
	puts("| 4. Exit                   |");
	puts("-----------------------------");
}

void print_list_mangas(){
	puts("--------------------------------------------");
	for(int i = 0;i<4;i++){
		printf("| %d. %-18s $%llu     %llu Volumes |\n",i,mangas[i]->name,mangas[i]->price,mangas[i]->number_of_volumes);
	}
	puts("--------------------------------------------");
}

void print_cart_items(){
	unsigned long long p=0;
	for(cart_item* iter=cart_list;iter;iter = iter->next){
		if(!iter->freed){
			printf("| %02d. %-18s Volume %llu   $%llu - Your reason to buy this: %s \n",iter->id,iter->item->name,iter->volume,iter->item->price,iter->reason);
			p += iter->item->price; 
		}
	}
	printf("|\n| Total: $%llu\n",p);
}
/* Buying stuff*/
void add_manga_to_cart(manga* to_add_manga,unsigned long long volume){
	cart_item *toadd_item = malloc(sizeof(struct cart_item));

	toadd_item->id = last_inserted_id++;
	toadd_item->volume = volume;
	toadd_item->item = to_add_manga;
	toadd_item->freed = 0;

	printf("why are you interested? ");
	read_str((char *)&toadd_item->reason,24);

	if(!cart_list){
		toadd_item->next = NULL;
		cart_list = toadd_item;
	} else {
		toadd_item->next = cart_list;
		cart_list = toadd_item;
	}
}

void buy_manga(){
	size_t manga_id;
	unsigned long long volume; 

	print_list_mangas();
	printf("Manga id: ");
	manga_id = read_num();

	if(manga_id > 3){
		puts("Wrong id!");
		return;
	}

	printf("Volume: ");
	volume = (unsigned long long)read_num();

	if(volume > mangas[manga_id]->number_of_volumes){
		puts("We don't have that!");
		return;		
	}

	add_manga_to_cart(mangas[manga_id],volume);
	puts("Added to your cart!");
}
/* Cart stuff */
void manager_cart(){
	char buf[8];
	size_t itemId;
	cart_item *prev;

	if(!cart_list){
		puts("Your cart is empty!");
		return;
	} 
	print_cart_items();

	printf("Do you want to remove a item from your cart?\n> ");
	read_str((char *)&buf,4);

	if(buf[0] == 'y'){
		printf("item's id: ");
		itemId = read_num();

		if(itemId >= last_inserted_id){
			puts("Wrong id!");
			return;
		}

		prev = NULL;
		for(cart_item *item = cart_list;item;item = item->next){
			if(item->id == itemId && !item->freed) {
				free(item);
				item->freed = 1;
				if(item->item == mangas[1] && item->volume == 15 && item->item->price == RE_ZERO_PRICE){
					puts("You can't remove this from your cart because it's so good");
					return;
				}

				if(!prev){
					cart_list = item->next;
				} else {
					prev->next = item->next;
				}

				puts("Item removed!");
				return;
			}
			prev = item;
		}
		puts("Item not found!");
	}
}
/* Feedback stuff*/
void do_feedback(){
	printf("Feedback size: ");
	size_t sz = read_num();	
	char *feedback = malloc(sz);
	printf("Feedback: ");
	read_str(feedback,sz);
	puts("Thank you but we don't care about your feedback!");
	free(feedback);
}

/* Proc stuff */
void add_manga_to_store(char *name,int price,int number_of_volumes){
	manga *toadd_manga = malloc(sizeof(struct manga));
	toadd_manga->name = strdup(name);
	toadd_manga->price = price;
	toadd_manga->number_of_volumes = number_of_volumes;

	for(int i=0;i<4;i++){	
		if(!mangas[i]){
			mangas[i] = toadd_manga;
			break;
		}
	}
}

void alarm_handle(){
	puts("We are closing...");
	_exit(1);
}

void init_proc(){
	signal(SIGALRM,&alarm_handle);
	alarm(TIMEOUT);
	setvbuf(stdin,NULL,_IONBF,0);
    setvbuf(stdout,NULL,_IONBF,0);
    setvbuf(stderr,NULL,_IONBF,0);

    add_manga_to_store("OreGairu",12,13);
    add_manga_to_store("Re:Zero LN",RE_ZERO_PRICE,22);
    add_manga_to_store("Attack on Titan",15,33);
    add_manga_to_store("Death note",18,12);
}

void main(){
	init_proc();
	while(1){
		print_main_menu();
		printf("> ");
		unsigned long selection = read_num();
		switch(selection){
			case 1:
				buy_manga();
				break;
			case 2:
				manager_cart();
				break;
			case 3:
				do_feedback();
				break;
			case 4:
				exit(0);
				break;
			default:
				puts("What??");
				break;
		}
	}
}


