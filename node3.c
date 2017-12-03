#include <stdio.h>

extern struct rtpkt {
	int sourceid;       /* id of sending router sending this pkt */
	int destid;         /* id of router to which pkt being sent
						(must be an immediate neighbor) */
	int mincost[4];    /* min cost to node 0 ... 3 */
};

extern int TRACE;
extern int YES;
extern int NO;

static struct distance_table
{
	int costs[4][4];
} dt3, *distance;
 
/* students to write the following two routines, and maybe some others */
// define 999 as infinity 
#define INF 999
//external function and variable
extern void tolayer2(struct rtpkt packet);
extern float clocktime;

//local functions and variables
int compute_shortest_path3();
void updata3();
void printf_sendinfo3(struct rtpkt *p);
void printdt3(struct distance_table *dtptr);

static int link[4];       //cost to neighbor
static int shortest[4];	  //smallest cost to destination

						  /*
						  * initialize router table
						  */
void rtinit3()
{
	int destination;        // destination node id 0, 1, 2, 3
	int neighbor;           // neighbor node id 0, 1, 2, 3

							//print the time function was called
	printf("time=%f> rtinit3\n", clocktime);

	//initialize dt
	distance = &dt3;

	// initialize the link costs to neighbor
	link[0] = 7;
	link[1] = INF;
	link[2] = 2;
	link[3] = 0;

	// initialize the router table 
	for (destination = 0; destination < 4; destination++)
	{
		for (neighbor = 0; neighbor < 4; neighbor++)
		{   //if destiantion is neighbor, cost is link cost, esle is infinity
			if (destination == neighbor) {
				distance->costs[destination][neighbor] = link[destination];
			}
			else {
				distance->costs[destination][neighbor] = INF;
			}
		}

		//at initialization step, the shorst path is link cost
		shortest[destination] = link[destination];
	}

	//update router table
	updata3();
	//print router table
	printdt3(distance);

}

void rtupdate3(struct rtpkt *rcvdpkt)
{
	int idx;
	//get source id
	int src = rcvdpkt->sourceid;;

	// print the time function was called 
	printf("time=%f> rtupdate3: node3 receiving a packet from node%d\n", clocktime, src);

	//update router table
	for (idx = 0; idx < 4; idx++)
	{
		distance->costs[idx][src] = link[src] + rcvdpkt->mincost[idx];
		if (distance->costs[idx][src] > INF)
			distance->costs[idx][src] = INF;
	}

	// print router table
	printdt3(distance);

	//if shortest path changed, update router table
	if (compute_shortest_path3())
		updata3();
}

/*
* compute the shortest path
*/
int compute_shortest_path3()
{
	int destination;        // destination node id 0, 1, 2, 3
	int neighbor;           // neighbor node id 0, 1, 2, 3
	int lowestCost;         // save shortest path and compare with recorde
	int changed = 0;         // whether shortest path changed; 0 is not changed; 1 is changed 

	for (destination = 0; destination < 4; destination++)
	{
		lowestCost = distance->costs[destination][0];

		for (neighbor = 1; neighbor < 4; neighbor++)
		{
			if (lowestCost > distance->costs[destination][neighbor])
				lowestCost = distance->costs[destination][neighbor];
		}

		//if shortest patch changed, update shortest path
		if (lowestCost != shortest[destination]) {
			shortest[destination] = lowestCost;
			//mark shortest path changed
			changed = 1;
		}
	}

	return changed;
}

/*
* update the packet and send it to the other nodes
*/
void updata3()
{
	int node;              // node id in the network 0, 1, 2, 3
	struct rtpkt pkt, *p;  // packet

						   //set packet source is node 3
	p = &pkt;
	p->sourceid = 3;

	//set mincost information in packet
	for (node = 0; node < 4; node++)
	{
		p->mincost[node] = shortest[node];
	}

	//send packet to node 0
	p->destid = 0;
	tolayer2(*p);
	printf_sendinfo3(p);
	//send packet to node 2
	p->destid = 2;
	tolayer2(*p);
	printf_sendinfo3(p);
}

/*
* print send information "%time %source send packet to %destination with cost %mincost"
*/
void printf_sendinfo3(struct rtpkt *p)
{
	printf("time=%f> node%d sent packet to node%d with following minimum costs: %d\n",
		clocktime, p->sourceid, p->destid, p->mincost[p->destid]);
}


void printdt3(struct distance_table *dtptr)
{
	printf("             via   \n");
	printf("   D3 |    0     2 \n");
	printf("  ----|-----------\n");
	printf("     0|  %3d   %3d\n", dtptr->costs[0][0], dtptr->costs[0][2]);
	printf("dest 1|  %3d   %3d\n", dtptr->costs[1][0], dtptr->costs[1][2]);
	printf("     2|  %3d   %3d\n", dtptr->costs[2][0], dtptr->costs[2][2]);
}
