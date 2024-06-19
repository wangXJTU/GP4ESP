from init_sys import init_sys
from fitness import fitness
from evolution import GA, DE
from swarm import PSO, ABC, WOA, GWO, HHO
from niching import nichingswarm
from single_point import SA
from time import time

'''
solution: num_srv dimensionality, each is 0~num_bs-1, 
            representing the base/edge station deploying server
'''

num_user = 1000
num_bs = 1000
num_srv = 600
load = 0.5

max_srv = 1000  # max service rate of servers
max_req = max_srv * load  # max request rate of BS
cloud_delay = 0.05

result_file = "results-" + str(num_bs / 1000) + "kBS-" + str(num_srv) + "ES-" + str(load) + "load" + ".csv"
rfile = open(result_file, "a")
print("Method", "Delay (s)", "Time (min)", sep=',', file=rfile)

#  service rates of servers; request rates of BSs
init = init_sys(num_bs, num_srv, max_req, max_srv)
srv_rate, req_rate = init.gen_sys()
perf = fitness(srv_rate, req_rate, cloud_delay)

ga = GA(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
start_time = time()
delay = ga.ga()
end_time = time()
print("GA", delay)
print("GA", delay, (end_time - start_time) / 60, sep=',', file=rfile)
start_time = time()
delay = ga.pgsao()
end_time = time()
print("GP4ESP", delay)
print("GP4ESP", delay, (end_time - start_time) / 60, sep=',', file=rfile)

start_time = time()
de = DE(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
delay = de.de()
end_time = time()
print("DE", delay)
print("DE", delay, (end_time - start_time) / 60, sep=',', file=rfile)

sa = SA(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
start_time = time()
delay = sa.sa()
end_time = time()
print("SA", delay)
print("SA", delay, (end_time - start_time) / 60, sep=',', file=rfile)

# C. Pandey, V. Tiwari, S. Pattanaik and D. Sinha Roy,
# "A Strategic Metaheuristic Edge Server Placement Scheme for Energy Saving in Smart City,"
# 2023 International Conference on Artificial Intelligence and Smart Communication (AISC),
# Greater Noida, India, 2023, pp. 288-292, doi: 10.1109/AISC56616.2023.10084941.
pso = PSO(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
start_time = time()
delay = pso.pso()
end_time = time()
print("PSO", delay)
print("PSO", delay, (end_time - start_time) / 60, sep=',', file=rfile)
start_time = time()
delay = pso.psom()
end_time = time()
print("PSOM", delay)
print("PSOM", delay, (end_time - start_time) / 60, sep=',', file=rfile)
start_time = time()
delay = pso.pso_sa()
end_time = time()
print("PSOSA", delay)
print("PSOSA", delay, (end_time - start_time) / 60, sep=',', file=rfile)

# Bing Zhou, Bei Lu and Zhigang Zhang,
# “Placement of Edge Servers in Mobile Cloud Computing using Artificial Bee Colony Algorithm”
# International Journal of Advanced Computer Science and Applications(IJACSA), 14(2), 2023.
# http://dx.doi.org/10.14569/IJACSA.2023.0140273
abc = ABC(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
start_time = time()
delay = abc.abc()
end_time = time()
print("ABC", delay)
print("ABC", delay, (end_time - start_time) / 60, sep=',', file=rfile)

#  Moorthy, R.S., Arikumar, K.S., Prathiba, B.S.B. (2023).
#  An Improved Whale Optimization Algorithm for Optimal Placement of Edge Server.
#  In: the 4th International Conference on Advances in Distributed Computing and Machine Learning (ICADCML 2023),
#  Rourkela, India, pp. 89-100. https://doi.org/10.1007/978-981-99-1203-2_8
woa = WOA(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
start_time = time()
delay = woa.woa_dim()
end_time = time()
print("WOA", delay)
print("WOA", delay, (end_time - start_time) / 60, sep=',', file=rfile)

hho = HHO(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
start_time = time()
delay = hho.hho()
end_time = time()
print("HHO", delay)
print("HHO", delay, (end_time - start_time) / 60, sep=',', file=rfile)

gwo = GWO(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
start_time = time()
delay = gwo.gwo()
end_time = time()
print("GWO", delay)
print("GWO", delay, (end_time - start_time) / 60, sep=',', file=rfile)

#  Xinglin Zhang, Jinyi Zhang, Chaoqun Peng, Xiumin Wang,
#  Multimodal Optimization of Edge Server Placement Considering System Response Time,
#  ACM Transactions on Sensor Networks, 2023, 19(1): 13, 20 pages,
#  https://doi.org/10.1145/3534649
niche = nichingswarm(srv_rate, req_rate, cloud_delay, dim=num_srv, high=num_bs)
start_time = time()
delay = niche.nPSO()
end_time = time()
print("nPSO", delay)
print("nPSO", delay, (end_time - start_time) / 60, sep=',', file=rfile)

rfile.close()
