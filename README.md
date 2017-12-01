Team members:
	Naveen Gaddam [111344916]
	Shalaka Sidmul [111367731]
PLATFORM.  
Language used in this implementation of Byzantine Chain Replication based SHUTTLE protocol is DistAlgo.
Following are the platform specifications:
	1. DistAlgo version 1.0.11
	2. Python version 3.5.2
	3. Testing and implementation carried out on Windows 10 operating system
	4. Types of hosts used in testing and implementation: Laptops (without any VMs)
	5. Each host used in testing had the same platform as mentioned in points 1 and 2.
	
INSTRUCTIONS.
	Execution of the implementation requires that DistAlgo and python be installed on the system.
	Scripts for running test cases are provided with the distribution.
	Each module creates a log file for each test case that is executed in './logs/<test_case_name>/'
	The scripts will start separate command prompts for each module.
	To run master module:
	
		python -m da --message-buffer-size 1000000 -n MasterNode  master.da <config-file-name>
	
	This will start a node named 'MasterNode' and run the 'main()' of master.da on that node.
	
	To run Olympus module: 
	
		python -m da --message-buffer-size 1000000 -n OlympusNode -D olympus.da
	
	To run replicas: 
	
		python -m da --message-buffer-size 1000000 -n ReplicaNode<replica-number> -D replica.da
		
	To run clients: 
	
		python -m da --message-buffer-size 1000000 -n ClientNode<client-number> -D client.da
				
	To run the test cases, please refer to the testing.txt provided with this distribution.

	All shell scripts to run test cases are present in '/config/<test_case_name>/'
	All test cases are documented in 'testing.txt' 
	
WORKLOAD GENERATION:

For pseudorandom workload generation, [for example:  pseudorandom(233,5)]
python library function: random.randint(1,n) is used.
First seed and generate sequence of random integers. For the above example, seed is 233 and a sequence of 5 random integers are generated. The random numbers generated are then mapped to one of the workload operations specified for that particular client in the config.txt.

BUGS AND LIMITATIONS: None observed


CONTRIBUTIONS:
	All modules were built by both team members equally.
	All testing was equally divided.

MAIN FILES
	
	Master : 'src/master.da'
	Olympus: 'src/olympus.da'
	Client: 'src/client.da'
	Replica: 'src/replica.da'
	
	Config files: 'config/<test_case_name>'
	Test case shell scripts: 'config/<test_case_name>.bat'
	
	Log files for each test case: 'logs/<test_case_name>/'
  
CODE SIZE.  
	
	(1) LOC:
			1. algorithm:  
				Master: 113
				Replica: 1264
				Olympus: 671
				Client: 518
			2. other: 228
			3. total: 2794
	Lines of code were obtained using CLOC
	
	(2) About 70% of the code is for the algorithm itself while the remianing is for fault injection, debugging, etc
	
LANGUAGE FEATURE USAGE.
	1. list comprehensions: 22
	2. dictionary comprehensions: 30
	3. set comprehensions (tuple): 21
	4. aggregations: none 
	5. quantifications none
